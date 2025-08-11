from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.database.db import get_db
from src.database.repositories.forecast_repository import get_historical_prices
from src.models.forecast_model import make_forecast

router = APIRouter(
    prefix="/api/v1/forecast",
    tags=["Forecast"]
)

@router.get("/")
def forecast_price(product_id: int, store_id: int, db: Session = Depends(get_db)):
    prices = get_historical_prices(db=db, product_id=product_id, store_id=store_id)

    if len(prices) < 30:
        raise HTTPException(status_code=400, detail="Not enough historical data to forecast.")

    forecast = make_forecast(prices)
    return {
        "product_id": product_id,
        "forecast_price": forecast,
        "based_on_last_days": len(prices)
    }




