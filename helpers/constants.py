import os

TWELVE_HOURS: int = 43200000
TWENTY_FOUR_HOURS = 86400000
EVERY_HOUR = 3600000
EVERY_EIGHT_HOURS = 28800000


# custom kwargs argument
REFRESH_RATE = 'refresh_rate'
LONGITUDE = 'longitude'
LATITUDE = 'latitude'

root_project_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
