import time
import jwt
from fastapi import HTTPException

from backend_utils.file_operations import read_config, load_json

info = read_config("database/config.txt")
SECRET_KEY = (info["jwt_secret"])
print(SECRET_KEY)


def generate_jwt_token(user):
    payload = {"username": user.username, "user_role": user.role}
    return {"token": generate_jwt(payload)}


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
                return decoded_token["user_role"]
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