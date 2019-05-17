from pytube import YouTube
from pathlib import Path
import os
import sys
import errno
import subprocess
import json

# Folder to save the videos
SAVE_PATH_VIDEOS = "./videos/"
SAVE_PATH_AUDIOS = "./audios/"

# Create folder if not exist
if not os.path.exists(SAVE_PATH_VIDEOS):
    try:
        os.makedirs(SAVE_PATH_VIDEOS)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

# Create folder if not exist
if not os.path.exists(SAVE_PATH_AUDIOS):
    try:
        os.makedirs(SAVE_PATH_AUDIOS)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

class audioHandlerClass:

    def extractSingleAudio(self, _filename):
        # Downloading
        print("--- Extracting Audio "+_filename)
        command = "ffmpeg -i "+SAVE_PATH_VIDEOS+_filename+".mp4" + \
            " -vn -ar 44100 -ac 2 -b:a 192k "+SAVE_PATH_AUDIOS+_filename+".mp3"
        subprocess.call(command, shell=True)
        print("--- "+_filename+" audio extracted")
        

    def downloadAudios(self):
        # Run the script
        print(60*"=")
        print("Extract Audios from youtube videos")
        files = [os.path.splitext(filename)[0]
                 for filename in os.listdir('./Videos')]
        for video_id in files:
            self.extractSingleAudio(video_id)
        print("--- Task Completed")
