from models.user import User
from utils.json_file_utils import load_json


def username_exists(file_path,user_request:User):
    db = load_json(file_path)
    if user_request.username in db:
        if user_request.role == db[user_request.username]["role"]:
            return db[user_request.username]
    else:
        return None