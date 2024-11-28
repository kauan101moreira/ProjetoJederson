from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


# Importa a lógica de conexão com o banco de dados
from .database import engine, Base, get_db


# Importa o roteador de filmes
from .routers import movies  # Importa o módulo 'movies'

app = FastAPI()

# Configura o CORS (ajuste as origens conforme necessário)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inicializa o banco de dados criando todas as tabelas
def init_db():
    Base.metadata.create_all(bind=engine)

init_db()  # Chama a função para criar as tabelas

# Inclui o roteador de filmes na aplicação principal
app.include_router(movies.router)

# Rota raiz opcional
@app.get("/")
def read_root():
    return {"message": "Bem-vindo ao sistema de gerenciamento de filmes!"}

# Para executar o servidor, use o seguinte comando na linha de comando:
# uvicorn app.main:app --reload
