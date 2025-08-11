from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from src.database.db import get_db
from src.database.repositories.retailer_repository import get_all_retailers
from src.models.schema import RetailerResponse

router = APIRouter()

@router.get("/", response_model=List[RetailerResponse])
def read_retailers(db: Session = Depends(get_db)):
    return get_all_retailers(db)


