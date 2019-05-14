from __future__ import unicode_literals
from pytube import YouTube
import os
import errno

# Folder to save the videos
SAVE_PATH = "./videos"

# link of the video to be downloaded
link = open('youtube_video_links.txt', 'r')  # opening the file

# Create folder if not exist
if not os.path.exists(SAVE_PATH):
    try:
        os.makedirs(SAVE_PATH)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

# Save video on the folder
def downloadVideo(videourl):
    
    print(60*"=")
    print("Downloading video -> "+i)
    print(60*"=")

    try:
        YouTube(videourl).streams.first().download(SAVE_PATH)
    except:
        print("Connection lost")

for i in link:
    downloadVideo(i)
