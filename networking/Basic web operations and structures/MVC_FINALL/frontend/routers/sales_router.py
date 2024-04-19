from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="view/templates")


@router.get("/show_sales", response_class=HTMLResponse)
async def showSales(request: Request):
    return templates.TemplateResponse("show_sales.html", {"request": request})
