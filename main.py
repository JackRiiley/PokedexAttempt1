from fastapi import FastAPI
from pokemon_logic import PokemonService

#Setting up the FastAPI object
app = FastAPI()

#Setting up home route for API requests
@app.get("/")
def home():
    return {"message": "Hello World"}

#Creating an API endpoint for all pokemon
@app.get("/pokemon")
def GetAllPokemon():
    pokemonService = PokemonService()
    return pokemonService.GetAllPokemon()

#Creating an API endpoint for searching for a pokemon
@app.get("/pokemon/{pokemon_name}")
def GetPokemonByName(pokemon_name: str):
    pokemonService = PokemonService()
    return pokemonService.GetPokemonByName(pokemon_name)