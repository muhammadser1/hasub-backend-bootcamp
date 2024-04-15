import pytest
from fastapi import HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.testclient import TestClient
from routers.student_router.read_student_router import \
    router  # Assuming your FastAPI app is defined in `read_student_router.py`
from utils.file_operations import load_json

client = TestClient(router)


# def test_get_all_students_sucess():
#     response = client.get("/students/read/get_all_students", params={"username": "1",
#     "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IjEiLCJ1c2VyIHJvbGUiOiJhZG1pbiIsImV4cCI6MTcxMjgyNjA4MH0.bYcZyoyM4zlMTbBQEviOEOMTXGli8ynGtlWQx16z7OI"})
#     assert response.status_code == 200
#     db_path = "tests/test_data/get_all_student.json"
#     db=load_json(db_path)
#     data = response.json()
#     assert db == data["students"]

def test_get_all_students_unauthorized():
    with pytest.raises(HTTPException) as response:
        response = client.get("/students/read/get_all_students", params={"username": "1",
                                                                         "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IjEiLCJ1c2VyIHJvbGUiOiJhZG1pbiIsImV4cCI6MTcxMjgyNjA4MH0.bYcZyoyM4zlMTbBQEviOEOMTXGli8ynGtlWQx16z7OI"})
    assert response.value.status_code == 401


def test_get_all_students_no_parameters():
    with pytest.raises(RequestValidationError) as response:
        response = client.get("/students/read/get_all_students", params={})

def test_get_all_students_no_parameters2():
    with pytest.raises(HTTPException) as response:
        response = client.get("/students/read/get_all_students", params={"username": 1,
                                                                         "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
".eyJ1c2VybmFtZSI6IjEiLCJ1c2VyIHJvbGUiOiJhZG1pbiIsImV4cCI6MTcxMjgyNjA4MH0.bYcZyoyM4zlMTbBQEviOEOMTXGli8ynGtlWQx16z7OI"})

def test_get_all_students_no_parameters3():
        with pytest.raises(HTTPException) as response:
            response = client.get("/students/read/get_all_students", params={"username": 10,
                                            "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
".eyJ1c2VybmFtZSI6IjEiLCJ1c2VyIHJvbGUiOiJhZG1pbiIsImV4cCI6MTcxMjgyNjA4MH0.bYcZyoyM4zlMTbBQEviOEOMTXGli8ynGtlWQx16z7OI"})