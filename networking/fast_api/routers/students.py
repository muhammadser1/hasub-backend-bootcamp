from fastapi import APIRouter, Path
from models.student import Student
from utils.db_fns import *
from utils.get_correct_file_path import get_students_data_file_path
from utils.student_utils.check_id_exists import check_student_id_exists
from utils.student_utils.update_student import update_student

router = APIRouter()


@router.get("/")
async def test():
    # Test end point to verify server functionality.
    print("hi from test end point")
    return "hi from test end point :)"

#$ curl -XPOST http://localhost:8000/students/add_student -d '{"id":1,"name":"aaa","age":10,"classes":["aa","bb"]}' -H "Content-Type: application/json"
@router.post("/students/add_student")
async def add_student(student: Student):
    """
    Add a new student to the database.
    :param student (Student) :   The student object representing the new student to be added.
    :return: A message confirming the successful addition of the student, with the student_id
    """
    file_path=get_students_data_file_path('db_students.json')
    if check_student_id_exists(file_path,str(student.id)):
        return "Student with this ID already exists"
    updated_db = update_student(file_path, student)
    write_json(updated_db, file_path)
    return {"message": "Student added successfully", "student_id": student.id}

#$ curl -X GET http://localhost:8000/get_student/3

@router.get("/students/get_student/{student_id}")
async def get_student(student_id: int = Path(..., desciption="Enter the id of the student")):
    """
     Retrieve information about a specific student by their ID.
    :param student_id (int): The ID of the student to retrieve.
    :return: dict: Information about the student with the specified ID.

    The function loads the database and then returns information about the specific student.
    If the student is not found, it returns an appropriate error message.
 """
    try:
        file_path = get_students_data_file_path('db_students.json')
        db_students = load_json(file_path)
        return db_students[str(student_id)]
    except FileNotFoundError:
        return {"error": "Database file not found"}
    except KeyError:
        return {"error": "Student not found"}
    except Exception as e:
        return {"error": f"An error occurred: {e}"}

#$ curl -X GET http://localhost:8000/get_students_in_class/Math

@router.get("/students/get_students_in_class/{class_name}")
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
        file_path = get_students_data_file_path('db_students.json')
        db_students = load_json(file_path)
        students_in_class = [student for student in db_students.values() if class_name in student.get("classes", [])]
        return students_in_class
    except FileNotFoundError:
        return {"error": "Database file not found"}
    except Exception as e:
        return {"error": f"An error occurred: {e}"}



#$ curl -X GET http://localhost:8000/students/get_all_students
@router.get("/students/get_all_students")
async def get_all_students():
    """
    The function returns all the students in the database.
    :return:
    dict: A dictionary containing the database of students. If an error occurs while reading the files,
     it returns an appropriate error message.
    """
    try:
        file_path = get_students_data_file_path('db_students.json')
        db_students = load_json(file_path)
        return db_students
    except FileNotFoundError:
        return {"error": "Database file not found"}
    except Exception as e:
        return {"error": f"An error occurred: {e}"}
