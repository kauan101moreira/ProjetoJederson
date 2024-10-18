# Importações do SQLAlchemy para criar as tabelas no banco de dados
from sqlalchemy import Column, Integer, String
from .database import Base

# Definição do modelo de dados "Movie" (Tabela do banco de dados)
class Movie(Base):
    __tablename__ = "movies" # Nome da tabela no banco de dados

    id = Column(Integer, primary_key=True, index=True) # Coluna de ID, chave primária
    title = Column(String, index=True)  # Coluna para armazenar o título do filme
    description = Column(String)
    rating = Column(Integer)
    genre = Column(String, index=True)  # Coluna para armazenar o gênero do filme
