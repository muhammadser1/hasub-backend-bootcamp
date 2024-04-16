from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse, HTMLResponse

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/get_image")
async def serve_img():
    image_path = "my_image.jpg"
    return FileResponse(image_path)


@app.get("/items/", response_class=HTMLResponse)
async def serve_html():
    with open("static/index.html", "r") as file:
        html_content = file.read()

    return HTMLResponse(content=html_content, status_code=200)
