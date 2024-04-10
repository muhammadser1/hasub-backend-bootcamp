import json


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
        if not isinstance(data, dict):
            raise ValueError("JSON data is not dict")
        return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        raise FileNotFoundError("Error FileNotFoundError")


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
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        raise FileNotFoundError("Error FileNotFoundError")


def read_config(file_path):
    """
    Read configuration from a text file.

    Parameters:
        file_path (str): The path to the text file containing configuration.

    Returns:
        dict: A dictionary containing configuration settings.
    Raises:
        FileNotFoundError: If the specified file does not exist.
        ValueError: If there is an issue with the file format or content.
    """
    try:
        config = {}
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                key, value = line.split('=', 1)
                config[key.strip()] = value.strip()
        return config
    except FileNotFoundError as e:
        raise e
    except Exception as e:
        raise ValueError(f"Error reading config file: {e}")
