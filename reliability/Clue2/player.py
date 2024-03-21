import random


class Player:
    def __init__(self, name, ):
        """
        Represents a player in the Clue game.

        Attributes:
            name (str): The name of the player.
            visited_places (list): List of visited places by the player.
            favorite_weapons (list): List of favorite weapons of the player.
            status (str): The status of the player, initially set to "innocent".
        """

        self.name = name
        self.visited_places = []
        self.favorite_weapons = []
        self.status = "innocent"

    def __str__(self):
        visited_places_str = ", ".join(self.visited_places)
        favorite_weapons_str = ", ".join(self.favorite_weapons)
        return f"Player: {self.name}\nVisited Places: {visited_places_str}\nFavorite Weapons: {favorite_weapons_str}"

    def add_visit_places(self, places):
        """
        Adds visited places to the player.

        Args:
            places (list): List of places to add as visited.

        Raises:
            ValueError: If 'places' list is empty.
            TypeError: If 'places' is not a list.
        """
        try:
            num_visited_places = random.randint(1, 3)
            self.visited_places = random.sample(places, min(num_visited_places, len(places)))
        except ValueError:
            raise ValueError("Error: Unable to add visited places. Check if 'places' list is empty")
        except TypeError:
            raise TypeError("Error: TypeError")

    def add_favorite_weapon(self, weapons):
        """
        Adds favorite weapons to the player.

        Args:
            weapons (list): List of weapons to add as favorite.

        Raises:
            ValueError: If 'weapons' list is empty.
        """
        try:
            num_favorite_weapons = random.randint(1, 3)
            self.favorite_weapons = random.sample(weapons, min(num_favorite_weapons, len(weapons)))
        except ValueError:
            raise ValueError("Error: Unable to add favorite weapons.")
        except TypeError:
            raise TypeError("Error: TypeError")
