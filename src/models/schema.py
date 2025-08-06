from pydantic import BaseModel

class PriceResponse(BaseModel):
    id: int
    item_id: int
    store_id: int
    value: float

    class Config:
        orm_mode = True

class ProductResponse(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class CategoryResponse(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class RetailerResponse(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

