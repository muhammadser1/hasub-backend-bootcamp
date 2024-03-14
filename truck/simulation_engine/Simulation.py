from simulation_engine.Road import Road
from simulation_engine.Truck import Truck


class Simulation:
    def __init__(self, roads):
        self.roads = roads
        self.truck = Truck(max_fuel_amount=1000, km_per_liter=10, repair_price_per_km=0.05, brand="Truck Brand")

    def start(self):

        for road in self.roads:
            print(self.truck.get_status())
            bool = self.truck.travel(road.length, road)
            if bool == False:
                break
