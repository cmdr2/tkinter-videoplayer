import os
from tkinter_video import VideoPlayer
import tkinter as tk

# get the path to example.mp4
video_path = "example.mp4"
video_path = os.path.join(os.path.dirname(__file__), video_path)

root = tk.Tk()
root.title("Basic Hello World Video Player")
player = VideoPlayer(root, video_path=video_path, height=360)
player.frame.pack()
root.mainloop()
