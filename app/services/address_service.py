from fastapi import  Depends,status,HTTPException
from app.models.models import  Address
from app.repositories.customer_repository import CustomerRepository
from app.repositories.address_repository import AddressRepository
from app.api.address.schemas import AddressSchema




class AddressService:
    def __init__(self, customer_repository: CustomerRepository = Depends(),
                 address_repository: AddressRepository= Depends()):
        self.customer_repository = customer_repository 
        self. address_repository = address_repository

    def create_address(self, address: AddressSchema):
        if address.primary == True:
            customer_address = self.address_repository.has_customer_id(address.customer_id)
            if customer_address:
                self.address_repository.update(customer_address.id,{"primary":False})

        self.address_repository.create(Address(**address.dict()))