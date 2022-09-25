from helpers.constants import *


def set_default_color_if_not_specified(kwargs):
    if 'bg' not in kwargs and 'background' not in kwargs:
        kwargs['bg'] = "black"


def extract_latitude(kwargs):
    if LATITUDE in kwargs:
        return kwargs.pop(LATITUDE)
    else:
        print("Error: Needs latitude to get weather forecast.")


def extract_longitude(kwargs):
    if LONGITUDE in kwargs:
        return kwargs.pop(LONGITUDE)
    else:
        print("Error: Needs longitude to get weather forecast.")


def extract_refresh_rate(kwargs, default_value = TWELVE_HOURS):
    if REFRESH_RATE in kwargs:
        return kwargs.pop(REFRESH_RATE)
    else:
        return default_value
