import json

with open('configfiles/config.json') as json_data_file:
    config = json.load(json_data_file)
    print("Opened config")

try:
    with open('configfiles/secret_config.json') as secret_json:
        secret_config = json.load(secret_json)
        # Merge two dictionaries, secret config replaces normal config
        config = {**config, **secret_config}
except:
    raise Exception("Please create configfiles/secret_config.json")
