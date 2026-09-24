from pydantic import BaseModel


class PokemonReq(BaseModel):
    idpokedex: int
    nome: str
    tipo: str
    nature: str
    ability: str