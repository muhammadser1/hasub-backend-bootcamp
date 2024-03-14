import json
import logging

# Configure logging
logging.basicConfig(filename='data.log', level=logging.INFO)

def load_data_from_json(file_path):
    """
    Load JSON data from a file.

    Args:
        file_path (str): The path to the JSON file to be loaded.

    Returns:
        dict: A dictionary containing the loaded JSON data.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        json.JSONDecodeError: If the file contains invalid JSON data.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            logging.info(f"Data loaded from JSON file: {file_path}")
        return data
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        raise
    except json.JSONDecodeError:
        logging.error(f"Invalid JSON data in file: {file_path}")
        raise


def save_data_to_json(data, file_path):
    """
    Save data to a JSON file.

    Args:
        data (dict): The data to be saved to the JSON file.
        file_path (str): The path to the JSON file where the data will be saved.

    Raises:
        FileNotFoundError: If the specified directory for the file does not exist.
        PermissionError: If the user does not have permission to write to the file.
    """
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
            logging.info(f"Data saved to JSON file: {file_path}")
    except FileNotFoundError:
        logging.error(f"Directory not found: {file_path}")
        raise
    except PermissionError:
        logging.error(f"Permission denied: {file_path}")
        raise
