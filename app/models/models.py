from sqlalchemy.sql.sqltypes import Boolean, Float, Integer, String
from app.db.db import Base
from sqlalchemy import Column

class Product(Base):

    __tablename__='products'
    
    id = Column(Integer, primary_key=True)
    description = Column(String(150))
    price = Column(Float(10,2))
    technical_details = Column(String(255))
    image = Column(String(255))
    visible = Column(Boolean, default=True)
    

class Supplier(Base):

    __tablename__='suppliers'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    