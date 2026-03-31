from fastapi import APIRouter, HTTPException
from models import Recipe, RecipeCreate
from db import recipes_db, next_id
from typing import Optional

router = APIRouter()



# GET: all recipes, one by ID (404 if missing), filter by cuisine or vegetarian status
@router.get("/", response_model=list[Recipe])
def get_recipies(cuisine: Optional[str] = None, is_vegetarian: Optional[bool] = None):
    try:
        if cuisine is None and is_vegetarian is None:
            return recipes_db
        else:
            recipes = recipes_db
            
            if cuisine is not None:
                recipes = [r for r in recipes if r.cuisine == cuisine]
            if is_vegetarian is not None:
                recipes = [r for r in recipes if r.is_vegetarian == is_vegetarian]
            
            return recipes
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="internal server error")

@router.get("/{recipe_id}", response_model=Recipe)
def get_one(recipe_id: int):
    try:
        recipe = next((r for r in recipes_db if r.id == recipe_id),None)
        if not recipe:
            raise KeyError()
        return recipe
    except KeyError:
        raise HTTPException(status_code=404, detail=f"Recipe {recipe_id} not found")
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="internal server error")






# POST: create new recipe, assign ID from next_id; return 409 if a recipe with the same name already exists
@router.post("/", response_model=Recipe)
def write_recipe(recipe: RecipeCreate):
    global recipes_db, next_id
    if any(r.name == recipe.name for r in recipes_db):
        raise HTTPException(status_code=409, detail="a recipe with this name already exists")
    insert_recipe = Recipe(id=next_id,**recipe.dict())
    recipes_db.append(insert_recipe)
    next_id += 1
    return insert_recipe

# PUT: replace a recipe entirely by ID; return 404 if not found
# DELETE: remove a recipe by ID; return 404 if not found, 204 with no body on success