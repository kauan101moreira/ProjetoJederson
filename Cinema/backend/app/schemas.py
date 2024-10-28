from pydantic import BaseModel
from typing import Optional



class MovieBase(BaseModel):
    title: str
    genre: str
    description: Optional[str] = None
    rating: Optional[float] = None
    year: int  

class MovieCreate(MovieBase):
    description: Optional[str] = None
    rating: Optional[float] = None

class Movie(MovieBase):
    id: int

    class Config:
        orm_mode = True

