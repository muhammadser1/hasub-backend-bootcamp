from fastapi import FastAPI

import pokemon_router

app = FastAPI()
app.include_router(pokemon_router.router)

@app.get("/server", tags=["tests"])
def test():
    """
    Test endpoint to check if the API is running.
    """
    print({"message": "backend server is working!"})
    return {"message": "backend server is working!"}
