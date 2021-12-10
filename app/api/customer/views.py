from fastapi import APIRouter, Depends,status
from app.models.models import Customer
from app.services.customer_service import CustomerService
from .schemas import CreateCustomerSchema, ShowCustomerSchema, UpdateCustomerSchema
from app.repositories.customer_repository import CustomerRepository
from  typing import List

from app.services.auth_service import get_user, only_admin
router = APIRouter(dependencies=[])

@router.post('/',status_code=status.HTTP_201_CREATED)
def create(customer:CreateCustomerSchema,customer_service:CustomerService = Depends()):
    customer_service.create_customer(customer)
    


@router.get('/',response_model=List[ShowCustomerSchema])
def index(repository: CustomerRepository = Depends()):
    return repository.get_all()


@router.put('/{id}')
def update(id:int,customer:UpdateCustomerSchema,repository: CustomerRepository = Depends()):
    repository.update(id,customer.dict())

@router.get('/{id}')
def show(id:int, repository: CustomerRepository = Depends()):
    return repository.get_by_id(id)