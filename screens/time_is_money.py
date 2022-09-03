import tkinter as tk
from tkinter.constants import *
from widgets.clock import Clock
from widgets.day_count_down import DayCountDown

class TimeIsMoney:
    def __init__(self, main_window: tk.Tk):
        time_is_money = tk.Label(main_window, font=('caviar dreams', 80), bg='black', fg='white')
        time_is_money.place(relx=0.5, rely=0.5, anchor=CENTER)
        time_is_money.config(text="Time is money!")

        clock = Clock(main_window)
        clock.place(0.5, 0.25)

        time_left_container = tk.Label(main_window)
        time_left_container.place(relx=0.5, rely=0.75, anchor=CENTER)
        time_left_container.configure(background='black')
        time_left_label = tk.Label(main_window, font=('caviar dreams', 30), bg='black', fg='white')
        time_left_label.pack(in_=time_left_container, side=TOP)
        time_left_label.config(text="Remaining work hours:")

        count_down = DayCountDown(main_window)
        count_down.pack(in_=time_left_container, side=BOTTOM)
