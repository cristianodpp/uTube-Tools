from moviepy.editor import VideoFileClip, concatenate_videoclips
from pytube import YouTube
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


class videoHandlerClass:

    def getVideo(self, _filename, videourl):
        videoTitle = YouTube(videourl).title
        
        # Title
        print("--- Title = " + videoTitle)
        
        # Downloading
        # https://www.youtube.com/watch?v=
        print("--- Downloading")
        YouTube(videourl).streams.first().download(
            output_path=SAVE_PATH_VIDEOS, filename=_filename) 

    def downloadVideos(self):
        # Run the script
        print("--- Starting video downloads")

        with open('youtube_video_links.json') as json_file:
            data = json.load(json_file)
            for item in data['video_list']:
                _filename = YouTube(item['video_id']).video_id

            # Completion
            print("--- Task Completed")
        print(60*"=")
