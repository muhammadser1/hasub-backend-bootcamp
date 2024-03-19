import pytest
from Raffle import Raffle


@pytest.fixture
def raffle():
    return Raffle(max_people=5, max_tickets=10, price_per_ticket=5)


def test_buy_ticket_valid_input(raffle):
    raffle.add_person("Alice")
    raffle.buy_ticket("Alice", 3)
    assert raffle.participants["Alice"] == 3
    assert raffle.total_earnings == 15


def test_buy_ticket_invalid_name(raffle):
    with pytest.raises(ValueError):
        raffle.buy_ticket("John", 2)


def test_buy_ticket_invalid_num_tickets(raffle):
    raffle.add_person("Bob")
    with pytest.raises(ValueError):
        raffle.buy_ticket("Bob", -1)


def test_buy_ticket_exceed_max_tickets(raffle):
    raffle.add_person("Charlie")
    with pytest.raises(ValueError):
        raffle.buy_ticket("Charlie", 15)


def test_buy_ticket_non_integer_num_tickets(raffle):
    raffle.add_person("David")
    with pytest.raises(TypeError):
        raffle.buy_ticket("David", 3.5)

def test_buy_ticket_invalid_name2(raffle):
    with pytest.raises(TypeError):
        raffle.buy_ticket(1422, 2)


def test_buy_ticket_invalid_name2(raffle):
    with pytest.raises(TypeError):
        raffle.buy_ticket({"das"}, 2)