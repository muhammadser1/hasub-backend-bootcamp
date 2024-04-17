from fastapi import HTTPException

from backend_utils.userAuth_utils.UserAuthDB_utils import retrieve_user_from_auth_db
from backend_utils.userAuth_utils.password_utils import verify_password


def authenticate_user(existing_user, user):
    if existing_user is None:
        raise HTTPException(404, "Failed to retrieve user data from the server")
    if existing_user == "Not Found":
        raise HTTPException(401, "Invalid credentials")
    stored_password_hash = existing_user.get("password")
    if not verify_password(stored_password_hash, user.password):
        raise HTTPException(401, "Invalid credentials")

    return True


def validate_and_check_existing_user(user):
    existing_user = retrieve_user_from_auth_db(user)
    if existing_user is None:
        raise HTTPException(404, "Failed to retrieve user data from the server")
    if existing_user != "Not Found":
        raise HTTPException(401, "Username already exists")

    else:
        return True