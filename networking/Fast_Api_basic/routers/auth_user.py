from fastapi import APIRouter, Path

from models.user import User
from utils.auth_utils.check_username_exists import check_username_exists
from utils.auth_utils.get_user_by_username import get_user_by_username
from utils.auth_utils.password_manager import verify_password
from utils.auth_utils.update_user_auth import update_user_auth
from utils.db_fns import write_json
from utils.get_json_file_path import get_json_file_path

router = APIRouter()


@router.get("/auth",tags=["tests"])
async def test():
    print("hi from test_auth_user end point")
    return "hi from test_auth_user end point :)"


@router.post('/auth/sign_up',tags=["auth"])
def sign_up(user: User):
    file_path = get_json_file_path('user.json')
    if check_username_exists(file_path, user.username):
        return "Username already exists"
    updated_users_db = update_user_auth(file_path, user)
    write_json(updated_users_db, file_path)
    return {"message": "User signed up successfully"}


@router.post('/auth/sign_in',tags=["auth"])
def sign_in(user: User):
    file_path = get_json_file_path('user.json')
    if not check_username_exists(file_path, user.username):
        return "Username is not exists"
    user_db = get_user_by_username(file_path, user.username)
    stored_pass = user_db["password"]
    if verify_password(stored_pass, user.password):
        return "user sign in successfully"
    else:
        return {"msg": "invalid creds"}
