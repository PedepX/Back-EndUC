from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from banco import db
from banco import Query

app = FastAPI(title="Ominitrix Sessão")

class Alien(BaseModel):
    idomnitrix: int
    nome: str
    raca: str
    planeta_natal: str
    habilidade: str

@app.post("/omnitrix")
def cadastrar_alien(alien: Alien):

    db.insert({
        "idomnitrix": alien.idomnitrix,
        "nome": alien.nome,
        "raca": alien.raca,
        "planeta_natal": alien.planeta_natal,
        "habilidade": alien.habilidade
    })

    return {
        "mensagem": "Alien catalogado com sucesso!",
        "alien": alien
    }

@app.get("/omnitrix/{idomnitrix}")
def buscar_alien(idomnitrix:int):

    AlienQuery = Query()


    alien = db.search(AlienQuery.idomnitrix == idomnitrix)

    if not alien:
        raise HTTPException(
            status_code=404,
            detail="Alien não catalogado."
        )

    return alien[0]