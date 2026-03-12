import google.generativeai as genai
import json
from app.core.config import settings

class AIService:
    def __init__(self):
        api_key = settings.GEMINI_API_KEY
    def __init__(self, api_key: str):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    def get_recipe_suggestion(self, ingredients: list[str]):
        prompt = f"""
        Act as a professional chef. I have these ingredients: {', '.join(ingredients)}.
        Provide ONE creative recipe. 
        Return ONLY a JSON object with this structure:
        {{
            "title": "Recipe Name",
            "ingredients": "List of ingredients",
            "instructions": "Step by step instructions",
            "calories": 300,
            "time": 20
        }}
        Do not include any extra text or markdown formatting.
        """

        try:
            response = self.model.generate_content(prompt)
            cleaned_response = response.text.replace('```json', '').replace('```', '').strip()
            return json.loads(cleaned_response)
        except Exception as e:
            return {"error": str(e)}