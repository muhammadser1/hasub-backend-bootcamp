from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer

from models.user import User
from utils.auth_utils import jwt_manager
from utils.auth_utils.get_user_by_username import username_exists
from utils.auth_utils.jwt_manager import verify_jwt
from utils.auth_utils.password_manager import verify_password
from utils.auth_utils.update_tokens import update_tokens
from utils.auth_utils.update_user_auth import update_user_auth
from utils.json_file_utils import *

router = APIRouter()


@router.get("/auth_user", tags=["tests"])
async def test():
    print({"msg": "test auth_user router is working!"})
    return {"msg": "test auth_user router is working!"}


@router.post('/auth_user/sign_up', tags=["auth"])
def sign_up(user: User):
    file_path = get_json_file_path('user.json')

    if username_exists(file_path, user):
        return "Username already exists"
    if user.role not in ["guest", "admin"]:
        return "user role is not correct"

    updated_users_db = update_user_auth(file_path, user)
    write_json(updated_users_db, file_path)

    auth_token = jwt_manager.generate_jwt({"username": user.username, "user role": user.role})
    token_db_path = get_json_file_path('db_tokens.json')
    update_tokens(token_db_path,user.username ,auth_token)

    return {"msg": "ser created", "token": auth_token}


@router.post('/auth_user/sign_in', tags=["auth"])
def sign_in(user: User):
    file_path = get_json_file_path('user.json')
    username_db = username_exists(file_path, user)
    if username_db is None:
        return "Username is not exists"

    stored_pass = username_db["password"]
    if verify_password(stored_pass, user.password):
        # return "user sign in successfully"
        auth_token = jwt_manager.generate_jwt({"username": user.username, "user role": user.role})
        token_db_path = get_json_file_path('db_tokens.json')
        update_tokens(token_db_path, user.username, auth_token)
        return {"msg": "user sign in successfully", "token": auth_token}
    else:
        return {"msg": "invalid creds"}
