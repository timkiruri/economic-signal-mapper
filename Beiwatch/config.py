import os
from typing import Optional

class Settings:
    """Application settings"""
    
    # Database
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./economic_data.db")
    
    # API
    API_TITLE: str = "Price Tracking API"
    API_VERSION: str = "1.0.0"
    API_DESCRIPTION: str = "API for tracking and forecasting product prices across retailers"
    
    # CORS
    ALLOWED_ORIGINS: list = [
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:3001",
    ]
    
    # ML Model paths
    MODEL_PATH: str = os.getenv("MODEL_PATH", "src/models/product_price_lstm.h5")
    SCALER_PATH: str = os.getenv("SCALER_PATH", "MODEL/price_scaler.save")
    
    # Forecasting
    MIN_FORECAST_DATA_POINTS: int = 30
    MAX_FORECAST_DATA_POINTS: int = 60

