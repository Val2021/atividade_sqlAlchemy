from fastapi import  Depends
from app.models.models import Customer
from app.repositories.user_repository import  UserRepository
from app.repositories.customer_repository import  CustomerRepository
from app.api.customer.schemas import CreateCustomerSchema
from app.services.user_service import UserService



class CustomerService:
    def __init__(self, user_repository:   UserRepository = Depends(), customer_repository:CustomerRepository = Depends(),user_service: UserService = Depends() ):
        self.user_repository = user_repository
        self.customer_repository = customer_repository
        self.user_service = user_service
    
    def create_customer(self, customer:CreateCustomerSchema ):
        user_id = self.user_service.create_customer_user(customer.user)
        
        customer_data = customer.dict()
        del customer_data["user"]
        customer_data.update({"user_id": user_id})
        
        self.customer_repository.create(Customer(**customer_data))
        
        
        