from typing import Union
from fastapi import FastAPI, HTTPException
import youtube_dl
from pathlib import Path
from schemas import *
from starlette.responses import FileResponse
import logging
import re
import uuid
import os

ROOT = Path(__file__).parent
DOWNLOAD = ROOT / 'download'

app = FastAPI()
# conversion_status = {}

# logging.basicConfig(
#     level=logging.INFO,
#     format="%(asctime)s [%(levelname)s]: %(message)s",
#     handlers=[
#         logging.StreamHandler(),
#     ]
# )
# logger = logging.getLogger(__name__)


@app.post("/convert")
async def convert(url: Url):

    try:
        task_id = str(uuid.uuid4())
        
        video_info = youtube_dl.YoutubeDL().extract_info(url= url, download= False)
        file_name = f"{video_info['title']}"       
        options = {
            'format':'bestaudio/best',
            'keepvideo':False,
            'outtmpl':file_name,
        }
        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download([video_info['webpade_url']])
        
        return {
            "task_id": task_id,
            "url": url,
            }
    
    except Exception as err:
        print(err)
 
# @app.get("/status/{task_id}")
# async def check_download_status(video_id: Convert):
#     """Returns the status for the given ID"""
#     try:
#         if video_id in conversion_status:
#             return conversion_status[video_id]
#         else:
#             raise HTTPException(status_code=404, detail="Video ID not found")
#     except HTTPException as err:
#         print(err)

    
# @app.get("/download/{task_id}")
# async def download_mp3(task_id: str) -> FileResponse:
#     """Downloads the audio file for the given ID"""
#     try:
#         for video_id, status in conversion_status.items():
#             if status["task_id"] == task_id:
#                 if status["status"] == "completed":
#                     mp3_path = status["mp3_path"]
#                     return FileResponse(mp3_path, filename=os.path.basename(mp3_path))
#                 elif status["status"] == "failed":
#                     raise HTTPException(status_code=400, detail="Conversion failed")
#                 else:
#                     raise HTTPException(status_code=400, detail="Conversion in progress")
#     except HTTPException as err:
#         print(err)


