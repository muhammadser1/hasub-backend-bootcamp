import os
import sys

import gameUI
from Clue_game import Game
from utils.clear_log_file import clear_log_file
from utils.get_integer_input import get_integer_input
from utils.read_file import read_file


def main(file_path):
    clear_log_file("game.log")

    max_attempts = 5
    attempt = 1

    while attempt <= max_attempts:
        try:
            places, weapons = read_file(file_path)
            break
        except Exception as e:
            print("Error reading file:", e)
            if attempt < max_attempts:
                file_path = input("Please enter another file path: ")
                attempt += 1
            else:
                print("Max attempts reached. Exiting...")
                sys.exit(1)

    player_num = get_integer_input("Enter number of players: ", min_value=3)
    game_ui = gameUI.GameUi()

    game = Game(places, weapons, player_num, game_ui)
    game.start()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <file_path>")
        sys.exit(1)
    main(sys.argv[1])
