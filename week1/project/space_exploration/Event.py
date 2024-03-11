class Event:
    def __init__(self, name, significant_damage, description, minor_damage):
        self.name = name
        self.significant_damage = significant_damage
        self.description = description
        self.minor_damage = minor_damage

    def __str__(self):
        return f"Event: {self.name}\nSignificant Damage: {self.significant_damage}\nMinor Damage: {self.minor_damage}\n"

    def resolve(self):
        pass

    def check_input(range1, range2):
        # range1 =< get input number <= range2
        flag = 1
        while flag == 1:
            get_input = input("Your Choice: ")
            if get_input.isdigit() == 1:
                get_input = (int)(get_input)
                if get_input >= range1 and get_input <= range2:
                    flag = 0
            if flag == 1:
                print("Invalid  input.\n")
        return get_input