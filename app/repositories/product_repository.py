from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.db import get_db
from app.models.models import Product
from .base_repository import BaseRepository


class ProductRepository(BaseRepository):
    def __init__(self, session: Session = Depends(get_db)):
        super().__init__(session, Product)
    

    def get_productprice_id(self, id):
        query = self.session.query(self.model).filter_by(id=id).first()
        return query 


