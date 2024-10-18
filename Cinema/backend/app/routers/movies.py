# Importações necessárias para definir as rotas do FastAPI
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, models, schemas
from ..database import SessionLocal, engine

# Criação do router para lidar com rotas de filmes
router = APIRouter()

# Garante que as tabelas estejam criadas no banco de dados
models.Base.metadata.create_all(bind=engine)

# Função que retorna a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rota para obter todos os filmes
@router.get("/movies", response_model=list[schemas.Movie])
def read_movies(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    movies = crud.get_movies(db, skip=skip, limit=limit)
    return movies

# Rota para obter um filme específico pelo ID
@router.get("/movies/{movie_id}", response_model=schemas.Movie)
def read_movie(movie_id: int, db: Session = Depends(get_db)):
    db_movie = crud.get_movie(db, movie_id=movie_id)
    if db_movie is None:
        raise HTTPException(status_code=404, detail="Filme não encontrado")
    return db_movie

# Rota para criar um novo filme
@router.post("/movies", response_model=schemas.Movie)
def create_movie(movie: schemas.MovieCreate, db: Session = Depends(get_db)):
    return crud.create_movie(db=db, movie=movie)

# Rota para deletar um filme pelo ID
@router.delete("/movies/{movie_id}", response_model=schemas.Movie)
def delete_movie(movie_id: int, db: Session = Depends(get_db)):
    db_movie = crud.get_movie(db, movie_id=movie_id)
    if db_movie is None:
        raise HTTPException(status_code=404, detail="Filme não encontrado")
    return crud.delete_movie(db=db, movie_id=movie_id)

