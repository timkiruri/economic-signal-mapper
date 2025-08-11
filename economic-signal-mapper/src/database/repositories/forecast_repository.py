
import numpy as np
from tensorflow.keras.models import load_model
import joblib
from sqlalchemy.orm import Session
from src.models.price import Price
from datetime import datetime, timedelta

# Load the model once
model = load_model("src/models/product_price_lstm.h5")
scaler = joblib.load("MODEL/price_scaler.save")

def make_forecast(input_data):
    """
    input_data: List of raw price values (not normalized).
    Returns: Predicted price (denormalized).
    """
    # Normalize input using saved scaler
    normalized_input = scaler.transform(np.array(input_data).reshape(-1, 1))
    input_array = normalized_input.reshape((1, len(normalized_input), 1))

    # Predict
    prediction = model.predict(input_array)

    # Denormalize output
    denormalized_price = scaler.inverse_transform([[prediction[0][0]]])[0][0]
    return round(float(denormalized_price), 2)

from sqlalchemy.orm import Session
from src.models.price import Price
from datetime import datetime, timedelta

def get_historical_prices(db: Session, product_id: int, store_id: int, days: int = 30):
    start_date = datetime.utcnow() - timedelta(days=days)
    prices = (
        db.query(Price)
        .filter(
            Price.item_id == product_id,
            Price.store_id == store_id,
            Price.created_at >= start_date
        )
        .order_by(Price.created_at.asc())
        .all()
    )
    return [float(price.value) for price in prices]




