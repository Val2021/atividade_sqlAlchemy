from fastapi import APIRouter, Depends,status
from app.models.models import PaymentMethod
from .schemas import PaymentMethodSchema, ShowPaymentMethodSchema
from sqlalchemy.orm import Session
from  typing import List
from app.db.db import get_db

router = APIRouter()

@router.post('/',status_code=status.HTTP_201_CREATED)
def create(payment_method:PaymentMethodSchema,db:Session =Depends(get_db)):
    db.add(PaymentMethod(**payment_method.dict()))
    db.commit()

@router.get('/',response_model=List[ShowPaymentMethodSchema])
def index(db:Session =Depends(get_db)):
    return db.query(PaymentMethod).all()

@router.put('/{id}')
def update(id:int,payment_method:PaymentMethodSchema,db:Session =Depends(get_db)):
    query = db.query(PaymentMethod).filter_by(id=id)
    query.update(payment_method.dict())
    db.commit()


@router.get('/{id}')
def show(id:int, db:Session =Depends(get_db)):
    return db.query(PaymentMethod).filter_by(id=id).first()