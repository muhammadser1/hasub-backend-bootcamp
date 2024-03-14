def sort_dict_by_keys(input_dict):
    """
    Sort a dictionary by its keys in a case-insensitive manner.

    This function takes a dictionary as input and returns a new dictionary
    with its keys sorted in a case-insensitive manner.

    Parameters:
    - input_dict (dict): The dictionary to be sorted.

    Returns:
    - sorted_dict (dict): The sorted dictionary.
    """
    sorted_keys = sorted(input_dict.keys(), key=lambda x: x.lower())
    sorted_dict = {k: input_dict[k] for k in sorted_keys}
    return sorted_dict
