import random


class Game:
    def __init__(self,events,ship):
        self.events=events
        self.ship=ship
        self.game_over = 0
        self.data=[]
    def start(self):
        print("Starting the game!")
        while not self.game_over and self.ship.health>0 and self.ship.fuel>0:
            print(self.ship)
            self.data.append(str(self.ship))
            event=random.choice(self.events)
            print(event.description)
            if event.name=="Cosmic_Boost":
                bonus_fuel,bonus_health,coin=event.resolve()
                self.update_status(-bonus_health,-bonus_fuel,coin)

            if event.name == "Black_Hole":
                dmg=event.resolve()
                self.update_status(dmg)

            if event.name == "Pirates":
                dmg,coins=event.resolve()
                self.update_status(dmg,0,coins)

            if event.name == "Asteroid_Field":
                dmg,fuel=event.resolve()
                self.update_status(dmg, fuel, 0)

            self.data.append(event.description)
            print("0. continue the game")
            print("1. end this")
            self.game_over=int(input("Enter '0' to continue the game or '1' to end it: "))

    def update_status(self,dmg=0,fuel=0,coin=0):
        self.ship.health-=dmg
        self.ship.fuel -= fuel
        self.ship.coin += coin