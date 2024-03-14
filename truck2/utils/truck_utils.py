from simulation_engine.Truck import Truck


def load_trucks(trucks):
    """
    Load truck data and initialize Truck objects.

    Args:
        trucks (list): List of dictionaries containing truck data.

    Returns:
        list: List of Truck objects.
    """
    tmp = []
    for truck in trucks:
        tmp.append(Truck(truck["max_fuel_amount"],truck["km_per_liter"],truck["repair_price_per_km"],truck["brand"]))
    return tmp



