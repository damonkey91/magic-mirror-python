import requests
import json


def get_joke_of_today():
    response = requests.get("https://api.jokes.one/jod")
    if response.ok:
        json_response = json.loads(response.text)
        joke = json_response["contents"]["jokes"][0]["joke"]["text"]
        return joke
