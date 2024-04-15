from models.userAuth_model import User
from utils.file_operations import load_json, write_json
from utils.userAuth_utils.password_utils import hash_password


def check_username_exists_in_db(username: str):
    db_user_path = "data/userAuth_data.json"
    user_db = load_json(db_user_path)
    return username in user_db


def is_valid_user_role(role: str):
    return role in ["guest", "admin"]


def add_user_to_auth_db(user: User):
    """
    Update the database with a new student.
    """
    hashed_password = hash_password(user.password)
    db_user_path = "data/userAuth_data.json"
    db_users = load_json(db_user_path)
    db_users[user.username] = {
        "username": user.username,
        "password": hashed_password,
        "role": user.role
    }
    write_json(db_users, db_user_path)
    return db_users


def retrieve_user_from_auth_db(user_request: User):
    """
    Check if a user with the given username exists in the database and has the specified role.

    Parameters:
        file_path (str): The path to the JSON database file.
        user_request (User): The user object to check.

    Returns:
        dict or None: The user data if found, or None if the user is not found.
    """

    db_user_path = "data/userAuth_data.json"
    try:
        db = load_json(db_user_path)
        if user_request.username in db:
            if user_request.role == db[user_request.username]["role"]:
                return db[user_request.username]
            else:
                return "Not Found"
        else:
            return "Not Found"
    except Exception as e:
        return None
