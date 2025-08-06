from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from src.database.db import get_db
from src.database.repositories.price_repository import get_all_prices
from src.models.schema import PriceResponse

router = APIRouter()

@router.get("/", response_model=List[PriceResponse])
def read_prices(db: Session = Depends(get_db)):
    return get_all_prices(db)
