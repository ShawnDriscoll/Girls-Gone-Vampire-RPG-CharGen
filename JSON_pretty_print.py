
import json
import pprint

with open('Sample Char.tps', 'r') as json_file:
    data = json.load(json_file)

    pprint.pprint(data)
