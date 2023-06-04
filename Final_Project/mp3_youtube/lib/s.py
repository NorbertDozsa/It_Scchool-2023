from flask import Flask, request, jsonify
from pytube import YouTube
from pytube.exceptions import RegexMatchError
from pytube.exceptions import VideoUnavailable
from moviepy.editor import *
import os

app = Flask(__name__)

@app.route('/download', methods=['POST'])
def download_mp3():
    try:
        # Get the video URL from the request body
        video_url = request.json.get('video_url')

        # Download the video
        try:
            yt = YouTube(video_url)
        except (RegexMatchError, VideoUnavailable) as e:
            response = {
                'error': str(e)
            }
            return jsonify(response), 400

        video = yt.streams.get_audio_only()
        video.download()

        # Convert the downloaded video to MP3
        video_filename = video.default_filename
        mp4_file = video_filename
        mp3_file = mp4_file.replace(".mp4", ".mp3")
        video_clip = VideoFileClip(mp4_file)
        audio_clip = video_clip.audio
        audio_clip.write_audiofile(mp3_file)
        audio_clip.close()
        video_clip.close()

        # Delete the original video file
        os.remove(mp4_file)

        # Return the MP3 file path in the response
        response = {
            'mp3_file': mp3_file
        }
        return jsonify(response)

    except Exception as e:
        response = {
            'error': str(e)
        }
        return jsonify(response), 500

if __name__ == '__main__':
    app.run(debug=True)
