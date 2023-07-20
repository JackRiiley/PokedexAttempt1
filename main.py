from fastapi import FastAPI
from pokemon_logic import PokemonService
from sqlalchemy.orm import Session, Depends
from database_configs.connection import engine, Base, SessionLocal, get_db
from database_configs import models
from parse_data import parse_pokemon, parse_stats

Base.metadata.create_all(bind=engine)


#Setting up the FastAPI object
app = FastAPI()

#Setting up home route for API requests
@app.get("/")
def home():
    return {"message": "Hello World"}

#Creating an API endpoint for all pokemon
@app.get("/pokemon")
def GetAllPokemon(db: Session = Depends(get_db)):
    return

#Creating an API endpoint for searching for a pokemon
@app.get("/pokemon/{pokemon_name}")
def GetPokemonByName(pokemon_name: str):
    pokemonService = PokemonService()
    return pokemonService.GetPokemonByName(pokemon_name)