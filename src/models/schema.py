from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PriceResponse(BaseModel):
    item_name: str
    price: float
    currency: str
    category: str
    store:str
    region: str
    timestamp: datetime
    source_url: Optional[str]
    data_quality: Optional[float] 
    
"""All Pydantic models inherit from this. It gives validation and auto docs."""
class AlertResponse(BaseModel):
    item_name: str
    store: str
    price_change: float
    direction: str
    threshold: float
    timestamp: datetime
    description: str

    class Config:
        orm_mode = True
