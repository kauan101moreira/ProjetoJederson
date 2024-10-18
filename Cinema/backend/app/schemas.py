from pydantic import BaseModel
from typing import List, Optional

class MovieBase(BaseModel):
    title: str  # Campo para o título do filme
    description: str  # Campo para a descrição do filme
    rating: float  # Campo para a classificação do filme
    genre: str  # Campo para o gênero do filme

class MovieCreate(MovieBase):
    pass  # Classe para criar novos filmes

class Movie(MovieBase):
    id: int  # Campo para o ID do filme

    class Config:
        orm_mode = True  # Ativa a compatibilidade com ORM para conversão automática

