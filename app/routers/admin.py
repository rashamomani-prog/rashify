from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.recipe import Recipe
from app.schemas.recipe import RecipeOut, RecipeBase
from app.routers.auth import get_db, get_current_user

router = APIRouter()

def is_admin(user=Depends(get_current_user)):
    if user.role != "admin":
        raise HTTPException(status_code=403, detail="Not allowed")
    return user

@router.post("/recipes", response_model=RecipeOut)
def create_recipe(recipe: RecipeBase, db: Session = Depends(get_db), admin_user=Depends(is_admin)):
    new_recipe = Recipe(**recipe.model_dump(), owner_id=admin_user.id)
    db.add(new_recipe)
    db.commit()
    db.refresh(new_recipe)
    return new_recipe


@router.put("/recipes/{recipe_id}", response_model=RecipeOut)
def update_recipe(
    recipe_id: int,
    body: RecipeBase,
    db: Session = Depends(get_db),
    admin_user=Depends(is_admin),
):
    """Update recipe by ID (admin only)."""
    recipe = db.query(Recipe).filter(Recipe.id == recipe_id).first()
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    for key, value in body.model_dump().items():
        setattr(recipe, key, value)
    db.commit()
    db.refresh(recipe)
    return recipe


@router.delete("/recipes/{recipe_id}", status_code=204)
def delete_recipe(
    recipe_id: int,
    db: Session = Depends(get_db),
    admin_user=Depends(is_admin),
):
    """Delete recipe by ID (admin only)."""
    recipe = db.query(Recipe).filter(Recipe.id == recipe_id).first()
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    db.delete(recipe)
    db.commit()
    return None

