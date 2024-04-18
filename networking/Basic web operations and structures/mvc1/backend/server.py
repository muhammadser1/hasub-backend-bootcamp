from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from routers import sales_router
from routers import userAuth_router

app = FastAPI()

origins = [
    "http://127.0.0.1:8080","*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(userAuth_router.router)
app.include_router(sales_router.router)

@app.get("/server", tags=["tests"])
def test():
    """
    Test endpoint to check if the API is running.
    """
    print({"message": "API is working!"})
    return {"message": "API is working!"}
