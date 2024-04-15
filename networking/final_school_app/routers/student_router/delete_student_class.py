from fastapi import APIRouter, Depends, HTTPException

from utils.decorators import logging
from utils.dependencies import role_authorization
from utils.file_operations import load_json, write_json

router = APIRouter()
check_admin_token = role_authorization("admin")
check_guest_token = role_authorization("guest")
check_all_token = role_authorization("all")


@router.get("/students/delete", tags=["tests"])
@logging
def test():
    # Test end point to verify server functionality.
    print({"msg": "tests DELETE student router is working!"})
    return {"msg": "tests DELETE student router is working!"}


@router.delete("/students/delete/delete_student_by_id", tags=["students"])
@logging
def delete_student(student_id: str, token: str = Depends(check_all_token)):
    """

    :param student_id:
    :param token:
    :return:
    """
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


@router.delete("/students/delete_all_students", tags=["students"])
@logging
def delete_all_students(token: str = Depends(check_admin_token)):
    """

    :param token:
    :return:
    """
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
