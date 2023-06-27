import re
from pytube import YouTube

def extract_video_id(url):
    # Extract the video ID from the URL using regex
    regex_pattern = 'r"(?<=v=|v\/|vi=|vi\/|youtu.be\/|\/v\/|\/e\/|embed\/|user\/\S+\/|shorts\/|attribution_link\?a\=|embed%\u200C\u200B2Fwatch%\u200C\u200B3Fv%\u200C\u200B3D|%2Fv%2F|embed%\u200C\u200B2Fwatch%\u200C\u200B3Fv%\u200C\u200B3D|youtu.be%\u200C\u200B2Fwatch%\u200C\u200B3Fv%\u200C\u200B3D|v=%2Fwatch%3Fv%3D)[^#&?]*"'
    match = re.search(regex_pattern, url)

    if match:
        video_id = match.group()
        return video_id
    else:
        return None

# Example usage
# url = "https://www.youtube.com/watch?v=ABC123xyz"
# video_id = extract_video_id(url)

# if video_id:
#     print("Video ID:", video_id)
#     # Use pytube to work with the video
#     # For example, you can download it:
#     try:
#         yt = YouTube(url)
#         yt.streams.first().download()
#     except Exception as e:
#         print("Error:", str(e))
# else:
#     print("No video ID found in the URL.")

extract_video_id("https://www.youtube.com/watch?v=ru1QMhYjN-Q&ab_channel=Rayzeh")