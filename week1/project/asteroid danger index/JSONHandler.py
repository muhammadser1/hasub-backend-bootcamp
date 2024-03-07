import json
from datetime import datetime, timedelta


class JSONHandler:
    @staticmethod
    def write_data_to_json(data, filename, date):
        processed_data = []

        for i in range(7):
            date_string = date
            date_object = datetime.strptime(date_string, "%Y-%m-%d")
            new_date = date_object + timedelta(days=i)
            new_date_string = new_date.strftime("%Y-%m-%d")
            for planet in data["near_earth_objects"][new_date_string]:
                tmp = {}
                tmp["date"] = new_date_string
                tmp["id"] = planet["id"]
                tmp["name"] = planet["name"]
                tmp["est diameter min"] = planet["estimated_diameter"]["kilometers"]["estimated_diameter_min"]
                tmp["est diameter max"] = planet["estimated_diameter"]["kilometers"]["estimated_diameter_max"]
                tmp["miss_distance"] = planet["close_approach_data"][0]["miss_distance"]["kilometers"]
                tmp["relative_velocity"] = planet["close_approach_data"][0]["relative_velocity"]["kilometers_per_hour"]
                processed_data.append(tmp)
        with open(filename, 'w') as json_file:
            json.dump(processed_data, json_file, indent=4)

    @staticmethod
    def read_data_from_json(filename):
        # Read data from JSON file
        with open(filename, 'r') as json_file:
            data = json.load(json_file)
        return data
