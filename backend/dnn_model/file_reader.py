import json


def read_intents_file():
    filepath = 'corpus/intents.json'
    with open(filepath) as json_data:
        intents = json.load(json_data)
    print(intents)
    return intents

read_intents_file()