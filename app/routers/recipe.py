from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from app.database.database import SessionLocal
from app.models.recipe import Recipe, favorites_table
from typing import List
from sqlalchemy import or_
router = APIRouter(prefix="/recipes", tags=["Recipes"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
def get_recipes(category: str = None, db: Session = Depends(get_db)):
    query = db.query(Recipe)
    if category:
        query = query.filter(Recipe.category == category)
    return query.all()


@router.get("/search")
def search_by_ingredients(items: str = Query(..., description="المكونات مفصولة بفاصلة"), db: Session = Depends(get_db)):
    ingredients_list = [item.strip().lower() for item in items.split(",")]
    all_recipes = db.query(Recipe).all()

    matched_recipes = []
    for recipe in all_recipes:
        if any(ing in recipe.ingredients.lower() for ing in ingredients_list):
            matched_recipes.append(recipe)
    return matched_recipes
@router.get("/recipes/search")
def search_recipes(query: str, db: Session = Depends(get_db)):
    # بيبحث في العنوان، المكونات، أو حتى القسم (Category)
    results = db.query(Recipe).filter(
        or_(
            Recipe.title.ilike(f"%{query}%"),
            Recipe.ingredients.ilike(f"%{query}%"),
            Recipe.category.ilike(f"%{query}%")
        )
    ).all()
    return results

@router.post("/{recipe_id}/favorite")
def toggle_favorite(recipe_id: int, user_id: int, db: Session = Depends(get_db)):
    recipe = db.query(Recipe).filter(Recipe.id == recipe_id).first()
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found!")

    query = favorites_table.select().where(
        (favorites_table.c.user_id == user_id) &
        (favorites_table.c.recipe_id == recipe_id)
    )
    existing_fav = db.execute(query).fetchone()

    if existing_fav:
        delete_stmt = favorites_table.delete().where(
            (favorites_table.c.user_id == user_id) &
            (favorites_table.c.recipe_id == recipe_id)
        )
        db.execute(delete_stmt)
        db.commit()
        return {"status": "unfavorited", "message": "Removed from favorites 💔"}
    else:
        insert_stmt = favorites_table.insert().values(user_id=user_id, recipe_id=recipe_id)
        db.execute(insert_stmt)
        db.commit()
        return {"status": "favorited", "message": "Added to favorites ❤️"}
