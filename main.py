from pytube import YouTube, Stream, StreamQuery
from pytube.exceptions import VideoUnavailable
import keyboard
import os
import ffmpeg



print("This is a YouTube video downloader program. To continue, ", end="")
print("please input your chosen URL. You will then be provided ", end="")
print("with a video or audio option to pick from.")
print("Once that is done, the file will be found in 'Downloads'.")
print("To close the program, press the 'esc' key")

while True:
    while True:
        try:
            url = input("Enter your YouTube URL here: ")
            yt = YouTube(url)
        except VideoUnavailable:
            print("Video is unavailable, try again")
        else:
            break  
    print(f"You inputted: {yt.title}")
    while True:
        audio_or_video = input("Enter audio/video for your preferred videotype: ")
        if audio_or_video in ["audio", "video"]:
            break
        else:
            audio_or_video = input("Try again: ")
    

    

    
keyboard.wait('esc')
print("Exited program")