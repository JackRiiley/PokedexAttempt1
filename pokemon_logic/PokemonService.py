from sqlalchemy.orm import Session
from database_configs.connection import engine, Base, SessionLocal, get_db
from database_configs.models import Pokemon, PokemonStats
class PokemonService:
    def __init__ (self, db: Session):
        self.db = db
    
    def GetAllPokemon(self):
        return self.db.query(Pokemon).all()
    
    def GetPokemonStats(self):
        return self.db.query(PokemonStats).all()
    
    def GetPokemonWithStats(self):
        return self.db.query(Pokemon).join(Pokemon.stats).all()
    
    def search_pokemon(self, search_term: str):
        # Perform a case-insensitive substring search using ilike
        search_query = f"%{search_term}%"
        pokemon_results = self.db.query(Pokemon).filter(Pokemon.name.ilike(search_query)).all()
        return pokemon_results