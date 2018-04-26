import json

# This code loads data from data_in.json
# into a Python dictionary called d

with open('music.json') as json_data:
    d = json.load(json_data)

print(d)
