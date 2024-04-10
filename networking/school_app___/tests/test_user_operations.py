import pytest

from utils.auth_utils.user_operations import is_valid_user_role, is_username_duplicate_in_db


def test_is_valid_user_role_valid():
    assert is_valid_user_role("guest") == True
    assert is_valid_user_role("admin") == True
    assert is_valid_user_role("no role") == False


def test_is_username_duplicate_in_db():
    assert is_username_duplicate_in_db("1") == True
    assert is_username_duplicate_in_db("2222") == False
    assert is_username_duplicate_in_db("") == False

    with pytest.raises(TypeError):
        is_username_duplicate_in_db(None)

    with pytest.raises(TypeError):
        is_username_duplicate_in_db([])

    with pytest.raises(TypeError):
        is_username_duplicate_in_db(123)
