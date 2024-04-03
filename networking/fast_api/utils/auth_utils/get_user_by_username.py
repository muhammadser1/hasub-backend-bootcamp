from utils.db_fns import load_json


def get_user_by_username(file_path,username: str):
    db = load_json(file_path)
    if username in db:
        return db[username]
    else:
        raise FileNotFoundError(f'username: {username} not in db')