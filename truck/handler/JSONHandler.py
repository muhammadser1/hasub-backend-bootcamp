import json


def load_data_from_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


def save_data_to_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
