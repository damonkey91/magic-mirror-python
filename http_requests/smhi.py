import requests
import json
from datetime import timedelta, datetime
import dateutil.parser
import pytz
from models.weather_forecast_model import WeatherForecastDay, WeatherForecast


def get_seven_days_forecast(lon, lat):
    response = requests.get(f"https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/{lon}/lat/{lat}/data.json")
    if response.ok:
        weather_forecast = WeatherForecast()
        json_response = json.loads(response.text)
        ten_days_compressed_forecasts = _compress_forecasts_to_days(json_response)
        for key_datetime, parameter_dict in ten_days_compressed_forecasts.items():
            weekday_forecast = _create_weekday_forecast(key_datetime, parameter_dict)
            weather_forecast.forecasts.append(weekday_forecast)

        for forecast in json_response["timeSeries"]:
            valid_time = forecast["validTime"]
            forecast_datetime = dateutil.parser.isoparse(valid_time)
            utc = pytz.UTC
            time_now = utc.localize(_hour_rounder(datetime.now()))
            if time_now <= forecast_datetime:
                forecast_datetime_string = _date_to_string_key(forecast_datetime)
                now_forecast_raw = {}
                _extract_values_from_forecast(forecast["parameters"], now_forecast_raw)
                now_forecast = _create_weekday_forecast(forecast_datetime_string, now_forecast_raw)
                weather_forecast.now = now_forecast
                break

        return weather_forecast


def _compress_forecasts_to_days(json_response):
    day_forecasts = {}
    for forecast in json_response["timeSeries"]:
        forecast_datetime = forecast["validTime"]
        forecast_date_string = _date_to_string_key(dateutil.parser.isoparse(forecast_datetime).date())
        if not(forecast_date_string in day_forecasts):
            day_forecasts[forecast_date_string] = {}
        _extract_values_from_forecast(forecast["parameters"], day_forecasts[forecast_date_string])
    return day_forecasts


def _date_to_string_key(date: datetime):
    return date.strftime("%Y/%m/%d")


def _extract_values_from_forecast(parameters: list, day_forecast: dict):
    for parameter in parameters:
        parameter_name = parameter["name"]
        if not (parameter_name in day_forecast):
            day_forecast[parameter_name] = []
        day_forecast[parameter_name].append(parameter["values"][0])


def _hour_rounder(date):
    # Rounds to nearest hour by adding a timedelta hour if minute >= 30
    return (date.replace(second=0, microsecond=0, minute=0, hour=date.hour)
               +timedelta(hours=date.minute//30))


def _create_weekday_forecast(datetime_string: str, parameters: dict):
    weather_forecast_day = WeatherForecastDay()
    weather_forecast_day.date = datetime.strptime(datetime_string, "%Y/%m/%d")
    weather_forecast_day.temp_unit = "°C"
    weather_forecast_day.wind_unit = "m/s"
    weather_forecast_day.precipitation_unit = "mm"

    for key, value_list in parameters.items():
        if key == "t": # t = air temperature
            weather_forecast_day.max_temp = int(max(value_list))
            weather_forecast_day.min_temp = int(min(value_list))
        elif key == "ws": # ws = wind speed
            weather_forecast_day.max_wind = int(max(value_list))
            weather_forecast_day.min_wind = int(min(value_list))
        elif key == "tcc_mean": # tcc_mean = Mean value of total cloud cover
            pass
        elif key == "pcat": # pcat = Precipitation category(rain, snow)
            pass
        elif key == "pmean": # pmean = Mean precipitation intensity
            weather_forecast_day.precipitation = sum(value_list)
        elif key == "Wsymb2": # Wsymb2 = Weather symbol
            most_frequent_occurring_prognosis = max(set(value_list), key = value_list.count)
            weather_forecast_day.prognosis = most_frequent_occurring_prognosis
    return weather_forecast_day


def _get_prognosis_string(prognosis: int):
    if prognosis == 1:
        return "Clear sky"
    elif prognosis == 2:
        return "Nearly clear sky"
    elif prognosis == 3:
        return "Variable cloudiness"
    elif prognosis == 4:
        return "Halfclear sky"
    elif prognosis == 5:
        return "Cloudy sky"
    elif prognosis == 6:
        return "Overcast"
    elif prognosis == 7:
        return "Fog"
    elif prognosis == 8:
        return "Light rain showers"
    elif prognosis == 9:
        return "Moderate rain showers"
    elif prognosis == 10:
        return "Heavy rain showers"
    elif prognosis == 11:
        return "Thunderstorm"
    elif prognosis == 12:
        return "Light sleet showers"
    elif prognosis == 13:
        return "Moderate sleet showers"
    elif prognosis == 14:
        return "Heavy sleet showers"
    elif prognosis == 15:
        return "Light snow showers"
    elif prognosis == 16:
        return "Moderate snow showers"
    elif prognosis == 17:
        return "Heavy snow showers"
    elif prognosis == 18:
        return "Light rain"
    elif prognosis == 19:
        return "Moderate rain"
    elif prognosis == 20:
        return "Heavy rain"
    elif prognosis == 21:
        return "Thunder"
    elif prognosis == 22:
        return "Light sleet"
    elif prognosis == 23:
        return "Moderate sleet"
    elif prognosis == 24:
        return "Heavy sleet"
    elif prognosis == 25:
        return "Light snowfall"
    elif prognosis == 26:
        return "Moderate snowfall"
    elif prognosis == 27:
        return "Heavy snowfall"


def _get_precipitation_category(precipitation_cat:int):
    if precipitation_cat == 0:
        return "No precipitation"
    elif precipitation_cat == 1:
        return "Snow"
    elif precipitation_cat == 2:
        return "Snow and rain"
    elif precipitation_cat == 3:
        return "Rain"
    elif precipitation_cat == 4:
        return "Drizzle"
    elif precipitation_cat == 5:
        return "Freezing rain"
    elif precipitation_cat == 6:
        return "Freezing drizzle"
