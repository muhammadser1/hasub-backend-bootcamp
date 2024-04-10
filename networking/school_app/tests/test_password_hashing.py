import bcrypt
import pytest
from utils.auth_utils.password_utils import hash_password,verify_password


def test_hash_password_correct():
    password="123"
    hashed_pass=hash_password(password)
    assert bcrypt.checkpw(password.encode('utf-8'), hashed_pass.encode('utf-8'))==True
def test_hash_password_wrong_pass():
    password="123"
    hashed_pass=hash_password(password)
    password+="4"
    assert bcrypt.checkpw(password.encode('utf-8'), hashed_pass.encode('utf-8'))==False

def test_hash_password_not_string_input():
    password=[] ## not string
    with pytest.raises(TypeError):
        hash_password(password)

def test_verify_password_correct():
    password="123"
    hashed_pass=hash_password(password)
    assert verify_password(hashed_pass,password)==True

def test_verify_password_correct():
    password="123"
    hashed_pass=hash_password(password)
    password="1234"
    assert verify_password(hashed_pass,password)==False

def test_verify_password_not_string_input():
    with pytest.raises(TypeError):
        verify_password("12312312", None)
    with pytest.raises(TypeError):
        verify_password("12312312", [])
    with pytest.raises(TypeError):
        verify_password("12312312", 12312312)