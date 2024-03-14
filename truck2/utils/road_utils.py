from simulation_engine.Road import Road


def load_roads(roads):
    """
    Load road data and initialize Road objects.

    Args:
        roads (list): List of dictionaries containing road data.

    Returns:
        list: List of Road objects.
    """
    tmp = []
    for road in roads:
        tmp.append(
            Road(road["road_type"]["name"], road["road_type"]["fuel_consumption"], road["road_type"]["mental_health"],
                 road["road_type"]["wheel_wear"], road["length"]))
    return tmp


