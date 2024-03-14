import csv


def get_records_from_csv(file_path):
    """
    Reads records from a CSV file and returns them as a dictionary.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        dict: A dictionary containing record names as keys and their corresponding amounts as values.
    """
    records = {}
    try:
        with open(file_path, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                records[row["RECORD_NAME"]] = int(row["AMOUNT"])
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error: {e}")
    return records


def write_records_to_csv(records, file_path):
    """
    Writes records to a CSV file.

    Args:
        records (dict): A dictionary containing record names as keys and their corresponding amounts as values.
        file_path (str): The path to the CSV file to write.

    Returns:
        None
    """
    try:
        with open(file_path, 'w', newline='') as csvfile:
            fieldnames = ['RECORD_NAME', 'AMOUNT']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for name, amount in records.items():
                writer.writerow({'RECORD_NAME': name, 'AMOUNT': amount})
        print(f"Records successfully written to '{file_path}'.")
    except Exception as e:
        print(f"Error: {e}")
