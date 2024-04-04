from models.user import User
from utils.auth_utils.password_manager import hash_password
from utils.json_file_utils import *


def update_user_auth(file_path: str, user:User):
    """
    Update the database with a new student.
    :param file_path:
    :param file_path (str): The path to the database file.
    :param user (User): The user object to be added to the database.
    :return: Updated database with the new student added.
    """
    hashed_password = hash_password(user.password)

    db_users= load_json(file_path)
    db_users[user.username] = {
        "username": user.username,
        "password":hashed_password,
        "role":user.role
    }
    return db_users
