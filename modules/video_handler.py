from moviepy.editor import VideoFileClip, concatenate_videoclips
from pytube import YouTube
import os
import sys
import errno
import subprocess

# link of the video to be downloaded
link = open('youtube_video_links.txt', 'r')  # opening the file

# Folder to save the videos
SAVE_PATH_VIDEOS = "./videos/"
SAVE_PATH_AUDIOS = "./audios/"

# link of the video to be downloaded
link = open('youtube_video_links.txt', 'r')  # opening the file

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
        print("--- Downloading")
        YouTube(videourl).streams.first().download(
            output_path=SAVE_PATH_VIDEOS, filename=_filename)

    def downloadVideos(self):
        # Run the script
        print("--- Starting video downloads")
        for i in link:

            # Filename specification
            _filename = YouTube(i).video_id

            self.getVideo(_filename, i)
            #extractAudio(_filename, i)

            # Completion
            print("--- Task Completed")
        print(60*"=")
