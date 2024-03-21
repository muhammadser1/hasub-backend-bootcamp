import logging
import random

from utils.get_integer_input import get_integer_input
from player import Player

logging.basicConfig(filename='game.log', level=logging.INFO, format='%(asctime)s - %(message)s')


class Game():
    def __init__(self, places, weapons, num_players, game_ui):
        """
        Initialize the Game instance.

        Parameters:
            places (list): List of place names.
            weapons (list): List of weapon names.
            num_players (int): Number of players in the game.
        """
        self.places = places
        self.weapons = weapons
        self.num_players = num_players
        self.players = None
        self.murder = None
        self.game_ui = game_ui

    def create_players(self):
        """Create player instances and assign them random places and favorite weapons."""
        self.players = [Player(f"Player {i + 1}") for i in range(self.num_players)]
        for player in self.players:
            try:
                player.add_favorite_weapon(self.weapons)
                player.add_visit_places(self.places)
            except TypeError as e:
                print("Error:", e)

        self.murder = random.choice(self.players)
        self.murder.status = "assassin"

    def generate_murder(self):
        """
        Generate details of the murder for the current round.

        Randomly selects a murder place and a non-assassin player as the victim.
        """
        murder_place = random.choice(self.murder.visited_places)
        murder_weapon = random.choice(self.murder.favorite_weapons)
        non_assassins = self.non_assassin_players()
        died_player = random.choice(non_assassins)
        self.players.remove(died_player)
        logging.info(
            f"Murder details - Place: {murder_place}, Weapon: {murder_weapon}, Died Player: {died_player.name}")
        return murder_place

    def non_assassin_players(self):
        """
        Get a list of non-assassin players.

        Returns:
            list: List of Player objects with status 'innocent'.
        """
        non_assassins = []
        for player in self.players:
            if player.status == "innocent":
                non_assassins.append(player)
        return non_assassins

    def validate_player(self, player_name: str):
        """
        Validate the existence of a player by name.

        Parameters:
            player_name (str): The name of the player to validate.

        Returns:
            Player or None: The player object if found, None otherwise.
        """
        for player in self.players:
            if player.name == player_name:
                return player
        print("Player not found. Please enter a valid player name.")
        return None

    def accuse(self):
        while True:
            accused_player_name = input("Enter the name of the player you want to accuse: ")
            accused_player = self.validate_player(accused_player_name)
            if accused_player is not None:
                if accused_player.status == "assassin":
                    print(f"Congratulations! You have correctly accused {accused_player.name}. You win!")
                    return "you win"
                else:
                    print(f"Sorry, {accused_player.name} is not the murderer.")
                    return

    def suspect(self):
        """
        Allow the player to suspect another player.

        This method prompts the user to enter the name of the player they want to suspect. It then validates
        the player's existence and randomly selects visited places and favorite weapons of the suspected player
        to display as part of the suspicion.

        The method allows the player to suspect up to two players in one game round.

        If an error occurs while selecting visited places or favorite weapons (e.g., empty lists), an error message
        is printed, and the method continues execution.

        Returns:
            None
        """
        count = 0
        while True and (count < 2):
            sus_player = input("Enter the name of the player you want to suspect: ")
            sus_player = self.validate_player(sus_player)

            if sus_player is not None:
                try:
                    visited_places = random.sample(sus_player.visited_places, min(2, len(sus_player.visited_places)))
                    favorite_weapon = random.sample(sus_player.favorite_weapons,
                                                    min(1, len(sus_player.favorite_weapons)))
                    print(sus_player.name, visited_places, favorite_weapon)
                    count += 1
                except ValueError:
                    print("Error occurred while selecting visited places or favorite weapon.")

    def start(self):
        self.create_players()
        menu_choice = 0
        while self.num_players > 2:
            try:
                if menu_choice != 1:
                    self.generate_murder()
                self.game_ui.display_menu()
                menu_choice = get_integer_input("Enter your choice: ", 1, 2)
                if menu_choice == 1:
                    self.game_ui.view_players(self.players)
                elif menu_choice == 2:
                    self.suspect()
                    flag = self.accuse()
                    if flag == "you win":
                        break
            except ValueError:
                print("Invalid choice. Please enter 1 or 2.")
