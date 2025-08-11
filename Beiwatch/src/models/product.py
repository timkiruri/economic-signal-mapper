from sqlalchemy import Column, Integer, String,ForeignKey
from sqlalchemy.orm import relationship
from src.database.db import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

 
   

    category_id = Column(Integer, ForeignKey("categories.id"))  
    category = relationship("Category", back_populates="products")  

    prices = relationship("Price", back_populates="product")