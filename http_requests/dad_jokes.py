import requests
import json


def get_dad_jokes():
    response = requests.get("https://api.dadjokes.io/api/random/joke")
    if response.ok:
        json_response = json.loads(response.text)
        setup = json_response["body"][0]["setup"]
        punchline = json_response["body"][0]["punchline"]
        joke = f"{setup}\n{punchline}"
        return joke
