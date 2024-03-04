import requests

def get_pokemon_info(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(data["abilities"])
    else:
        print(f"Failed to fetch Pokémon data. Status code: {response.status_code}")

get_pokemon_info("pikachu")
