from typing import Union
from fastapi import FastAPI, HTTPException, Request, Query
from pytube import YouTube
from pytube.exceptions import PytubeError
from starlette.responses import FileResponse
from schemas import Convert 
from urllib.parse import parse_qs, urlparse
import logging
import re
import uuid
import os

app = FastAPI()
conversion_status = {}

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s]: %(message)s",
    handlers=[
        logging.StreamHandler(),
    ]
)
logger = logging.getLogger(__name__)


@app.get("/convert/")
async def get_url_id(request: Request, url: str = Query(...)) -> Convert:
    """Returns a converted ID for the given URL"""

    raw_url = url
    if raw_url is None:
        raise HTTPException(status_code=400, detail="Error: URL parameter 'url' is missing")


    try:
        # Unique task id for every url
        task_id = str(uuid.uuid4())

        # Check if the url is correct
        if not re.match(r'^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+$', url):
            raise HTTPException(status_code=404, detail="Error: URL not found")

        query_params = parse_qs(urlparse(raw_url).query)
        video_id = query_params.get("v", [None])[0]
        if not video_id:
            raise HTTPException(status_code=404, detail="Error: Unable to extract video ID from link")

        # video_id = None
        # if "/watch?v=" in raw_url:
        #     video_id = raw_url.split("/watch?v=")[1][:11]
        # elif "/v/" in raw_url:
        #     video_id = raw_url.split("/v/")[1][:11]
        # elif "youtu.be/" in raw_url:
        #     video_id = raw_url.split("youtu.be/")[1][:11]
        #     logger.info(f"Extraction completed for video_id: {video_id}")
        # if not video_id:
        #     raise HTTPException(status_code=404, detail="Error: Unable to extract video ID from link")
        # logger.error(f"Extraction failed for video_id: {video_id}")

        # video_id_match = re.search(r'(?:[?&]v=|\/)([0-9A-Za-z_-]{11})', raw_url)
        # if video_id_match is None:
        #     raise HTTPException(status_code=404, detail="Error: Unable to extract video ID from link")
         # video_id = video_id_match.group(1)
       

        # Update conversion status
        if video_id in conversion_status:
            status = conversion_status[video_id]["status"]
            if status == "completed":
                return {"status": status,
                        "message": "Conversion already completed"}
            elif status == "in progress":
                return {"status": status,
                        "message": "Conversion already in progress"}

        # Get YT object, convert, download
        yt = YouTube(video_id)
        video = yt.streams.filter(only_audio=True).first()
        video_path = f"temp_{task_id}.mp4"
        video.download(filename=video_path)

        mp3_path = f"{task_id}.mp3"
        os.system(f"ffmpeg -i {video_path} {mp3_path}")
        os.remove(video_path)
        
        conversion_status[video_id] = {"status": "completed", "mp3_path": mp3_path, "task_id": task_id}
        logger.info(f"Conversion completed for task_id: {task_id}")
        return {"status": "completed",
                "message": "Conversion completed",
                "task_id": task_id}


    except PytubeError as err:    
        conversion_status[video_id] = {"status": "failed",
                                       "error": str(err)}
        logger.error(f"Conversion failed for task_id: {task_id}, Error: {str(err)}")
        raise HTTPException(status_code=400, detail=str(err))

 
@app.get("/status/{task_id}")
async def check_download_status(task_id: str):
    """Returns the status for the given ID"""
    try:
        if task_id in conversion_status:
            return conversion_status[task_id]
        else:
            raise HTTPException(status_code=404, detail="Video ID not found")
    except HTTPException as err:
        print(err)

    
@app.get("/download/{task_id}")
async def download_mp3(task_id: str):
    """Downloads the audio file for the given ID"""
    try:
        for video_id, status in conversion_status.items():
            if status["task_id"] == task_id:
                if status["status"] == "completed":
                    mp3_path = status["mp3_path"]
                    return FileResponse(mp3_path, filename=os.path.basename(mp3_path))
                elif status["status"] == "failed":
                    raise HTTPException(status_code=400, detail="Conversion failed")
                else:
                    raise HTTPException(status_code=400, detail="Conversion in progress")
    except HTTPException as err:
        print(err)
