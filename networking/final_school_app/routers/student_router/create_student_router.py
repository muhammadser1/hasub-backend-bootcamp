from fastapi import APIRouter, Depends

from models.student_model import Student
from utils.decorators import logging
from utils.dependencies import role_authorization
from utils.student_utils.student_exists_in_db import student_exists_in_db
from utils.student_utils.update_student import update_student

router = APIRouter()
check_admin_token = role_authorization("admin")
check_guest_token = role_authorization("guest")
check_all_token = role_authorization("all")


@router.get("/students/create", tags=["tests"])
@logging
def test():
    # Test end point to verify server functionality.
    print({"msg": "tests CREATE student router is working!"})
    return {"msg": "tests CREATE student router is working!"}


@logging
@router.post("/students/create/add_student", tags=["students"])
def add_student(student: Student, user_data: str = Depends(check_admin_token)):
    """

    :param student:
    :param user_data:
    :return:
    """
    if student_exists_in_db(student_id=student.id):
        print("message: Student with this ID already exists")
        return {"message": "Student with this ID already exists"}
    updated_db = update_student(student=student)
    return {"message": "Student added successfully", "student_id": student.id}
