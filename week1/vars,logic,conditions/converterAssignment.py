def conversion_temp():
    type_check = 1
    while type_check:
        print("1.F to C")
        print("2.C to F ")
        type_input = input("Please select the number corresponding to the type of conversion: ")
        if type_input.isdigit() == 1:
            type_input = (int)(type_input)
            if type_input >= 1 and type_input <= 2:
                match type_input:
                    case 1:
                        value = input("What is the source value?")
                        if value.isdigit() == 1:
                            value = (float)(value)
                            return float((value - 32) * 5 / 9)
                    case 2:
                        value = input("What is the source value?")
                        if value.isdigit() == 1:
                            value = (float)(value)
                            return float((value * 9 / 5) + 32)
        if type_check == 1:
            print("Wrong Input")
def conversion_speed():
    type_check = 1
    while type_check:
        print("1.KPH TO MPH")
        print("2.MPH TO KPH")
        type_input = input("Please select the number corresponding to the type of conversion: ")
        if type_input.isdigit() == 1:
            type_input = (int)(type_input)
            if type_input >= 1 and type_input <= 2:
                match type_input:
                    case 1:
                        value = input("What is the source value?")
                        if value.isdigit() == 1:
                            value = (float)(value)
                            return value / 1.609
                    case 2:
                        value = input("What is the source value?")
                        if value.isdigit() == 1:
                            value = (float)(value)
                            return value * 1.609
        if type_check == 1:
            print("Wrong Input")
def conversion_weight():
    type_check = 1
    while type_check:
        print("1.kg to stone.")
        print("2.kg to lbs.")
        print("\n3.stone to kg.")
        print("4.stone to lbs.")
        print("\n5.lbs to kg.")
        print("6.lbs to stone.")
        type_input = input("Please select the number corresponding to the type of conversion: ")
        if type_input.isdigit() == 1:
            type_input = (int)(type_input)
            if type_input >= 1 and type_input <= 6:
                match type_input:
                    case 1:
                        value = input("What is the source value?")
                        if value.isdigit() == 1:
                            value = (float)(value)
                            return value / 6.35
                    case 2:
                        value = input("What is the source value?")
                        if value.isdigit() == 1:
                            value = (float)(value)
                            return value * 2.205
                    case 3:
                        value = input("What is the source value?")
                        if value.isdigit() == 1:
                            value = (float)(value)
                            return value*6.35
                    case 4:
                        value = input("What is the source value?")
                        if value.isdigit() == 1:
                            value = (float)(value)
                            return value * 14
                    case 5:
                        value = input("What is the source value?")
                        if value.isdigit() == 1:
                            value = (float)(value)
                            return value/2.205
                    case 6:
                        value = input("What is the source value?")
                        if value.isdigit() == 1:
                            value = (float)(value)
                            return value / 14
        if type_check == 1:
            print("Wrong Input")
if __name__ == "__main__":
    type_check = 1
    while type_check == 1:
        print("1. Temp")
        print("2. Speed")
        print("3. Weigh")
        type_input = input("Please select the number corresponding to the type of conversion: ")
        if type_input.isdigit() == 1:
            type_input = (int)(type_input)
            if type_input >= 1 and type_input <= 3:
                match type_input:
                    case 1:
                        print(conversion_temp())
                        type_check = 0
                    case 2:
                        print(conversion_speed())
                        type_check = 0
                    case 3:
                        print(conversion_weight())
                        type_check = 0
        if type_check == 1:
            print("Wrong Input")