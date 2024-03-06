import random
from Event import Event


class Black_Hole(Event):
    def __init__(self, name, significant_damage, description, minor_damage):
        super().__init__(name, significant_damage, description, minor_damage)

    def resolve(self):  # return dmg,fuel(0)
        print("1. Passage Through")
        print("2. Navigate Around")
        player_choice = int(input("Enter your choice: "))
        if player_choice == 1:  # Passage Through
            random_number = random.randint(1, 10)
            if random_number > 4:
                return self.significant_damage
            else:
                return self.minor_damage
        elif player_choice == 2:  # Navigate Around
            return self.minor_damage
