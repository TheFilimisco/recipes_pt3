from typing import Union

from pydantic import BaseModel

class RecipeInput(BaseModel):
    name: str
    ingredients: list[str]
    instructions: list[str]
    prepTimeMinutes: int
    cookTimeMinutes: int
    servings: int
    difficulty: str
    cuisine: str
    caloriesPerServing: int
    tags: list[str]
    userId: int
    image: str
    rating: float
    reviewCount: int
    mealType: list[str]

class RecipeOutput(BaseModel):
    id: Union[int,None]
    name: str
    ingredients: list[str]
    instructions: list[str]
    prepTimeMinutes: int
    cookTimeMinutes: int
    servings: int
    difficulty: str
    cuisine: str
    caloriesPerServing: int
    tags: list[str]
    userId: int
    image: str
    rating: float
    reviewCount: int
    mealType: list[str]
