from fastapi import APIRouter, Depends,status
from app.models.models import Supplier
from .schemas import SupplierSchema, ShowSupplierSchema
from app.repositories.supplier_repository import SupplierRepository
from  typing import List


router = APIRouter()

@router.post('/',status_code=status.HTTP_201_CREATED)
def create(supplier: SupplierSchema,repository: SupplierRepository = Depends()):
    repository.create(Supplier(**supplier.dict()))


@router.get('/',response_model=List[ShowSupplierSchema])
def index(repository: SupplierRepository = Depends()):
    return repository.get_all()


@router.put('/{id}')
def update(id:int,supplier:SupplierSchema,repository: SupplierRepository = Depends()):
    repository.update(id,supplier.dict())

@router.get('/{id}')
def show(id:int, repository: SupplierRepository = Depends()):
    return repository.get_by_id(id)