from pydantic import BaseModel

class CustomerSchema(BaseModel):
    
    first_name :str
    last_name :str
    phone_number : str
    genre : str
    document_id :str
    birth_date :str
    user_id :int

class ShowCustomerSchema(CustomerSchema):
    id: int
    class Config:
        orm_mode = True