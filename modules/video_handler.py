from pytube import YouTube
import core
import json

class videoHandlerClass:

    def getVideo(self, videoId):
        videoDetail = YouTube(core.YOUTUBE_LINK+videoId)
        
        # Title
        print("--- Title = " + videoDetail.title)
        
        # Downloading
        print("--- Downloading")
        YouTube(core.YOUTUBE_LINK+videoId).streams.first().download(
            output_path=core.SAVE_PATH_VIDEOS, filename=videoId)

    def downloadVideos(self):
        # Run the script
        print("--- Starting video downloads")

        with open('youtube_video_links.json') as json_file:
            data = json.load(json_file)
            for item in data['video_list']:
                self.getVideo(item['video_id'])

            # Completion
            print("--- Task Completed")
        print(60*"=")
