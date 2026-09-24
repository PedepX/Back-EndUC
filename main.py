from fastapi import FastAPI

from routes.pokemon import router as pokemon_router

app = FastAPI(title="Pokedex Banco de Dados")

app.include_router(pokemon_router)