from fastapi import APIRouter, Depends, Path

from models.student import Student
from utils.decorators import log_function_call
from utils.dependencies import *
from utils.file_operations import load_json, write_json
from utils.students_utils.get_students_by_class import get_students_by_class
from utils.students_utils.retrieve_student_by_username import retrieve_student_by_username
from utils.students_utils.student_exists_in_db import student_exists_in_db
from utils.students_utils.update_student import update_student

router = APIRouter()


@router.get("/students", tags=["tests"])
@log_function_call
def test():
    # Test end point to verify server functionality.
    print({"msg": "test student router is working!"})
    return {"msg": "test student router is working!"}


@log_function_call
@router.post("/students/add_student", tags=["students"])
def add_student(student: Student, user_data: str = Depends(check_admin_token)):
    if student_exists_in_db(student_id=student.id):
        return {"message": "Student with this ID already exists"}
    updated_db = update_student(student=student)
    return {"message": "Student added successfully", "student_id": student.id}

@router.get("/students/get_students_in_class/{class_name}", tags=["students"])
@log_function_call
def get_students_in_class(class_name: str, user_data: str = Depends(check_admin_token)):
    students_in_class = get_students_by_class(class_name)
    return students_in_class
##########################################################################
@router.get("/students/get_student/{student_id}", tags=["students"])
@log_function_call
def retrieve_student_by_id(student_id: int = Path(..., desciption="Enter the id of the student"),user_data: str = Depends(check_all_token)):
    """
    """
    try:
        db_student_path = "data/db_students.json"
        student_info = retrieve_student_by_username(db_path=db_student_path, username=student_id)
        print(student_info)
        return student_info
    except FileNotFoundError:
        return {"error": "Database file not found"}
    except KeyError:
        return {"error": "Student not found"}
    except Exception as e:
        return {"error": f"An error occurred: {e}"}

@router.get("/students/get_all_students", tags=["students"])
@log_function_call
def get_all_students(user_data: str = Depends(check_all_token)):
    """
    """
    try:
        db_student_path = "data/db_students.json"
        db_students = load_json(db_student_path)
        print({"students": db_students})

        return {"students": db_students}
    except FileNotFoundError:
        return {"error": "Database file not found"}
    except Exception as e:
        return {"error": f"An  error occurred: {e}"}
from fastapi import HTTPException
from fastapi import Depends

@router.delete("/students/delete_all_students", tags=["students"])
@log_function_call
def delete_all_students(token: str = Depends(check_admin_token)):
    try:
        db_student_path = "data/db_students.json"
        db_Students = load_json(db_student_path)
        db_Students.clear()
        write_json(db_Students, db_student_path)
        result = {"message": "All students deleted successfully"}
        print(result)
        return result
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Database file not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")


@router.delete("/students/delete_student_by_id", tags=["students"])
@log_function_call
def delete_student(student_id: str, token: str = Depends(check_admin_token)):
    db_student_path = "data/db_students.json"
    db_Students = load_json(db_student_path)
    if student_id in db_Students:
        del db_Students[student_id]
        result = {"msg": f"Student with {student_id} id is removed"}
        write_json(db_Students, db_student_path)
        print(db_Students)
        return result
    else:
        print({"msg: ", "student is not existed"})
        return {"msg: ", "student is not existed"}

