from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from odm import Pokemon

app = FastAPI(title="Pokedex Banco de Dados")

class PokemonReq(BaseModel):
    idpokedex: int
    nome: str
    tipo: str
    nature: str
    ability: str

@app.post("/pokemon")
def cadastrar_pokemon(dados: PokemonReq):

    pokemon_existente = Pokemon.objects(
        idpokedex=dados.idpokedex).first()

    if pokemon_existente:
        raise HTTPException(
            status_code=400,
            detail="Pokémon já foi cadastrado"
        )

    pokemon = Pokemon(
        idpokedex=dados.idpokedex,
        nome=dados.nome,
        tipo=dados.tipo,
        nature=dados.nature,
        ability=dados.ability
)

    pokemon.save()

    return {
        "mensagem": "Pokémon cadastrado com sucesso!",
        "pokemon": {
            "idpokedex": pokemon.idpokedex,
            "nome": pokemon.nome,
            "tipo": pokemon.tipo,
            "nature": pokemon.nature,
            "ability": pokemon.ability
        }
    }

@app.get("/pokemon/{idpokedex}")
def buscar_pokemon(idpokedex: int):

    pokemon = Pokemon.objects(idpokedex=idpokedex).first()

    if not pokemon:
        raise HTTPException(
            status_code=404,
            detail="Pokémon não encontrado"
        )

    return {
        "idpokedex": pokemon.idpokedex,
        "nome": pokemon.nome,
        "tipo": pokemon.tipo,
        "nature": pokemon.nature,
        "ability": pokemon.ability
    }

@app.put("/pokemon/{idpokedex}")
def atualizar_pokemon(idpokedex: int, pokemon_dados: PokemonReq):

    pokemon = Pokemon.objects(idpokedex=idpokedex).first()

    if not pokemon:
        raise HTTPException(
            status_code=404,
            detail="Pokémon não encontrado"
        )

    pokemon.update(**pokemon_dados.dict())

    pokemon.reload()

    return {
        "message": "Pokémon atualizado com sucesso", 
        "pokemon": {
            "idpokedex": pokemon.idpokedex,
            "nome": pokemon.nome,
            "tipo": pokemon.tipo,
            "nature": pokemon.nature,
            "ability": pokemon.ability
        }
    }

@app.delete("/pokemon/{idpokedex}")
def deletar_pokemon(idpokedex: int):

    pokemon = Pokemon.objects(idpokedex=idpokedex).first()

    if not pokemon:
        raise HTTPException(
            status_code=404,
            detail="Pokémon não encontrado"
        )

    pokemon.delete()

    return {"message": "Pokémon deletado da Pokedex com sucesso!"}