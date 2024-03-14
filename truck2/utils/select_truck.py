def select_truck(trucks):
    """
    Display a list of available trucks and prompt the user to select one by its index.

    Args:
        trucks (list): A list of available trucks.

    Returns:
        Truck: The selected truck object.

    Raises:
        ValueError: If the user input is not a valid number or the selected index is out of range.
    """
    print("Available Trucks:")
    for index, truck in enumerate(trucks):
        print(f"{index + 1}. {truck}")

    while True:
        try:
            choice = int(input("Select a truck by entering its index: "))
            if 1 <= choice <= len(trucks):
                return trucks[choice - 1]
            else:
                print("Invalid index. Please enter a valid index.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
