import numpy as np
from tensorflow.keras.models import load_model
import joblib

# Load model and scaler ONCE globally
model = load_model("src/models/product_price_lstm.h5")
scaler = joblib.load("MODEL/price_scaler.save")

def make_forecast(input_data):
    """
    input_data: List of raw price values (not normalized).
    Returns: Predicted price (denormalized).
    """
    normalized_input = scaler.transform(np.array(input_data).reshape(-1, 1))
    input_array = normalized_input.reshape((1, len(normalized_input), 1))
    prediction = model.predict(input_array)
    denormalized_price = scaler.inverse_transform([[prediction[0][0]]])[0][0]
    return round(float(denormalized_price), 2)
