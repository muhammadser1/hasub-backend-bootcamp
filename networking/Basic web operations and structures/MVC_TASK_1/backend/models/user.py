from json import JSONDecodeError
from urllib import request

from fastapi import APIRouter, Request, Body, HTTPException
from pydantic import BaseModel
from starlette.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

router = APIRouter()
templates = Jinja2Templates(directory="view/templates")



class LoginData(BaseModel):
    username: str
    password: str

@router.post("/login")
async def login(login_data: LoginData):
    username = login_data.username
    password = login_data.password
    if username == "1" and password == "1":
        return {"message": "Login successful"}
    else:
        raise HTTPException(status_code=401, detail="Invalid username or password")