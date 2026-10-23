import pytest
from fastapi import HTTPException
from loguru import logger

import routes.pokemon as pokemon_routes
from schema.pokemon import PokemonReq


class FakeQuery:
    def __init__(self, pokemon):
        self.pokemon = pokemon

    def first(self):
        return self.pokemon


class FakePokemon:
    records = {}

    def __init__(self, **dados):
        self.__dict__.update(dados)

    @classmethod
    def objects(cls, **filtros):
        return FakeQuery(cls.records.get(filtros["idpokedex"]))

    def save(self):
        self.records[self.idpokedex] = self

    def update(self, **dados):
        self.__dict__.update(dados)

    def reload(self):
        return self

    def delete(self):
        self.records.pop(self.idpokedex)


@pytest.fixture
def caplog_loguru(caplog):
    handler_id = logger.add(caplog.handler, format="{message}", level="INFO")
    yield caplog
    logger.remove(handler_id)


@pytest.fixture
def fake_pokemon(monkeypatch):
    FakePokemon.records = {}
    monkeypatch.setattr(pokemon_routes, "Pokemon", FakePokemon)
    return FakePokemon


def dados_pokemon(**sobrescritos):
    dados = {
        "idpokedex": 25,
        "nome": "Pikachu",
        "tipo": "Elétrico",
        "nature": "Alegre",
        "ability": "Static",
    }
    dados.update(sobrescritos)
    return PokemonReq(**dados)


def test_cadastrar_pokemon_registra_log(caplog_loguru, fake_pokemon):
    resultado = pokemon_routes.cadastrar_pokemon(dados_pokemon())

    assert resultado["pokemon"]["nome"] == "Pikachu"
    assert "Pokémon cadastrado: Pokédex 25 (Pikachu)" in caplog_loguru.text
    assert caplog_loguru.records[-1].levelname == "INFO"


def test_cadastro_duplicado_registra_aviso(caplog_loguru, fake_pokemon):
    pokemon_routes.cadastrar_pokemon(dados_pokemon())

    with pytest.raises(HTTPException) as erro:
        pokemon_routes.cadastrar_pokemon(dados_pokemon())

    assert erro.value.status_code == 400
    assert "Cadastro rejeitado: Pokémon da Pokédex 25 já existe" in caplog_loguru.text
    assert caplog_loguru.records[-1].levelname == "WARNING"


def test_buscar_pokemon_registra_log(caplog_loguru, fake_pokemon):
    pokemon_routes.cadastrar_pokemon(dados_pokemon())

    resultado = pokemon_routes.buscar_pokemon(25)

    assert resultado["nome"] == "Pikachu"
    assert "Pokémon consultado: Pokédex 25" in caplog_loguru.text
    assert caplog_loguru.records[-1].levelname == "INFO"


def test_buscar_pokemon_inexistente_registra_aviso(caplog_loguru, fake_pokemon):
    with pytest.raises(HTTPException) as erro:
        pokemon_routes.buscar_pokemon(999)

    assert erro.value.status_code == 404
    assert "Busca falhou: Pokémon da Pokédex 999 não encontrado" in caplog_loguru.text
    assert caplog_loguru.records[-1].levelname == "WARNING"


def test_atualizar_pokemon_registra_log(caplog_loguru, fake_pokemon):
    pokemon_routes.cadastrar_pokemon(dados_pokemon())

    resultado = pokemon_routes.atualizar_pokemon(
        25,
        dados_pokemon(nome="Raichu")
    )

    assert resultado["pokemon"]["nome"] == "Raichu"
    assert "Pokémon atualizado: Pokédex 25" in caplog_loguru.text
    assert caplog_loguru.records[-1].levelname == "INFO"


def test_deletar_pokemon_registra_log(caplog_loguru, fake_pokemon):
    pokemon_routes.cadastrar_pokemon(dados_pokemon())

    resultado = pokemon_routes.deletar_pokemon(25)

    assert resultado["message"] == "Pokémon deletado da Pokedex com sucesso!"
    assert 25 not in fake_pokemon.records
    assert "Pokémon excluído: Pokédex 25" in caplog_loguru.text
    assert caplog_loguru.records[-1].levelname == "INFO"


@pytest.mark.parametrize(
    "operacao",
    [
        lambda: pokemon_routes.atualizar_pokemon(999, dados_pokemon()),
        lambda: pokemon_routes.deletar_pokemon(999),
    ],
)
def test_atualizar_ou_deletar_inexistente_registra_aviso(
    operacao,
    caplog_loguru,
    fake_pokemon,
):
    with pytest.raises(HTTPException) as erro:
        operacao()

    assert erro.value.status_code == 404
    assert caplog_loguru.records[-1].levelname == "WARNING"
