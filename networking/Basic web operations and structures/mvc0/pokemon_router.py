from fastapi import APIRouter, HTTPException
import requests

router = APIRouter()


@router.get("/pokemon", tags=["tests"])
def test():
    """
    Test endpoint to check if the API is running.
    """
    print({"message": "pokemon router is working!"})
    return {"message": "pokemon router is working!"}


@router.get("/pokemon/{name}")
async def get_pokemon_info(name: str):
    pokeapi_url = f"https://pokeapi.co/api/v2/pokemon/{name}"
    response = requests.get(pokeapi_url)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Pokémon not found")
    pokemon_data = response.json()
    pokemon_info = {
        "name": pokemon_data["name"],
        "types": [type_data["type"]["name"] for type_data in pokemon_data["types"]],
        "abilities": [ability_data["ability"]["name"] for ability_data in pokemon_data["abilities"]],
    }
    return pokemon_info
