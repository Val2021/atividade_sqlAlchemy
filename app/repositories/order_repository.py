from fastapi.param_functions import Depends
from app.models.models import Base
from app.db.db import get_db
from app.models.models import Order, OrderProduct,OrderStatus
from .base_repository import BaseRepository
from sqlalchemy.orm import Session
import random


class OrderRepository(BaseRepository):
    def __init__(self, session: Session = Depends(get_db)):
        super().__init__(session, Order)
    
    def create_order_product(self, OrderProduct: Base):
        self.session.add(OrderProduct)
        self.session.commit()
    
    def create_status_order(self, OrderStatus: Base):
        self.session.add(OrderStatus)
        self.session.commit()


    def update_status_order(self, id: int, attributes: dict):
        self.session.query(OrderStatus).filter_by(id=id).update(attributes)
        self.session.commit()
