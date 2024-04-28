from fastapi import APIRouter, HTTPException
from models.user import User

from utils.user_operations import retrieve_user_from_auth_db

from utils.password_utils import verify_password

router = APIRouter()


@router.get("/backend/userAuth_routerTEST", tags=["tests"])
def test():
    """
    Test endpoint to check if the API is running.
    """
    print({"message": "userAuth_routerTEST is working!"})
    return {"message": "userAuth_routerTEST is working!"}


@router.post("/login", tags=["LoginPage"])
async def login(login_data: User):
    # existing_user = retrieve_user_from_auth_db(login_data)
    # print(login_data)
    # if existing_user is None:
    #     raise HTTPException(status_code=401, detail="Invalid credentials")
    #
    # stored_password = existing_user["password"]
    #
    # if not verify_password(stored_password, login_data.password):
    #     raise HTTPException(status_code=401, detail="Invalid credentials")

    return {"message": "Login successful"}