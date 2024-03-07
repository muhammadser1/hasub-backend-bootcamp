class ApiKeyReader:

    def __init__(self, file_name_key):
        self.file_name_key = file_name_key

    def read_api_key(self):
        """Read and return the API key from the file.

        Returns:
            str: The API key read from the file.
        """
        with open(self.file_name_key, 'r') as file:
            return file.read().strip()
