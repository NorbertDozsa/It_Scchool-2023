from pytube import YouTube
from moviepy.editor import *
import re

def get_mp3_yt(url: str):
    yt = YouTube(url)
    audio_stream = yt.streams.filter(only_audio=True).first()

    # Download the audio stream as a .mp4 file
    audio_file = audio_stream.download()

    # Use moviepy to convert the .mp4 file to a .mp3 file
    audio_clip = AudioFileClip(audio_file)
    audio_clip.write_audiofile(audio_file[:-4] + ".mp3")


get_mp3_yt("https://www.youtube.com/watch?v=YhEtMIXlk-w&ab_channel=NeferLopez")