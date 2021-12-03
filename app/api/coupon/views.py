from fastapi import APIRouter, Depends,status
from app.models.models import Coupon
from .schemas import CouponSchema,ShowCouponSchema
from fastapi.exceptions import HTTPException
from app.repositories.coupon_repository import CouponRepository
from  typing import List


router = APIRouter()

@router.post('/',status_code=status.HTTP_201_CREATED)
def create(coupon:CouponSchema,repository: CouponRepository = Depends()):
    repository.create(Coupon(**coupon.dict()))

@router.get('/',response_model=List[ShowCouponSchema])
def index(repository: CouponRepository = Depends()):
    return repository.get_all()

@router.put('/{id}')
def update(id:int,coupon:CouponSchema,repository: CouponRepository = Depends()):
     repository.update(id,coupon.dict())

@router.get('/{id}')
def show(id:int, repository: CouponRepository = Depends()):
    return repository.get_by_id(id)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_coupon(id: int,repository: CouponRepository = Depends()):
    result=repository.delete(id)
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail = f'Coupon com o id:{id} não encontrado')
    
    