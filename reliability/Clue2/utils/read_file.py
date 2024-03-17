from pathlib import Path

from data.reader import Readers


def read_file(file_path):
    """
    Read data from the specified file using the appropriate reader based on the file extension.

    Parameters:
        file_path (str): The path to the input file.

    Returns:
        tuple: A tuple containing the places and weapons read from the file.
    """
    extension = Path(file_path).suffix
    readers = Readers()
    func_name = extension[1:] + "_reader"
    func = getattr(readers, func_name, None)

    if func:
        return func(file_path)
    else:
        raise ValueError("No reader found for extension:", extension)