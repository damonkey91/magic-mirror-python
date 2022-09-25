import requests
import json
from enum import Enum


class joke_type_enum(Enum):
    RANDOM = "random"
    TODAY = "today"


def get_zen_quote(type: joke_type_enum):
    response = requests.get(f"https://zenquotes.io/api/{type.value}")
    if response.ok:
        json_response = json.loads(response.text)
        quote = json_response[0]["q"]
        author = json_response[0]["a"]
        text = f"{quote}\n{author}"
        return text
