import google.generativeai as genai
from config import settings

genai.configure(api_key=settings.GEMINI_API_KEY)

model = genai.GenerativeModel('gemini-pro')


def get_ai_recipe_suggestion(user_ingredients, recipes_list_103):
    prompt = f"""
    I have these recipes: {recipes_list_103}
    The user has these ingredients: {user_ingredients}
    Suggest the best recipe from my list and explain why.
    """

    response = model.generate_content(prompt)
    return response.text


def settings():
    return None