def get_integer_input(msg_to_show:str, min_value=None, max_value=None) -> int:
    """
    Prompt the user to input an integer value within the specified range and return it.

    Parameters:
        msg_to_show (str): Message to display to the user as a prompt.
        min_value (int, optional): Minimum allowed integer value (inclusive). Defaults to None.
        max_value (int, optional): Maximum allowed integer value (inclusive). Defaults to None.

    Returns:
        int: The integer value entered by the user.
    """
    # Loop until a valid integer input within the specified range is provided
    while True:

        # Prompt the user for input
        user_input = input(msg_to_show)
        # Check if the input is a valid integer
        if user_input.isdigit():
            # Convert the input to an integer
            integer_value = int(user_input)
            # Check if the integer is within the specified range
            if (min_value is None or integer_value >= min_value) and (max_value is None or integer_value <= max_value):
                return integer_value
            else:
                print(f"Input must be within the range [{min_value}-{max_value}].")
        else:
            print("Invalid input. Please enter a valid integer.")