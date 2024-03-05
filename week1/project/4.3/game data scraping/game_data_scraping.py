import requests
from game_element import *
if __name__ == "__main__":

    url = "https://store.steampowered.com/"
    response = requests.get(url)
    if response.status_code == 200:
        html_extract_game(response)
    else:
        print("Failed to fetch data from the Steam store.")