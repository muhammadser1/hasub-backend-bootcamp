from utils.file_operations import load_json


def check_username_exists_in_db(username: str):
    db_user_path = "data/userAuth_data.json"
    user_db = load_json(db_user_path)
    return username in user_db


def is_valid_user_role(role: str):
    return role in ["guest", "admin"]
