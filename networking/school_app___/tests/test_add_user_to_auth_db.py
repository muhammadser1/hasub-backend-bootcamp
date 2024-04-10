import pytest

from models.user import User
from utils.auth_utils.user_operations import add_user_to_auth_db



def test_add_user_to_auth_db():
    user = User(username="1", password="1", role="guest")
    updated_db = add_user_to_auth_db(user)
    assert updated_db[user.username]["username"] == user.username
    assert updated_db[user.username]["role"] == user.role
