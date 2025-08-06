from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.database.db import Base

class Retailer(Base):
    __tablename__ = "retailers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    prices = relationship("Price", back_populates="retailer")

