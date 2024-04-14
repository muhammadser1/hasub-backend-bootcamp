import json

from utils.decorators import try_except_decorator, log_function_call


@log_function_call
def load_json(file_path):
    """
    Load JSON data from a file.

    Parameters:
        file_path (str): The path to the JSON file.

    Returns:
        dict: The loaded JSON data.
    """
    print(file_path+"Aa")
    with open(file_path+"Aa", 'r') as file:
        data = json.load(file)

@try_except_decorator
def write_json(data, file_path):
    """
    Write JSON data to a file.

    Parameters:
        data (dict): The JSON data to write.
        file_path (str): The path to the JSON file.
    """
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)



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