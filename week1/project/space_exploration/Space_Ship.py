class Ship:
    def __init__(self, name, health, fuel):
        self.name = name
        self.health = health
        self.fuel = fuel
        self.coin=0
    def __str__(self):
        return f"Ship: {self.name}, health: {self.health}, fuel: {self.fuel}, coin: {self.coin}  "