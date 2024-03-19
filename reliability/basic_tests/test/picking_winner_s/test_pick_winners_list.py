import pytest

from LotterySystem import pick_winners_list


def contains_sublist(lst, sublist):
    for item in sublist:
        if item not in lst:
            return False
    return True


@pytest.fixture
def participants():
    return ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"]


def test_pick_winners(participants):
    winners = pick_winners_list(participants, 2)
    assert contains_sublist(participants, winners)


def test_pick_winners_all(participants):
    winners = pick_winners_list(participants, len(participants))
    assert contains_sublist(participants, winners)


def test_pick_winners_single(participants):
    winners = pick_winners_list(participants, 1)
    assert contains_sublist(participants, winners)


def test_pick_winners_empty():
    participants = []
    with pytest.raises(ValueError):
        assert pick_winners_list(participants, 2)


def test_pick_winners_len_smaller_n(participants):
    with pytest.raises(ValueError):
        assert pick_winners_list(participants, 10)


def test_pick_winners_n_neg(participants):
    with pytest.raises(ValueError):
        assert pick_winners_list(participants, -1)


def test_pick_winners_n_zero(participants):
    with pytest.raises(ValueError):
        assert pick_winners_list(participants, 0)
