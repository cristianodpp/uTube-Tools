# Youtube Tools
Python Script with a few tools to handle youtube videos from the list (file txt).
The script have 3 options (Download Video, Download Audio, Create a video) and will run automatically reading the file youtube_video_links (here you put the video id, start time and end time).

[![Software License](https://img.shields.io/badge/license-MIT-brightgreen.svg?style=flat-square)](LICENSE.md)

This project uses [pytube](https://github.com/nficano/pytube) to download the video or audio, [ffmeg](https://github.com/FFmpeg/FFmpeg) to process multimedia content and [moviepy](https://github.com/Zulko/moviepy) to video editing.

## Requirements
    - python3 
    - pytube 
    - ffmpeg 
    - moviepy 

## Install
    Install the latest version of python 3. 

    ``` bash
        $ brew install python3
    ```
    ``` bash
        $ pip3 install pytube
    ```
    ``` bash
        $ pip3 install ffmpeg
    ```
    ``` bash
        $ pip3 install moviepy
    ```

