import os
import tkinter as tk
from tkinter import font
from tkinter_videoplayer import VideoPlayer

video_path = "example.mp4"
video_path = os.path.join(os.path.dirname(__file__), video_path)

root = tk.Tk()
root.title("Tkinter Video - Combined Examples")
root.geometry("1400x900")

# Custom font for titles
title_font = font.Font(family="Arial", size=20, weight="bold")
code_font = font.Font(family="Consolas", size=10)

main_frame = tk.Frame(root)
main_frame.pack(expand=True, fill=tk.BOTH)

# 2x2 grid
for i in range(2):
    main_frame.grid_rowconfigure(i, weight=1)
for j in range(2):
    main_frame.grid_columnconfigure(j, weight=1)

examples = [
    {
        "title": "Basic Hello World",
        "args": "VideoPlayer(root, video_path=video_path, height=240)",
        "player_args": {"video_path": video_path, "height": 240},
    },
    {
        "title": "Video Without Controls",
        "args": "VideoPlayer(root, video_path=video_path, controls=False, autoplay=True, loop=True, height=240)",
        "player_args": {"video_path": video_path, "controls": False, "autoplay": True, "loop": True, "height": 240},
    },
    {
        "title": "Looping Video",
        "args": "VideoPlayer(root, video_path=video_path, loop=True, autoplay=True, height=240)",
        "player_args": {"video_path": video_path, "loop": True, "autoplay": True, "height": 240},
    },
    {
        "title": "Autoplay Video",
        "args": "VideoPlayer(root, video_path=video_path, autoplay=True, height=240)",
        "player_args": {"video_path": video_path, "autoplay": True, "height": 240},
    },
]

for idx, ex in enumerate(examples):
    row, col = divmod(idx, 2)
    frame = tk.Frame(main_frame, bd=2, relief=tk.RIDGE, padx=10, pady=10)
    frame.grid(row=row, column=col, sticky="nsew", padx=10, pady=10)

    title = tk.Label(frame, text=ex["title"], font=title_font)
    title.pack(anchor="n")

    player = VideoPlayer(frame, **ex["player_args"])
    player.frame.pack(pady=10)

    code_label = tk.Label(frame, text=ex["args"], font=code_font, fg="#333", bg="#f4f4f4", anchor="w", justify="left")
    code_label.pack(fill=tk.X, pady=5)

root.mainloop()
