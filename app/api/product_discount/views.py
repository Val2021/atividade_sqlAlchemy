from fastapi import APIRouter, Depends,status,HTTPException
from app.api.payment_method.schemas import PaymentMethodSchema
from app.models.models import PaymentMethod, ProductDiscount
from app.repositories.payment_method_repository import PaymentMethodRepository
from app.repositories.product_discount_repository import ProductDiscountRepository
from app.services.product_discount_service import ProductDiscountService
from .schemas import ShowProductDiscountSchema, ProductDiscountSchema
from sqlalchemy.orm import Session
from  typing import List
from app.db.db import get_db

router = APIRouter()


# def check_payment_method(product_discount: ProductDiscountSchema,db:Session =Depends(get_db)):



@router.post('/',status_code=status.HTTP_201_CREATED)
def create(product_discount: ProductDiscountSchema, repository: ProductDiscountRepository = Depends()):
    
    # query1 = db.query(PaymentMethod).filter_by( id=product_discount.payment_method_id, enabled=True).first( )
    # if not query1:
    #     raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Não poderá ser criado o desconto para essa forma de pagamento")
        
    # query = db.query(ProductDiscount).filter_by(product_id = product_discount.product_id, payment_method_id=product_discount.payment_method_id).first()
    # if  query:
    #     raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Ja existe um desconto para essa forma de pagamento")
            
    # else:
    #     db.add(ProductDiscount(**product_discount.dict()))
    #     db.commit()

@router.get('/',response_model=List[ShowProductDiscountSchema])
def index(repository: ProductDiscountRepository = Depends()):
    return repository.get_all()

@router.put('/{id}')
def update(id:int,product_discount:ProductDiscountSchema,repository: ProductDiscountRepository = Depends()):
    repository.update(id,product_discount.dict())


@router.get('/{id}')
def show(id:int, repository: ProductDiscountRepository = Depends()):
    return repository.get_by_id(id)