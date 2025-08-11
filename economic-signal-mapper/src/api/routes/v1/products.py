from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from src.database.db import get_db
from src.database.repositories.product_repository import get_all_products
from src.models.schema import ProductResponse

router = APIRouter()

@router.get("/", response_model=List[ProductResponse])
def read_products(db: Session = Depends(get_db)):
    return get_all_products(db)


