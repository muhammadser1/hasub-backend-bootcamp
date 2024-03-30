import json
import threading
import time
import logging

### good usage of loggin. important for maintainability and relaibility
### but if you want to add loggin - use it! on every function, on every major operations
logging.basicConfig(filename="log_file", level=logging.INFO, format='%(asctime)s  - %(message)s')


def find_server_index(servers, server_):
    ### is there a faster way to do this?
    for index, server in enumerate(servers):
        if server == server_:
            return index
    return -1


class LoadBalancer:
    def __init__(self, event_generator, servers):
        ### logicaly, the load balancer dosent needs the event generator, they just need to cummunicate. we will learn how
        self.event_generator = event_generator
        self.servers = servers
        self.current_server_index = 0
        self.counters = [0 for _ in servers]
        # self.existing_data = {f"Server {i}": [] for i in range(1, len(servers) + 1)}
        self.report_thread = threading.Thread(target=self.print_report_thread)

    def process_events(self):
        self.report_thread.start()
        for event in self.event_generator.generate_events():
            self.handle_event(event)

    def handle_event(self, event):
        # Here you can implement any logic to process the event

        least_server_index = min(enumerate(self.counters), key=lambda x: x[1])[0]
        server = self.servers[least_server_index]
        self.counters[least_server_index] += event["tickets"]
        for _ in range(event["tickets"]):
            server.sell_ticket(event['event'])
            server.process_request(event)
        # self.existing_data[f"Server {least_server_index + 1}"].append(event["timestamp"])
        print("Received event:", event)

    def generate_report(self):
        report = "Load Balancer Report:\n"
        report += "Total Requests Received: {}\n".format(sum(self.counters))
        report += "Request Distribution:\n"
        for i, counter in enumerate(self.counters):
            report += f"- Server {i+1}: {counter}\n"
        return report

    def print_report_thread(self):
        while True:
            report = self.generate_report()
            logging.info(report)
            ### remove before submitting
            # print("aaaaaaaaaaaaaaaaaaaaaaaaa")
            time.sleep(5)
