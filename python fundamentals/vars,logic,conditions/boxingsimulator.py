import random

if __name__ == "__main__":
    win_array1 = [0, -1, -1, 1]
    win_array2 = [1, 0, -1, -1]
    win_array3 = [1, 1, 0, -1]
    win_array4 = [-1, 1, 1, 0]
    arrays=[win_array1,win_array2,win_array3,win_array4]
    flag_fight = 1
    my_point = 0
    cpu_point = 0
    while flag_fight:
        print("1. championship fight (5 rounds).")
        print("2. regular fight      (3 rounds).")
        type_input = input("Please select the type of fight: ")
        if type_input.isdigit() == 1:
            type_input = (int)(type_input)
            if type_input >= 1 and type_input <= 2:
                flag_fight = 0
                if (type_input == 1):
                    rounds_num = 5
                else:
                    rounds_num = 3
    i = 1
    flag = 0
    while i <= rounds_num:
        flag = 0
        type_input = input("Please select the type of punch(1-4)")
        if type_input.isdigit() == 1:
            type_input = (int)(type_input)
            if type_input >= 1 and type_input <= 4:
                random_number = random.randint(1, 4)
                my_point+=arrays[type_input-1][random_number-1]
                cpu_point += (0- arrays[type_input-1][random_number - 1])

                print("my punch number is: " + str(type_input))
                print("computer punsh num is: "+ str(random_number))
                print("my point is "+ str(my_point))
                print("cpu_point  is " + str(cpu_point))
                i += 1
            else:
                flag = 1
        else:
            flag = 1
        if (flag == 1):
            print("wrong input, try again \n")

    print("I am the winner siiiiiiiiii") if my_point > cpu_point else print("Loser")
