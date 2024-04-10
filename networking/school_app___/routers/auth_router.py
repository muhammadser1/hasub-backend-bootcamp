from fastapi import APIRouter, HTTPException

from models.user import User
from utils.auth_utils import jwt_manager
from utils.auth_utils.password_utils import verify_password
from utils.auth_utils.user_operations import add_user_to_auth_db
from utils.auth_utils.jwt_manager import update_tokens_in_db
from utils.auth_utils.user_operations import *
from utils.decorators import log_function_call

router = APIRouter()


@router.get("/auth_user", tags=["tests"])
@log_function_call
def test():
    print({"msg": "test auth_user router is working!"})
    return {"msg": "test auth_user router is working!"}


@router.post('/auth_user/sign_up', tags=["auth"])
@log_function_call
def sign_up(user: User):
    """

    :param user:
    :return:
    """
    if is_username_duplicate_in_db(user.username):  # unique username
        raise HTTPException(status_code=400, detail="Username already exists")
    if not is_valid_user_role(user.role):  # guest should be [admin,guest]
        raise HTTPException(status_code=400, detail="error: User role is not correct")
    try:
        add_user_to_auth_db(user)
        auth_token = jwt_manager.generate_jwt({"username": user.username, "user role": user.role})
        update_tokens_in_db(user.username, auth_token)
        return {"msg": "user created", "token": auth_token}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"error: An error occurred while creating the user: {e}")

@router.post('/auth_user/sign_in', tags=["auth"])
@log_function_call
def sign_in(user: User):
    """
    :param user:
    :return:
    """
    existing_user = is_username_duplicate_in_db(user.username)
    if existing_user is None:
        raise HTTPException(status_code=400, detail="Username is not exists")
    existing_user = retrieve_user_from_auth_db(user)

    if existing_user is None:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    else:
        stored_password = existing_user["password"]
        if not verify_password(stored_password, user.password):
            raise HTTPException(status_code=401, detail="Invalid credentials")
        else:
            auth_token = jwt_manager.generate_jwt({"username": user.username, "user role": user.role})
            update_tokens_in_db(user.username, auth_token)
            return {"token": auth_token}