from sqlalchemy.orm import Session
from typing import List
from src.models.retailer import Retailer

def get_all_retailers(db: Session) -> List[Retailer]:
    return db.query(Retailer).all()
