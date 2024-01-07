from pytube import YouTube
from pytube import Playlist
import gradio as gr 
import webbrowser
import os
import nest_asyncio
nest_asyncio.apply

file_path = "your file path goes here :)"


async def playlist(url:str, media:str) -> None:
    p = Playlist(url)
    for video in p.videos:
        gr.Info("Downloading -- {}".format(video.title))
        if media == "a":
            video.streams.filter(only_audio=True).first().download(file_path)
        elif media == "v":
            video.streams.get_highest_resolution().download(file_path)


def video(url:str, media:str) -> None:
    v = YouTube(url)
    gr.Info("Downloading {}".format(v.title))
    if media == "a":
        v.streams.filter(only_audio=True).first().download(file_path)
    elif media == "v":
        v.streams.get_highest_resolution().download(file_path)


async def mainCaller(url:str, type, batch):
    try:
        if type == 'Audio' and batch == 'Video':
            video(url, 'a')
        elif type == 'Audio' and batch == 'Playlist':
            await playlist(url, 'a')
        elif type == 'Audio + Video' and batch == 'Video':
            video(url, 'v')
        else:
            await playlist(url, 'v')
        return "Files have been downloaded! (Location:{})".format(file_path)
    except:
        gr.Error("Something has gone wrong (i.e., Age-Restrictions)")

demo = gr.Interface(
    fn=mainCaller,
    inputs=['text', 
            gr.Radio(['Audio', 'Audio + Video']),
            gr.Radio(['Video', 'Playlist'])],
    outputs=['text']
)
os.system('pip install pytube --upgrade')
os.system('pip install gradio --upgrade')
os.system('pip install nest_asyncio --upgrade')
browser= webbrowser.open_new("http://127.0.0.1:7860")
demo.launch()

