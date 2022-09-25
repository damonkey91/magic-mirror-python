import tkinter as tk
from tkinter.constants import *
from widgets.components.weather_forecast_row import WeatherForecastRow
from http_requests.smhi import get_seven_days_forecast
from helpers.widget_kwargs_functions import *


class WeatherForecast(tk.Frame):
    def __init__(self, *args, **kwargs):
        self.lat = extract_latitude(kwargs)
        self.lon = extract_longitude(kwargs)
        self.refresh_rate = extract_refresh_rate(kwargs)
        set_default_color_if_not_specified(kwargs)
        super().__init__(*args, **kwargs)
        self.rows = []

        for _ in range(6):
            forecast_row = WeatherForecastRow(self)
            forecast_row.pack(in_=self, side=TOP, expand=TRUE)
            self.rows.append(forecast_row)
        self._update()

    def _update(self):
        weather_forecasts = get_seven_days_forecast(self.lon, self.lat)
        if weather_forecasts:
            for index, row in enumerate(self.rows):
                day_forecast = weather_forecasts.forecasts[index]
                row.update(day_forecast)
        self.after(self.refresh_rate, self._update)
