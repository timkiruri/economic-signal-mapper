from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from src.database.database import Base

class Alert(Base):
    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, ForeignKey("items.id"))
    store_id = Column(Integer, ForeignKey("stores.id"))
    price_change = Column(Float)
    direction = Column(String)  # 'increase' or 'decrease'
    threshold = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)
    description = Column(String)

    item = relationship("Item")
    store = relationship("Store")
