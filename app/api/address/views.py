from fastapi import APIRouter, Depends,status
from app.models.models import Address
from app.services.address_service import AddressService
from .schemas import AddressSchema, ShowAddressSchema
from app.repositories.address_repository import AddressRepository
from fastapi.exceptions import HTTPException
from  typing import List


router = APIRouter()

@router.post('/',status_code=status.HTTP_201_CREATED)
def create(address: AddressSchema,service: AddressService = Depends()):
    service.create_address(address)


@router.get('/',response_model=List[ShowAddressSchema])
def index(repository: AddressRepository = Depends()):
    return repository.get_all()


@router.put('/{id}')
def update(id:int,address:AddressSchema,repository: AddressRepository = Depends()):
    repository.update(id,address.dict())

@router.get('/{id}')
def show(id:int, repository: AddressRepository = Depends()):
    return repository.get_by_id(id)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_coupon(id: int,repository: AddressRepository = Depends()):
    result=repository.delete(id)
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail = f'Endereço com o id:{id} não encontrado')