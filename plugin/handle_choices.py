def handle_apples():
    return "You chose apples!"


def handle_bats():
    return "You chose bats!"


choices = {
    'A': handle_apples,
    'B': handle_bats
}

choice = 'A'  # Example choice

if choice in choices:
    message = choices[choice]()
    print(message)
else:
    print(f'Invalid choice: {choice}')
