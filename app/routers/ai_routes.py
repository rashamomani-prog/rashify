from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.models.recipe import Recipe
import google.generativeai as genai

router = APIRouter()


@router.post("/predict")
async def get_ai_recommendation(user_query: dict, db: Session = Depends(get_db)):
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

        The user is asking: "{user_query.get('text')}"

        Please recommend the best 3 recipes from the list above. 
        Return ONLY the IDs of the recipes as a comma-separated list (e.g., 1, 15, 22).
        """
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)
        recommended_ids = [int(i.strip()) for i in response.text.split(',')]
        final_recommendations = db.query(Recipe).filter(Recipe.id.in_(recommended_ids)).all()

        return final_recommendations

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))