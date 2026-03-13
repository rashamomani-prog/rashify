from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.routers import ai_routes
from app.database.database import engine, Base
from app.models import user, recipe
from app.routers import auth, recipe as recipe_router, admin, ai_routes # أضفنا ai_routes

app = FastAPI(title="Rashify API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# إنشاء الجداول في قاعدة البيانات
Base.metadata.create_all(bind=engine)

app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(recipe_router.router, prefix="/recipes", tags=["Recipes"])
app.include_router(admin.router, prefix="/admin", tags=["Admin"])
app.include_router(ai_routes.router, prefix="/ai", tags=["AI & Smart Suggestions"]) # الـ Router الجديد
app.include_router(ai_routes.router, prefix="/ai", tags=["AI"])
@app.get("/")
def root():
    return {
        "message": "Welcome to Rashify API",
        "status": "Running",
        "mode": "Development (Multi-Device Support)"
    }

if __name__ == "__main__":
    import uvicorn
    # host="0.0.0.0" هي السر اللي بيخلي التلفون واللابتوب يشوفوا بعض
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)