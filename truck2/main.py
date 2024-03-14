from handler.JSONHandler import load_data_from_json
from simulation_engine.Simulation import Simulation
from utils.road_utils import load_roads
from utils.select_truck import select_truck
from utils.truck_utils import load_trucks

road_data = load_data_from_json("data_files/roads.json")
truck_data = load_data_from_json("data_files/trucks.json")

roads = load_roads(road_data["roads"])
trucks = load_trucks(truck_data["trucks"])

truck = select_truck(trucks)

simulation = Simulation(roads, truck)
simulation.start()