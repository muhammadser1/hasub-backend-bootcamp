import os


def get_json_file_path(file_name:str):
    """
    Get the file path for the students data JSON file.
    """
    script_directory = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(script_directory, '..', 'data', file_name)
    return file_path
