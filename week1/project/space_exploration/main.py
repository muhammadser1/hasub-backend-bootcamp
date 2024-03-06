import json
from Space_Ship import *
from Black_Hole import *
from Asteroid_Field import *
from Pirates import *
from Game import *
from Cosmic_Boost import *

def load_ship_data(filename):  # Loads ship data from a JSON file.
    with open(filename, "r") as json_file:
        return json.load(json_file)
def check_input(range1, range2):  #: Handles input validation for selecting a ship number.
    # range1 =< get input number <= range2
    flag = 1
    while flag == 1:
        get_input = input("Enter the ship number: ")
        if get_input.isdigit() == 1:
            get_input = (int)(get_input)
            if get_input >= range1 and get_input <= range2:
                flag = 0
        if flag == 1:
            print("Invalid  input.\n")
    return get_input
def pick_ship():  # allows the user to pick one, and returns the selected ship.
    ships = load_ship_data("ships.json")
    print("This is the list of available ships. Please pick one.\n")
    for i, (ship) in enumerate(ships):
        print(i, ".", ship)
    random_number = check_input(0, len(ships) - 1)
    return Ship(ships[random_number]["name"], ships[random_number]["health"], ships[random_number]["fuel"])
def init_events():  # Initializes a list of game events.
    event_list = [Black_Hole("Black_Hole",15,"A black hole appears nearby!",5), Asteroid_Field("Asteroid_Field", 20,"You encounter a dangerous asteroid field!",10,10),
                  Pirates("Pirates", 15,"Space pirates attack your ship!",15,10),Cosmic_Boost("Cosmic_Boost",10,10,10,"you uncover valuable resources")]
    return event_list
if __name__ == "__main__":
    print(" *** This is a space exploration game. Have fun! *** \n")
    ship = pick_ship()
    events = init_events()
    game = Game(events,ship )
    game.start()
    with open("strings_data.json", "w") as json_file:
        json.dump(game.data, json_file, indent=4)