from fastapi import FastAPI, Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/server", tags=["tests"])
def test():
    """
    Test endpoint to check if the API is running.
    """
    print({"message": "API is working!"})
    return {"message": "API is working!"}


@app.get("/login", response_class=HTMLResponse)
async def login(request: Request):
    # Define the data to pass to the template
    data = {"title": "Welcome to My Website" }

    # Render the "index2.html" template with the provided data
    return templates.TemplateResponse("login.html", {"request": request, **data})
