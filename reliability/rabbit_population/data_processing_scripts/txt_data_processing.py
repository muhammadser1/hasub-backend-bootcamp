def read_records_num(file_name):
    """
    Reads the number of records from a file.

    Args:
        file_name (str): The path to the file containing the number of records.

    Returns:
        int or None: The number of records read from the file, or None if the file content is not a valid integer.
    """
    try:
        with open(file_name, "r") as file:
            text = file.read().strip()
            if text.isdigit():
                return int(text)
            else:
                return None
    except Exception as e:
        print(f"Error occurred while reading records number from file: {e}")
        return None


def update_records_num(file_name, new_num):
    """
    Updates the number of records in a file by adding a new number.

    Args:
        file_name (str): The path to the file containing the number of records.
        new_num (int): The number to add to the existing number of records.
    """
    try:
        number = read_records_num(file_name)
        if number is not None:
            number += new_num
            with open(file_name, "w") as file:
                file.write(str(number))
        else:
            print("Error: Unable to update the records number. File content is not a valid integer.")
    except Exception as e:
        print(f"Error occurred while updating records number in file: {e}")

#
# records_num_path = "../data/records_num"
# try:
#     update_records_num(records_num_path, 50)
# except Exception as e:
#     print(f"Error occurred: {e}")

