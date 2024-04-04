from fastapi import FastAPI, Request

# from routers import students
# from routers import auth_user

server = FastAPI()

# # # routes
# app.include_router(students.router)
# app.include_router(auth_user.router)

@server.middleware("http")
async def log_req(request: Request, call_next):
    print(f'got req. to: {request.url}, method: {request.method}')
    response = await call_next(request)
    return response


@server.get("/",tags=["tests"])
async def test():
    """
    Test endpoint to check if the API is running.
    """
    return {"message": "API is working!"}
# curl -XPOST http://localhost:8000/auth/sign_up -d '{"username":"sarrm","password":"124"}' -H "Content-Type: application/json"
