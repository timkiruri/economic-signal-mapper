from sqlalchemy.orm import Session
from typing import List
from src.models.price import Price

def get_all_prices(db: Session) -> List[Price]:
    return db.query(Price).all()


