from typing import Union
from fastapi import FastAPI, HTTPException
from pytube import YouTube
from pytube.exceptions import PytubeError
from pathlib import Path
from starlette.responses import FileResponse
import re
import uuid
import os

ROOT = Path(__file__).parent

app = FastAPI()
conversion_status = {}


@app.get("/convert/{url}")
async def get_url_id(url: str):
    """Returns a converted ID for the given URL"""

    try:
        task_id = str(uuid.uuid4())

        if not re.match(r'^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+$', url):
            raise HTTPException(status_code=404, detail="Error: URL not found")
        
        video_id = None

        if "/watch?v=" in url:
            video_id = url.split("/watch?v=")[1][:11]
        elif "/v/" in url:
            video_id = url.split("/v/")[1][:11]
        elif "youtu.be/" in url:
            video_id = url.split("youtu.be/")[1][:11]
        if not video_id:
            raise HTTPException(status_code=404, detail="Error: Unable to extract video ID from link")
        
        if video_id in conversion_status:
            status = conversion_status[video_id]["status"]
            if status == "completed":
                return {"status": status, "message": "Conversion already completed"}
            elif status == "in progress":
                return {"status": status, "message": "Conversion already in progress"}

        yt = YouTube(video_id)
        video = yt.streams.filter(only_audio=True).first()
        video_path = f"temp_{task_id}.mp4"
        video.download(filename=video_path)

        mp3_path = f"{task_id}.mp3"
        os.system(f"ffmpeg -i {video_path} {mp3_path}")
        os.remove(video_path)
        
        conversion_status[video_id] = {"status": "completed", "mp3_path": mp3_path, "task_id": task_id}

        return {"status": "completed", "message": "Conversion completed", "task_id": task_id}


    except PytubeError as err:    
        conversion_status[video_id] = {"status": "failed", "error": str(err)}
        raise HTTPException(status_code=400, detail=str(err))

 
@app.get("/status/{task_id}")
async def check_download_status(video_id: str):
    """Returns the status for the given ID"""
    try:
        if video_id in conversion_status:
            return conversion_status[video_id]
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
