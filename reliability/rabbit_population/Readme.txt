My code includes the following components:

log_info: I save all the records that I delete because the number is bigger than the total number of rabbits.



Data Folder:
records_num.txt: Saves the number of rabbits.
sample.json: Stores the records as a list of dictionaries. Each element of the list is a dictionary containing information about time, births, and deaths.
I chose to use a list because I need to iterate over the index. If I were to iterate over dictionaries directly, skipping records during deletion would be problematic.




Data Processing Scripts Folder:
txt_data_processing: This module handles reading and writing the number of rabbits from/to a text file.
json_handler: Responsible for processing JSON files, providing functionalities for reading and writing with raise_random_exception_with_probability for error handling.




Backend Dict:
This dictionary includes an __init__ function that manages the backend's functionality, such as reading and updating the number of rabbits.
Rabbit Sensor Dict:
This component includes an __init__ function responsible for creating and generating new records, as well as updating the JSON file.




Main:
I utilize multiprocessing to run these packages in parallel.


Handling Errors:

I implemented a loop with a maximum number of tries for each operation (reading/writing). If the operation fails,
the loop provides additional attempts for all possible exceptions.

If a 'FileNotFoundError' occurs, the user is prompted to input the absolute path, granting them another chance to proceed.

For 'PermissionError', I designed a basic authentication function where the user can input their username and password.
 If the credentials match (password == username), the user receives more attempts (resetting the try count).

When encountering a 'FileExistsError', the user is given the option to choose whether to overwrite the existing file.
 If he opts not to overwrite, the program exits; if he chooses to overwrite, the operation proceeds.

I understand that a more advanced approach could involve creating multiple 'sample.json' files if reading or writing fails,
 but due to time constraints, I have not implemented this yet. However, I have demonstrated a simplified version of error handling in
 file reading during a recent class session on Tuesdays."