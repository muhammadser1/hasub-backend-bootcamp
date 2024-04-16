from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    # Define the data to pass to the template
    data = {"title": "Welcome to My Website", "name": "Muhammad"}

    # Render the "index2.html" template with the provided data
    return templates.TemplateResponse("index2.html", {"request": request, **data})
