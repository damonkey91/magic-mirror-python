import tkinter as tk
from tkinter.constants import *
from datetime import datetime, timedelta, time


class DayCountDown():
    def __init__(self, main_window: tk.Tk, font=('caviar dreams', 130), bg='black', fg='white'):
        self.count_down = tk.Label(main_window, font=font, bg=bg, fg=fg)
        self._tick()

    def place(self, relx:float, rely:float):
        self.count_down.place(relx=relx, rely=rely, anchor=CENTER)

    def pack(self, in_, side, expand=YES):
        self.count_down.pack(in_=in_, side=side, expand=expand)

    def _tick(self):
        time_left = self._time_until_end_of_day()

        self.count_down.config(text=time_left)
        self.count_down.after(1000, self._tick)

    def _time_until_end_of_day(self, dt=None):
        if dt is None:
            dt = datetime.now()
        tomorrow = dt + timedelta(days=1)
        time_left = datetime.combine(tomorrow, time.min) - dt
        return str(time_left).split('.', 2)[0]
