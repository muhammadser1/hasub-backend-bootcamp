class Planet:
    def __init__(self, name, bonus_fuel, coins,event,weather):
        self.name = name
        self.bonus_fuel = bonus_fuel
        self.coins = coins
        self.event = event
        self.weather=weather
    def __str__(self):
        return f"Planet: {self.name}, coins: {self.coins}, bonus_fuel: {self.bonus_fuel}"