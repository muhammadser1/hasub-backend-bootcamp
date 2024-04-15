from fastapi import APIRouter, Depends, Path, HTTPException

from utils.decorators import logging
from utils.dependencies import role_authorization
from utils.file_operations import load_json
from utils.student_utils.get_students_by_class import get_students_by_class
from utils.student_utils.retrieve_student_by_username import retrieve_student_by_username

router = APIRouter()
check_admin_token = role_authorization("admin")
check_guest_token = role_authorization("guest")
check_all_token = role_authorization("all")


@router.get("/students/read", tags=["tests"])
@logging
def test():
    # Test end point to verify server functionality.
    print({"msg": "tests READ student router is working!"})
    return {"msg": "tests READ student router is working!"}


@router.get("/students/read/get_students_in_class/{class_name}", tags=["students"])
@logging
def get_students_in_class(class_name: str, user_data: str = Depends(check_admin_token)):
    """

    :param class_name:
    :param user_data:
    :return:
    """
    students_in_class = get_students_by_class(class_name)
    return students_in_class


@router.get("/students/read/get_all_students", tags=["students"])
@logging
def get_all_students(user_data: str = Depends(check_all_token)):
    """
    """
    try:
        db_student_path = "data/db_students.json"
        db_students = load_json(db_student_path)
        print({"students": db_students})

        return {"students": db_students}
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Database file not found")



@router.get("/students/read/get_student/{student_id}", tags=["students"])
@logging
def retrieve_student_by_id(student_id: int = Path(..., desciption="Enter the id of the student"),
                           user_data: str = Depends(check_all_token)):
    """
    """
    try:
        db_student_path = "data/db_students.json"
        student_info = retrieve_student_by_username(db_path=db_student_path, username=student_id)
        print(student_info)
        return student_info
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Database file not found")
