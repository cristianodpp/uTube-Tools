import errno
import os
from modules import audio_handler
from modules import video_handler
from modules import maker

class coreClass:
    def main(self):

        # Print the menu
        print("\n Options Available:")
        print("[1] - Download videos")
        print("[2] - Extract utube audio to mp3")
        print("[3] - Generate a new video")
        print("[0] - Exit")
        print("\n")

        # Select option
        option = input('Enter the number to execute: ')

        # Download videos from youtube
        if option == '1':
            videoHandler = video_handler.videoHandlerClass()
            videoHandler.downloadVideos()

        # Extract utube audio to mp3
        elif option == '2':
            audioHandler = audio_handler.audioHandlerClass()
            audioHandler.downloadAudios()

        # Generate a new video
        elif option == '3':
            makerHandler = maker.makerHandlerClass()
            makerHandler.generateVideo()

        # Exit
        elif option == '0':
            print("\n"+5*"*"+" closed "+5*"*"+"\n")
            sys.exit()
