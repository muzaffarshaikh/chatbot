import json


def read_intents_file():
    filepath = 'intents.json'
    with open(filepath) as json_data:
        intents = json.load(json_data)
    return intents
