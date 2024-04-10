
from fastapi import APIRouter, Depends

from models.student import Student
from utils.decorators import log_function_call
from utils.dependencies import role_authorization
from utils.student_utils.student_exists_in_db import student_exists_in_db
from utils.student_utils.update_student import update_student

router = APIRouter()
check_admin_token = role_authorization("admin")
check_guest_token = role_authorization("guest")
check_all_token = role_authorization("all")

@router.get("/students/create", tags=["tests"])
@log_function_call
def test():
    # Test end point to verify server functionality.
    print({"msg": "test CREATE student router is working!"})
    return {"msg": "test CREATE student router is working!"}


@log_function_call
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