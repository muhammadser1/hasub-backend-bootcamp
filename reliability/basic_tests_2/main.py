from LotterySystem import pick_winner_single, pick_multiple_winners
from Raffle import Raffle


def pick_single_winner(participants):
    try:
        winner = pick_winner_single(participants)
        print("Winner:", winner)
    except IndexError as e:
        print("Error:", e)
    except TypeError as e:
        print("Error:", e)


def pick_list_winners(participants, num):
    try:
        winners = pick_multiple_winners(participants, num)
        print("Winners:", winners)
    except ValueError as e:
        print("Error:", e)
    except IndexError as e:
        print("Error:", e)
    except TypeError as e:
        print("Error:", e)


if __name__ == '__main__':
    participants = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"]
    pick_single_winner(participants)
    pick_list_winners(participants, 3)

    raffle = Raffle(max_people=5, max_tickets=20, price_per_ticket=10)

    participants = ["Alice", "Bob", "Charlie", "David", "Eve"]
    for participant in participants:
        raffle.add_person(participant)

    try:
        raffle.buy_ticket("Alice", 3)
        raffle.buy_ticket("Bob", 2)
        raffle.buy_ticket("Charlie", 1)
        raffle.buy_ticket("David", 1)
        raffle.buy_ticket("Eve", 4)
    except ValueError as e:
        print(f"An error occurred while buying tickets: {e}")

    try:
        winner = raffle.select_winner()
    except ValueError as e:
        print(f"An error occurred while buying tickets: {e}")

    print("Winner of the raffle:", winner)
