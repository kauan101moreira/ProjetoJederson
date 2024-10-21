# Importações necessárias
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import movies
from .database import engine, Base

# Inicializa o FastAPI
app = FastAPI()

# Configura o CORS para permitir o frontend fazer requisições
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # URL do frontend React (ajuste conforme necessário)
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos HTTP (GET, POST, PUT, DELETE)
    allow_headers=["*"],  # Permite todos os cabeçalhos
)

# Cria as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

# Inclui as rotas
app.include_router(movies.router)

# Rota raiz
@app.get("/")
def root():
    return {"message": "Bem-vindo ao sistema de gerenciamento de filmes!"}

