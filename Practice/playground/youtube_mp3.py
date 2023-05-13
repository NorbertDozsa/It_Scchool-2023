from pytube import YouTube
import requests
from pathlib import Path
from time import sleep
from moviepy.editor import *
import asyncio


ROOT = Path(__file__).parent
SONGS = ROOT / "songs.txt"
SONGS_CLEAN1 = ROOT / "songs_clean1.txt"
SONGS_CLEAN2 = ROOT / "songs_clean2.txt"
DOWNLOADS = ROOT / "downloads"

async def mp3_download(url):
    yt = YouTube(url)
    out_file = yt.streams.filter(progressive=True, file_extension='mp4')\
        .order_by("resolution")\
        .desc()\
        .first()\
        .download(output_path=DOWNLOADS)
    out_file_path = Path(out_file)
    print(f"Downloading {out_file_path.name}")
    mp3_name = f"{out_file_path.name.split('.')[0]}.mp3"
    mp3_path = out_file_path.parent / "mp3" / mp3_name

    # videoclip = VideoFileClip(str(out_file_path))
    # audioclip = videoclip.audio
    # audioclip.write_audiofile(str(mp3_path))
    # audioclip.close()
    # videoclip.close()


with SONGS_CLEAN2.open() as songs:
    url_list = songs.readlines()

async def main():
    await asyncio.gather(*[mp3_download(i) for i in url_list], return_exceptions=False)

asyncio.run(main())