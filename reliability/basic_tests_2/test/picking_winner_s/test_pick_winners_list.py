import pytest

from LotterySystem import pick_multiple_winners


def contains_sublist(lst, sublist):
    for item in sublist:
        if item not in lst:
            return False
    return True


@pytest.fixture
def participants():
    return ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"]


def test_pick_winners_no_input(participants):
    with pytest.raises(TypeError):
        assert pick_multiple_winners()


def test_pick_winners_no_input2(participants):
    with pytest.raises(TypeError):
        assert pick_multiple_winners(participants)


def test_pick_winners_no_input3(participants):
    with pytest.raises(TypeError):
        assert pick_multiple_winners(2)


def test_pick_winner_participants_not_list():
    participants = None
    with pytest.raises(TypeError):
        pick_multiple_winners(participants, 10)


def test_pick_winners(participants):
    winners = pick_multiple_winners(participants, 2)
    assert contains_sublist(participants, winners)


def test_pick_winners_non_string_elements():
    participants = ["Alice", 123, "Bob", "", "David", 456, "Eve", "Frank"]
    winner = pick_multiple_winners(participants, 2)
    assert winner


def test_pick_winners_list():
    participants = ["bob"]
    winner = pick_multiple_winners(participants, 1)
    assert winner[0] in participants


def test_pick_winners_participants_not_list3():
    participants = {"aaa"}
    with pytest.raises(TypeError):
        pick_multiple_winners(participants, 1)


def test_pick_winners_participants_not_list1():
    participants = ""
    with pytest.raises(TypeError):
        pick_multiple_winners(participants)


def test_pick_winners_participants_not_list2():
    participants = "aaaaaaa"
    with pytest.raises(TypeError):
        pick_multiple_winners(participants)


###################################################################

def test_pick_winners_all(participants):
    winners = pick_multiple_winners(participants, len(participants))
    assert contains_sublist(participants, winners)


def test_pick_winners_len_smaller_n(participants):
    with pytest.raises(ValueError):
        assert pick_multiple_winners(participants, 10)


def test_pick_winners_n_neg(participants):
    with pytest.raises(ValueError):
        assert pick_multiple_winners(participants, -1)


def test_pick_winners_n_zero(participants):
    with pytest.raises(ValueError):
        assert pick_multiple_winners(participants, 0)
