from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI()

# Mount the "static" directory to serve static files (like index.html)
static_path = Path(__file__).parent / "static"
app.mount("/static", StaticFiles(directory=str(static_path)), name="static")


@app.get("/1")
async def get_index(request: Request):
    index_path = static_path / "index.html"
    print(index_path)
    return FileResponse(index_path, media_type="text/html")


@app.get("/get_image")
async def get_image():
    image_path = "1.jpg"  # Adjust the image path accordingly
    return FileResponse(image_path)
