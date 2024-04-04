from utils.file_operations import load_json


def student_exists_in_db(db_path: str, student_id: int) -> bool:
    """
    Check if a student with the given ID exists in the database.

    Parameters:
        db_path (str): The path to the student database file.
        student_id (int): The ID of the student to check.

    Returns:
        bool: True if the student exists in the database, False otherwise.
    """
    student_data = load_json(db_path)
    return str(student_id) in student_data
