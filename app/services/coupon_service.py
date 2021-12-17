from fastapi import  Depends,status,HTTPException
from app.models.models import  Coupon
from app.repositories.coupon_repository import CouponRepository
from app.api.coupon.schemas import CouponSchema


class CouponService:

    def __init__(self,coupon_repository: CouponRepository= Depends()) -> None:
        self.coupon_repository = coupon_repository


    def create_coupon(self, coupon:CouponSchema):
        if self.coupon_repository.has_coupon(coupon.code):
             raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Esse Código ja existe")
        return self.coupon_repository.create(Coupon(**coupon.dict()))
    
   
