from fastapi import APIRouter
from database import Session
from models.animal import Animal
from models.schema import AnimalCreate

router = APIRouter()


@router.post("/animals")
def add_animal(animal: AnimalCreate):

    session = Session()

    try:
        novo_animal = Animal(
            cor=animal.cor,
            especie=animal.especie,
            tipo=animal.tipo,
            nome_especie=animal.nome_especie
        )

        session.add(novo_animal)
        session.commit()
        session.refresh(novo_animal)

        return {
            "message": "Animal cadastrado com SUCESSO!",
            "id": novo_animal.id
        }

    except Exception as e:
        session.rollback()

        return {
            "error": True,
            "message": str(e)
        }

    finally:
        session.close()


@router.get("/animals/")
def obter_animais():

    session = Session()

    try:
        animais = session.query(Animal).all()

        return [
            {
                "id": animal.id,
                "nome_especie": animal.nome_especie,
                "especie": animal.especie
            }
            for animal in animais
        ]

    finally:
        session.close()