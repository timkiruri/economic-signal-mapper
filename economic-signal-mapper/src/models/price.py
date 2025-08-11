from sqlalchemy import Column, Integer, ForeignKey, Numeric, DateTime
from sqlalchemy.orm import relationship
from src.database.db import Base

class Price(Base):
    __tablename__ = "prices"

    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, ForeignKey("products.id"))
    store_id = Column(Integer, ForeignKey("retailers.id"))
    value = Column(Numeric(10, 2))
    date = Column(DateTime)

    # Optional relationships
    product = relationship("Product", back_populates="prices")
    retailer = relationship("Retailer", back_populates="prices")
