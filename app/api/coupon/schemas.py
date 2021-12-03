from datetime import  datetime
from pydantic import BaseModel



class CouponSchema(BaseModel):
    code :str
    expire_at: datetime
    limit: int
    type:str
    value:float
    

class ShowCouponSchema(CouponSchema):
    id:int
    class Config:
        orm_mode = True