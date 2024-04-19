from fastapi import FastAPI, Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

from controllers import auth_controller
from models import user

app = FastAPI()
templates = Jinja2Templates(directory="views/templates")
app.include_router(auth_controller.router)
app.include_router(user.router)


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})
