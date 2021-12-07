
from fastapi.exceptions import HTTPException
from fastapi import APIRouter, Depends,status
from app.services.user_service import UserService
from .schemas import UserSchema
from app.models.models import User
from app.repositories.user_repository import UserRepository
import bcrypt

from app.services.auth_service import get_user, only_admin
router = APIRouter(dependencies=[])

@router.post('/')
def create(user: UserSchema, service: UserService = Depends()): ### esta dando pau
    service.create_user(user.email,user)
    # user.password = bcrypt.hashpw(
    #     user.password.encode('utf8'), bcrypt.gensalt()) #colocar no serviço 
    

@router.get('/')
def index(repository: UserRepository = Depends()):
    return repository.get_all()


@router.put('/{id}')
def update(id:int,user:UserSchema,service: UserService = Depends()):
    service.update_user(id,user)
    


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id: int,repository: UserRepository = Depends()):
    result=repository.delete(id)
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail = f'O usuário com :{id} não encontrado')