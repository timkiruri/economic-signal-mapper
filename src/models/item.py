# Importing necessary libraries
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base



class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'))

    category = relationship("Category", back_populates="items")
    prices = relationship("Price", back_populates="item")
    

    