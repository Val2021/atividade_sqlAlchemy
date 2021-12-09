from fastapi import APIRouter,Depends

from app.repositories.order_repository import OrderRepository
from .schemas import OrderSchema, ShowOrderStatusSchema

router = APIRouter()

from app.services.auth_service import get_customer_user
router = APIRouter(dependencies=[])

@router.post('/')
def create(order: OrderSchema,customer = Depends(get_customer_user)):
    return order

# @router.put('/{id}')
# def update(id:int,orderstatus:OrderSchema,repository: CategoryRepository = Depends()):
#     repository.update(id,category.dict())


@router.get('/')
def index(repository: OrderRepository = Depends()):
    return repository.get_all()

@router.get('/{id}')
def show(id:int,repository: OrderRepository = Depends()):
    return repository.get_by_id(id)