from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "sqlite:///meudb.db"

engine = create_engine(DATABASE_URL)

Base = declarative_base()

Session = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)