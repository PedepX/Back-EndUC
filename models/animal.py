from sqlalchemy import Column, Integer, String
from database import Base


class Animal(Base):
    __tablename__ = "animals"

    id = Column(Integer, primary_key=True)
    cor = Column(String)
    especie = Column(String)
    tipo = Column(String)
    nome_especie = Column(String)