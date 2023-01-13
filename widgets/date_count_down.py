import tkinter as tk
from tkinter.constants import *
from datetime import datetime
from helpers.widget_kwargs_functions import *


class DateCountDown(tk.LabelFrame):
    def __init__(self, *args, **kwargs):
        self.stop_date = datetime.now()
        set_default_color_if_not_specified(kwargs)
        super().__init__(*args, **kwargs)
        self.config(borderwidth=0)
        background_color = kwargs.get("bg")
        foreground_color = kwargs.get('fg')
        font = kwargs.get('font')

        units = ["  DAYS   ", "  HOURS  ", " MINUTES ", " SECONDS "]
        self.value_labels = []
        for unit in units:
            unit_frame = tk.LabelFrame(self, kwargs)
            unit_frame.config(borderwidth=0)
            value_label = tk.Label(unit_frame, font=font, bg=background_color, fg=foreground_color)
            value_label.pack(in_=unit_frame, side=TOP, expand=TRUE)
            self.value_labels.append(value_label)
            unit_label = tk.Label(unit_frame, font=(font[0], int(font[1]/3.5)), bg=background_color, fg=foreground_color)
            unit_label.pack(in_=unit_frame, side=TOP, expand=TRUE)
            unit_label.config(text=unit)
            unit_frame.pack(in_=self, side=LEFT, expand=TRUE)


    def set_stop_date(self, stop_date):
        self.stop_date = stop_date
        self._update()

    def _update(self):
        values = self._time_until_stop_date(self.stop_date)
        for i in range(len(self.value_labels)):
            self.value_labels[i].config(text=values[i])
        self.after(1000, self._update)

    @staticmethod
    def _time_until_stop_date(stop_date):
        time_left = stop_date - datetime.now()
        days = time_left.days
        count_hours, remaining = divmod(time_left.seconds, 3600)
        count_minutes, count_seconds = divmod(remaining, 60)
        return days, count_hours, count_minutes, count_seconds
