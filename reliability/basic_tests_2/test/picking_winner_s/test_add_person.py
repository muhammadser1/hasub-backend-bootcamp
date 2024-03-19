import pytest

from Raffle import Raffle


@pytest.fixture
def raffle():
    return Raffle(10, 100, 10)


def test_add_no_input(raffle):
    with pytest.raises(TypeError):
        raffle.add_person()


def test_add_not_String_input(raffle):
    with pytest.raises(TypeError):
        raffle.add_person(5)


def test_add_duplicated_name(raffle):
    raffle.add_person("john")
    raffle.add_person("john")
    assert len(raffle.participants) == 1


def test_add(raffle):
    raffle.add_person("john1")
    raffle.add_person("john2")
    raffle.add_person("john3")
    assert len(raffle.participants) == 3


def test_add_equ_max():
    raffle = Raffle(2, 100, 100)
    raffle.add_person("john1")
    raffle.add_person("john2")
    assert len(raffle.participants) == 2


def test_add_more_max():
    raffle = Raffle(2, 100, 100)
    with pytest.raises(ValueError):
        raffle.add_person("john1")
        raffle.add_person("john2")
        raffle.add_person("john3")
