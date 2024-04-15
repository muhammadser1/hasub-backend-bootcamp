from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Initialize Jinja2Templates instance
templates = Jinja2Templates(directory="templates")


# Define a route to render the HTML page using Jinja2
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    # Sample data
    context = {"title": "Welcome to FastAPI with Jinja2", "message": "Hello, world!"}
    # Render the HTML template with context data
    return templates.TemplateResponse("index.html", {"request": request, **context})
