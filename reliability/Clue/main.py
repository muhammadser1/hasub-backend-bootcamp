import os
import sys
from pathlib import Path

from Clue_Game2 import Game
from data.reader import Readers


def clear_log_file(file_path):
    """Clear the contents of the specified log file."""
    with open(file_path, 'w'):
        pass


def read_file(file_path):
    """
    Read data from the specified file using the appropriate reader based on the file extension.

    Parameters:
        file_path (str): The path to the input file.

    Returns:
        tuple: A tuple containing the places and weapons read from the file.
    """
    extension = Path(file_path).suffix
    readers = Readers()
    func_name = extension[1:] + "_reader"
    func = getattr(readers, func_name, None)

    if func:
        return func(file_path)
    else:
        raise ValueError("No reader found for extension:", extension)


def get_integer_input(msg_to_show: str, min_value=None, max_value=None) -> int:
    """
    Prompt the user to input an integer value within the specified range and return it.

    Parameters:
        msg_to_show (str): Message to display to the user as a prompt.
        min_value (int, optional): Minimum allowed integer value (inclusive). Defaults to None.
        max_value (int, optional): Maximum allowed integer value (inclusive). Defaults to None.

    Returns:
        int: The integer value entered by the user.
    """
    while True:
        user_input = input(msg_to_show)
        if user_input.isdigit():
            integer_value = int(user_input)
            if (min_value is None or integer_value >= min_value) and (max_value is None or integer_value <= max_value):
                return integer_value
            else:
                print(f"Input must be within the range [{min_value}-{max_value}].")
        else:
            print("Invalid input. Please enter a valid integer.")


if len(sys.argv) != 2:
    print("Usage: python main.py <file_path>")
    sys.exit(1)

# Clear the log file
clear_log_file("game.log")

file_path = sys.argv[1]
file_path = os.path.join("data", "data_input", file_path)

# Attempt to read the file
try:
    places, weapons = read_file(file_path)
except Exception as e:
    print("Error reading file:", e)
    # Ask the user to input another file path
    file_path = input("Please enter another file path: ")
    try:
        places, weapons = read_file(file_path)
    except Exception as e:
        print("Error reading file:", e)
        sys.exit(1)

player_num = get_integer_input("Enter number of players: ", min_value=1)

game = Game(places, weapons, player_num)
game.start()
