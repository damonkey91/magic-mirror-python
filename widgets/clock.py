import tkinter as tk
from tkinter.constants import *
from datetime import datetime


class Clock:
    def __init__(self, main_window: tk.Tk, font=('caviar dreams', 130), bg='black', fg='white'):
        self.clock = tk.Label(main_window, font=font, bg=bg, fg=fg)
        self._tick()

    def place(self, relx:float, rely:float):
        self.clock.place(relx=relx, rely=rely, anchor=CENTER)

    def pack(self, in_, side, expand=YES):
        self.clock.pack(in_=in_, side=side, expand=expand)

    def _tick(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")

        self.clock.config(text=current_time)
        self.clock.after(1000, self._tick)
