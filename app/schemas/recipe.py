from pydantic import BaseModel

class RecipeBase(BaseModel):
    title: str
    description: str | None = None

class RecipeOut(RecipeBase):
    id: int
    user_id: int
    likes: int

    class Config:
        orm_mode = True