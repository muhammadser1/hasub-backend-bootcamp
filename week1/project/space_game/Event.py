class Black_Hole:
    def __init__(self, name):
        self.name = name
        self.dmg=1000
        self.des= "A black hole appears nearby!"
    def __str__(self):
        return f"Event: {self.name}, dmg: {self.dmg},  {self.des}"
class Asteroid_Field:
    def __init__(self, name,dmg):
        self.name = name
        self.dmg=dmg
        self.des= "You encounter a dangerous asteroid field!"

class Alien_Diplomacy:
    def __init__(self, name,coin):
        self.name = name
        self.coin=coin
        self.des= "You encounter a peaceful alien civilization."
        self.dmg=0
class Pirates:
    def __init__(self, name, dmg,coin):
        self.name = name
        self.dmg = dmg
        self.coin = coin
        self.des= "Space pirates attack your ship!"
