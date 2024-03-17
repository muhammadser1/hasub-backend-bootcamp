import os
import sys

import gameUI
from Clue_game import Game
from utils.clear_log_file import clear_log_file
from utils.get_integer_input import get_integer_input
from utils.read_file import read_file


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python main.py <file_path>")
        sys.exit(1)

    clear_log_file("game.log")

    file_path = sys.argv[1]
    file_path = os.path.join("data", "data_input", file_path)

    try:
        places, weapons = read_file(file_path)
    except Exception as e:
        print("Error reading file:", e)

        file_path = input("Please enter another file path: ")
        try:
            places, weapons = read_file(file_path)
        except Exception as e:
            print("Error reading file:", e)
            sys.exit(1)

    player_num = get_integer_input("Enter number of players: ", min_value=3)
    game_ui = gameUI.GameUi()

    game = Game(places, weapons, player_num,game_ui)
    game.start()
