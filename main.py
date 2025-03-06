from typing import Optional

from fastapi import FastAPI, HTTPException, status
from client import RecipeInput,RecipeOutput
from database import read_db, save_db

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
def create_recipe(recipe: RecipeInput) -> dict:
    new_id = (max(recipes.keys())+1)
    new_recipe = {"id": new_id}
    new_recipe.update(recipe)
    recipes[new_id] = new_recipe
    save_db(DB_PATH, "recipes", recipes)
    return new_recipe

@app.put("/recipes/{recipe_id}", status_code=status.HTTP_200_OK)
def update_recipe(recipe_id: int, recipe: RecipeInput) -> RecipeOutput:
    updated_recipe = get_recipe(recipe_id)
    updated_recipe.update(recipe)
    save_db(DB_PATH, "recipes", recipes)
    return updated_recipe

@app.delete("/recipes/{recipe_id}", status_code=status.HTTP_200_OK)
def delete_recipe(recipe_id: int) -> dict:
    if recipe_id in recipes.keys():
        recipes.pop(recipe_id)
        save_db(DB_PATH, "recipes", recipes)
        return {"message": "Book deleted", "deleted_book":recipe_id}
    raise HTTPException(status_code=404, detail="Recipe not found")

@app.get("/recipes/cuisine/{cuisine_name}", status_code=status.HTTP_200_OK)
def get_recipes_by_cuisine(cuisine_name: str) -> list[RecipeOutput]:
    list_recipes = []
    for recipe in recipes.values():
        if recipe["cuisine"] == cuisine_name:
            list_recipes.append(recipe)
    return list_recipes

@app.get("/recipes/difficulty/{difficulty}", status_code=status.HTTP_200_OK)
def get_recipes_by_difficulty(difficulty: str) -> list[RecipeOutput]:
    list_recipes = []
    for recipe in recipes.values():
        if recipe["difficulty"] == difficulty:
            list_recipes.append(recipe)
    return list_recipes

@app.get("/recipes/ingredient/{ingredient_name}", status_code=status.HTTP_200_OK)
def get_recipes_by_difficulty(ingredient_name: str) -> list[RecipeOutput]:
    list_recipes = []
    for recipe in recipes.values():
        for ingredient in recipe["ingredients"]:
            if ingredient_name.lower() in ingredient.lower():
                list_recipes.append(recipe)
    return list_recipes


@app.get("/recipes/prep_time_minutes/{time_minutes}", status_code=status.HTTP_200_OK)
def get_recipes_by_time_minutes(time_minutes: int) -> list[RecipeOutput]:
    list_recipes = []
    for recipe in recipes.values():
        if recipe["prepTimeMinutes"] <= time_minutes:
            list_recipes.append(recipe)
    return list_recipes

@app.get("/recipes/meal_type/{meal_type}", status_code=status.HTTP_200_OK)
def get_recipes_by_meal_type(meal_type: str) -> list[RecipeOutput]:
    list_recipes = []
    for recipe in recipes.values():
        for meal in recipe["mealType"]:
            if meal_type.lower() in meal.lower():
                list_recipes.append(recipe)
    return list_recipes

@app.get("/recipes/calories_by_Serving/{calories}", status_code=status.HTTP_200_OK)
async def get_recipes_by_calories_max(calories: int, sort: Optional[bool] = False) -> list[RecipeOutput]:
    list_recipes = []
    for recipe in recipes.values():
        if recipe["caloriesPerServing"] <= calories:
            list_recipes.append(recipe)
    if list_recipes == []:
        raise HTTPException(status_code=404, detail="Recipes empty")
    return sorted(list_recipes, key=lambda re: re["caloriesPerServing"], reverse=sort)





