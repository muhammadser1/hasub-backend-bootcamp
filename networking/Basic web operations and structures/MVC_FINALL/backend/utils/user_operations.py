from models.user import User
from utils.json_handler import load_json


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
        db_user_path = "database/user_db.json"
        db = load_json(db_user_path)
        if user_request.username in db:
            if user_request.role == db[user_request.username]["role"]:
                return db[user_request.username]
        else:
            return None
    except Exception as e:
        print(f"An error occurred while loading JSON file: {e}")
        return None
