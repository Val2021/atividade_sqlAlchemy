
# from sqlalchemy import Column, Float, Integer, String, create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import relationship, sessionmaker
# from sqlalchemy.sql.schema import ForeignKey


# engine = create_engine("sqlite:///test.db", echo=True)
# Session = sessionmaker(bind=engine)
# session = Session()

# Base = declarative_base()

# class Category(Base):
#     __tablename__ = "category"
#     id = Column(Integer, primary_key=True)
#     name = Column(String(50))
#     description =  Column(String())
#     profitability = Column(Float)
    

# def __repr__(self) -> str:
#      return f"Category(name={self.name})"

# class Product(Base):
#     __tablename__ = "product"
#     id = Column(Integer, primary_key=True)
#     description = Column(String(200))
#     price = Column(Float)
#     category_id = Column(Integer, ForeignKey(Category.id)) ##Ver
#     category = relationship("Category", backref="category")

# def __repr__(self) -> str:
#      return f"Product(name={self.name})"

# Base.metadata.create_all(engine) ## Ver

# c1 = Category(description = "Viagem", profitability = "20")
# c2 = Category(description = "Esporte", profitability = "15")
# p1 = Product(description="Bola",price = "30",category=c1 )
# p2 = Product(description="Google Pro",price = "1600",category=c2 )

# session.add_all([c1,c2,p1,p2])

# session.commit()
