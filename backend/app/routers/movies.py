from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import crud, schemas, models
from ..database import get_db

router = APIRouter()

@router.get("/movies", response_model=list[schemas.Movie])
def read_movies(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Retorna uma lista de filmes, com suporte a paginação usando skip e limit.
    """
    try:
        movies = crud.get_movies(db, skip=skip, limit=limit)
        return movies
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao buscar filmes: {str(e)}")

@router.post("/movies", response_model=schemas.Movie)
def create_movie(movie: schemas.MovieCreate, db: Session = Depends(get_db)):
    """
    Cria um novo filme com base nos dados fornecidos.
    """
    try:
        return crud.create_movie(db=db, movie=movie)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao criar filme: {str(e)}")

@router.get("/movies/{movie_id}", response_model=schemas.Movie)
def read_movie(movie_id: int, db: Session = Depends(get_db)):
    """
    Retorna um único filme com base no ID fornecido.
    """
    try:
        db_movie = crud.get_movie(db, movie_id=movie_id)
        if db_movie is None:
            raise HTTPException(status_code=404, detail="Filme não encontrado")
        return db_movie
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao buscar filme: {str(e)}")

@router.delete("/movies/{movie_id}")
def delete_movie(movie_id: int, db: Session = Depends(get_db)):
    """
    Deleta um filme com base no ID fornecido.
    """
    try:
        db_movie = crud.get_movie(db, movie_id=movie_id)
        if db_movie is None:
            raise HTTPException(status_code=404, detail="Filme não encontrado")
        crud.delete_movie(db=db, movie_id=movie_id)
        return {"message": "Filme removido com sucesso"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao deletar filme: {str(e)}")

