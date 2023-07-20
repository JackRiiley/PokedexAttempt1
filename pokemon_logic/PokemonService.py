from sqlalchemy.orm import Session
from database_configs.connection import engine, Base, SessionLocal, get_db
from database_configs.models import Pokemon, PokemonStats
class PokemonService:
    def __init__ (self, db: Session):
        self.db = db
    
    def GetAllPokemon(self):
        return self.db.query(Pokemon).all()