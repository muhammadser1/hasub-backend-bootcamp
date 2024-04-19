from urllib import request

from fastapi import FastAPI, Request
from starlette.responses import HTMLResponse, FileResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/server", tags=["tests"])
def test():
    """
    Test endpoint to check if the API is running.
    """
    print({"message": "API is working!"})
    return {"message": "API is working!"}


@app.get("/login", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.get("/show_sales", response_class=HTMLResponse)
async def showSales(request: Request):
    return templates.TemplateResponse("show_sales.html", {"request": request})


@app.get("/logout", response_class=HTMLResponse)
async def serve_img():
    return FileResponse("static/my_image.jpg")


@app.get("/logout_html", response_class=HTMLResponse)
async def serve_html():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Logout</title>
    </head>
    <body>
        <img src="static/my_image.jpg" alt="Goodbye!">
    </body>
    </html>
    """
    return html_content


@app.get("/", response_class=HTMLResponse)
async def home(request:Request):
    return templates.TemplateResponse("home.html", {"request": request})

