from fastapi import APIRouter, Depends,status
from app.models.models import PaymentMethod
from .schemas import PaymentMethodSchema, ShowPaymentMethodSchema
from app.repositories.payment_method_repository import PaymentMethodRepository
from  typing import List


router = APIRouter()

@router.post('/',status_code=status.HTTP_201_CREATED)
def create(payment_method:PaymentMethodSchema,repository: PaymentMethodRepository = Depends()):
    repository.create(PaymentMethod(**payment_method.dict()))

@router.get('/',response_model=List[ShowPaymentMethodSchema])
def index(repository: PaymentMethodRepository = Depends()):
    return repository.get_all()
    

@router.put('/{id}')
def update(id:int,payment_method:PaymentMethodSchema,repository: PaymentMethodRepository = Depends()):
     repository.update(id,payment_method.dict())


@router.get('/{id}')
def show(id:int, repository: PaymentMethodRepository = Depends()):
    return repository.get_by_id(id)