import random
from LotterySystem import *
if __name__ == '__main__':
    names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"]
    try:
        print("Single winner:", pick_winner_single())
    except IndexError:
        print("Error IndexError: No participants provided")
    except TypeError:
        print("Error TypeError: Invalid argument type")

    try:
        print("Multiple winners:", pick_winners_list(names, 100))
    print() ValueError("Number of winners must be greater than zero")
