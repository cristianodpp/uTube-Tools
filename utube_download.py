from __future__ import unicode_literals
from pytube import YouTube
import os
import sys
import errno
import subprocess

# Hide errors
sys.tracebacklimit = 0

# Folder to save the videos
SAVE_PATH = "./videos/"
SAVE_PATH_TEMP = "./videos/temp_audio_files/"

# link of the video to be downloaded
link = open('youtube_video_links.txt', 'r')  # opening the file

# Create folder if not exist
if not os.path.exists(SAVE_PATH):
    try:
        os.makedirs(SAVE_PATH)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

# Create folder if not exist
if not os.path.exists(SAVE_PATH_TEMP):
    try:
        os.makedirs(SAVE_PATH_TEMP)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise


def downloadVideo(videourl):

    videoTitle = YouTube(videourl).title

    # Title
    print(60*"-")
    print("Title = " + videoTitle)

    # Filename specification
    _filename = YouTube(videourl).video_id

    # Downloading
    print("--- Downloading")
    YouTube(videourl).streams.first().download(
        output_path=SAVE_PATH, filename=_filename)

    # Downloading
    print("--- Extracting Audio")
    command = "ffmpeg -i "+SAVE_PATH+_filename+".mp4" + \
        " -vn -ar 44100 -ac 2 -b:a 192k "+SAVE_PATH_TEMP+_filename+".mp3"
    subprocess.call(command, shell=True)

    # Completion
    print(60*"-")
    print("--- Completed")

# Run the script
print(60*"=")
print("Pool Videos")
for i in link:
    downloadVideo(i)
print(60*"=")
