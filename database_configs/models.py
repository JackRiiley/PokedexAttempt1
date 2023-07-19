from sqlalchemy import Column, Integer, String, Boolean
from database_configs.connection import Base

class Pokemon(Base):
    __tablename__ = "pokemon"
    number = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    type1 = Column(String)
    type2 = Column(String)
    generation = Column(Integer)
    legendary = Column(Boolean)