from models.user import User
from utils.auth_utils.input_validation import validate_user_input
from utils.auth_utils.password_utils import hash_password
from utils.file_operations import load_json, write_json


def is_username_duplicate_in_db(username: str):
    if not isinstance(username, str):
        raise TypeError("Username must be a string")
    try:
        db_user_path = "data/db_users.json"
        user_db = load_json(db_user_path)
        return username in user_db
    except Exception as e:
        raise Exception(f"An unexpected error occurred: {e}")


def is_valid_user_role(role: str):
    return role in ["guest", "admin"]


def retrieve_user_from_auth_db(user_request: User) -> dict:
    """
    Check if a user with the given username exists in the database and has the specified role.

    Parameters:
        file_path (str): The path to the JSON database file.
        user_request (User): The user object to check.

    Returns:
        dict or None: The user data if found, or None if the user is not found.
    """
    try:
        db_user_path = "data/db_users.json"
        db = load_json(db_user_path)
        if user_request.username in db:
            if user_request.role == db[user_request.username]["role"]:
                return db[user_request.username]
        else:
            return None
    except Exception as e:
        print(f"An error occurred while loading JSON file: {e}")
        return None


def add_user_to_auth_db(user: User):
    """
    Update the database with a new student.
    :param file_path:
    :param file_path (str): The path to the database file.
    :param user (User): The user object to be added to the database.
    :return: Updated database with the new student added.
    """
    validate_user_input(user)
    hashed_password = hash_password(user.password)
    db_user_path = "data/db_users.json"
    db_users = load_json(db_user_path)
    db_users[user.username] = {
        "username": user.username,
        "password": hashed_password,
        "role": user.role
    }
    write_json(db_users, db_user_path)
    return db_users
