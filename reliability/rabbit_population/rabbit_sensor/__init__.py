import datetime
import random
import time
from data_processing_scripts.json_handler import process_json_operation
from data_processing_scripts.txt_data_processing import read_records_num, update_records_num


def generate_random_records(records):
    """
    Generates a random record with a timestamp, number of rabbit deaths, and number of rabbit births.
    """
    for _ in range(10):
        record = {"timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                  "rabbit_deaths": random.randint(1, 10),
                  "rabbit_births": random.randint(1, 5)}
        records.append(record)
        time.sleep(random.randint(1, 5))
    return records


def generate_and_save_records():
    """
    Generates random records and saves them to a JSON file.
    """
    records_num_path = "data/records_num"
    records_path = "data/sample.json"
    records_num = read_records_num(records_num_path)

    while records_num < 250:
        try:

            records = process_json_operation(records_path,"r")
            records = generate_random_records(records)
            process_json_operation(records_path,"w" ,records)

            try:
                update_records_num(records_num_path, 10)
                print("new data updated")
            except Exception as e:
                print(f"Error occurred: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
        records_num = read_records_num(records_num_path)
    print("sensor end")


generate_and_save_records()
