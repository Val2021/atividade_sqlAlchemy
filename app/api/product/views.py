from fastapi import APIRouter, Depends,status
from app.models.models import Product
from .schemas import ProductSchema, ShowProductSchema
from app.repositories.product_repository import ProductRepository
from  typing import List

from app.services.auth_service import get_user, only_admin

router = APIRouter(dependencies=[])


@router.post('/',status_code=status.HTTP_201_CREATED)
def create(product: ProductSchema, repository: ProductRepository = Depends()):
    repository.create(Product(**product.dict()))
   
@router.get('/',response_model=List[ShowProductSchema])
def index(repository: ProductRepository = Depends()):
    return repository.get_all()

@router.put('/{id}')
def update(id:int,product:ProductSchema,repository: ProductRepository = Depends()):
    repository.update(id,product.dict())
    
@router.get('/{id}',response_model=ShowProductSchema) ##ver pq response_model
def show(id:int, repository: ProductRepository = Depends()):
    return repository.get_by_id(id)
   
