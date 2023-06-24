from fastapi import FastAPI
from pytube import YouTube
from moviepy.editor import AudioFileClip

app = FastAPI()

@app.get("/download/{url}")
async def download_yt_audio(url: str):
    try:
        yt = YouTube(url)
        audio_stream = yt.streams.filter(only_audio=True).first()

        # Download the audio stream as a .mp4 file
        audio_file = audio_stream.download()

        # Use moviepy to convert the .mp4 file to a .mp3 file
        audio_clip = AudioFileClip(audio_file)
        mp3_file = audio_file[:-4] + ".mp3"
        audio_clip.write_audiofile(mp3_file)

        return {"message": "Audio downloaded and converted successfully", "mp3_file": mp3_file}
    except Exception as e:
        return {"message": "Error occurred while downloading audio", "error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
