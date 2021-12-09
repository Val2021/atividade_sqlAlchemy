from datetime import datetime
from fastapi import  Depends,status,HTTPException
from app.api.customer.schemas import CustomerUserSchema
from app.api.order.schemas import OrderSchema, ProductSchema
from app.models.models import Order, OrderProduct
from app.repositories.customer_repository import CustomerRepository
from app.repositories.order_repository import OrderRepository
from app.repositories.product_discount_repository import ProductDiscountRepository
from app.repositories.product_repository import ProductRepository
from app.repositories.user_repository import UserRepository
from app.repositories.coupon_repository import CouponRepository
import random


class OrderService:
    def __init__(self, order_repository: OrderRepository = Depends(), product_repository: ProductRepository = Depends(), product_discount:ProductDiscountRepository = Depends(),coupon_discount:CouponRepository = Depends()):
                self.order_repository = order_repository
                self.product_repository = product_repository
                self.product_discount = product_discount
                self.coupon_discount = coupon_discount
                

    def create_order(self, order:OrderSchema):
        total_value = 0
        if not order.coupon_code:
            if len(order.products)==1:
               discount = self.product_discount.have_discount(order.products[0].id,order.payment_method_id)
               if discount:
                    if  discount.mode == "percentage":
                        total_discount = order.products[0] * discount.value
                    if  discount.mode == "value":
                        total_discount =  discount.value
        else:
            coupon = self.coupon_discount.has_coupon(order.coupon_code)
            if coupon.limit == 0 and coupon.expire_at > datetime.now():
               raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Esse coupon ja atigiu sua cota de uso ou ja expirou")
            total_discount = coupon.value
            self.coupon_discount.update(coupon.id,{"limit":coupon.limit - 1})
        list_order_product = []
        for product in order.products:
            total_value += product.quantity * self.product_repository.get_by_id(product.id).price
            list_order_product.append({"product_id":product.id,"quantity":product.quantity})
        result = random.sample(range(0,100), 4)
        order_data = order.dict()
        order_data.update({"number":result, "status":"ORDER PLACED","total_value":total_value,"total_discount":total_discount})
        order_id = self.order_repository.create(Order(**order_data)) 
        for product in list_order_product:
            product["order_id"]=order_id
            self.order_repository.create_order_product(OrderProduct(**product))
        
