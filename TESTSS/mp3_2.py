from pytube import YouTube
import moviepy.editor as mp

def download_youtube_video(url):
    youtube = YouTube(url)
    video = youtube.streams.filter(only_audio=True).first()
    # video.download()
    print(video)
def convert_to_mp3(filename):
    video_clip = mp.VideoFileClip(filename)
    mp3_filename = filename[:-4] + ".mp3"
    video_clip.audio.write_audiofile(mp3_filename)
    video_clip.close()


youtube_url = "https://www.youtube.com/watch?v=8bwGMnIWVlY"
video_filename = "video.mp4"

download_youtube_video(youtube_url)
convert_to_mp3(video_filename)
