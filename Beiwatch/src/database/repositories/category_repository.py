from sqlalchemy.orm import Session
from typing import List
from src.models.category import Category

def get_all_categories(db: Session) -> List[Category]:
    return db.query(Category).all()
