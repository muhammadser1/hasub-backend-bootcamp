import logging
import os

from data_files.csv_handler import get_records, write_records
from utils.get_selected_record import set_environment_variable
from utils.sorting import sort_dict_by_keys

logging.basicConfig(filename='recordFileName_log.log', level=logging.INFO, format='%(asctime)s - %(message)s')

import os
import logging


def PrintAll():
    """
    Print all records from a file specified in the environment variable 'file_path'.

    Parameters:
    None

    Returns:
    None
    """
    records = get_records(os.environ.get('file_path'))
    if not records:
        logging.info("The record is empty")
    else:
        display_records(records, True)


import logging


def display_records(records, do_logging=False):
    """
    Display records either on the console or through logging.

    This function takes a dictionary of records and displays them either on the console or
    through logging, depending on the value of the do_logging parameter.

    Parameters:
    - records (dict): A dictionary containing records to display.
    - do_logging (bool, optional): If True, records will be logged; otherwise, they will be printed on the console.
                                    Default is False.

    Returns:
    None
    """
    records = sort_dict_by_keys(records)
    for i, (name, amount) in enumerate(records.items()):
        if do_logging:
            logging.info(f"PrintAll {name} {amount}")
        else:
            print(f"{i}. {name} {amount}")


def PrintTotalAmount():
    """
    Print the total amount of all records from a file specified in the environment variable 'file_path'.

    Parameters:
    None

    Returns:
    None
    """
    record = get_records(os.environ.get('file_path'))
    record = sort_dict_by_keys(record)

    count = 0
    for _, amount in record.items():
        count += int(amount)
    logging.info(f"PrintAmount: {count}")


def init():
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
    record = get_records(os.environ.get('file_path'))
    set_environment_variable('file_path', "input2.csv")
    write_records(record, "input2.csv")
