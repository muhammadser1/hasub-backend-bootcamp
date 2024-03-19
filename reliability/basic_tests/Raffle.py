class Raffle:
    def __init__(self, max_people, max_tickets, price_per_ticket):
        self.max_people = max_people
        self.max_tickets = max_tickets
        self.price_per_ticket = price_per_ticket
        self.total_earnings = 0
        self.participants = {}

