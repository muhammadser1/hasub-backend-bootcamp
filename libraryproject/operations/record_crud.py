import logging
import os

from data_files.csv_handler import *
from operations.record_printer import display_records
from utils.get_selected_record import get_record_at_index
from utils.sorting import sort_dict_by_keys

logging.basicConfig(filename='recordFileName_log.log', level=logging.INFO, format='%(asctime)s - %(message)s')


def get_and_search_records(name):
    """
    Retrieve records from a CSV file and search for a specific record by name.

    Args:
        name (str): The name of the record to search for.

    Returns:
        dict: A dictionary containing records matching the search criteria.
    """
    records_origin = get_records_from_csv(os.environ.get('file_path'))
    records = search(name)
    return records_origin, records


def add_record(name, amount):
    """
    Add a record with the specified name and amount.

    Args:
        name (str): The name of the record.
        amount (int): The amount to add to the record.

    Returns:
        None
    """
    records_origin, records = get_and_search_records(name)
    if not records:
        records_origin[name] = amount
    else:
        selected_name, selected_value = get_record_at_index(records, msg="Enter the index of the record to add: ")
        records_origin[selected_name] = selected_value + amount

    write_records_to_csv(sort_dict_by_keys(records_origin), "input2.csv")
    logging.info(f" Insert  Success")


def delete_record(name, amount):
    """
    Delete a record with the specified name and amount.

    Args:
        name (str): The name of the record to delete.
        amount (int): The amount to delete from the record.

    Returns:
        None
    """
    records_origin, records = get_and_search_records(name)

    if not records or name not in records:
        logging.error("Delete failure.")
        return
    else:
        old_name, old_value = get_record_at_index(records, msg="Enter the index of the record to delete: ")
        if amount == old_value:
            records_origin.pop(old_name)
        elif amount > old_value:
            logging.error("Delete failure.")
            return
        elif amount < old_value:
            records_origin[old_name] = old_value - amount
    write_records_to_csv(records_origin, "input2.csv")
    logging.info(f"Delete Success")


def search(name, do_logging=False):
    """Searches for a record in the database based on the record name."""
    filtered_records = {}
    record = get_records_from_csv(os.environ.get('file_path'))

    for record_name, value in record.items():
        if name in record_name:
            filtered_records[record_name] = value
    if (name not in filtered_records or not filtered_records) and do_logging:
        logging.info("Search failure.")
    else:
        display_records(filtered_records)
        if do_logging:
            logging.info(f"Search Success")
        return filtered_records


def update_record(name, new_value, field='name'):
    """
    Update a record in the database with the specified name and value.

    Args:
        name (str): The name of the record to update.
        new_value (str|int): The new value to update the record with.
        field (str, optional): The field to update ('name' or 'amount'). Defaults to 'name'.

    Returns:
        None
    """
    try:
        records_origin, records = get_and_search_records(name)

        if not records:
            if field == 'name':
                return records
        old_name, old_value = get_record_at_index(records, msg="Enter the index of the record to update: ")
        if field == 'name':
            records_origin.pop(old_name)
            records_origin[new_value] = old_value
            logging.info("UpdateName Success.")
        elif field == 'amount':
            if new_value < 1:
                logging.error("UpdateAmount failure: Amount must be greater than 0.")
                return
            records_origin[old_name] = new_value
            logging.info("UpdateAmount Success.")

        write_records_to_csv(sort_dict_by_keys(records_origin), "input2.csv")
    except Exception as e:
        logging.error(f"Error updating record: {e}")


def update_record_name(name, new_name):
    """Updates the name of a record in the database."""
    records = update_record(name, new_name, field='name')
    if not records:
        logging.error("UpdateName failure: Record not found.")


def update_record_amount(name, new_amount):
    """Updates the amount of a record in the database."""
    records = update_record(name, new_amount, field='amount')
    if not records:
        logging.error("UpdateAmount failure: Record not found.")
