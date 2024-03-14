class Truck:
    def __init__(self, max_fuel_amount, km_per_liter, repair_price_per_km, brand):
        self.max_fuel_amount = max_fuel_amount
        self.km_per_liter = km_per_liter
        self.repair_price_per_km = repair_price_per_km
        self.brand = brand
        self.mental_health = 100
        self.total_expenses = 0
        self.current_fuel = max_fuel_amount

    def can_travel(self, distance):
        return distance <= self.current_fuel * self.km_per_liter

    def travel(self, distance, road):
        if self.can_travel(distance):
            fuel_consumed = distance / self.km_per_liter
            self.consume_fuel(distance)
            self.mental_health += road.mental_effect  # Adjust mental health based on road type
            self.total_expenses += fuel_consumed * self.repair_price_per_km  # Increment total expenses for fuel
            self.total_expenses += distance * road.wheel_damage_effect  # Increment total expenses for wheel wear
            return True
        else:
            return False

    def consume_fuel(self, distance):
        self.current_fuel -= distance / self.km_per_liter

    def get_status(self):
        return {
            "fuel_level": self.current_fuel,
            "mental_health": self.mental_health,
            "total_expenses": self.total_expenses
        }
