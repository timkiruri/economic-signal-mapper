from src.database.db import get_db
from src.database.models.price import Price

db = next(get_db())

prices = db.query(Price).limit(5).all()
for price in prices:
    print(f"Price ID: {price.id}, Value: {price.value}")

