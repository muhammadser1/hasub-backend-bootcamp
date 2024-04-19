from fastapi import Request, APIRouter
from starlette.responses import HTMLResponse, FileResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/show_sales", response_class=HTMLResponse)
async def showSales(request: Request):
    return templates.TemplateResponse("show_sales.html", {"request": request})

