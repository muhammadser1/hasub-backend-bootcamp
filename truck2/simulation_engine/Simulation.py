import logging

# Configure logging
logging.basicConfig(filename='data.log', level=logging.INFO)

from simulation_engine.Road import Road
from simulation_engine.Truck import Truck

class Simulation:
    def __init__(self, roads, truck):
        self.roads = roads
        self.truck = truck

    def start(self):
        """
        Begins the simulation, iterating over the roads and simulating the truck's travel along each road.

        Stops the simulation if the truck cannot travel a road due to insufficient fuel or mental health.
        """
        for road in self.roads:
            logging.info("Truck status: %s", self.truck.get_status())
            can_continue = self.truck.travel(road.length, road)
            if not can_continue:
                logging.warning("Truck unable to travel further. Stopping simulation.")
                break
