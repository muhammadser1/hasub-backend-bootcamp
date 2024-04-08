from fastapi import HTTPException

from models.user import User
from utils.auth_utils.password_utils import verify_password
from utils.auth_utils.user_operations import is_username_duplicate_in_db, retrieve_user_from_auth_db


async def authenticate_user(user: User):
    print(user)
    existing_user = retrieve_user_from_auth_db(user)
    print(existing_user)
    if existing_user is None:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    stored_password = existing_user["password"]
    if not verify_password(stored_password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return existing_user