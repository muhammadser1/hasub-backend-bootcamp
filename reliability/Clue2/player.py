import random


class Player:
    def __init__(self, name, ):
        self.name = name
        self.visited_places = []
        self.favorite_weapons = []
        self.status = "innocent"

    def __str__(self):
        visited_places_str = ", ".join(self.visited_places)
        favorite_weapons_str = ", ".join(self.favorite_weapons)
        return f"Player: {self.name}\nVisited Places: {visited_places_str}\nFavorite Weapons: {favorite_weapons_str}"

    def add_visit_places(self, places):
        try:
            num_visited_places = random.randint(1, 3)
            self.visited_places = random.sample(places, min(num_visited_places, len(places)))
        except ValueError:
            print("Error: Unable to add visited places. Check if 'places' list is empty ")

    def add_favorite_weapon(self, weapons):
        try:
            num_favorite_weapons = random.randint(1, 3)
            self.favorite_weapons = random.sample(weapons, min(num_favorite_weapons, len(weapons)))
        except ValueError:
            print(
                "Error: Unable to add favorite weapons. Check if 'weapons' list is empty")
