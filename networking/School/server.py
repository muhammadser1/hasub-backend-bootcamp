from fastapi import FastAPI
from starlette.requests import Request

from routers import userAuth_router

app = FastAPI()
app.include_router(userAuth_router.router)


@app.middleware("http")
async def log_req(request: Request, call_next):
    print(f'log_req: got req. to: {request.url}, method: {request.method}')
    response = await call_next(request)
    return response


@app.get("/server", tags=["tests"])
def test():
    """
    Test endpoint to check if the API is running.
    """
    print({"message": "API is working!"})
    return {"message": "API is working!"}
