class Road:
    def __init__(self, name, fuel_consumption, mental_effect, wheel_damage_effect,length):
        self.name = name
        self.fuel_consumption = fuel_consumption
        self.mental_effect = mental_effect
        self.wheel_damage_effect = wheel_damage_effect
        self.length=length
    def __str__(self):
        return f"Road name: {self.name}, Fuel Consumption: {self.fuel_consumption}, Mental Effect: {self.mental_effect}, Wheel Damage Effect: {self.wheel_damage_effect}, Length: {self.length}"