import sys
from cli import cli_interface
from utils.environment_variable import *


def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <file_path>")
        return
    file_path = sys.argv[1]
    set_environment_variable('file_path', file_path)
    initialize_environment_with_new_records()
    cli_interface()


if __name__ == "__main__":

    main()
