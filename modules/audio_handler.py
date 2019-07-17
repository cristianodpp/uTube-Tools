from pytube import YouTube
from pathlib import Path
import prepare
import core
import os
import sys
import errno
import subprocess
import json


class audioHandlerClass:

    def extractSingleAudio(self, _filename):
        # Downloading
        print("--- Extracting Audio "+_filename)
        command = "ffmpeg -i "+prepare.SAVE_PATH_VIDEOS+_filename+'.mp4' + \
            " -vn -ar 44100 -ac 2 -b:a 192k "+prepare.SAVE_PATH_AUDIOS+_filename+'.mp3'
        subprocess.call(command, shell=True)
        print("--- "+_filename+" audio extracted")

    def downloadAudios(self):
        # Run the script
        print(60*"=")
        print("Extract Audios from youtube videos")
        files = [os.path.splitext(filename)[0]
                 for filename in os.listdir('./Videos')]
        for video_id in files:
            fileName = Path(prepare.SAVE_PATH_AUDIOS + video_id+'.mp3')
            if not fileName.exists():
                self.extractSingleAudio(video_id)
            else:
                print(
                    f"----- File < {video_id}.mp3 > already downloaded.")

        print("--- Task Completed")

        # Call menu
        core.coreClass().main()
