from typing import List
from models import Recipe


recipes_db: List[Recipe] = [
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
next_id: int = 4
