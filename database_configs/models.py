from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database_configs.connection import Base

class Pokemon(Base):
    __tablename__ = "pokemon"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True) #added this to try resolve duplicate number issue - not tried yet
    number = Column(Integer)
    name = Column(String, index=True)
    type1 = Column(String)
    type2 = Column(String)
    generation = Column(Integer)
    legendary = Column(Boolean)
    
    stats_id = Column(Integer, ForeignKey("pokemon_stats.id"), unique=True)
    stats = relationship("PokemonStats", back_populates="pokemon")
    
    
class PokemonStats(Base):
    __tablename__ = "pokemon_stats"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    total = Column(Integer)
    hp = Column(Integer)
    attack = Column(Integer)
    defense = Column(Integer)
    sp_atk = Column(Integer)
    sp_def = Column(Integer)    
    speed = Column(Integer)
    
    pokemon = relationship("Pokemon", back_populates="stats", uselist=False)