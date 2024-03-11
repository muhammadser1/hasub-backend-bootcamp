import random
from Event import Event


class Asteroid_Field(Event):
    def __init__(self, name, significant_damage, description, minor_damage, fuel):
        super().__init__(name, significant_damage, description, minor_damage)
        self.feul = fuel

    def resolve(self):  # return dmg,fuel
        print("1. Fire at the asteroids")
        print("2. Evade the asteroids")
        player_choice = int(input("Enter your choice: "))
        if player_choice == 1:  # Fire at the asteroids
            return self.minor_damage, self.feul
        if player_choice == 2:  # Evade the asteroids
            return self.significant_damage, self.feul / 3
