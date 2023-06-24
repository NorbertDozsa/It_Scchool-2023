from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, FileResponse
from pathlib import Path
from schemas import *
from pytube import *
import sys
import os

app = FastAPI()
ROOT = Path(__file__).parent
DOWNLOAD = ROOT / 'download'

@app.get("/convert/{url}")
async def convert_url(url: str) -> Convert:
    """Converts YouTube URL to a specific ID"""
    DOWNLOAD.mkdir(exist_ok=True)
    yt = YouTube(str(url))
    audio_stream = yt.streams.filter(only_audio=True).first()
    out_file = audio_stream.download(DOWNLOAD)

    return FileResponse("DOWNLOAD/outfile.mp4") 

