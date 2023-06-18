from fastapi import FastAPI, HTTPException
from pytube import YouTube, extract
from pytube.exceptions import PytubeError
from starlette.responses import FileResponse
import uvicorn
import os
import uuid

app = FastAPI()
conversion_status = {}
url = "https://www.youtube.com/watch?v=HjL9wodEx08"
@app.get("/convert/")
async def convert_to_mp3(url: str):
    try:
        # Generate a unique ID for the conversion task
        task_id = str(uuid.uuid4())

        # Extract the video ID from the URL
        video_id = extract.video_id(url)

        # Check if the video ID is already in progress or completed
        if video_id in conversion_status:
            status = conversion_status[video_id]["status"]
            if status == "completed":
                return {"status": status, "message": "Conversion already completed", "task_id": conversion_status[video_id]["task_id"]}
            elif status == "in progress":
                return {"status": status, "message": "Conversion already in progress", "task_id": conversion_status[video_id]["task_id"]}

        # Download the YouTube video
        yt = YouTube(video_id)
        video = yt.streams.filter(only_audio=True).first()
        video_path = f"temp_{task_id}.mp4"
        video.download(filename=video_path)

        # Store the conversion status
        conversion_status[video_id] = {"status": "in progress", "task_id": task_id}

        # Perform the conversion to MP3
        mp3_path = f"{task_id}.mp3"
        os.system(f"ffmpeg -i {video_path} {mp3_path}")

        # Remove the temporary video file
        os.remove(video_path)

        # Update the conversion status to completed
        conversion_status[video_id] = {"status": "completed", "mp3_path": mp3_path, "task_id": task_id}

        return {"status": "completed", "message": "Conversion completed", "task_id": task_id}

    except PytubeError as e:
        # Mark conversion as failed if an error occurs
        conversion_status[video_id] = {"status": "failed", "error": str(e), "task_id": task_id}
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/status/{task_id}")
async def check_status(task_id: str):
    for video_id, status in conversion_status.items():
        if status["task_id"] == task_id:
            return status
    raise HTTPException(status_code=404, detail="Task ID not found")

@app.get("/download/{task_id}")
async def download_file(task_id: str):
    for video_id, status in conversion_status.items():
        if status["task_id"] == task_id:
            if status["status"] == "completed":
                mp3_path = status["mp3_path"]
                return FileResponse(mp3_path, filename=os.path.basename(mp3_path))
            elif status["status"] == "failed":
                raise HTTPException(status_code=400, detail="Conversion failed")
            else:
                raise HTTPException(status_code=400, detail="Conversion in progress")
    raise HTTPException(status_code=404, detail="Task ID not found")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
