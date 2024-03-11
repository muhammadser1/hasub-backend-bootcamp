# input_user.py

import logging

# Configure logging
logging.basicConfig(filename='input.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


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
        logging.info(f"User input: {user_input}")

        if user_input.isdigit():
            integer_value = int(user_input)
            if (min_value is None or integer_value >= min_value) and (max_value is None or integer_value <= max_value):
                logging.info("Valid input received.")
                return integer_value
            else:
                logging.warning("Input out of range.")
                print(f"Input must be within the range [{min_value}-{max_value}].")
        else:
            logging.warning("Invalid input received.")
            print("Invalid input. Please enter a valid integer.")
