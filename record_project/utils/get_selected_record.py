import os

from utils.get_integer_input import get_integer_input
from utils.sorting import sort_dict_by_keys


def get_selected_index(records, index):
    """Returns the record at the specified index in the sorted dictionary.

    Args:
        records (dict): A dictionary containing record names as keys and their corresponding amounts as values.
        index (int): The index of the record to retrieve.

    Returns:
        list: A list containing the record name and its corresponding amount at the specified index.
              If the index is out of range, returns None.
    """
    records = sort_dict_by_keys(records)
    for i, (record_name, amount) in enumerate(records.items()):
        if i == index:
            return [record_name, amount]
    return None


def get_selected_record(records,msg):
    """
    Get the index of the record to update and retrieve the selected record.

    Parameters:
    - records (dict): The dictionary of records.

    Returns:
    - selected_record (tuple): A tuple containing the name and value of the selected record.
    """
    index = get_integer_input(msg, 0, len(records) - 1)
    return get_selected_index(records, index)



def set_environment_variable(name, value):
    """Sets an environment variable with the given name and value."""
    os.environ[name] = value
