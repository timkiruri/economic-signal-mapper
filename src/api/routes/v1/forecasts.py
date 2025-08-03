from fastapi import APIRouter
from typing import List
from src.database.repositories.forecast_repository import make_forecast

router = APIRouter(
    prefix="/api/v1/forecast",
    tags=["Forecast"]
)

@router.post("/predict")
async def forecast_price(prices: List[float]):
    """
    Predict the next price using past normalized price list.
    """
    prediction = make_forecast(prices)
    return {"predicted_price": prediction}