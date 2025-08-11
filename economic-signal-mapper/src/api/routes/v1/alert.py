from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from src.models.schema import AlertResponse
from src.database.database import get_db
from src.database.repositories.alert_repository import get_all_alerts

router = APIRouter(
    prefix="/api/v1/alerts",
    tags=["Alerts"]
)

@router.get("/", response_model=List[AlertResponse])
def read_alerts(db: Session = Depends(get_db)):
    return get_all_alerts(db)
