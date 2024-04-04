from utils.file_operations import load_json


def retrieve_student_by_username(db_path, username: int):
    """
    Retrieve a student from the database by username.

    Parameters:
        file_path (str): The path to the database file.
        username (str): The username of the student to retrieve.

    Returns:
        dict or None: The student data if found, None otherwise.
    """
    try:
        db = load_json(db_path)
        if str(username) in db:
            return db[str(username)]
        else:
            return None
    except FileNotFoundError:
        # Handle file not found error
        print(f"Error: File '{db_path}' not found.")
        return None
    except Exception as e:
        # Handle other unexpected errors
        print(f"An error occurred: {e}")
        return None