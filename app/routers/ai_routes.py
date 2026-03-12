from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.models.recipe import Recipe  # تأكدي إن الموديل بهذا الاسم
from app.services.ai_service import AIService
from pydantic import BaseModel
import os

router = APIRouter()


# --- 1. ميزة البحث (Search) عن الوصفات في قاعدة البيانات ---
@router.get("/search")
def search_recipes(query: str, db: Session = Depends(get_db)):
    # بيبحث في العنوان والمكونات عن أي نص بيشبه اللي دخله المستخدم
    results = db.query(Recipe).filter(
        (Recipe.title.ilike(f"%{query}%")) |
        (Recipe.ingredients.ilike(f"%{query}%"))
    ).all()
    return results


# --- 2. ميزة اقتراحات الـ AI (Gemini) ---
class IngredientsRequest(BaseModel):
    ingredients: list[str]


@router.post("/suggest")
async def get_ai_suggestion(request: IngredientsRequest):
    # بيقرأ المفتاح من ملف الـ .env
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise HTTPException(status_code=500, detail="Gemini API Key is missing in .env file")

    ai_service = AIService(api_key=api_key)
    result = ai_service.get_recipe_suggestion(request.ingredients)

    if "error" in result:
        raise HTTPException(status_code=500, detail=result["error"])

    return result