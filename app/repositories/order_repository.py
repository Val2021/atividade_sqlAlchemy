from fastapi.param_functions import Depends
from app.db.db import get_db
from app.models.models import Order, OrderProduct
from .base_repository import BaseRepository
from sqlalchemy.orm import Session
import random


class OrderRepository(BaseRepository):
    def __init__(self, session: Session = Depends(get_db)):
        super().__init__(session, Order)
    
    def create_order_product(self):
        self.session.add(OrderProduct)
        self.session.commit()
