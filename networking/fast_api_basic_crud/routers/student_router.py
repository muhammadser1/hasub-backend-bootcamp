from fastapi import APIRouter, Path, Request
from models.student import Student
from utils.auth_utils.jwt_manager import check_token
from utils.file_operations import write_json, load_json
from utils.students_utils.get_students_by_class import get_students_by_class
from utils.students_utils.parse_student_from_request import parse_student_from_request
from utils.students_utils.retrieve_student_by_username import retrieve_student_by_username
from utils.students_utils.student_exists_in_db import student_exists_in_db
from utils.students_utils.update_student import update_student

router = APIRouter()


@router.get("/students", tags=["tests"])
async def test():
    # Test end point to verify server functionality.
    print({"msg": "test student router is working!"})
    return {"msg": "test student router is working!"}


@router.get("/students/get_students_in_class/{class_name}", tags=["students"])
async def get_students_in_class(request: Request, class_name: str, username: str):
    """
        Retrieve all students belonging to a specific class.
    :param class_name (str): the name of the class to retrieve students for.
    :return:
        list[dict] of all the students that belonging to this class.

    The function iterates over the loaded database and checks if the classes of the students contain the specified class
        name. It then adds the matching students to a list and returns it.
    """
    db_student_path = "data/db_students.json"
    token_path = "data/db_user_tokens.json"
    token_status = check_token(request, username, token_path)

    if token_status == "admin":
        students_in_class = get_students_by_class(db_student_path, class_name)
        return students_in_class
    elif token_status == "guest":
        return {"message": "You are not an admin"}
    else:
        return {"message": "Invalid token"}

@router.post("/students/add_student", tags=["students"])
async def add_student(request: Request, username: str):
    db_student_path = "data/db_students.json"
    token_path = "data/db_user_tokens.json"
    student = await parse_student_from_request(request)
    if check_token(request, username, token_path) == "admin":
        if student_exists_in_db(db_path=db_student_path, student_id=student.id):
            return {"message": "Student with this ID already exists"}
        updated_db = update_student(file_path=db_student_path, student=student)
        write_json(updated_db, db_student_path)
        return {"message": "Student added successfully", "student_id": student.id}
    if check_token(request, username, token_path) == "guest":
        return {"message":"you are not an admin"}

@router.get("/students/get_student/{student_id}", tags=["students"])
async def get_student(student_id: int = Path(..., desciption="Enter the id of the student")):
    """
     Retrieve information about a specific student by their ID.
    :param student_id:
    :param student_id (int): The ID of the student to retrieve.
    :return: dict: Information about the student with the specified ID.

    The function loads the database and then returns information about the specific student.
    If the student is not found, it returns an appropriate error message.
 """
    try:
        db_student_path = "data/db_students.json"
        return retrieve_student_by_username(db_path=db_student_path, username=student_id)
    except FileNotFoundError:
        return {"error": "Database file not found"}
    except KeyError:
        return {"error": "Student not found"}
    except Exception as e:
        return {"error": f"An error occurred: {e}"}


@router.get("/students/get_all_students", tags=["students"])
async def get_all_students():
    """
    The function returns all the students in the database.
    :return:
    dict: A dictionary containing the database of students. If an error occurs while reading the files,
     it returns an appropriate error message.
    """
    try:
        db_student_path = "data/db_students.json"
        db_students = load_json(db_student_path)
        return {"students": db_students}
    except FileNotFoundError:
        return {"error": "Database file not found"}
    except Exception as e:
        return {"error": f"An  error occurred: {e}"}



