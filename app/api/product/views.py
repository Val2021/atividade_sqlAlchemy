from fastapi import APIRouter, Depends,status
from starlette.routing import Route

from app.models.models import Product
from .schemas import ProductSchema, ShowProductSchema
from sqlalchemy.orm import Session
from  typing import List
from app.db.db import get_db

router = APIRouter()

@router.post('/',status_code=status.HTTP_201_CREATED)
def create(product: ProductSchema,db:Session =Depends(get_db)):
    db.add(Product(**product.dict()))
    db.commit()
   

@router.get('/',response_model=List[ShowProductSchema])
def index(db:Session =Depends(get_db)):
    return db.query(Product).all()

@router.put('/{id}')
def update(id:int,product:ProductSchema,db:Session =Depends(get_db)):
    query = db.query(Product).filter_by(id=id)
    query.update(product.dict())
    db.commit()


@router.get('/{id}')
def show(id:int, db:Session =Depends(get_db)):
    return db.query(Product).filter_by(id=id).first()
   
