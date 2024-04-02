from models.student import Student
from utils.db_fns import load_json


def update_student(file_path: str, student: Student):
    """
    Update the database with a new student.
    :param file_path (str): The path to the database file.
    :param student (Student): The student object to be added to the database.
    :return: Updated database with the new student added.
    """
    db_students = load_json(file_path)
    if str(student.id) in db_students:
        return "Student with this ID already exists"
    db_students[student.id] = {
        "id": student.id,
        "name": student.name,
        "age": student.age,
        "classes": student.classes
    }
    return db_students