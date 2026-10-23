from fastapi import APIRouter, HTTPException
from loguru import logger

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
        logger.warning(
            "Cadastro rejeitado: Pokémon da Pokédex {} já existe",
            dados.idpokedex
        )
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
    logger.info(
        "Pokémon cadastrado: Pokédex {} ({})",
        pokemon.idpokedex,
        pokemon.nome
    )

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
        logger.warning(
            "Busca falhou: Pokémon da Pokédex {} não encontrado",
            idpokedex
        )
        raise HTTPException(
            status_code=404,
            detail="Pokémon não encontrado"
        )

    logger.info("Pokémon consultado: Pokédex {}", idpokedex)
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
        logger.warning(
            "Atualização falhou: Pokémon da Pokédex {} não encontrado",
            idpokedex
        )
        raise HTTPException(
            status_code=404,
            detail="Pokémon não encontrado"
        )

    pokemon.update(**pokemon_dados.dict())

    pokemon.reload()
    logger.info("Pokémon atualizado: Pokédex {}", idpokedex)

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
        logger.warning(
            "Exclusão falhou: Pokémon da Pokédex {} não encontrado",
            idpokedex
        )
        raise HTTPException(
            status_code=404,
            detail="Pokémon não encontrado"
        )

    pokemon.delete()
    logger.info("Pokémon excluído: Pokédex {}", idpokedex)

    return {
        "message": "Pokémon deletado da Pokedex com sucesso!"
    }