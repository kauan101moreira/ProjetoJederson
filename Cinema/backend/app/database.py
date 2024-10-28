# database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# Define a URL do banco de dados SQLite
SQLALCHEMY_DATABASE_URL = "sqlite:///./movies.db"

# Configura o engine do banco de dados
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Sessão local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para a criação de modelos
Base = declarative_base()

# Cria as tabelas no banco de dados
def init_db():
    Base.metadata.create_all(bind=engine)

# Dependência do banco de dados para usar nas rotas
def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
