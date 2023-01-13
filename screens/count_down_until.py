import tkinter as tk
from tkinter.constants import *
from widgets.date_count_down import DateCountDown
from datetime import datetime
from helpers.constants import root_project_path
import os

class CountDown:
    def __init__(self, main_window: tk.Tk):
        stop_date = datetime(2023, 2, 22, 16, 0, 0)

        header = tk.Label(main_window, font=('caviar dreams', 30), bg='black', fg='white')
        header.place(relx=0.5, rely=0.25, anchor=CENTER)
        header.config(text=f"Birthday 22 February.")

        ROOT_DIR = root_project_path
        heart_image_path = os.path.join(ROOT_DIR, "resources", "heart joke.png")

        broken_heart_canvas = tk.Canvas(main_window, bg='black', highlightthickness=0)
        broken_heart_canvas.place(relx=0.5, rely=0.75, anchor=CENTER)
        main_window.img_broken_heart = img_broken_heart = tk.PhotoImage(master=broken_heart_canvas, file=heart_image_path)
        broken_heart_canvas.create_image(0, 0, anchor=NW, image=img_broken_heart)
        broken_heart_canvas.config(width=img_broken_heart.width(), height=img_broken_heart.height())

        path_crying_face = os.path.join(ROOT_DIR, "resources", "loudly-crying-face.png")

        canvas_crying_face = tk.Canvas(main_window, bg='black', highlightthickness=0)
        canvas_crying_face.place(relx=0.5, rely=0.5, anchor=CENTER)
        main_window.img_crying_face = img_crying_face = tk.PhotoImage(master=canvas_crying_face,
                                                                        file=path_crying_face)
        canvas_crying_face.create_image(0, 0, anchor=NW, image=img_crying_face)
        canvas_crying_face.config(width=img_crying_face.width(), height=img_crying_face.height())

        count_down_label = DateCountDown(main_window, font=('caviar dreams', 80), bg='black', fg='white')
        count_down_label.place(relx=0.5, rely=0.35, anchor=CENTER)
        count_down_label.set_stop_date(stop_date)