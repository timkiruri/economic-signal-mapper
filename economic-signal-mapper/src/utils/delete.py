# clean_quickmart_data.py

from src.database.db import SessionLocal
from src.database.models import Retailer, Price, Product
from sqlalchemy.orm import Session

db: Session = SessionLocal()

retailer_name = "Quickmart"  # or "Naivas", etc.

# Get the retailer
retailer = db.query(Retailer).filter_by(name=retailer_name).first()

if retailer:
    # Delete all prices linked to this retailer
    prices = db.query(Price).filter_by(retailer_id=retailer.id).all()
    for price in prices:
        db.delete(price)

    db.commit()
    print(f"✅ Deleted {len(prices)} price records for {retailer_name}.")

else:
    print(f"❌ Retailer '{retailer_name}' not found.")
