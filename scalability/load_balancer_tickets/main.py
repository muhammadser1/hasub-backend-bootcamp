import json
import random

from load_balancer import LoadBalancer
from request_stream import RequestGenerator
from server import Server


def save_tickets(file_path, tickets_list):
    with open(file_path, 'w') as f:
        json.dump(tickets_list, f)


def fill_json(file_path):
    event_list = {"Concert": 0, "Sports Game": 0, "Theater Show": 0, "Movie Premiere": 0}
    quantity = 500

    for _ in range(quantity):
        event_name = random.choice(list(event_list.keys()))
        tickets = random.randint(1, 10)
        event_list[event_name] += tickets

    save_tickets(file_path, event_list)
    print("JSON file initialized in main.py")


if __name__ == "__main__":
    file_path = "tickets.json"
    # fill_json(file_path)
    server1 = Server("tickets.json", max_requests_per_time=8, requests_threshold_delay=3, max_concurrent_requests=3)
    server2 = Server("tickets.json", max_requests_per_time=7, requests_threshold_delay=3, max_concurrent_requests=3)
    server3 = Server("tickets.json", max_requests_per_time=6, requests_threshold_delay=3, max_concurrent_requests=3)
    servers = [server1,server2,server3]

    request_generator = RequestGenerator()
    load_balancer = LoadBalancer(request_generator, servers)

    load_balancer.process_events()

