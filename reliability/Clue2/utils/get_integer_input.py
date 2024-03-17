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
        try:
            user_input = int(input(msg_to_show))
            if (min_value is None or user_input >= min_value) and (max_value is None or user_input <= max_value):
                return user_input
            else:
                print(f"Input must be within the range [{min_value}-{max_value}].")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
