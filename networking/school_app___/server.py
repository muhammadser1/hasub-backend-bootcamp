from fastapi import FastAPI

from routers import auth_router, chating_websocket
from routers.student_routers import read_student_router,create_student_router,delete_student_class
from utils.decorators import log_function_call
app = FastAPI()

# # # # routes
app.include_router(auth_router.router)
app.include_router(read_student_router.router)
app.include_router(create_student_router.router)
app.include_router(delete_student_class.router)
app.include_router(chating_websocket.app)
# @app.middleware("http")
# async def log_req(request: Request, call_next):
#     print(f'log_req: got req. to: {request.url}, method: {request.method}')
#     response = await call_next(request)
#     return response


@app.get("/server", tags=["tests"])
@log_function_call
def test():
    """
    Test endpoint to check if the API is running.
    """
    print({"message": "API is working!"})
    return {"message": "API is working!"}
# curl -XPOST http://localhost:8000/auth/sign_up -d '{"username":"sarrm","password":"124"}' -H "Content-Type: application/json"
