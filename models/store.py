from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base

class Store(Base):
    __tablename__ = 'stores'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    location = relationship("StoreLocation", uselist=False, back_populates="store")
    prices = relationship("Price", back_populates="store")

class StoreLocation(Base):
    __tablename__ = 'store_locations'

    id = Column(Integer, primary_key=True)
    store_id = Column(Integer, ForeignKey('stores.id'))
    location_name = Column(String, nullable=False)

    store = relationship("Store", back_populates="location")