import json
import matplotlib.pyplot as plt
import numpy as np


def create_tag_dic(tag_dict):
    file_path = "data.json"
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    for game_name, game_info in data.items():
        words = game_info["Info"].split(", ")
        for i in range(len(words)):
            tag_dict[words[i]] = 0
    c = 0
    while c < 2:
        for game_name, game_info in data.items():
            words = game_info["Info"].split(", ")
            for i in range(len(words)):
                if c == 0:
                    tag_dict[words[i]] = 0
                else:
                    tag_dict[words[i]] += 1
        c += 1
def fill_x_y(tag_dict):
    x_axis=[]
    y_axis=[]
    for k,v in tag_dict.items():
        x_axis.append(k)
        y_axis.append(v)
    return x_axis,y_axis
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
def main():
    tag_dict = {}
    create_tag_dic(tag_dict)
    print(tag_dict)
    Keymax = max(zip(tag_dict.values(), tag_dict.keys()))[1]
    print("\nThe max tag is", Keymax, "with a value of:", tag_dict[Keymax])
    x_axis,y_axis=fill_x_y(tag_dict)
    x = np.array(x_axis)
    y = np.array(y_axis)
    bars = plt.bar(x, y)
    get_input=10
    for i in range(len(x_axis)):
        print(i,". "+x_axis[i])
    print("Please choose a tag:\n")
    while get_input!=1:
        get_input=check_input(0,len(x_axis)-1)
        if get_input>=0 and get_input<=72:
            break
    print("the % of ", x_axis[get_input]," from the games list is : ", y_axis[get_input] / len(y_axis))
    bars[get_input].set_color('red')
    plt.show()
