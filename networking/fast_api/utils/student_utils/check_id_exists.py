from utils.db_fns import load_json


def check_student_id_exists(file_path: str, student_id: str) -> bool:
    """
    Check if a student with the given ID already exists in the database.
    :param file_path (str): The path to the database file.
    :param student_id (str): The ID of the student to check.
    :return: True if the student with the given ID exists, False otherwise.
    """
    db_students = load_json(file_path)
    return str(student_id) in db_students