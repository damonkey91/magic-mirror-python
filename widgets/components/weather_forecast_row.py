import tkinter as tk
from tkinter.constants import *
from tkinter import ttk
from helpers.widget_kwargs_functions import set_default_color_if_not_specified
from models.weather_forecast_model import WeatherForecastDay
import os
from helpers.constants import root_project_path


class WeatherForecastRow(tk.Frame):
    def __init__(self, *args, **kwargs):
        set_default_color_if_not_specified(kwargs)
        super().__init__(*args, **kwargs)
        background_color = self.cget('bg')

        separator = ttk.Separator(self, orient='horizontal')
        separator.pack(fill='x')

        self.day_label = tk.Label(self, font=('caviar dreams', 20), bg=background_color, fg='white')
        self.day_label.pack(in_=self, side=LEFT, expand=YES)

        self.weather_symbol = tk.Canvas(self, bg=background_color, highlightthickness=0)
        self.weather_symbol.pack(in_=self, side=LEFT, expand=YES)

        temp_frame = tk.Frame(self)
        temp_frame.pack(in_=self, side=LEFT, expand=YES)
        temp_frame.configure(bg=background_color)

        self.max_temp_label = tk.Label(temp_frame, font=('caviar dreams', 20), bg=background_color, fg='white')
        self.max_temp_label.pack(in_=temp_frame, side=TOP, expand=YES)

        self.min_temp_label = tk.Label(temp_frame, font=('caviar dreams', 20), bg=background_color, fg='white')
        self.min_temp_label.pack(in_=temp_frame, side=BOTTOM, expand=YES)

        self.precipitation_label = tk.Label(self, font=('caviar dreams', 20), bg=background_color, fg='white')
        self.precipitation_label.pack(in_=self, side=LEFT, expand=YES)

        wind_frame = tk.Frame(self)
        wind_frame.pack(in_=self, side=LEFT, expand=YES)
        wind_frame.configure(bg=background_color)

        self.max_wind_speed_label = tk.Label(wind_frame, font=('caviar dreams', 20), bg=background_color, fg='white')
        self.max_wind_speed_label.pack(in_=wind_frame, side=TOP, expand=YES)

        self.min_wind_speed_label = tk.Label(wind_frame, font=('caviar dreams', 20), bg=background_color, fg='white')
        self.min_wind_speed_label.pack(in_=wind_frame, side=BOTTOM, expand=YES)

    def update(self, day_forecast: WeatherForecastDay):
        ROOT_DIR = root_project_path
        weather_symbols_dir = os.path.join(ROOT_DIR, "resources", "SMHI_weather_icons")
        files = [filename for filename in os.listdir(weather_symbols_dir) if filename.startswith(f"{day_forecast.prognosis}_")]
        img_path = os.path.join(weather_symbols_dir, files[0])
        self.img = tk.PhotoImage(master=self.weather_symbol, file=img_path)
        self.img = self.img.subsample(int(self.img.height()/30)) # shrink the image
        self.weather_symbol.create_image(0, 0, anchor=NW, image=self.img)
        self.weather_symbol.config(width=self.img.width(), height=self.img.height())

        self.day_label.config(text=day_forecast.get_weekday_short())
        self.max_temp_label.config(text=day_forecast.get_max_temp_string())
        self.min_temp_label.config(text=day_forecast.get_min_temp_string())
        self.precipitation_label.config(text=day_forecast.get_precipitation_string())
        self.max_wind_speed_label.config(text=day_forecast.get_max_wind_string())
        self.min_wind_speed_label.config(text=day_forecast.get_min_wind_string())
