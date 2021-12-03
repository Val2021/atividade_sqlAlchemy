
from fastapi import  Depends,status,HTTPException
from app.models.models import PaymentMethod, ProductDiscount
from app.repositories.payment_method_repository import PaymentMethodRepository
from app.repositories.product_discount_repository import ProductDiscountRepository
from app.api.product_discount.schemas import ProductDiscountSchema




class ProductDiscountService:
    def __init__(self, payment_method_repository: PaymentMethodRepository = Depends(),
                 product_discount_repository: ProductDiscountRepository = Depends()):
        self.payment_method_repository = payment_method_repository
        self.product_discount_repository = product_discount_repository
        
    def create_discount(self, discount: ProductDiscountSchema):
        query1 =  payment_method_repository( id=discount.payment_method_id, enabled=True).first( )
        print("query1",query1)
        if not query1:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Não poderá ser criado o desconto para essa forma de pagamento")
    
        query = self.product_discount_repository(product_id = discount.product_id, payment_method_id=discount.payment_method_id).first()
        print("query",query)
        if  query:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Ja existe um desconto para essa forma de pagamento")
        
        else:
            self.product_discount_repository.create(ProductDiscount(**discount.dict()))
            



