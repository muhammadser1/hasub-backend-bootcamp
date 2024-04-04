from utils.json_file_utils import load_json


def get_student_by_username(file_path, username: str):
    db = load_json(file_path)
    if username in db:
        return db[username]
    else:
        return None