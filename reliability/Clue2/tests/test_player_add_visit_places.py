import pytest

from player import Player


def check_if_places_in_list(player, places):
    for place in player.visited_places:
        if place not in places:
            return False
    return True


def test_add_visit_places():
    places = [
        "Place 1",
        "Place 2",
        "Place 3",
        "Place 4",
        "Place 5",
    ]
    player = Player("Test Player")
    player.add_visit_places(places)
    assert check_if_places_in_list(player, places)


def test_add_visit_places_with_empty_list():
    player = Player("Test Player")
    places = []
    player.add_visit_places(places)
    assert len(player.visited_places) == 0


def test_add_visit_places_with_none():
    player = Player("Test Player")
    player.add_visit_places([])


def test_add_visit_places_with_wrong_input():
    player = Player("Test Player")
    places = {}
    with pytest.raises(TypeError):
        player.add_visit_places(places)


def test_add_visit_places__one_place():
    player = Player("Test Player")
    places = ["Place 1"]
    player.add_visit_places(places)
    assert player.visited_places == places
