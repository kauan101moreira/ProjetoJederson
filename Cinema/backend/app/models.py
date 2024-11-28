from sqlalchemy import Column, Integer, String, Float
from .database import Base

class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    duration = Column(Integer, nullable=False)
    rating = Column(Float, nullable=True)  
    genre = Column(String, index=True)
    year = Column(Integer, nullable=False)