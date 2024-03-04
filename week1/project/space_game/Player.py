class Ship:
    def __init__(self, name,place, health, fuel):
        self.name = name
        self.health = health
        self.fuel = fuel
        self.place=place
        self.coin=0
        self.place_id=0
    def __str__(self):
        return f"Ship: {self.name}, health: {self.health}, fuel: {self.fuel}, place: {self.place}, coin: {self.coin}  "