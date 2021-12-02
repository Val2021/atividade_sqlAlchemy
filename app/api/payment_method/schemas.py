from pydantic import BaseModel
from sqlalchemy import orm

class PaymentMethodSchema(BaseModel):
    name:str
    enabled:bool

class ShowPaymentMethodSchema(PaymentMethodSchema):
    id:int
    class Config:
        orm_mode = True
