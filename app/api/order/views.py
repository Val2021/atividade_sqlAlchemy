from fastapi import APIRouter,Depends

from app.repositories.order_repository import OrderRepository
from app.services.order_service import OrderService
from .schemas import OrderSchema, OrderStatusSchema, ShowOrderStatusSchema

router = APIRouter()

from app.services.auth_service import get_customer_user
router = APIRouter(dependencies=[])

# @router.post('/')
# def create(order: OrderSchema,customer = Depends(get_customer_user), service:OrderService = Depends() ):
#     service.create_order(order)

@router.post('/')
def create(order: OrderSchema, service:OrderService = Depends() ):
    service.create_order(order)

@router.put('/{id}')
def update(id:int, orderstatus:OrderStatusSchema, order_repository:OrderRepository = Depends()):
    order_repository.create_order_product(id, orderstatus.dict())
    


@router.get('/')
def index(repository: OrderRepository = Depends()):
    return repository.get_all()

@router.get('/{id}')
def show(id:int,repository: OrderRepository = Depends()):
    return repository.get_by_id(id)