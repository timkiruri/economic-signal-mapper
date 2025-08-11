# src/models/category.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.database.db import Base

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    products = relationship("Product", back_populates="category")


