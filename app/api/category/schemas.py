from pydantic import BaseModel
from sqlalchemy import orm

class CategorySchema(BaseModel):
    name: str
    

class ShowCategorySchema(CategorySchema):
    id:int
    class Config:
        orm_mode = True
