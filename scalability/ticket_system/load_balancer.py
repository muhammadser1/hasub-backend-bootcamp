from server import Server

from request_stream import RequestGenerator


class LoadBalancer:
    def __init__(self, event_generator, servers):
        self.event_generator = event_generator
        self.servers = servers
        self.current_server_index = 0

    def process_events(self):
        for event in self.event_generator.generate_events():
            self.handle_event(event)

    def handle_event(self, event):
        # Here you can implement any logic to process the event
        server = self.servers[self.current_server_index]
        self.current_server_index = (self.current_server_index + 1) % len(self.servers)
        server.sell_ticket(event['event'])

# Example usage:
# if __name__ == "__main__":
#     request_generator = RequestGenerator()
#     load_balancer = LoadBalancer(request_generator)
#
#     load_balancer.process_events()
