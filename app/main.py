from fastapi import FastAPI
from app.database.database import engine, Base
from app.models import user
from app.routers import auth

app = FastAPI()
Base.metadata.create_all(bind=engine)
app.include_router(auth.router)
@app.get("/")
def root():
    return {"message": "Welcome to Rashify API 🍳"}