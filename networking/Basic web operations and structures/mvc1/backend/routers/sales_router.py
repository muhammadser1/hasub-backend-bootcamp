from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse

from utils.file_operations import load_json

router = APIRouter()


@router.get("/sales", tags=["tests"])
def test():
    print({"msg": "tests sales router is working!"})
    return {"msg": "tests sales router is working!"}


@router.get("/sales/get_sales_data", tags=["sales"])
def get_sales_data():
    sales_data = load_json("database/db_sales.json")
    return sales_data
