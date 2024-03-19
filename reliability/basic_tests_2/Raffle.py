import random


class Raffle:
    def __init__(self, max_people, max_tickets, price_per_ticket):
        self.max_people = max_people
        self.max_tickets = max_tickets
        self.price_per_ticket = price_per_ticket
        self.total_earnings = 0
        self.participants = {}

    def add_person(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        try:
            if len(self.participants) >= self.max_people:
                raise ValueError("Maximum number of people reached")
            if name in self.participants:
                print(f"{name} is already in the raffle.")
            else:
                self.participants[name] = 0
                print(f"{name} has been added to the raffle.")
        except TypeError:
            raise TypeError("Invalid argument type")

    def buy_ticket(self, name, num_tickets):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not isinstance(num_tickets, int):
            raise TypeError("Number of tickets must be an integer")

        if name not in self.participants:
            raise ValueError("Person is not a participant")
        if num_tickets <= 0:
            raise ValueError("Number of tickets must be positive")
        if self.participants[name] + num_tickets > self.max_tickets:
            raise ValueError("Exceeds maximum number of tickets")

        try:
            cost = num_tickets * self.price_per_ticket
            self.total_earnings += cost
            self.participants[name] += num_tickets
        except TypeError:
            raise TypeError("Invalid argument type")

    def select_winner(self):
        if not self.participants:
            raise ValueError("No participants in the raffle")
        total_tickets = sum(self.participants.values())
        winning_ticket = random.randint(1, total_tickets)
        current_ticket = 0
        for name, tickets in self.participants.items():
            current_ticket += tickets
            if current_ticket >= winning_ticket:
                return name
