import random
from Event import Event


class Pirates(Event):
    def __init__(self, name, significant_damage, description, minor_damage, coins):
        super().__init__(name, significant_damage, description, minor_damage)
        self.coins=coins

    def resolve(self):  # return dmg,coins
        print("1. Negotiate")
        print("2. flee")
        print("3. fight")
        player_choice = int(input("Enter your choice: "))
        if player_choice == 3:  # Fire at the asteroids
            return self.significant_damage, 0
        if player_choice == 2:  # Evade the asteroids
            return self.minor_damage, 0
        if player_choice == 1:  # Evade the asteroids
            return 0, self.coins
