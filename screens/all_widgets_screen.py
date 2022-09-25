import tkinter as tk
from tkinter.constants import *
from widgets.clock import Clock
from widgets.day_count_down import DayCountDown
from widgets.inspiration_quotes import InspirationQuotes
from widgets.dad_jokes import DadJokes
from widgets.joke_of_today import JokeOfToday
from widgets.quote_of_today import QuoteOfToday
from widgets.zen_quotes import ZenQuotes
from widgets.weather_forecast import WeatherForecast
from helpers.constants import *

class AllWidgets:
    def __init__(self, main_window: tk.Tk):
        weather = WeatherForecast(main_window, longitude=11.9697, latitude=57.7128, refresh_rate=EVERY_HOUR)
        weather.pack(in_=main_window, side=LEFT, expand=NO, anchor=NW)

        clock = Clock(main_window, font=('caviar dreams', 20))
        clock.pack(in_=main_window, side=LEFT, expand=FALSE)

        count_down = DayCountDown(main_window, font=('caviar dreams', 20))
        count_down.pack(in_=main_window, side=LEFT, expand=FALSE, anchor=N)

        inspiration_quote = InspirationQuotes(main_window, refresh_rate=EVERY_EIGHT_HOURS, font=('caviar dreams', 20))
        inspiration_quote.pack(in_=main_window, side=TOP, expand=TRUE)

        dad_jokes = DadJokes(main_window, refresh_rate=EVERY_EIGHT_HOURS, font=('caviar dreams', 20))
        dad_jokes.pack(in_=main_window, side=TOP, expand=TRUE)

        joke_of_today = JokeOfToday(main_window, font=('caviar dreams', 20))
        joke_of_today.pack(in_=main_window, side=TOP, expand=TRUE)

        quote_of_today = QuoteOfToday(main_window, font=('caviar dreams', 20))
        quote_of_today.pack(in_=main_window, side=TOP, expand=TRUE)

        zen_quotes = ZenQuotes(main_window, refresh_rate=EVERY_EIGHT_HOURS, font=('caviar dreams', 20))
        zen_quotes.pack(in_=main_window, side=TOP, expand=TRUE)
