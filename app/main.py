from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.database.database import engine, Base
from app.models import user, recipe
from app.routers import auth, admin, ai_routes, recipe as recipe_router

app = FastAPI(title="Rashify API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(recipe_router.router, prefix="/recipes", tags=["Recipes"])
app.include_router(admin.router, prefix="/admin", tags=["Admin"])
app.include_router(ai_routes.router, prefix="/ai", tags=["AI & Smart Suggestions"])

@app.get("/")
def root():
    return {
        "message": "Welcome to Rashify API",
        "status": "Running",
        "mode": "Development (Multi-Device Support)",
        "project": "cv_digital / Rashify"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)