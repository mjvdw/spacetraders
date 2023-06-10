import json


def pprint(json_data):
    json_formatted_str = json.dumps(json_data, indent=2)
    print(json_formatted_str)
