from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.db import get_db
from app.models.models import ProductDiscount
from .base_repository import BaseRepository
from .crud.delete import CRUDDelete

class ProductDiscountRepository(BaseRepository,CRUDDelete):
    def __init__(self, session: Session = Depends(get_db)):
        super().__init__(session, ProductDiscount)

    
    def have_discount(self, product_id,payment_method_id ):
        query = self.session.query(self.model).filter_by(product_id = product_id, payment_method_id=payment_method_id).first()
        return query != None
    #new
    def remove(self, id):
        self.query().filter_by(id=id).delete()

