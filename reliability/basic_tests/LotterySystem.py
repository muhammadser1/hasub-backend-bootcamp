import random


def pick_winner_single(participants=""):
    """Pick a single winner randomly from a list of names."""
    try:
        return random.choice(participants)
    except IndexError:
        raise IndexError("Error: No participants provided")
    except TypeError:
        raise TypeError("Invalid argument type")


def pick_winners_list(participants="", n=0):
    """
    Pick N winners randomly from a list of names.
    Returns a list with the selected names in their selection order.
    """
    try:
        if n <= 0:
            raise ValueError("Number of winners exceeds the number of participants or negative n")
        return random.sample(participants, n)
    except IndexError:
        raise IndexError("Error: No participants provided")
    except TypeError:
        raise TypeError("Invalid argument type")
    except ValueError:
        raise ValueError("Number of winners exceeds the number of participants or negative n")
