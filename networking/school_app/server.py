from fastapi import FastAPI, Request

from routers import auth_router, student_router
from utils.decorators import log_function_call

app = FastAPI()

# # # # routes
# app.include_router(student_router.router)
# app.include_router(auth_router.router)
# app.include_router(test.router)


#
# @app.middleware("http")
# async def log_req(request: Request, call_next):
#     print(f'log_req: got req. to: {request.url}, method: {request.method}')
#     response = await call_next(request)
#     return response



@app.get("/server", tags=["tests"])
@log_function_call
async def test():
    """
    Test endpoint to check if the API is running.
    """
    return {"message": "API is working!"}
# curl -XPOST http://localhost:8000/auth/sign_up -d '{"username":"sarrm","password":"124"}' -H "Content-Type: application/json"
