from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.recipe import Recipe
from app.schemas.recipe import RecipeOut, RecipeBase
from app.routers.auth import get_db, get_current_user

router = APIRouter()

def is_admin(user=Depends(get_current_user)):
    if user.email != "admin@example.com":
        raise HTTPException(status_code=403, detail="Not allowed")
    return user

@router.post("/admin/recipes", response_model=RecipeOut)
def create_recipe(recipe: RecipeBase, db: Session = Depends(get_db), admin_user=Depends(is_admin)):
    new_recipe = Recipe(**recipe.dict(), user_id=admin_user.id)
    db.add(new_recipe)
    db.commit()
    db.refresh(new_recipe)
    return new_recipe

