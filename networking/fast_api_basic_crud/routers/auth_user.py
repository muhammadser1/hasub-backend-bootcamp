from fastapi import APIRouter, Depends
from models.user import User
from utils.auth_utils.password_utils import verify_password
from utils.auth_utils.user_operations import *
from utils.file_operations import *

router = APIRouter()


@router.get("/auth_user", tags=["tests"])
async def test():
    print({"msg": "test auth_user router is working!"})
    return {"msg": "test auth_user router is working!"}


@router.post('/auth_user/sign_up', tags=["auth"])
def sign_up(user: User):
    db_user_path = "data/db_users.json"

    if is_username_duplicate(db_user_path, user.username):
        return {"error": "Username already exists"}
    if not is_valid_user_role(user.role):
        return {"error": "User role is not correct"}

    try:
        add_user_to_auth_db(db_user_path, user)
        return {"msg": f"User created with ID: {user.username}"}
    except Exception as e:
        return {"error": f"An error occurred while creating the user: {e}"}


@router.post('/auth_user/sign_in', tags=["auth"])
def sign_in(user: User):
    db_user_path = "data/db_users.json"
    existing_user = is_username_duplicate(db_user_path, user.username)
    if existing_user is None:
        return {"error": "Username is not exists"}
    else:
        existing_user = retrieve_user_from_auth_db(db_user_path, user)
        if existing_user is None:
            return {"msg": "invalid creds"}
        else:
            stored_password = existing_user["password"]
            if not verify_password(stored_password, user.password):
                return {"error: Invalid credentials"}
            else:
                return {"message": "Sign-in successful"}
