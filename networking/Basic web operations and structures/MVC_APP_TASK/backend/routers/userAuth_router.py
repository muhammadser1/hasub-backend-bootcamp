from fastapi import APIRouter, HTTPException

from backend_utils.userAuth_utils.UserAuthDB_utils import retrieve_user_from_auth_db, update_tokens_in_db, \
    add_user_to_auth_db
from backend_utils.userAuth_utils.authentication_utils import authenticate_user, \
    validate_and_check_existing_user
from backend_utils.userAuth_utils.jwt_token_manager import generate_jwt_token
from models.userAuth_model import User

router = APIRouter()


@router.get("/auth_user", tags=["tests"])
def test():
    print({"msg": "tests auth_user router is working!"})
    return {"msg": "tests auth_user router is working!"}


@router.post('/auth_user/sign_in', tags=["auth"])
def sign_in(user: User):
    """
        :param user:
        :return:
        """
    existing_user = retrieve_user_from_auth_db(user)
    authenticate_user(existing_user, user)
    token = generate_jwt_token(user)
    update_tokens_in_db(user.username, token["token"])
    return token


@router.post('/auth_user/sign_up', tags=["auth"])
def sign_up(user: User):
    """
    :param user:
    :return:
    """

    if validate_and_check_existing_user(user):
        if user.role not in ["admin", "guest"]:
            raise HTTPException(status_code=400,
                                detail="Invalid user role. User role must be either 'admin' or 'guest'.")

    add_user_to_auth_db(user)
    token = generate_jwt_token(user)
    update_tokens_in_db(user.username, token["token"])
    return token
