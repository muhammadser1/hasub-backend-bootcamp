from models.student import Student
from utils.json_file_utils import *

from utils.json_file_utils import load_json


def update_student(file_path: str, student: Student):
    """
    Update the database with a new student.
    :param file_path (str): The path to the database file.
    :param student (Student): The student object to be added to the database.
    :return: Updated database with the new student added.
    """
    db_students = load_json(file_path)
    db_students[student.id] = {
        "id": student.id,
        "name": student.name,
        "age": student.age,
        "classes": student.classes
    }

    return db_students
