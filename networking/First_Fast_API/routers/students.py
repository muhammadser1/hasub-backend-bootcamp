from http.client import HTTPException
from fastapi import APIRouter, Path
from models.student import Student
from utils.db_fns import *
from utils.update_student import *

router = APIRouter()


@router.get("/")
async def test():
    # Test end point to verify server functionality.
    print("hi from test end point")
    return "hi from test end point :)"


@router.post("/add_student")
async def add_student(student: Student):
    """
    Add a new student to the database.
    :param student (Student) :   The student object representing the new student to be added.
    :return: A message confirming the successful addition of the student, with the student_id
    """
    file_path = ".\data\db_students.json"
    updated_db = update_student(file_path, student)
    write_json(updated_db, file_path)
    return {"message": "Student added successfully", "student_id": student.id}

# @router.get("/get_student/{student_id}")
# async def get_student(student_id: int = Path(..., desciption="Enter the id of the student")):
#     """
#      Retrieve information about a specific student by their ID.
#     :param student_id (int): The ID of the student to retrieve.
#     :return: dict: Information about the student with the specified ID.
#
#     The function loads the database and then returns information about the specific student.
#     If the student is not found, it returns an appropriate error message.
#  """
#     try:
#         file_path = "./data/db_students.json"
#         db_students = load_json(file_path)
#         return db_students[str(student_id)]
#     except FileNotFoundError:
#         return {"error": "Database file not found"}
#     except KeyError:
#         return {"error": "Student not found"}
#     except Exception as e:
#         return {"error": f"An error occurred: {e}"}
#
#
# @router.get("/get_students_in_class/{class_name}")
# async def get_students_in_class(class_name: str = Path(..., description="Enter the class")):
#     """
#         Retrieve all students belonging to a specific class.
#     :param class_name (str): the name of the class to retrieve students for.
#     :return:
#         list[dict] of all the students that belonging to this class.
#
#     The function iterates over the loaded database and checks if the classes of the students contain the specified class
#         name. It then adds the matching students to a list and returns it.
#     """
#     try:
#         file_path = "./data/db_students.json"
#         db_students = load_json(file_path)
#         students = []
#
#         for student, value in db_students.items():
#             if class_name in value["classes"]:
#                 students.append(value)
#         return students
#     except FileNotFoundError:
#         return {"error": "Database file not found"}
#     except Exception as e:
#         return {"error": f"An error occurred: {e}"}
#
#
# @router.get("/get_all_students")
# async def get_all_students():
#     """
#     The function returns all the students in the database.
#     :return:
#     dict: A dictionary containing the database of students. If an error occurs while reading the files,
#      it returns an appropriate error message.
#     """
#     try:
#         file_path = "./data/db_students.json"
#         db_students = load_json(file_path)
#         return db_students
#     except FileNotFoundError:
#         return {"error": "Database file not found"}
#     except Exception as e:
#         return {"error": f"An error occurred: {e}"}
