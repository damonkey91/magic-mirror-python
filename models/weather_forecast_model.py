from datetime import datetime


class WeatherForecastDay:
    date: datetime = datetime(1970,1,1)
    prognosis: int
    max_temp: int = -273
    min_temp: int = -273
    temp_unit: str = "°C"
    precipitation: float = 0
    precipitation_unit: str = "mm"
    max_wind: int = -1
    min_wind: int = -1
    wind_unit: str = "m/s"

    def get_weekday_short(self):
        return self.date.strftime("%a")

    def get_day_and_month(self):
        day_month = self.date.strftime("%d %b")
        if day_month.startswith("0"):
            return day_month[1:len(day_month)]
        return day_month

    def get_max_temp_string(self):
        return f"{self.max_temp}{self.temp_unit}"

    def get_min_temp_string(self):
        return f"{self.min_temp}{self.temp_unit}"

    def get_precipitation_string(self):
        return f"{self.precipitation:.1f}{self.precipitation_unit}"

    def get_max_wind_string(self):
        return f"{self.max_wind}{self.wind_unit}"

    def get_min_wind_string(self):
        return f"{self.min_wind}{self.wind_unit}"


class WeatherForecast:
    now: WeatherForecastDay = WeatherForecastDay()
    forecasts: [WeatherForecastDay] = []