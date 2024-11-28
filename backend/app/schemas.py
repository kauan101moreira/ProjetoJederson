from pydantic import BaseModel
from typing import Optional



class MovieBase(BaseModel):
    title: str
    genre: str
    duration: int
    rating: Optional[float] = None
    year: int  

class MovieCreate(MovieBase):
    rating: Optional[float] = None

class Movie(MovieBase):
    id: int

    class Config:
        orm_mode = True

