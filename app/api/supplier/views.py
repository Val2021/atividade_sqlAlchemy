from fastapi import APIRouter, Depends,status
from app.models.models import Supplier
from .schemas import SupplierSchema, ShowSupplierSchema
from app.repositories.supplier_repository import SupplierRepository
from  typing import List

from app.services.auth_service import get_user, only_admin
# router = APIRouter(dependencies=[Depends(only_admin)])
router = APIRouter(dependencies=[])

@router.post('/',status_code=status.HTTP_201_CREATED)
def create(supplier: SupplierSchema,repository: SupplierRepository = Depends()):
    return repository.create(Supplier(**supplier.dict()))


@router.get('/',response_model=List[ShowSupplierSchema])
def index(repository: SupplierRepository = Depends()):
    return repository.get_all()


@router.put('/{id}')
def update(id:int,supplier:SupplierSchema,repository: SupplierRepository = Depends()):
    return repository.update(id,supplier.dict())

@router.get('/{id}')
def show(id:int, repository: SupplierRepository = Depends()):
    return repository.get_by_id(id)