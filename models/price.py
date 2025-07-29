from sqlalchemy import Column, Integer, DateTime, ForeignKey, Numeric, Enum
from sqlalchemy.orm import relationship
from models.base import Base
from models.enums import DataQualityEnum

class Price(Base):
    __tablename__ = 'prices'

    id = Column(Integer, primary_key=True)
    item_id = Column(Integer, ForeignKey('items.id'))
    store_id = Column(Integer, ForeignKey('stores.id'))
    value = Column(Numeric(10, 2), nullable=False)
    date = Column(DateTime, nullable=False)
    data_quality = Column(Enum(DataQualityEnum), default=DataQualityEnum.GOOD)

    item = relationship("Item", back_populates="prices")
    store = relationship("Store", back_populates="prices")
    