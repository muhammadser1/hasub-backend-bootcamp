from models.userAuth_model import User
from utils.raise_validation_error import raise_validation_error
from utils.userAuth_utils.password_utils import verify_password
from utils.userAuth_utils.user_operations import check_username_exists_in_db, is_valid_user_role


def authenticate_user(existing_user, user):
    if existing_user is None:
        raise_validation_error(401, "somthing is wrong in retrieve_user_from_auth_db function")
    if existing_user == "Not Found":
        raise_validation_error(401, "Invalid credentials")

    stored_password_hash = existing_user.get("password")
    if not stored_password_hash or not verify_password(stored_password_hash, user.password):
        raise_validation_error(401, "Invalid credentials")
    return True


def validate_user(user: User) -> str:
    username_exists = check_username_exists_in_db(user.username)
    if username_exists is None:
        return "Something went wrong while checking username"
    if username_exists:
        return "Username already exists"
    if not is_valid_user_role(user.role):
        return "User role is not correct"

    return ""
