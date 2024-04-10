from models.user import User
from utils.auth_utils.password_utils import hash_password
from utils.auth_utils.user_operations import retrieve_user_from_auth_db, add_user_to_auth_db


def test_retrieve_user_from_auth_db_user_exists_with_correct_role():
    user_request = User(username="1", role="admin",password="1")
    db=add_user_to_auth_db(user_request)
    result_user = retrieve_user_from_auth_db(user_request)
    assert result_user["role"]==user_request.role
    assert result_user["username"]==user_request.username


def test_retrieve_user_from_auth_db_user_exists_with_incorrect_role():
    user_request = User(username="1", role="admin",password="1")
    db=add_user_to_auth_db(user_request)
    result_user = retrieve_user_from_auth_db(user_request)
    user_request.role="guest"
    assert result_user["role"]!=user_request.role
    assert result_user["username"]==user_request.username

