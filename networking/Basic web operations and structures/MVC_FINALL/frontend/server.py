from fastapi import FastAPI

from routers import login_routes,sales_router

app = FastAPI()
app.include_router(login_routes.router)
app.include_router(sales_router.router)


@app.get("/frontend", tags=["tests"])
def test():
    """
    Test endpoint to check if the API is running.
    """
    print({"message": "frontend server is working!"})
    return {"message": "frontend server is working!"}
