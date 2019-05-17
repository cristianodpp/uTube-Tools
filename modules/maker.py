from moviepy.editor import *
import errno
import os

SAVE_PATH_VIDEOS = "./videos_compiled/"

# Create folder if not exist
if not os.path.exists(SAVE_PATH_VIDEOS):
    try:
        os.makedirs(SAVE_PATH_VIDEOS)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise


class makerHandlerClass:

    def generateVideo(self):
        
        print('--- Generating a video')


        screensize = (720, 460)
        txtClip = TextClip('Cool effect', color='white', font="Amiri-Bold",
                        kerning=5, fontsize=100)

        clip1 = VideoFileClip("videos/HQMkxmtPZhg.mp4").subclip(t_start='00:15:00.00', t_end='00:15:05.00')
        clip2 = VideoFileClip("videos/e7KmVb9YOCk.mp4").subclip(t_start='00:04:00.00', t_end='00:04:05.00')
        clip3 = VideoFileClip("videos/PIraI9CNuzQ.mp4").subclip(t_start='00:06:00.00', t_end='00:06:05.00')
        
        final_clip = concatenate([
            clip1.set_start(0).crossfadein(0.5).audio_fadeout(clip2.start),
            clip2.crossfadein(1).audio_fadein(clip1.end-1).audio_fadeout(clip2.end),
            clip3.crossfadein(1).audio_fadein(clip2.end-1).audio_fadeout(clip3.end)],
            padding=-1, method="compose")

        final_clip.write_videofile(
            SAVE_PATH_VIDEOS + "my_concatenation.mp4", codec='libx264', audio_codec='aac', remove_temp=True)

        print("--- Task Completed")
