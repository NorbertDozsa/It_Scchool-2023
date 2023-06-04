from flask import Flask, request, jsonify
from pytube import YouTube
from pytube.exceptions import RegexMatchError, VideoUnavailable
from moviepy.editor import *
import os

app = Flask(__name__)

# @app.route('/convert')
# def convert(video_):
#     try:
#         video_url = request.args.get('url')
#         return video_url
#     except Exception as err:
#         print(err)

# convert("www.youtube.com/watch?v=dQw4w9WgXcQ")