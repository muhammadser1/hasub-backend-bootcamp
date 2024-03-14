from handler.JSONHandler import load_data_from_json
from simulation_engine.Simulation import Simulation
from utils.road_utils import load_roads

road_data = load_data_from_json("data_files/roads.json")
roads = load_roads(road_data["roads"])
simulation = Simulation(roads)
simulation.start()
