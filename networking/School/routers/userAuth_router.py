from fastapi import APIRouter, HTTPException
from models.userAuth_model import User
from utils.decorators import log_function_call
from utils.raise_validation_error import raise_validation_error
from utils.userAuth_utils.authentication_utils import authenticate_user, validate_user
from utils.userAuth_utils.jwt_manager import generate_jwt_token

from utils.userAuth_utils.user_operations import add_user_to_auth_db,retrieve_user_from_auth_db

router = APIRouter()


@router.get("/auth_user", tags=["tests"])
def test():
    print({"msg": "test auth_user router is working!"})
    return {"msg": "test auth_user router is working!"}


@router.post('/auth_user/sign_up', tags=["auth"])
@log_function_call
def sign_up(user: User):
    raise HTTPException(status_code=404, detail="User signup failed: Some detail message")

    # validation_errors = validate_user(user)
    # if validation_errors:
    #     raise_validation_error(400, validation_errors)
    #     return validation_errors
    # add_user_to_auth_db(user)
    # auth_token=generate_jwt_token(user)
    # return "msg:user created",auth_token


@router.post('/auth_user/sign_in', tags=["auth"])
@log_function_call
def sign_in(user: User):
    """
    :param user:
    :return:
    """
    existing_user = retrieve_user_from_auth_db(user)
    authenticate_user(existing_user, user)
    return generate_jwt_token(user)


