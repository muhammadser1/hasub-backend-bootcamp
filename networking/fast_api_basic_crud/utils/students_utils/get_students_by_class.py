from utils.file_operations import load_json


def get_students_by_class(db_student_path: str, class_name: str) -> list:
    """
    Retrieve students belonging to a specific class from the database.
    :param db_student_path (str): the path to the JSON database file containing student data.
    :param class_name (str): the name of the class to retrieve students for.
    :return:
        list[dict]: list of all the students that belong to the specified class.
    """
    db_students = load_json(db_student_path)
    students_in_class = [student for student in db_students.values() if class_name in student.get("classes", [])]
    return students_in_class
