from pathlib import Path
from moviepy.editor import *
import os
from multiprocessing import Pool


ROOT = Path(__file__).parent
SONGS = ROOT / "songs.txt"
SONGS_CLEAN1 = ROOT / "songs_clean1.txt"
SONGS_CLEAN2 = ROOT / "songs_clean2.txt"
DOWNLOADS = ROOT / "downloads"

file_list = [f for f in DOWNLOADS.iterdir() if f.is_file()]


def mp4_to_mp3(file):
    print(f"[{os.getpid()}] Converting {file.name}")
    mp3_name = f"{file.name.split('.')[0]}.mp3"
    mp3_path = file.parent / "mp3" / mp3_name

    videoclip = VideoFileClip(str(file))
    audioclip = videoclip.audio
    audioclip.write_audiofile(str(mp3_path))
    audioclip.close()
    videoclip.close()


if __name__ == "__main__":
    print(f"Converting {len(file_list)} files...")
    with Pool(8) as p:
        print(p.map(mp4_to_mp3, file_list))

