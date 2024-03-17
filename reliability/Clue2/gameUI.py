class GameUi:
    def __init__(self):
        pass

    def display_menu(self):
        """
        Display the game menu.

        This method prints the available options for the player to choose from.
        """
        print("1. View List of Players")
        print("2. Raise Suspicion")

    def view_players(self,players):
        """
        View the list of live players.

        This method prints the names of all live players in the game.
        """
        print("List of Live Players:")
        for player in players:
            print(player.name)
