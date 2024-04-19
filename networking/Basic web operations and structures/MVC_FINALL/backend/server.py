from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from routers import userAuth_router,sales_router

app = FastAPI()
origins = [
    "http://127.0.0.1:9000","*"
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


@app.get("/backend", tags=["tests"])
def test():
    """
    Test endpoint to check if the API is running.
    """
    print({"message": "backend server is working!"})
    return {"message": "backend server is working!"}

