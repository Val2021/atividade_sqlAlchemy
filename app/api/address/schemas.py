from pydantic import BaseModel

class AddressSchema(BaseModel):
    
    address: str
    city:str
    state:str
    number:str
    zipcode:str
    neighbourhood:str
    primary:bool
    customer_id:int

class ShowAddressSchema(AddressSchema):

    id: int
    class Config: #para conseguir fazer um cast de objetos de sqlalchemy para objetos de pydantic
        orm_mode = True
