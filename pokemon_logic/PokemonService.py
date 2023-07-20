from sqlalchemy.orm import Session, Depends
from database_configs.connection import engine, Base, SessionLocal, get_db
from database_configs.models import Pokemon, PokemonStats
class PokemonService:
    def __init__ (self):
        pass
    
    def GetAllPokemon(self, db: Session):
        return db.query(Pokemon).join(PokemonStats, PokemonStats.pokemon_id == Pokemon.id).all()
    
    def GetPokemonByName(self, pokemon_name: str):
        
        for pokemon in PokemonList:
            if pokemon["name"].__contains__(pokemon_name.lower()):
                return pokemon
        
        return {"message": "Pokemon not found"}