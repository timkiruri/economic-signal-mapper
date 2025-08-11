from pydantic import BaseModel, ConfigDict
from datetime import datetime

class ProductResponse(BaseModel):
    id: int
    name: str

    model_config = ConfigDict(from_attributes=True)

class RetailerResponse(BaseModel):
    id: int
    name: str

    model_config = ConfigDict(from_attributes=True)

class PriceResponse(BaseModel):
    id: int
    item_id: int
    store_id: int
    value: float
    date: datetime
    product: ProductResponse
    retailer: RetailerResponse

    model_config = ConfigDict(from_attributes=True)

class CategoryResponse(BaseModel):
    id: int
    name: str

    model_config = ConfigDict(from_attributes=True)




