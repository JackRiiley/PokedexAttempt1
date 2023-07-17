from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://pokemondb_l9et_user:wvhuoDGOhMHDvAiqI4iXv4SAwjcph217@dpg-ciqoset9aq0dcpt1e7v0-a.frankfurt-postgres.render.com/pokemondb_l9et"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()