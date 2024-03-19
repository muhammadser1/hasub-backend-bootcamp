import pytest

from LotterySystem import pick_winner_single


@pytest.fixture
def participants():
    return ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"]


def test_pick_winner(participants):
    winner = pick_winner_single(participants)
    assert winner in participants


def test_pick_winner_empty():
    participants=[]
    with pytest.raises(IndexError):
        assert pick_winner_single(participants)


def test_pick_winner_single():
    participants = ["bob"]
    winner = pick_winner_single(participants)
    assert winner == "bob"


def test_pick_winner_duplicate(participants):
    participants = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Bob", "Bob"]
    winner = pick_winner_single(participants)
    assert winner in participants


def test_pick_winner_non_string_elements():
    participants = ["Alice", 123, "Bob", "", "David", 456, "Eve", "Frank"]
    winner = pick_winner_single(participants)
    assert winner in participants

def test_pick_winner_participants_not_list():
    participants = "sadasd"  # Invalid input: not a list
    with pytest.raises(TypeError):
        pick_winner_single(participants)


def test_pick_winner_participants_not_list():
    participants = None
    with pytest.raises(TypeError):
        pick_winner_single(participants)