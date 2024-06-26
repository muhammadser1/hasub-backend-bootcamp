import time
import jwt
from fastapi import HTTPException

from utils.file_operations import *

info = read_config("data/config.txt")
SECRET_KEY = (info["jwt_secret"])
print(SECRET_KEY)


def generate_jwt(payload, expiration_time=60):
    payload['exp'] = int(time.time()) + expiration_time
    encoded_jwt = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return encoded_jwt


def verify_jwt(user_jwt, username: str):
    try:
        db_tokens = load_json("data/db_user_tokens.json")
        if username in db_tokens and db_tokens[username] == user_jwt:
            decoded_token = jwt.decode(user_jwt, SECRET_KEY, algorithms=["HS256"])
            expiration_time = decoded_token.get("exp", 0)
            current_time = int(time.time())

            if expiration_time >= current_time:
                print("Token is valid")
                return decoded_token["user role"]
            else:
                print("Token has expired")
        else:
            print("Invalid token")
    except jwt.ExpiredSignatureError:
        print("Token has expired")
    except jwt.InvalidTokenError:
        print("Invalid token")

    return False


def check_token(token: str, username: str):
    try:
        result = verify_jwt(token, username)
        if result:
            return result
        unauthorized_exception = HTTPException(status_code=401, detail="Unauthorized access")
        raise unauthorized_exception
    except Exception as e:
        raise e


def update_tokens_in_db(username: str, tokens: str):
    """
    Update the database with a new student.
    :param file_path:
    :param file_path (str): The path to the database file.
    :param user (User): The user object to be added to the database.
    :return: Updated database with the new student added.
    """
    token_db_path = "data/db_user_tokens.json"
    db_users = load_json(token_db_path)
    db_users[username] = tokens
    write_json(db_users, token_db_path)
    return db_users
