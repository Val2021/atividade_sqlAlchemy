from pydantic import BaseModel
from sqlalchemy import orm

class SupplierSchema(BaseModel):
    name: str
    

class ShowSupplierSchema(SupplierSchema):
    id:int
    class Config:
        orm_mode = True
