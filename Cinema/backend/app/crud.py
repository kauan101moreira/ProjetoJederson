# Importações necessárias para manipular o banco de dados
from sqlalchemy.orm import Session
from . import models, schemas

# Função para obter todos os filmes do banco de dados
def get_movies(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Movie).offset(skip).limit(limit).all()

# Função para obter um filme específico pelo ID
def get_movie(db: Session, movie_id: int):
    return db.query(models.Movie).filter(models.Movie.id == movie_id).first()

# Função para criar um novo filme
def create_movie(db: Session, movie: schemas.MovieCreate):
    db_movie = models.Movie(title=movie.title, genre=movie.genre)  # Cria um objeto Movie
    db.add(db_movie)  # Adiciona ao banco de dados
    db.commit()  # Confirma a transação
    db.refresh(db_movie)  # Atualiza o objeto com os dados do banco
    return db_movie  # Retorna o novo filme criado


# Função para deletar um filme pelo ID
def delete_movie(db: Session, movie_id: int):
    db_movie = db.query(models.Movie).filter(models.Movie.id == movie_id).first()
    if db_movie:
        db.delete(db_movie)
        db.commit()
    return db_movie

