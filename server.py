import uvicorn
from fastapi import FastAPI
from database import engine, Base
from routes import animal_router

Base.metadata.create_all(bind=engine)

api = FastAPI(
    title="API MVC de Animais",
    description="CRUD seguindo padrões MVC com FastAPI e SQLAlchemy.",
    version="4.0.0"
)

api.include_router(animal_router, prefix="/animals", tags=["Animais"])

if __name__ == "__main__":
    uvicorn.run(api, host="127.0.0.1", port=8000)