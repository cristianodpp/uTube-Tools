import errno
import os

SAVE_PATH_VIDEOS = "./videos/"
SAVE_PATH_AUDIOS = "./audios/"
SAVE_PATH_VIDEOS_COMPILED = "./videos_compiled/"
YOUTUBE_LINK = "https://www.youtube.com/watch?v="

class prepareClass:
    def main(self):

        # Create folder if not exist
        if not os.path.exists(SAVE_PATH_VIDEOS):
            try:
                os.makedirs(SAVE_PATH_VIDEOS)
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise

        # Create folder if not exist
        if not os.path.exists(SAVE_PATH_VIDEOS_COMPILED):
            try:
                os.makedirs(SAVE_PATH_VIDEOS_COMPILED)
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