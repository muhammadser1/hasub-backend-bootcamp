import random


def pick_winner_single(participants):
    """Pick a single winner randomly from a list of names."""
    try:
        if not isinstance(participants, list):
            raise TypeError("Invalid argument type")
        return random.choice(participants)
    except IndexError:
        raise IndexError("Error: No participants provided")
    except TypeError:
        raise TypeError("Invalid argument type")


def pick_multiple_winners(participants, num):
    """
    Pick N winners randomly from a list of names.
    Returns a list with the selected names in their selection order.
    """
    try:
        if not isinstance(participants, list):
            raise TypeError("Invalid argument type")

        if not isinstance(num, int) or num <= 0:
            raise ValueError("Number of winners must be a non-negative integer")

        return random.sample(participants, num)
    except TypeError:
        raise TypeError("Invalid argument type")

