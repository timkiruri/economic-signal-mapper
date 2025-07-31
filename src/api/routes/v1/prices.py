from fastapi import APIRouter, Query
from typing import List, Optional
from datetime import datetime
from src.models.schema import PriceResponse
from fastapi import Depends
from src.database.database import get_db
from sqlalchemy.orm import Session

from src.database.repositories.price_repository import (
    get_current_prices
)

router = APIRouter(
    prefix="/api/v1/prices",
    tags=["Prices"]
)

@router.get("/current", response_model=List[PriceResponse])
async def get_current_prices_route(
    item_name: Optional[str] = Query(None),
    region: Optional[str] = Query(None),
    store: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    """
    Gets the latest prices for items. filtered by item_name, region, and store.
    """
    return get_current_prices(item_name, region, store, db)

# @router.get("/historical", response_model=List[PriceResponse])
# async def get_historical_prices_route(
#     item_name: Optional[str] = Query(None),
#     start_date: Optional[datetime]=Query(None),
#     end_date: Optional[datetime]=Query(None)
# ):
#     """
#     Gets the historical prices for items. filtered by item name, start date, or end date.
#     """
#     return get_historical_prices(item_name, start_date, end_date)