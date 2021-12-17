
from typing import Optional

from pydantic import BaseModel
from sqlalchemy import orm
from enum import Enum
#from app.api.product.schemas import ShowProductSchema
#from app.api.payment_method.schemas import ShowPaymentMethodSchema


class DiscountMode(str,Enum):
    VALUE = 'value'
    PERCENTAGEM = 'percentage'

class ProductDiscountSchema(BaseModel):
    mode: DiscountMode
    value: float
    product_id: int
    payment_method_id:int

class ShowProductSchema(BaseModel):
    id: int
    description: str
    price:float
    technical_details:str
    image:str
    visible:bool
    category_id: int
    supplier_id:int

    class Config:
        orm_mode = True

class ShowPaymentMethodSchema(BaseModel):
    name:str
    # enabled:bool
    id: int

    class Config:
        orm_mode = True

class ShowProductDiscountSchema( ProductDiscountSchema):
    id: int
    product:ShowProductSchema
    payment_method:ShowPaymentMethodSchema
    class Config:
        orm_mode = True
