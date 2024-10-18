from fastapi import FastAPI
from .routers import movies
from .database import engine, Base

# Inicializa o FastAPI
app = FastAPI()

# Cria as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

# Inclui as rotas
app.include_router(movies.router)

@app.get("/")
def root():
    return {"message": "Bem-vindo ao sistema de gerenciamento de filmes!"}
