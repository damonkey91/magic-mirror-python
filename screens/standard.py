import tkinter as tk
from tkinter.constants import *

from widgets.clock import Clock
from widgets.inspiration_quotes import InspirationQuotes
from widgets.weather_forecast import WeatherForecast
from helpers.constants import *

class Standard:
    def __init__(self, main_window: tk.Tk):
        clock = Clock(main_window, font=('caviar dreams', 40))
        clock.pack(in_=main_window, side=TOP, expand=FALSE, pady=(10, 10))

        weather = WeatherForecast(main_window, longitude=11.9697, latitude=57.7128, refresh_rate=EVERY_HOUR)
        weather.pack(in_=main_window, side=TOP, expand=NO, anchor=NW)

        inspiration_quote = InspirationQuotes(main_window, refresh_rate=EVERY_EIGHT_HOURS, font=('caviar dreams', 20))
        inspiration_quote.pack(in_=main_window, side=BOTTOM, expand=FALSE, pady=(10, 10))
