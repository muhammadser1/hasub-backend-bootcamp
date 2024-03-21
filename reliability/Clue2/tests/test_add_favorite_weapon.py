import pytest
from player import Player


def check_if_weapons_in_list(player, weapons):
    for weapon in player.favorite_weapons:
        if weapon not in weapons:
            return False
    return True


def test_add_favorite_weapon():
    weapons = [
        "Weapon 1",
        "Weapon 2",
        "Weapon 3",
        "Weapon 4",
        "Weapon 5",
    ]
    player = Player("Test Player")
    player.add_favorite_weapon(weapons)
    assert check_if_weapons_in_list(player, weapons)


def test_add_favorite_weapon_with_empty_list():
    player = Player("Test Player")
    weapons = []
    player.add_favorite_weapon(weapons)
    assert len(player.favorite_weapons) == 0


def test_add_favorite_weapon_with_none():
    player = Player("Test Player")
    player.add_favorite_weapon([])
    assert len(player.favorite_weapons) == 0


def test_add_favorite_weapon_with_wrong_input():
    player = Player("Test Player")
    weapons = {}
    with pytest.raises(TypeError):
        player.add_favorite_weapon(weapons)


def test_add_favorite_weapon_one_weapon():
    player = Player("Test Player")
    weapons = ["Weapon 1"]
    player.add_favorite_weapon(weapons)
    assert player.favorite_weapons == weapons
