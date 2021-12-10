from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel
from enum import Enum

class OrderStatusType(str,Enum):
    ORDER_PLACED = 'ORDER PLACED'
    ORDED_PAID =  'ORDED PAID'
    ORDER_SHIPPED =  'ORDER SHIPPED'
    ORDER_RECEIVED= 'ORDER RECEIVED'
    ORDER_COMPLETED ='ORDER COMPLETED'
    ORDER_CANCELLED = 'ORDER CANCELLED'

class ProductSchema(BaseModel):
    id: int
    quantity: int


class OrderSchema(BaseModel):
    address_id: int
    payment_method_id: int
    coupon_code: Optional[str] = None
    products: List[ProductSchema]

class OrderStatusSchema(BaseModel):
    status:OrderStatusType

class ShowOrderStatusSchema(OrderStatusSchema):
    order_id:int
    created_at: datetime
    class Config:
        orm_mode = True
    