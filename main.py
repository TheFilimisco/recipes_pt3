import json

import jsonable
from fastapi import FastAPI, HTTPException, status
from client import RecipeInput,RecipeOutput
from fastapi.encoders import jsonable_encoder

from database import read_db


DB_PATH = "data/recipes.json"
recipes = read_db(DB_PATH, "recipes")

app = FastAPI()

@app.get("/")
def root():
    return {"message": "This server is running!"}

@app.get("/recipes")
def get_recipes() -> list[RecipeOutput]:
    return recipes.values()

@app.get("/recipes/{recipe_id}")
def get_recipe(recipe_id: int) -> RecipeOutput:
    if recipe_id in recipes.keys():
        return recipes[recipe_id]
    raise HTTPException(status_code=404, detail="Recipe not found")

@app.post("/recipes", status_code=status.HTTP_201_CREATED)
def create_recipe(recipe: RecipeInput):
    new_id = (max(recipes.keys())+1)
    new_recipe = {"id": new_id}
    new_recipe.update(recipe)
    recipes[new_id] = new_recipe
    return new_recipe

@app.put("/recipes/{recipe_id}", status_code=status.HTTP_200_OK)
def update_recipe(recipe_id: str, recipe: dict):
    #TODO
    recipes[recipe_id] = recipe
    return recipes[recipe_id]

@app.delete("/recipes/{recipe_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_recipe(recipe_id: int):
    if recipe_id in recipes.keys():
        del recipes[recipe_id]
        return {"message": "Recipe deleted"}
    raise HTTPException(status_code=404, detail="Recipe not found")