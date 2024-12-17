from pytube import YouTube, Stream, StreamQuery
#import keyboard
#import os
#import ffmpeg

# keyboard.add_hotkey('esc', exit)
print("This is a YouTube video downloader program. To continue, ", end="")
print("please input your chosen URL. You will then be provided ", end="")
print("with a video or audio option to pick from.")
print("Once that is done, the file will be found in this folder.")
print("To close the program, press the 'esc' key")

while True:
    url = input("Enter your YouTube URL here: ")
    yt = YouTube(url)
    while True:
        audio_or_video = input("Enter audio/video for your preferred videotype: ")
        if audio_or_video in ["audio", "video"]:
            break
        else:
            audio_or_video = input("Try again: ")
    if audio_or_video == "audio":
        stream = yt.streams.get_audio_only()
    else:
        stream = yt.streams.get_highest_resolution()
    stream.download()

    
    
