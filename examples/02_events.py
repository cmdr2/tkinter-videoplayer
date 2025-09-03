import os
from tkinter_video import VideoPlayer
import tkinter as tk
from tkinter import messagebox

# get the path to example.mp4
video_path = "example.mp4"
video_path = os.path.join(os.path.dirname(__file__), video_path)

root = tk.Tk()
root.title("Events Example - MessageBox")
player = VideoPlayer(root, video_path=video_path, height=360)
player.frame.pack()


def on_play():
    messagebox.showinfo("Event", "Video started!")


def on_pause():
    messagebox.showinfo("Event", "Video paused.")


def on_ended():
    messagebox.showinfo("Event", "Video ended.")


player.add_event_listener("play", on_play)
player.add_event_listener("pause", on_pause)
player.add_event_listener("ended", on_ended)

root.mainloop()
