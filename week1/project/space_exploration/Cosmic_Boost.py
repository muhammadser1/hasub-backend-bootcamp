import random
from Event import Event


class Cosmic_Boost(Event):
    def __init__(self, name, bonus_fuel,bonus_health,coins,description):
        self.name=name
        self.bonus_fuel = bonus_fuel
        self.bonus_health = bonus_health
        self.description = description
        self.coins=coins
    def resolve(self):
        return self.bonus_fuel,self.bonus_health,self.coins
