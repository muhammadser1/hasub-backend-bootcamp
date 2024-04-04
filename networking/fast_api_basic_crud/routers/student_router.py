from fastapi import APIRouter, Path, Request
from models.student import Student
from utils.file_operations import write_json, load_json
from utils.students_utils.retrieve_student_by_username import retrieve_student_by_username
from utils.students_utils.student_exists_in_db import student_exists_in_db
from utils.students_utils.update_student import update_student

router = APIRouter()


@router.get("/students", tags=["tests"])
async def test():
    # Test end point to verify server functionality.
    print({"msg": "test student router is working!"})
    return {"msg": "test student router is working!"}


@router.post("/students/add_student", tags=["students"])
async def add_student(student: Student):
    """
   #     Add a new student to the database.
   #
   #     Parameters:
   #         student (Student): The student object containing information about the student to be added.
   #
   #     Returns:
   #         dict or str: A dictionary with a success message and the student ID if the student is added successfully.
   #                      If a student with the same ID already exists, returns a string indicating the conflict.
   #     """
    db_student_path = "data/db_students.json"
    if student_exists_in_db(db_path=db_student_path,student_id= student.id):
        print("message:Student with this ID already exists")
        return {"message": "Student with this ID already exists"}

    updated_db = update_student(file_path=db_student_path,student= student)
    write_json(updated_db, db_student_path)
    print("message: Student added successfully, student_id:", student.id)
    return {"message": "Student added successfully", "student_id": student.id}


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
        return retrieve_student_by_username(db_path=db_student_path,username=student_id)
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


@router.get("/students/get_students_in_class/{class_name}", tags=["students"])
async def get_students_in_class(class_name: str = Path(..., description="Enter the class")):
    """
        Retrieve all students belonging to a specific class.
    :param class_name (str): the name of the class to retrieve students for.
    :return:
        list[dict] of all the students that belonging to this class.

    The function iterates over the loaded database and checks if the classes of the students contain the specified class
        name. It then adds the matching students to a list and returns it.
    """
    try:
        db_student_path = "data/db_students.json"
        db_students = load_json(db_student_path)
        students_in_class = [student for student in db_students.values() if class_name in student.get("classes", [])]
        return students_in_class
    except FileNotFoundError:
        return {"error": "Database file not found"}
    except Exception as e:
        return {"error": f"An error occurred: {e}"}
