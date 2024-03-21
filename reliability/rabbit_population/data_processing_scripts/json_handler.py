import json
import random

failure_probability = 0


def get_credentials():
    username = input('Enter username: ')
    password = input('Enter password: ')
    return username == password


def raise_random_exception_with_probability():
    global failure_probability
    try:
        if random.random() < failure_probability:

            random_exception = random.choice([
                FileNotFoundError,
                PermissionError,
                IsADirectoryError,
                FileExistsError,
                NotADirectoryError,
                IOError
            ])
            raise random_exception("Random exception raised")
        else:

            if failure_probability < 1.0:
                failure_probability += 0.05
                print('Failure probability after increase:', failure_probability)
    except Exception as e:
        print(f"Exception caught: {type(e).__name__} - {e}")
        failure_probability = 0
        raise e


def process_json_operation(file_name, operation, data=None):
    try_count = 0
    max_retries = 5
    while try_count < max_retries:
        try:
            raise_random_exception_with_probability()
            with open(file_name, operation) as file:
                if operation == "w":
                    json.dump(data, file, indent=4)
                    return
                elif operation == "r":
                    return json.load(file)
        except FileNotFoundError as e:
            print('File not found:', e)
            print('Please provide the absolute path to the file.')
            file_name = input('Enter the absolute path: ')
        except PermissionError as e:
            print('Permission denied:', e)
            if get_credentials():
                try_count = 0
                print("Reset the try count")
            else:
                exit()
        except FileExistsError as e:
            print('File exists:', e)
            decision = input("Do you want to overwrite it? (yes/no): ")
            if decision != "yes":
                print("Operation canceled by the user.")
                return False
        except NotADirectoryError as e:
            print('Not a directory:', e)
        except IOError as e:
            print('Input/output error:', e)

        try_count += 1
    print(
        f"Failed to {'load' if operation == 'r' else 'save'} records to JSON file '{file_name}' after {max_retries} attempts")
    return None if operation == "r" else False
