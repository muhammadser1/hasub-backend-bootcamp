from fastapi import FastAPI

from controllers import auth_controller

app = FastAPI()
app.include_router(auth_controller.router)

@app.get("/frontend", tags=["tests"])
def test():
    """
    Test endpoint to check if the API is running.
    """
    print({"message": "frontend server is working!"})
    return {"message": "frontend server is working!"}
