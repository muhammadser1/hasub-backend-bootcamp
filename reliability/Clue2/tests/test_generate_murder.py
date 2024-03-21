from Clue_game import Game
from player import Player


def test_generate_murder_place():
    places = ["Room A", "Room B", "Room C"]
    weapons = ["Knife", "Gun", "Poison"]

    game = Game(places, weapons, 3, None)
    game.create_players()

    murder_place = game.generate_murder()
    for i in range(3):
        if game.players[i].status == "assassin":
            break
    assert murder_place in game.players[i].visited_places
