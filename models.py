from pydantic import BaseModel
from typing import Optional

class Recipe(BaseModel):
    id: int
    name: str
    cuisine: str
    preparation_time: int
    is_vegetarian: bool = False

class RecipeCreate(BaseModel):
    name: str
    cuisine: str
    preparation_time: int
    is_vegetarian: bool = False