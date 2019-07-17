from pathlib import Path
from pytube import YouTube
import prepare
import core
import json

class videoHandlerClass:

    def getVideo(self, videoId):
        videoDetail = YouTube(prepare.YOUTUBE_LINK+videoId)

        # Title
        print("--- Title = " + videoDetail.title)

        # Downloading
        print("--- Downloading")
        YouTube(prepare.YOUTUBE_LINK+videoId).streams.first().download(
            output_path=prepare.SAVE_PATH_VIDEOS, filename=videoId)

    def downloadVideos(self):
        # Run the script
        print("--- Starting video downloads")

        with open('youtube_video_links.json') as json_file:
            data = json.load(json_file)
            for item in data['video_list']:
                fileName = Path(prepare.SAVE_PATH_VIDEOS +
                                item['video_id']+'.mp4')
                if not fileName.exists():
                    self.getVideo(item['video_id'])
                else:
                    print(
                        f"----- File < {item['video_id']}.mp4 > already downloaded.")

            # Completion
            print("--- Task Completed")

            # Call menu
            core.coreClass().main()
        print(60*"=")
