from datetime import datetime
from fastapi import APIRouter,Depends,status
from app.models.models import OrderStatus

from app.repositories.order_repository import OrderRepository
from app.services.order_service import OrderService
from .schemas import OrderSchema, OrderStatusSchema, ShowOrderStatusSchema

# router = APIRouter()

# from app.services.auth_service import get_customer_user
# router = APIRouter(dependencies=[])

from app.services.auth_service import get_user, only_admin,get_customer_user
router = APIRouter(dependencies=[Depends(get_customer_user)])

# @router.post('/')
# def create(order: OrderSchema,customer = Depends(get_customer_user), service:OrderService = Depends() ):
#     service.create_order(order)

@router.post('/',status_code=status.HTTP_201_CREATED)
def create(order: OrderSchema, service:OrderService = Depends() ):
    return service.create_order(order)

@router.put('/{id}')
def update(id:int, orderstatus:OrderStatusSchema, order_repository:OrderRepository = Depends()): ## ?????? duvida com o id
    # order_repository.create_order_product(orderstatus)
    order_status = orderstatus.dict()
    order_status["order_id"] = id
    order_status['created_at'] =  datetime.now()
    return order_repository.create_status_order(OrderStatus(**order_status))
    


@router.get('/')
def index(repository: OrderRepository = Depends()):
    return repository.get_all()

@router.get('/{id}')
def show(id:int,repository: OrderRepository = Depends()):
    return repository.get_by_id(id)