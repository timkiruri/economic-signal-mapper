from sqlalchemy.orm import Session
from typing import List
from src.models.product import Product

def get_all_products(db: Session) -> List[Product]:
    return db.query(Product).all()
