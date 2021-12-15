
from fastapi import  Depends,status,HTTPException
from app.models.models import  ProductDiscount
from app.repositories.payment_method_repository import PaymentMethodRepository
from app.repositories.product_discount_repository import ProductDiscountRepository
from app.api.product_discount.schemas import ProductDiscountSchema




class ProductDiscountService:
    def __init__(self, payment_method_repository: PaymentMethodRepository = Depends(),
                 product_discount_repository: ProductDiscountRepository = Depends()):
        self.payment_method_repository = payment_method_repository
        self.product_discount_repository = product_discount_repository
        
    def create_discount(self, discount: ProductDiscountSchema):
        if not self.payment_method_repository.is_enabled(discount.payment_method_id):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Não poderá ser criado o desconto para essa forma de pagamento")

        if  self.product_discount_repository.have_discount(discount.product_id,discount.payment_method_id):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Ja existe um desconto para essa forma de pagamento")
        
        return self.product_discount_repository.create(ProductDiscount(**discount.dict()))



    
        
            
        
        
            



