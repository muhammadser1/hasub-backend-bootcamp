from fastapi import APIRouter, Request
from starlette.responses import  JSONResponse
from starlette.templating import Jinja2Templates

router = APIRouter()
mock_users = {"user1": "password1", "user2": "password2"}


@router.get("/user_models", tags=["tests"])
def test():
    print({"msg": "tests user_models router is working!"})
    return {"msg": "tests user_models router is working!"}


@router.post("/login")
async def login(username: str, password: str):
    print(username,password)
    if username == "1" and password == "1":
        return JSONResponse(status_code=200, content={"success": True})
    else:
        return JSONResponse(status_code=401, content={"success": False, "error": "Invalid username or password"})
