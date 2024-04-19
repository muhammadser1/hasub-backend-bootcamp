from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates


router = APIRouter()
templates = Jinja2Templates(directory="views/templates")


@router.get("/auth_user", tags=["tests"])
def test():
    print({"msg": "tests auth_user router is working!"})
    return {"msg": "tests auth_user router is working!"}


@router.get("/login", response_class=HTMLResponse,tags=["Auth"])
async def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})
