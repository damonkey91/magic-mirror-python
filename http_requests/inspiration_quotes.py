import requests
import json
import random


def get_inspiration_quote():
    response = requests.get("https://type.fit/api/quotes")
    if response.ok:
        json_response = json.loads(response.text)
        index = random.randint(0, len(json_response)-1)
        quote = json_response[index]["text"]
        author = json_response[index]["author"]
        text = f"{quote}\n{author}"
        return text
