import tkinter as tk
from PIL import Image, ImageTk

class AnimatedGifLabel(tk.Label):
    def __init__(self, master, file_path, size=(200, 200), **kwargs):
        super().__init__(master, **kwargs)
        self.file_path = file_path
        self.frames = []
        self.size = size

        self.load_frames()

    def load_frames(self):
        gif = Image.open(self.file_path)
        try:
            while True:
                # Resize the frame to the specified size
                frame_resized = gif.resize(self.size)
                self.frames.append(ImageTk.PhotoImage(frame_resized))
                gif.seek(gif.tell() + 1)
        except EOFError:
            pass

    def animate(self, index=0):
        self.config(image=self.frames[index])
        self.after(100, lambda: self.animate((index + 1) % len(self.frames)))

    def config_image(self, file_path):
        self.file_path = file_path
        self.frames = []
        self.load_frames()