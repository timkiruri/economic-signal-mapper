# Importing necessary libraries
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base

class ItemCategory(Base):
    __tablename__ = 'item_categories'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

    items = relationship("Item", back_populates="category")

class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    category_id = Column(Integer, ForeignKey('item_categories.id'))

    category = relationship("ItemCategory", back_populates="items")
    prices = relationship("Price", back_populates="item")