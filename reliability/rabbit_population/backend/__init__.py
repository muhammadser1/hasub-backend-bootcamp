import logging
import time
import random

from data_processing_scripts.json_handler import process_json_operation
from data_processing_scripts.txt_data_processing import read_records_num, update_records_num

logging.basicConfig(filename='log_info.log', level=logging.DEBUG,
                    format='%(asctime)s  - %(message)s')


def read_records(records_path, records_num_path):
    """
    Read records from a JSON file and retrieve the current number of records.

    Args:
        records_path (str): The file path to the JSON file containing records.
        records_num_path (str): The file path to the file containing the current number of records.

    Returns:
        tuple: A tuple containing the loaded records (list) and the current number of records (int).
    """
    try:
        number = read_records_num(records_num_path)
    except Exception as e:
        print(f"Error occurred while updating records number in file: {e}")
    number2 = 0
    while number2 - number < 10:
        time.sleep(random.randint(5, 10))
        number2 = read_records_num(records_num_path)
    records = process_json_operation(records_path, "r")
    return records, number


def process_records():
    """
    Perform data processing on records.

    Args:
        records_path (str): The file path to the JSON file containing records.
        records_num_path (str): The file path to the file containing the current number of records.
    """
    records_num_path = "data/records_num"
    records_path = "data/sample.json"
    number = 0
    index = 0
    while number <= 250:
        records, number = read_records(records_path, records_num_path)
        deleted_count = 0
        while index < len(records):
            record = records[index]
            if record["rabbit_deaths"] > number:
                logging.info(f"{records[index]} is deleted, total rabbit count is: {number}")
                records.pop(index)
                deleted_count += 1
            else:
                number += record["rabbit_births"]
                number -= record["rabbit_deaths"]
                index += 1

        try:
            process_json_operation(records_path, "w", records)
            update_records_num(records_num_path, number + (0 - deleted_count))
        except Exception as e:
            print(f"Error occurred while updating records: {e}")
        number = read_records_num(records_num_path)
    print("backend end")

print("backend started")
process_records()
