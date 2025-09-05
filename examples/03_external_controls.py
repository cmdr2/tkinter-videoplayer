import os
from tkinter_videoplayer import VideoPlayer
import tkinter as tk

# get the path to example.mp4
video_path = "example.mp4"
video_path = os.path.join(os.path.dirname(__file__), video_path)

if not os.path.exists(video_path):
    raise FileNotFoundError(f"Video file not found: {video_path}")

# make the video
root = tk.Tk()
root.title("External Controls Example")
player = VideoPlayer(root, video_path=video_path, controls=False, height=360)
player.frame.pack()

controls_frame = tk.Frame(root)
controls_frame.pack(pady=10)

root.resizable(False, False)


def play():
    player.play()


def pause():
    player.pause()


def stop():
    player.stop()


def jump_to_1():
    player.currentTime = 1.0


def jump_to_2():
    player.currentTime = 2.0


btn_play = tk.Button(controls_frame, text="Play", command=play)
btn_pause = tk.Button(controls_frame, text="Pause", command=pause)
btn_stop = tk.Button(controls_frame, text="Stop", command=stop)
btn_jump1 = tk.Button(controls_frame, text="Jump to 1s", command=jump_to_1)
btn_jump2 = tk.Button(controls_frame, text="Jump to 2s", command=jump_to_2)

btn_play.pack(side=tk.LEFT, padx=5)
btn_pause.pack(side=tk.LEFT, padx=5)
btn_stop.pack(side=tk.LEFT, padx=5)
btn_jump1.pack(side=tk.LEFT, padx=5)
btn_jump2.pack(side=tk.LEFT, padx=5)

root.mainloop()
