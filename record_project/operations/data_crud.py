import logging
import os
from data_files.csv_handler import write_records, get_records
from operations.record_renderer import display_records
from utils.get_integer_input import get_integer_input

from utils.get_selected_record import get_selected_index, set_environment_variable, get_selected_record
from utils.sorting import sort_dict_by_keys

logging.basicConfig(filename='recordFileName_log.log', level=logging.INFO, format='%(asctime)s - %(message)s')


def add_record(name, amount):
    records_origin = get_records(os.environ.get('file_path'))
    records = search(name)
    if not records:
        records_origin[name] = amount
    else:
        selected_name, selected_value=get_selected_record(records,msg="Enter the index of the record to add: ")

        records_origin[selected_name] = selected_value + amount
        records_origin = sort_dict_by_keys(records_origin)
    write_records(records_origin, "input2.csv")
    logging.info(f" Insert  Success")


def delete_record(name, amount):
    records_origin = get_records(os.environ.get('file_path'))
    records = search(name)
    if not records or name not in records:
        logging.error("Delete failure.")
        return
    else:
        old_name, old_value = get_selected_record(records, msg="Enter the index of the record to delete: ")
        if amount == old_value:
            records_origin.pop(old_name)
        elif amount > old_value:
            logging.error("Delete failure.")
            return
        elif amount < old_value:
            records_origin[old_name] = old_value - amount
    logging.info(f"Delete Success")
    write_records(records_origin, "input2.csv")


def update_name(old_name, new_name):
    """Updates the name of a record in the database."""
    update_record(old_name, new_name, "name")


def update_amount(name, new_amount):
    """Updates the number of copies of a record in the database."""
    update_record(name, new_amount, "amount")


def update_record(name, new_value, field='name'):
    """Updates a record in the database."""
    records_origin = get_records(os.environ.get('file_path'))
    records = search(name)

    if not records:
        if field == 'name':
            logging.error("UpdateName failure.")
        else:
            logging.error("UpdateAmount failure.")
        return
    old_name, old_value = get_selected_record(records, msg="Enter the index of the record to update: ")
    if field == 'name':
        records_origin.pop(old_name)
        records_origin[new_value] = old_value
        logging.error("UpdateName Search.")
    elif field == 'amount':
        if new_value < 1:
            logging.error("amount must be greater than 0.")
            return
        records_origin[old_name] = new_value
        logging.error("UpdateAmount Success.")

    write_records(records_origin, "input2.csv")


def search(name, do_logging=False):
    """Searches for a record in the database based on the record name."""
    filtered_records = {}
    record = get_records(os.environ.get('file_path'))

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