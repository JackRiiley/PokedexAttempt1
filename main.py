from fastapi import FastAPI

#Setting up the FastAPI object
app = FastAPI()

#Setting up home route for API requests
@app.get("/")
def home():
    return {"message": "Hello World"}

#Creating an API endpoint for all pokemon
@app.get("/pokemon")
def GetAllPokemon():
    #TO-DO: implement this 
    return

#Creating an API endpoint for searching for a pokemon
@app.get("/pokemon/{pokemon_name}")
def GetPokemonByName(pokemon_name: str):
    for pokemon in PokemonList:
        if pokemon["name"].__contains__(pokemon_name.lower()):
            return pokemon
        
    return {"message": "Pokemon not found"}