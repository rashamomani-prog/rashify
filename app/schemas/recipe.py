from pydantic import BaseModel


class RecipeBase(BaseModel):
    title: str
    ingredients: str
    instructions: str
    image_url: str | None = None
    category: str | None = None


class RecipeOut(RecipeBase):
    id: int
    owner_id: int | None = None

    class Config:
        from_attributes = True