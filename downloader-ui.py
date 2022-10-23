from cProfile import label
from email.mime import image
from importlib.resources import path
from tkinter import *
from tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube

import shutil

# functions


def select_path():
    # allows user to select path in the computer explorer
    path = filedialog.askdirectory()
    path_label.config(text=path)


def download_file():
    # get user path
    get_link = link_field.get()
    # get selected path
    user_path = path_label.cget("text")
    screen.title('downloading...')
    # download video
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    video_clip = VideoFileClip(mp4_video)
    video_clip.close()
    # move file to selected save folder
    shutil.move(mp4_video, user_path)
    screen.title('download complete!')


screen = Tk()
title = screen.title('youtube downloader')
canvas = Canvas(screen, width=500, height=500)
canvas.pack()

# logo
logo_img = PhotoImage(file='images.png')
canvas.create_image(250, 80, image=logo_img)
# resize
#logo_img = logo_img.subsample(5, 5)

# yt link field
link_field = Entry(screen, width=50)
link_label = Label(screen, text="enter a youtube link: ", font=('Arial', 15))

# select path to download
path_label = Label(
    screen, text="select where would you like to download: ", font=('Arial', 15))
select_btn = Button(screen, text="select", command=select_path)

# add "path to download to" window
canvas.create_window(250, 280, window=path_label)
canvas.create_window(250, 330, window=select_btn)

# add things to canvas
canvas.create_window(250, 210, window=link_label)
canvas.create_window(250, 250, window=link_field)

# download btns
download_btn = Button(screen, text="download file", command=download_file)
# add path button to the canvas
canvas.create_window(250, 390, window=download_btn)

screen.mainloop()
