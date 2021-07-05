import json

config = {}

print("import config")
with open('config.json') as config_file:
    config = json.load(config_file)