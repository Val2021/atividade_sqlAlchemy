from fastapi import APIRouter, Depends,status
from app.models.models import Address
from app.services.address_service import AddressService
from .schemas import AddressSchema, ShowAddressSchema
from app.repositories.address_repository import AddressRepository
from fastapi.exceptions import HTTPException
from  typing import List

from app.services.auth_service import get_user, only_admin
router = APIRouter(dependencies=[Depends(only_admin)])



@router.post('/',status_code=status.HTTP_201_CREATED)
def create(address: AddressSchema,service: AddressService = Depends(),repository: AddressRepository = Depends()):
    service.validate_address(address)
    repository.create(Address(**address.dict()))

@router.get('/',response_model=List[ShowAddressSchema])
def index(repository: AddressRepository = Depends()):
    return repository.get_all()


@router.put('/{id}')
def update(id:int,address:AddressSchema,repository: AddressRepository = Depends(),service: AddressService = Depends()):
    service.validate_address(address)
    repository.update(id,address.dict())

@router.get('/{id}')
def show(id:int, repository: AddressRepository = Depends()):
    return repository.get_by_id(id)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_address(id: int,repository: AddressRepository = Depends()):
    result=repository.remove(id)
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail = f'Endereço com o id:{id} não encontrado')