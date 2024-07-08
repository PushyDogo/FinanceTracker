from typing import Literal
from pydantic import BaseModel

class CategoryBase(BaseModel):
    name: Literal['Food', 'Income', 'Housing']

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int

    class Config:
        orm_mode = True
