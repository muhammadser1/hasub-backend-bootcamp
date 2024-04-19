from fastapi import APIRouter

from utils.json_handler import load_json

router = APIRouter()


@router.get("/sales/get_sales_data", tags=["sales"])
def get_sales_data():
    sales_data = load_json("database/db_sales.json")
    print(sales_data)
    return sales_data
