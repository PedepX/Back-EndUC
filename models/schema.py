from pydantic import BaseModel


class AnimalCreate(BaseModel):
    cor: str
    especie: str
    tipo: str
    nome_especie: str


class AnimalResponse(BaseModel):
    id: int
    nome_especie: str
    especie: str

    class Config:
        from_attributes = True