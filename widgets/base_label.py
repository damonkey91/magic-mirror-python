import tkinter as tk
from tkinter.constants import *


class BaseLabel(tk.Label):
    def __init__(self, *args, **kwargs):
        if 'bg' not in kwargs and 'background' not in kwargs:
            kwargs['bg'] = "black"
            kwargs['fg'] = "white"
        super().__init__(*args, **kwargs)
        self.bind('<Configure>', lambda e: self.config(wraplength=self.winfo_width()))
        self._update()

    def _update(self):
        self.config(text="base_label")
