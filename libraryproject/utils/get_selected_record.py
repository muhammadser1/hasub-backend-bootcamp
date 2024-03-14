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


def get_record_at_index(records, message):
    """
    Get the index of the record to update and retrieve the selected record.

    Args:
        records (dict): The dictionary of records.
        message (str): The message to prompt the user for input.

    Returns:
        tuple or None: A tuple containing the name and value of the selected record.
                       Returns None if the index is out of range.
    """
    index = get_integer_input(message, 0, len(records) - 1)
    selected_record = get_selected_index(records, index)
    return selected_record if selected_record else None


