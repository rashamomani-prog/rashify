from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import or_

from app.database.database import get_db
from app.models.recipe import Recipe, favorites_table
from app.models.user import User
from app.routers.auth import get_current_user, get_current_user_optional

router = APIRouter(tags=["Recipes"])


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
@router.get("/by-query")
def search_recipes(query: str = Query(..., description="Search in title, ingredients, or category"), db: Session = Depends(get_db)):
    results = db.query(Recipe).filter(
        or_(
            Recipe.title.ilike(f"%{query}%"),
            Recipe.ingredients.ilike(f"%{query}%"),
            Recipe.category.ilike(f"%{query}%")
        )
    ).all()
    return results


@router.get("/favorites")
def get_my_favorites(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Return all recipes the current user has favorited. Auth required."""
    rows = db.execute(
        favorites_table.select().where(favorites_table.c.user_id == current_user.id)
    ).fetchall()
    recipe_ids = [row.recipe_id for row in rows]
    if not recipe_ids:
        return []
    return db.query(Recipe).filter(Recipe.id.in_(recipe_ids)).all()


@router.get("/{recipe_id}/favorite")
def get_favorite_status(
    recipe_id: int,
    db: Session = Depends(get_db),
    current_user: User | None = Depends(get_current_user_optional),
):
    """Return whether the current user has this recipe in favorites. No auth = not favorited."""
    recipe = db.query(Recipe).filter(Recipe.id == recipe_id).first()
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    if not current_user:
        return {"favorited": False}
    row = db.execute(
        favorites_table.select().where(
            (favorites_table.c.user_id == current_user.id)
            & (favorites_table.c.recipe_id == recipe_id)
        )
    ).fetchone()
    return {"favorited": row is not None}


@router.get("/{recipe_id}")
def get_recipe(recipe_id: int, db: Session = Depends(get_db)):
    """Return one recipe by ID."""
    recipe = db.query(Recipe).filter(Recipe.id == recipe_id).first()
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe


@router.post("/{recipe_id}/favorite")
def toggle_favorite(
    recipe_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    recipe = db.query(Recipe).filter(Recipe.id == recipe_id).first()
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")

    user_id = current_user.id
    fav_query = favorites_table.select().where(
        (favorites_table.c.user_id == user_id) & (favorites_table.c.recipe_id == recipe_id)
    )
    existing_fav = db.execute(fav_query).fetchone()

    if existing_fav:
        delete_stmt = favorites_table.delete().where(
            (favorites_table.c.user_id == user_id) & (favorites_table.c.recipe_id == recipe_id)
        )
        db.execute(delete_stmt)
        db.commit()
        return {"status": "unfavorited", "message": "Removed from favorites 💔"}
    else:
        insert_stmt = favorites_table.insert().values(user_id=user_id, recipe_id=recipe_id)
        db.execute(insert_stmt)
        db.commit()
        return {"status": "favorited", "message": "Added to favorites ❤️"}
