from pydantic import BaseModel
from sqlalchemy import orm

class ProductSchema(BaseModel):
    description: str
    price:float
    technical_details:str
    image:str
    visible:bool

class ShowProductSchema(ProductSchema):
    id:int
    class Config:
        orm_mode = True
