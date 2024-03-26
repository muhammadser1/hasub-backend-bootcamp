import json
import random

from load_balancer import LoadBalancer
from request_stream import RequestGenerator
from server import Server


def save_tickets(file_path, tickets_list):
    with open(file_path, 'w') as f:
        json.dump(tickets_list, f)


if __name__ == "__main__":
    import json
    import random


    def save_tickets(file_path, tickets_list):
        with open(file_path, 'w') as f:
            json.dump(tickets_list, f)


if __name__ == "__main__":
    import random

    # event_list = {"Concert": 0, "Sports Game": 0, "Theater Show": 0, "Movie Premiere": 0}
    # quantity = 500
    #
    # for _ in range(quantity):
    #     event_name = random.choice(list(event_list.keys()))
    #     tickets = random.randint(1, 10)
    #     event_list[event_name] += tickets
    #
    # save_tickets("tickets.json", event_list)
    # print("JSON file initialized in main.py")
    # {"Concert": 610, "Sports Game": 700, "Theater Show": 785, "Movie Premiere": 695}
    server1 = Server("tickets.json", max_requests_per_time=10, requests_threshold_delay=3, max_concurrent_requests=5)
    server2 = Server("tickets.json", max_requests_per_time=10, requests_threshold_delay=3, max_concurrent_requests=5)
    server3 = Server("tickets.json", max_requests_per_time=10, requests_threshold_delay=3, max_concurrent_requests=5)
    servers = [server1]

    request_generator = RequestGenerator()
    load_balancer = LoadBalancer(request_generator, servers)

    load_balancer.process_events()
