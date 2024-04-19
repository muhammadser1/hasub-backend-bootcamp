import json


def load_json(file_path):
    """
    Load JSON data from a file.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return {}


def save_json(data, file_path):
    """
    Save JSON data to a file.
    """
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
