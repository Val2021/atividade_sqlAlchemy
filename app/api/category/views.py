from fastapi import APIRouter, Depends,status
from app.models.models import Category
from .schemas import CategorySchema, ShowCategorySchema
from app.repositories.category_repository import CategoryRepository
from  typing import List


router = APIRouter()

@router.post('/',status_code=status.HTTP_201_CREATED)
def create(category: CategorySchema, repository: CategoryRepository = Depends()):
    repository.create(Category(**category.dict()))
    

@router.get('/',response_model=List[ShowCategorySchema])
def index(repository: CategoryRepository = Depends()):
    return repository.get_all()

@router.put('/{id}')
def update(id:int,category:CategorySchema,repository: CategoryRepository = Depends()):
    repository.update(id,category.dict())

@router.get('/{id}')
def show(id:int, repository: CategoryRepository = Depends()):
    return repository.get_by_id(id)
