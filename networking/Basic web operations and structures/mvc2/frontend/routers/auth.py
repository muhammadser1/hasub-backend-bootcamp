from fastapi import Request, APIRouter
from starlette.responses import HTMLResponse, FileResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")
router.mount("/static", StaticFiles(directory="static"), name="static")


@router.get("/logout2", response_class=HTMLResponse)
async def serve_img():
    print("jjjj")
    return FileResponse("static/logout.html")


@router.get("/login", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

