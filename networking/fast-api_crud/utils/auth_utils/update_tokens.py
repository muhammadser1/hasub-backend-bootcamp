from models.user import User
from utils.json_file_utils import load_json, write_json


def update_tokens(file_path: str, username:str,tokens:str):
    """
    Update the database with a new student.
    :param file_path:
    :param file_path (str): The path to the database file.
    :param user (User): The user object to be added to the database.
    :return: Updated database with the new student added.
    """

    db_users = load_json(file_path)
    db_users[username] = tokens
    write_json(db_users, file_path)
    return db_users
