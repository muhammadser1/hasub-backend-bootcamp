from Game import *


def check_input(range1, range2):  # range1 =< get input number <= range2
    flag = 1
    while flag == 1:
        get_input = input("")
        if get_input.isdigit() == 1:
            get_input = (int)(get_input)
            if get_input >= range1 and get_input <= range2:
                flag = 0
        if flag == 1:
            print("Invalid  input.\n")
    return get_input


def informations():
    print("Welcome to the space exploration game.\n"
          "There are 9 planets, each one may have an event. You should travel to the next planet or the one after that. If you arrive at the final planet alive, you will win the game. "
          "Each planet will give you bonus fuel and coins, but be aware, they may have events that harm you. Make each decision have consequences.\n")


def choosing_ship():
    get_input = 10
    while get_input > 3 or get_input < 0:
        print("Please choose which ship you want to pick. Enter the ship number:")
        get_input = check_input(0, 3)
        print("Nice choice! You picked a great ship.")
    return get_input


def inputs():
    get_input = check_input(1, 5)
    if get_input == 1:
        print(x.user_ship)
    if get_input == 2:
        x.print_rest(x.user_ship.place_id)
    if get_input == 3:
        print("the next planet is: ", x.list_planets[x.user_ship.place_id + 1])
        if x.list_planets[x.user_ship.place_id + 1].event is not None:
            print("Be, aware, there is", x.list_planets[x.user_ship.place_id + 1].event.name)
        print("1. Want to continue ?")
        print("2. Stop the game?")
        get_input=check_input(1,2)
        if get_input==1:
            x.update_status()
        if get_input ==2:
            return "stop"
    if get_input == 4:
        return "stop"


if __name__ == "__main__":
    x = Game()
    x.init_game()
    informations()
    x.print_ships()
    x.choose_ship(choosing_ship())
    Failed_Flag = True
    print("1. Lunch the ship")
    print("Press 1 to launch the ship and go")
    input2 = check_input(1, 1)
    while x.user_ship.health > 0 and Failed_Flag and x.user_ship.coin>=0 and x.user_ship.fuel:
        print("\n1. View Player_Ship status")
        print("2. Print the rest of planets")
        print("3. Move to the next planet")
        print("4. stop the game")
        input_user=inputs()
        if  x.user_ship.place_id==9:
            break
        if input_user=="stop":
            break
    if input_user == "stop":
        print("You have decided to stop the game.")
        print("Ship's health:", x.user_ship.health)
        print("Coins collected:", x.user_ship.coin)
    if x.user_ship.place_id == 9:
        print("Congratulations! You have successfully reached the final planet!")
        print("Ship's health:", x.user_ship.health)
        print("Coins collected:", x.user_ship.coin)
    if x.user_ship.health < 0:
        print("Unfortunately, your ship's health has depleted.")
        print("You died!")
    if x.user_ship.health < 0:
        print("Unfortunately, your ship's fuel has depleted.")
        print("You will drift into space without fuel. Game over!")

