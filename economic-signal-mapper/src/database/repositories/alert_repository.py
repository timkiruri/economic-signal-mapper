from sqlalchemy.orm import Session
from src.models.alert import Alert
from src.models.item import Item
from src.models.store import Store

def get_all_alerts(db: Session):
    alerts = db.query(Alert).all()
    return alerts
    

