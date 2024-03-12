class Truck:
    def __init__(self, max_fuel_amount, km_per_liter, repair_price_per_km, brand):
        self.max_fuel_amount = max_fuel_amount
        self.km_per_liter = km_per_liter
        self.repair_price_per_km = repair_price_per_km
        self.brand = brand
        self.mental_health = 100
        self.total_expenses = 0


def print_trucks(trucks):
    for truck in trucks:
        print(truck)


def select_truck(trucks):
    print("Available trucks:")
    print(trucks)
    # for i, truck in enumerate(trucks, start=1):
    #     print(f"{i}. {truck[i].brand}")
    #
    # while True:
    #     try:
    #         choice = int(input("Enter the number corresponding to the truck you want to select: "))
    #         if 1 <= choice <= len(trucks):
    #             selected_truck = trucks[choice - 1]
    #             print(f"You have selected {selected_truck.brand}.")
    #             return selected_truck
    #         else:
    #             print("Invalid choice. Please enter a number corresponding to the available trucks.")
    #     except ValueError:
    #         print("Invalid input. Please enter a number.")
