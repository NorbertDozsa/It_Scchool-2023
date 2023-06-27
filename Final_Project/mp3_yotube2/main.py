from typing import Union
from fastapi import FastAPI, HTTPException
from pytube import YouTube
from pytube.exceptions import PytubeError
from pathlib import Path
from starlette.responses import FileResponse
import logging
import re
import uuid
import os
from pydantic import BaseModel

class ConversionStatus(BaseModel):
    status: str
    mp3_path: str
    task_id: str

ROOT = Path(__file__).parent
DOWNLOAD = ROOT / 'download'

app = FastAPI()
conversion_status: dict[str, ConversionStatus] = {}

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s]: %(message)s",
    handlers=[
        logging.StreamHandler(),
    ]
)
logger = logging.getLogger(__name__)


@app.post("/convert/{url}")
async def post_url_id(url: str) -> dict[str, Union[str, dict[str, str]]]:
    """Returns a converted ID for the given URL"""

    try:
        # Unique task id for every url
        task_id: str = str(uuid.uuid4())

        # Check if the url is correct
        if not re.match(r'\bc\s*&&\s*d\.set\([^,]+\s*,\s*\([^)]*\)\s*\(\s*(?P<sig>[a-zA-Z0-9$]+)\(', url):
            raise HTTPException(status_code=404, detail="Error: URL not found")

        video_id: str = None
        if "/watch?v=" in url:
            video_id = url.split("/watch?v=")[1][:11]
        elif "/v/" in url:
            video_id = url.split("/v/")[1][:11]
        elif "youtu.be/" in url:
            video_id = url.split("youtu.be/")[1][:11]
            logger.info(f"Extraction completed for video_id: {video_id}")
        if not video_id:
            raise HTTPException(status_code=404, detail="Error: Unable to extract video ID from link")
        logger.error(f"Extraction failed for video_id: {video_id}")

        # Update conversion status
        if video_id in conversion_status:
            status = conversion_status[video_id].status
            if status == "completed":
                return {"status": status, "message": "Conversion already completed"}
            elif status == "in progress":
                return {"status": status, "message": "Conversion already in progress"}

        # Get YT object, convert, download

        yt = YouTube(url)
        video = yt.streams.filter(only_audio=True).first()
        video_path: str = f"temp_{task_id}.mp4"
        video.download(filename=video_path)

        mp3_path: str = f"{task_id}.mp3"
        os.system(f"ffmpeg -i {video_path} {mp3_path}")
        os.remove(video_path)

        conversion_status[video_id] = ConversionStatus(status="completed", mp3_path=mp3_path, task_id=task_id)
        logger.info(f"Conversion completed for task_id: {task_id}")
        return {"status": "completed", "message": "Conversion completed", "task_id": task_id}

    except PytubeError as err:
        conversion_status[video_id] = ConversionStatus(status="failed", error=str(err))
        logger.error(f"Conversion failed for task_id: {task_id}, Error: {str(err)}")
        raise HTTPException(status_code=400, detail=str(err))


@app.get("/status/{task_id}")
async def check_download_status(task_id: str) -> dict[str, Union[str, dict[str, str]]]:
    """Returns the status for the given ID"""
    try:
        if task_id in conversion_status:
            return conversion_status[task_id]
        else:
            raise HTTPException(status_code=404, detail="Task ID not found")
    except HTTPException as err:
        print(err)


@app.get("/download/{task_id}")
async def download_mp3(task_id: str) -> FileResponse:
    """Downloads the audio file for the given ID"""
    try:
        for video_id, status in conversion_status.items():
            if status.task_id == task_id:
                if status.status == "completed":
                    mp3_path = status.mp3_path
                    return FileResponse(mp3_path, filename=os.path.basename(mp3_path))
                elif status.status == "failed":
                    raise HTTPException(status_code=400, detail="Conversion failed")
                else:
                    raise HTTPException(status_code=400, detail="Conversion in progress")
    except HTTPException as err:
        print(err)
