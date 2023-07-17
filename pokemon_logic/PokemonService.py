class PokemonService:
    def __init__ (self):
        pass
    
    def GetAllPokemon(self):
    #TO-DO: implement this 
        return
    
    def GetPokemonByName(self, pokemon_name: str):
        
        for pokemon in PokemonList:
            if pokemon["name"].__contains__(pokemon_name.lower()):
                return pokemon
        
        return {"message": "Pokemon not found"}