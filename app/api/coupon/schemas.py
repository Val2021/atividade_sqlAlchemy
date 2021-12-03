from datetime import  datetime
from enum import Enum
from pydantic import BaseModel

class CouponTypeMode(str,Enum):
    VALUE = 'value'
    PERCENTAGEM = 'percentage'


class UpdateCouponSchema(BaseModel):
      expire_at: datetime
      limit: int
      
class CouponSchema(UpdateCouponSchema):
    code : str
    type:CouponTypeMode
    value:float
    

class ShowCouponSchema(CouponSchema):
    id:int
    class Config:
        orm_mode = True