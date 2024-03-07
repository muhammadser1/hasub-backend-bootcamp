import json

class JSONHandler:
    @staticmethod
    def write_data_to_json(data, filename):
        processed_data=[]
        for planet in data["near_earth_objects"]["2015-09-07"]:
            tmp={}
            tmp["id"]=planet["id"]
            tmp["name"] = planet["name"]
            tmp["est diameter min"]=planet["estimated_diameter"]["kilometers"]["estimated_diameter_min"]
            tmp["est diameter max"] = planet["estimated_diameter"]["kilometers"]["estimated_diameter_max"]
            tmp["miss_distance"]=planet["close_approach_data"][0] ["miss_distance"]["kilometers"]
            tmp["relative_velocity"]=planet["close_approach_data"][0] ["relative_velocity"]["kilometers_per_hour"]
            processed_data.append(tmp)

        with open(filename, 'w') as json_file:
            json.dump(processed_data, json_file, indent=4)

    @staticmethod
    def read_data_from_json(filename):
        # Read data from JSON file
        with open(filename, 'r') as json_file:
            data = json.load(json_file)
        return data
