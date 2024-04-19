from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="view/templates")
router.mount("/static", StaticFiles(directory="view/static"), name="static")


@router.get("/login", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})



@router.get("/logout", response_class=HTMLResponse)
async def serve_img():
    return FileResponse("view/static/my_image.jpg")