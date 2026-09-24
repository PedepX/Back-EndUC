from fastapi import APIRouter, HTTPException

from models.pokemon import Pokemon
from schema.pokemon import PokemonReq


router = APIRouter(
    prefix="/pokemon",
    tags=["Pokémon"]
)


@router.post("")
def cadastrar_pokemon(dados: PokemonReq):

    pokemon_existente = Pokemon.objects(
        idpokedex=dados.idpokedex
    ).first()

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


@router.get("/{idpokedex}")
def buscar_pokemon(idpokedex: int):

    pokemon = Pokemon.objects(
        idpokedex=idpokedex
    ).first()

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


@router.put("/{idpokedex}")
def atualizar_pokemon(
    idpokedex: int,
    pokemon_dados: PokemonReq
):

    pokemon = Pokemon.objects(
        idpokedex=idpokedex
    ).first()

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


@router.delete("/{idpokedex}")
def deletar_pokemon(idpokedex: int):

    pokemon = Pokemon.objects(
        idpokedex=idpokedex
    ).first()

    if not pokemon:
        raise HTTPException(
            status_code=404,
            detail="Pokémon não encontrado"
        )

    pokemon.delete()

    return {
        "message": "Pokémon deletado da Pokedex com sucesso!"
    }