from fastapi import FastAPI, Request

from routers import students

app = FastAPI()

# # routes
app.include_router(students.router)


@app.middleware("http")
async def log_req(request: Request, call_next):
    print(f'got req. to: {request.url}, method: {request.method}')
    response = await call_next(request)
    return response


@app.get("/")
async def test():
    """
    Test endpoint to check if the API is running.
    """
    return {"message": "API is working!"}
