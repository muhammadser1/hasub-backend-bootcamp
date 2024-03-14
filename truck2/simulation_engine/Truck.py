import logging

# Configure logging
logging.basicConfig(filename='truck.log', level=logging.INFO)

class Truck:
    def __init__(self, max_fuel_amount, km_per_liter, repair_price_per_km, brand):
        self.max_fuel_amount = max_fuel_amount
        self.km_per_liter = km_per_liter
        self.repair_price_per_km = repair_price_per_km
        self.brand = brand
        self.mental_health = 100
        self.total_expenses = 0
        self.current_fuel = max_fuel_amount

    def __str__(self):
        return f"brand={self.brand}, max_fuel_amount={self.max_fuel_amount}, km_per_liter={self.km_per_liter}, repair_price_per_km={self.repair_price_per_km})"

    def can_travel(self, distance):
        """
        Checks if the truck can travel a specified distance.

        Args:
            distance (float): The distance to check if the truck can travel.

        Returns:
            bool: True if the truck can travel the distance, False otherwise.
        """
        can_travel = distance <= self.current_fuel * self.km_per_liter and self.mental_health > 0
        logging.info("Truck can%s travel %s km", "" if can_travel else "not", distance)
        return can_travel

    def travel(self, distance, road):
        """
        Simulates the truck traveling a specified distance along a road.

        Args:
            distance (float): The distance the truck will travel.
            road (Road): The road along which the truck will travel.

        Returns:
            bool: True if the truck successfully travels the distance, False otherwise.
        """
        if self.can_travel(distance):
            self.current_fuel -= distance / self.km_per_liter
            self.mental_health += road.mental_effect  # Adjust mental health based on road type
            self.total_expenses += distance * road.wheel_damage_effect  # Increment total expenses for wheel wear
            logging.info("Truck traveled %s km along %s road", distance, road.name)
            return True
        else:
            logging.warning("Truck unable to travel %s km due to insufficient fuel or mental health", distance)
            return False

    def get_status(self):
        """
        Returns a dictionary containing the truck's current status.

        Returns:
            dict: A dictionary containing the truck's current fuel level, mental health, and total expenses.
        """
        status = {
            "fuel_level": self.current_fuel,
            "mental_health": self.mental_health,
            "total_expenses": self.total_expenses
        }
        logging.info("Truck status: %s", status)
        return status
