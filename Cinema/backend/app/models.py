from lib2to3.pytree import Base
from sqlalchemy import Column, Integer, String, Float
from .database import Base

class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, nullable=True)
    rating = Column(Float, nullable=True)  
    genre = Column(String, index=True)
    year = Column(Integer, nullable=True)  