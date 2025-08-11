import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from src.database.db import SessionLocal


import csv
from datetime import datetime
from sqlalchemy.orm import Session
from pathlib import Path



from src.database.models import Product, Category, Retailer, Price

# Path to the CSV file
BASE_DIR = Path(__file__).resolve().parent.parent
CSV_FILE = os.path.join(BASE_DIR, "scraper", "data", "naivas_cleaned.csv")

# Create a DB session
db: Session = SessionLocal()

# Retailer name for this dataset
retailer_name = "Naivas"

# Get or create the retailer
retailer = db.query(Retailer).filter_by(name=retailer_name).first()
if not retailer:
    retailer = Retailer(name=retailer_name)
    db.add(retailer)
    db.commit()
    db.refresh(retailer)

# Load the CSV
with open(CSV_FILE, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        # Safely extract fields
        product_name = (row.get('product_name') or '').strip()
        category_name = (row.get('category') or '').strip()

        # Skip if product_name or category is missing
        if not product_name or not category_name:
            print(f"Skipping row due to missing product or category: {row}")
            continue

        try:
            price_value = float(row.get('price') or 0)
        except ValueError:
            print(f"Invalid price in row: {row}")
            price_value = 0

        try:
            price_timestamp = datetime.strptime(row.get('date') or '', "%Y-%m-%d")
        except ValueError:
            print(f"Invalid date in row: {row}")
            price_timestamp = datetime.now()

        # Get or create category
        category = db.query(Category).filter_by(name=category_name).first()
        if not category:
            category = Category(name=category_name)
            db.add(category)
            db.commit()
            db.refresh(category)

        # Get or create product
        product = db.query(Product).filter_by(name=product_name, category_id=category.id).first()
        if not product:
            product = Product(name=product_name, category=category)
            db.add(product)
            db.commit()
            db.refresh(product)

        # Check if price already exists
        existing_price = db.query(Price).filter_by(
            product_id=product.id,
            retailer_id=retailer.id,
            timestamp=price_timestamp
        ).first()

        if not existing_price:
            price = Price(
                product_id=product.id,
                retailer_id=retailer.id,
                price=price_value,
                timestamp=price_timestamp
            )
            db.add(price)

    db.commit()

print("✅ Naivas data loaded successfully.")


