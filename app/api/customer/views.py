from fastapi import APIRouter, Depends,status
from app.models.models import Customer
from app.services.customer_service import CustomerService
from app.services.user_service import UserService
from .schemas import CreateCustomerSchema, ShowCustomerSchema, UpdateCustomerSchema
from app.repositories.customer_repository import CustomerRepository
from  typing import List

from app.services.auth_service import get_user, only_admin
router = APIRouter(dependencies=[])

@router.post('/',status_code=status.HTTP_201_CREATED)
def create(customer:CreateCustomerSchema,customer_service:CustomerService = Depends(),userservice: UserService = Depends(),repository: CustomerRepository = Depends()):
    user_id = userservice.create_customer_user(customer.user)
    new_customer = customer_service.replace_user(customer,user_id)
    return repository.create(Customer(**new_customer))
    
    


@router.get('/',response_model=List[ShowCustomerSchema])
def index(repository: CustomerRepository = Depends()):
    return repository.get_all()


@router.put('/{id}')
def update(id:int,customer:UpdateCustomerSchema, userservice: UserService = Depends(), repository: CustomerRepository = Depends(),customer_service:CustomerService = Depends()):
    user_id = userservice.update_user(customer.user)
    customer_updated = customer_service.replace_user(user_id)
    repository.update(id,customer_updated)

@router.get('/{id}')
def show(id:int, repository: CustomerRepository = Depends()):
    return repository.get_by_id(id)