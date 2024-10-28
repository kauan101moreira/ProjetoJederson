from sqlalchemy.orm import Session
from . import models, schemas
from fastapi import FastAPI, Depends, HTTPException


def get_movies(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Movie).offset(skip).limit(limit).all()

def get_movie(db: Session, movie_id: int):
    movie = db.query(models.Movie).filter(models.Movie.id == movie_id).first()
    if not movie:
        raise HTTPException(status_code=404, detail="Filme não encontrado")
    return movie

def create_movie(db: Session, movie: schemas.MovieCreate):
    db_movie = models.Movie(
        title=movie.title,
        genre=movie.genre,
        description=movie.description,
        rating=movie.rating,
        year=movie.year  # Certifique-se de que este campo exista no modelo
    )
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie

def delete_movie(db: Session, movie_id: int):
    db_movie = db.query(models.Movie).filter(models.Movie.id == movie_id).first()
    if not db_movie:
        raise HTTPException(status_code=404, detail="Filme não encontrado")
    db.delete(db_movie)
    db.commit()
    return db_movie
