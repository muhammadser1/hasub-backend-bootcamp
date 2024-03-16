from pathlib import Path
class Readers:
    @staticmethod
    def json_reader(file_path):
        print("Reading JSON file:", file_path)
        # Implement JSON reading logic here

    @staticmethod
    def txt_reader(file_path):
        print("Reading TXT file:", file_path)
        # Implement TXT reading logic here


def read_file(file_path):

    # Extract the file extension
    extension = Path(file_path).suffix # .json

    # Get the appropriate reader function based on the extension
    readers = Readers()
    func_name = extension[1:] + "_reader"
    func = getattr(readers, func_name, None) # json_reader

    # Call the function if it exists
    if func:
        func(file_path)
    else:
        print("No reader found for extension:", extension)


if __name__ == "__main__":
    # Filepath (getting it from main args)
    filepath = "aaa.json"
    read_file(filepath)
