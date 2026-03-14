from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.recipe import Recipe

router = APIRouter()


class AIPredictRequest(BaseModel):
    text: str


@router.post("/predict")
async def get_ai_recommendation(body: AIPredictRequest, db: Session = Depends(get_db)):
    try:
        import google.generativeai as genai
    except ImportError:
        raise HTTPException(status_code=503, detail="AI service not configured")

    try:
        all_recipes = db.query(Recipe).all()
        if not all_recipes:
            raise HTTPException(status_code=404, detail="No recipes found in database. Did you run the seed?")

        recipes_context = "\n".join([
            f"ID: {r.id}, Title: {r.title}, Ingredients: {r.ingredients}"
            for r in all_recipes
        ])
        prompt = f"""
You are a professional chef. Based on the following recipes available in our database:
{recipes_context}

The user is asking: "{body.text}"

Please recommend the best 3 recipes from the list above.
Return ONLY the IDs of the recipes as a comma-separated list (e.g., 1, 15, 22).
"""
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        raw_text = getattr(response, "text", None) or ""
        recommended_ids = []
        for part in raw_text.split(","):
            part = part.strip()
            if part.isdigit():
                recommended_ids.append(int(part))

        if not recommended_ids:
            return []
        final_recommendations = db.query(Recipe).filter(Recipe.id.in_(recommended_ids)).all()
        return final_recommendations

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))