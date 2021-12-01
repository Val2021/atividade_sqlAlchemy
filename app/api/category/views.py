from fastapi import APIRouter, Depends,status
from app.models.models import Category
from .schemas import CategorySchema, ShowCategorySchema
from sqlalchemy.orm import Session
from  typing import List
from app.db.db import get_db

router = APIRouter()

@router.post('/',status_code=status.HTTP_201_CREATED)
def create(category: CategorySchema,db:Session =Depends(get_db)):
    db.add(Category(**category.dict()))
    db.commit()

@router.get('/',response_model=List[ShowCategorySchema])
def index(db:Session =Depends(get_db)):
    return db.query(Category).all()

@router.put('/{id}')
def update(id:int,category:CategorySchema,db:Session =Depends(get_db)):
    query = db.query(Category).filter_by(id=id)
    query.update(category.dict())
    db.commit()

@router.get('/{id}')
def show(id:int, db:Session =Depends(get_db)):
    return db.query(Category).filter_by(id=id).first()
   
