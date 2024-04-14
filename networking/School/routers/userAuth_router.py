from fastapi import APIRouter, HTTPException

from models.userAuth_model import User
from utils.decorators import  log_function_call
from utils.file_operations import write_json, load_json
from utils.userAuth_utils.user_operations import check_username_exists_in_db, is_valid_user_role

router = APIRouter()


@router.get("/auth_user", tags=["tests"])
def test():
    print({"msg": "test auth_user router is working!"})
    return {"msg": "test auth_user router is working!"}


@router.post('/auth_user/sign_up', tags=["auth"])
@log_function_call
def sign_up(user: User):
    is_username_exists = check_username_exists_in_db(user.username)
    if is_username_exists is None:
        raise HTTPException(status_code=400, detail="somthing is wrong in sub function")
    if is_username_exists:
        print("Username already exists")
        raise HTTPException(status_code=400, detail="Username already exists")

    if not is_valid_user_role(user.role):
        print("User role is not correct")
        raise HTTPException(status_code=400, detail="error: User role is not correct")
    db_user_path = "data/db_u2sers.json"
    db_users = load_json(db_user_path)
    # write_json(db_users,"db_user_path")