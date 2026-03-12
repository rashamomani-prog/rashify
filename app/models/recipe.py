from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.database.database import Base

favorites_table = Table(
    'favorites', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id'), primary_key=True),
    Column('recipe_id', Integer, ForeignKey('recipes.id'), primary_key=True)
)


class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    ingredients = Column(String, nullable=False)
    instructions = Column(String, nullable=False)
    image_url = Column(String, nullable=True)
    category = Column(String, index=True)

    owner_id = Column(Integer, ForeignKey("users.id"))