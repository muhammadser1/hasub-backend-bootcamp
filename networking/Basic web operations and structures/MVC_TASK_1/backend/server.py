from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from models import user

app = FastAPI()
origins = [
    "http://127.0.0.1:8001","*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(user.router)


@app.get("/backend", tags=["tests"])
def test():
    """
    Test endpoint to check if the API is running.
    """
    print({"message": "backend server is working!"})
    return {"message": "backend server is working!"}

