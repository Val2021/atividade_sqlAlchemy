from fastapi import APIRouter, Depends,status,HTTPException
from app.api.payment_method.schemas import PaymentMethodSchema
from app.models.models import PaymentMethod, ProductDiscount
from app.repositories.payment_method_repository import PaymentMethodRepository
from app.repositories.product_discount_repository import ProductDiscountRepository
from app.services.product_discount_service import ProductDiscountService
from .schemas import ShowProductDiscountSchema, ProductDiscountSchema
from sqlalchemy.orm import Session
from  typing import List

router = APIRouter()


# def check_payment_method(product_discount: ProductDiscountSchema,db:Session =Depends(get_db)):



@router.post('/',status_code=status.HTTP_201_CREATED)
def create(product_discount: ProductDiscountSchema, service:ProductDiscountService = Depends()):
    service.create_discount(product_discount.product_id,product_discount.payment_method_id)
   
    
@router.get('/',response_model=List[ShowProductDiscountSchema])
def index(repository: ProductDiscountRepository = Depends()):
    return repository.get_all()

@router.put('/{id}')
def update(id:int,product_discount:ProductDiscountSchema,repository: ProductDiscountRepository = Depends()):
    repository.update(id,product_discount.dict())


@router.get('/{id}')
def show(id:int, repository: ProductDiscountRepository = Depends()):
    return repository.get_by_id(id)