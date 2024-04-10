from models.student import Student
from utils.file_operations import load_json, write_json


def update_student(student: Student):
    """
    Update student data in the database.

    Parameters:
        file_path (str): The path to the database file.
        student_id (int): The ID of the student to update.
        updated_data (dict): The updated data for the student.

    Returns:
        bool: True if the student is successfully updated, False otherwise.
    """
    try:
        db_path = "data/db_students.json"
        db_students = load_json(db_path)
        db_students[student.id] = {
            "id": student.id,
            "name": student.name,
            "age": student.age,
            "classes": student.classes
        }
        write_json(db_students, db_path)
        print(f"Student with ID {student.id} updated successfully.")
        return db_students
    except FileNotFoundError:
        print(f"Error: File '{db_path}' not found.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

