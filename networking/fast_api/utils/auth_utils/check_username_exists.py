from utils.db_fns import load_json


def check_username_exists(file_path: str, username: str) -> bool:
    """
    Check if a username already exists in the user data.
    :param file_path (str): The path to the user data JSON file.
    :param username (str): The username to check.
    :return: True if the username exists, False otherwise.
    """
    user_data = load_json(file_path)
    return username in user_data
