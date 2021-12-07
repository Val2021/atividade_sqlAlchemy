from datetime import date
from pydantic import BaseModel


class CustomerUserSchema(BaseModel):
    email: str
    password: str

class BaseCustomerSchema(BaseModel):
    first_name :str
    last_name :str
    phone_number : str
    genre : str
    birth_date : date
    user :  CustomerUserSchema



class CreateCustomerSchema(BaseCustomerSchema):
    document_id :str
    
class UpdateCustomerSchema(BaseCustomerSchema):
    pass



class ShowCustomerSchema(BaseModel):
    id: int
    first_name :str
    last_name :str
    phone_number : str
    genre : str
    birth_date : date
    class Config:
        orm_mode = True