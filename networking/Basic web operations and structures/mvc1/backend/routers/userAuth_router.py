from fastapi import APIRouter,Request
from starlette.responses import HTMLResponse

router = APIRouter()


@router.get("/auth_user", tags=["tests"])
def test():
    print({"msg": "tests auth_user router is working!"})
    return {"msg": "tests auth_user router is working!"}
