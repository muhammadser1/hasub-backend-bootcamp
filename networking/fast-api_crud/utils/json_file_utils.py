import json
import os


def load_json(file_path):
    """
    Load JSON data from a file.

    Parameters:
        file_path (str): The path to the JSON file.

    Returns:
        dict: The loaded JSON data.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON in file '{file_path}': {e}")
        return None


def write_json(data, file_path):
    """
    Write JSON data to a file.

    Parameters:
        data (dict): The JSON data to write.
        file_path (str): The path to the JSON file.
    """
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"JSON data written to '{file_path}' successfully.")
    except Exception as e:
        print(f"Error writing JSON data to file '{file_path}': {e}")


def get_json_file_path(file_name:str):
    """
    Get the file path for the JSON file.
    """
    script_directory = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(script_directory, '..', 'data', file_name)
    return file_path
