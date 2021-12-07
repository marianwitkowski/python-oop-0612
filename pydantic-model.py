"""
 Mapowanie danych z JSON na kolekcję obiektów
 z wykorzystaniem biblioteki Pydantic
"""
from pydantic import BaseModel, validator, \
    ValidationError, PositiveInt, conint, constr, EmailStr
from typing import List, Optional
import json

class Translator(BaseModel):
    name : str
    verified: bool
    email: Optional[EmailStr]

class Book(BaseModel):
    title: constr(min_length=2, max_length=255, strip_whitespace=True)
    author: str
    year_written: conint(gt=1600, lt=2022)
    #edition: str
    price: float
    score: Optional[PositiveInt] = 1
    translator: Optional[Translator]

    # @validator('year_written') # walidacja pola "price"
    # def year_wr_check(cls, value):
    #     if value<1400:
    #         raise ValueError(f"Za stara kniga! - rok {value}")
    #     return value


import time

if __name__ == "__main__":
    with open("books.json", "rt") as fd:
        data = json.load(fd)
        #print(len(data))
        try:
            ts1 = time.time_ns()
            books : List[Book] = [Book(**item) for item in data]
            print(books[4].dict(exclude={"price","score"}))
            ts2 = time.time_ns()
            print((ts2-ts1)/10E9)
        except ValidationError as exc:
            print(exc)