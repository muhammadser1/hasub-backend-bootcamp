class Simulation:
    def __init__(self, roads):
        """
        Initialize a Simulation object.

        Parameters:
            roads (list): List of road objects or data.

        """
        self.roads = roads
        self.truck = None
        self.total_fuel_consumed = 0
        self.total_wheel_damage = 0
        self.total_miles_traveled = 0
        self.total_expenses = 0

    def print_trucks(self, trucks):
        """
        Print the available trucks to choose from.
        """
        print("Available trucks:")
        for idx, truck in enumerate(trucks):
            print(f"{idx + 1}. {truck}")

    def select_truck(self, trucks):
        """
        Select a truck for the simulation.

        Returns:
            Truck: The selected truck object.
        """
        self.print_trucks(trucks)
        while True:
            choice = input("Select a truck by entering its number: ")
            if choice.isdigit():
                choice = int(choice) - 1
                print(len(trucks))

                if 0 <= choice < len(trucks):
                    return trucks[choice]
            print("Invalid selection. Please enter the number corresponding to the desired truck.")

    def simulate(self, trucks):
        """
        Simulate the truck's journey through the roads.
        """
        print("Starting the simulation...\n")
        self.truck = self.select_truck(trucks)

        print("\nSimulation completed.")
        print(f"Total fuel consumed: {self.total_fuel_consumed}")
        print(f"Total wheel damage: {self.total_wheel_damage}")
        print(f"Total miles traveled: {self.total_miles_traveled}")
        print(f"Total total expenses: {self.total_expenses}")
