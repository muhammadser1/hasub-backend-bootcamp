import os

from data_files.csv_handler import *


def set_environment_variable(name, value):
    """
    Sets an environment variable with the given name and value.

    Args:
        name (str): The name of the environment variable.
        value (str): The value to set for the environment variable.

    Returns:
        None
    """
    try:
        os.environ[name] = value
    except Exception as e:
        print(f"Error setting environment variable: {e}")


def initialize_environment_with_new_records():
    """
    Initialize the environment with new records from a specified file.

    This function retrieves records from a file specified by the 'file_path' environment variable,
    sets the 'file_path' environment variable to a new file ("input2.csv"), and writes the retrieved
    records to the new file.

    Parameters:
    None

    Returns:
    None
    """
    record = get_records_from_csv(os.environ.get('file_path'))
    set_environment_variable('file_path', "input2.csv")
    write_records_to_csv(record, "input2.csv")
