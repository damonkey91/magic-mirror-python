import requests
import json


def get_quote_of_today():
    response = requests.get("http://quotes.rest/qod.json")
    if response.ok:
        json_response = json.loads(response.text)
        quote = json_response["contents"]["quotes"][0]["quote"]
        author = json_response["contents"]["quotes"][0]["author"]
        text = f"{quote}\n{author}"
        return text
