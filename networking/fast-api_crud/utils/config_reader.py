def read_config(file_path):
    """
    Read configuration from a text file.

    Parameters:
        file_path (str): The path to the text file containing configuration.

    Returns:
        dict: A dictionary containing configuration settings.
    """
    config = {}
    with open(file_path, 'r') as file:
        for line in file:
            key, value = line.strip().split('=')
            config[key] = value
    return config
