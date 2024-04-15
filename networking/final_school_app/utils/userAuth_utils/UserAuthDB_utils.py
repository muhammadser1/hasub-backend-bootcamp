from models.userAuth_model import User
from utils.file_operations import load_json, write_json
from utils.userAuth_utils.password_utils import hash_password


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
        return "Not Found"
    except Exception as e:
        return None


def update_tokens_in_db(username: str, token: str):
    """

    :param token:
    :param username:
    :param tokens:
    :return:
    """
    db_user_path = "data/db_user_tokens.json"
    try:
        db_tokens = load_json(db_user_path)
        db_tokens[username] = token
        write_json(db_tokens, db_user_path)
        return db_tokens
    except Exception as e:
        return None


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
