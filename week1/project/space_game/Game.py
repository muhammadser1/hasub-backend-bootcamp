import json
from Event import *
from Planet import *
import random
from weather import load_weather_data
from Player import *
import time


class Game:
    def __init__(self):

        self.list_planets = []
        self.list_ships = []
        self.user_ship=None
        self.planet_names = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto",
                             "Kepler-22b"]
        self.random_event = [Black_Hole("Black_Hole"), Asteroid_Field("Asteroid_Field", 50),
                             Alien_Diplomacy("Alien_Diplomacy", 30), Pirates("Pirates", 10, 12)]
    def init_game(self):
        for i in range(10):
            self.init_planet(i)
        self.init_ships()
    def init_planet(self,i):
        planet_name = random.choice(self.planet_names)
        self.planet_names.remove(planet_name)
        coins = random.randint(1, 10)
        random_number = random.uniform(0, 1)
        bonus_fuel = random.randint(5, 20)
        event_random = None
        if random_number > 0.7:
            event_random = random.choice(self.random_event)
        loaded_weather_data = load_weather_data("weather_data.json")
        weather = loaded_weather_data["dataseries"][coins]
        if i==0:
            self.list_planets.append(Planet("earth", 0, 0, None, None))
        else:
            self.list_planets.append(Planet(planet_name, bonus_fuel, coins, event_random, weather))
    def init_ships(self):
        ships = load_ship_data("ships.json")
        for ship_ in ships:
            ship = Ship(ship_["name"], ship_["place"], ship_["health"], ship_["fuel"])
            self.list_ships.append(ship)
    def print_rest(self,i):
        while i<=9:
            print(self.list_planets[i])
            i+=1
    def print_ships(self):
        for i in range(len(self.list_ships)):
            print(i,". ",self.list_ships[i])
    def choose_ship(self,i):
        self.user_ship=self.list_ships[i]
        print(self.user_ship)
    def update_status(self):
        self.user_ship.place_id+=1
        self.user_ship.place=self.list_planets[self.user_ship.place_id+1].name
        self.user_ship.coin+=self.list_planets[self.user_ship.place_id+1].coins
        self.user_ship.fuel += self.list_planets[self.user_ship.place_id + 1].bonus_fuel
        if self.list_planets[self.user_ship.place_id+1].event is not None:
            self.user_ship.coin -= self.list_planets[self.user_ship.place_id+1].event.coin
            self.user_ship.health -= self.list_planets[self.user_ship.place_id + 1].event.dmg
def load_ship_data(filename):
    with open(filename, "r") as json_file:
        return json.load(json_file)
