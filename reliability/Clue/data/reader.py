import json


class Readers:

    @staticmethod
    def json_reader(file_path):
        try:
            with open(file_path) as f:
                config = json.load(f)
                places = config["places"]
                weapons = config["weapons"]
                return places,weapons
        except FileNotFoundError:
            print("File not found:", file_path)
            return

    @staticmethod
    def txt_reader(file_path):
        try:
            data = {}
            current_section = None

            with open(file_path, 'r') as file:
                for line in file:
                    line = line.strip()
                    if line:
                        if line.endswith(':'):
                            current_section = line[:-1]
                            data[current_section] = []
                        else:
                            data[current_section].append(line)

            return data.get("places", []), data.get("weapons", [])
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
            return [], []
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")
            return [], []
