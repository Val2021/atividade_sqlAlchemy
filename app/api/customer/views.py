from fastapi import APIRouter, Depends,status
from app.models.models import Customer
from .schemas import CustomerSchema, ShowCustomerSchema, UpdateCustomerSchema
from app.repositories.customer_repository import CustomerRepository
from  typing import List

from app.services.auth_service import get_user, only_admin
router = APIRouter(dependencies=[Depends(only_admin)])

@router.post('/',status_code=status.HTTP_201_CREATED)
def create(customer: CustomerSchema,repository: CustomerRepository = Depends()):
    repository.create(Customer(**customer.dict()))


@router.get('/',response_model=List[ShowCustomerSchema])
def index(repository: CustomerRepository = Depends()):
    return repository.get_all()


@router.put('/{id}')
def update(id:int,customer:UpdateCustomerSchema,repository: CustomerRepository = Depends()):
    repository.update(id,customer.dict())

@router.get('/{id}')
def show(id:int, repository: CustomerRepository = Depends()):
    return repository.get_by_id(id)