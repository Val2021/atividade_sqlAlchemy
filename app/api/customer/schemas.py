from pydantic import BaseModel




class UpdateCustomerSchema(BaseModel):
    first_name :str
    last_name :str
    phone_number : str
    genre : str
    birth_date :str
    # user_id :int

class CustomerSchema(UpdateCustomerSchema):

    document_id :str
    

class ShowCustomerSchema(CustomerSchema):
    id: int
    class Config:
        orm_mode = True