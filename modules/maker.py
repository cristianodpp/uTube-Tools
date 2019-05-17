from moviepy.editor import *
import errno
import os
import json
import datetime

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

        clipList = []
        concatenateClipList = []
        concatenateClipCount = 0
        
        # Prepare Open to json fiel
        with open('youtube_video_links.json') as json_file:
            
            # Read a json file with videos and put on var
            videoList = json.load(json_file)
            
            # Counter to clips
            clipCount = 0

            # Select the intervals from subclips
            for item in videoList['video_list']:
                clipList.append(VideoFileClip("videos/"+item['video_id']+".mp4").subclip(t_start=item['t_start'], t_end=item['t_end']))
                clipCount += 1
    
        # Set effects for each clip
        for clip in clipList:
            if(concatenateClipCount == 0):
                concatenateClipList.append(clip.set_start(0).crossfadein(0.5).audio_fadeout(clip.start))
            else:
                concatenateClipList.append(clip.crossfadein(1).audio_fadein(clip.end-1).audio_fadeout(clip.end))
            concatenateClipCount += 1
        
        # End the show
        closeClip = TextClip('Thanks for whatching', color='white', font="Amiri-Bold",
                             kerning=5, fontsize=100, bg_color='black').set_duration(5)
        
        # Push to concatenate clips 
        concatenateClipList.append(closeClip)

        # Execute the concatenate of clips
        final_clip = concatenate(
            concatenateClipList, padding=-1, method="compose")

        # Get time now
        dateToday = datetime.datetime.today()
        dateToday = dateToday.strftime('%Y%m%d%H%M%S')
        
        # Render the video
        final_clip.write_videofile(
            SAVE_PATH_VIDEOS + dateToday +".mp4", fps=60, codec='libx264', audio_codec='aac', remove_temp=True)

        print("--- Task Completed")
