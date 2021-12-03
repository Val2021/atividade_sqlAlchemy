from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Boolean, DateTime, Float, Integer, String
from app.db.db import Base
from sqlalchemy import Column


    

class Supplier(Base):

    __tablename__='suppliers'

    id = Column(Integer, primary_key=True)
    name = Column(String(45))
    

class Category(Base):

    __tablename__='categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(45))

class PaymentMethod(Base):

    __tablename__='payment_methods'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(45))
    enabled = Column(Boolean, default=True)

class Product(Base):

    __tablename__='products'
    
    id = Column(Integer, primary_key=True)
    description = Column(String(150))
    price = Column(Float(10,2))
    technical_details = Column(String(255))
    image = Column(String(255))
    visible = Column(Boolean, default=True)
    category_id = Column(Integer,ForeignKey('categories.id'))
    category = relationship(Category)
    supplier_id = Column(Integer,ForeignKey('suppliers.id'))
    supplier = relationship(Supplier)

class ProductDiscount(Base):

    __tablename__='product_discounts'
    
    id = Column(Integer, primary_key=True)
    mode = Column(String(45))
    value = Column(Float(10,2))
    product_id = Column(Integer,ForeignKey('products.id'))
    product = relationship(Product)
    payment_method_id = Column(Integer,ForeignKey('payment_methods.id'))
    payment_method = relationship(PaymentMethod)


class Coupon(Base):

    __tablename__='coupons'
    
    id = Column(Integer, primary_key=True)
    code = Column(String(10))
    expire_at = Column(DateTime())
    limit = Column(Integer())
    type = Column(String(15))
    value = Column(Float(10,2))
    
    

    

    