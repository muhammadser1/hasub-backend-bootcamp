import os
import sys

from data_files.csv_handler import *
from operations.record_renderer import init
from utils.get_selected_record import set_environment_variable


def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <file_path>")
        return
    file_path = sys.argv[1]
    set_environment_variable('file_path', file_path)
    init()
    import cli


if __name__ == "__main__":

    main()
