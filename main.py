from fastapi import FastAPI, HTTPException
from models import Recipe
from routers import recipes
import dotenv
import os

dotenv.load_dotenv()
software_version=os.getenv("VERSION_NUMBER")

app = FastAPI(title="Recipe API", version=software_version)

recipes_db = [
    Recipe(
        id=1,
        name="Spaghetti Carbonara", 
        cuisine="Italian", 
        preparation_time=30, 
        is_vegetarian=False
    ),
    Recipe(
        id=2,
        name="Rattatouille",
        cuisine="French",
        preparation_time=60,
        is_vegetarian=True
    ),
    Recipe(
        id=3,
        name="Tacos al Pastor",
        cuisine="Mexican",
        preparation_time=45,
        is_vegetarian=False
    )

]
next_id = 1

app.include_router(recipes.router, prefix="/recipes", tags=["recipes"])