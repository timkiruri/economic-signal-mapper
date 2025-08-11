# src/database/create_tables.py

from sqlalchemy import create_engine
from models import Base  

# Same DB location used by your app
engine = create_engine("sqlite:///economic_data.db")  

Base.metadata.create_all(bind=engine)
print("Tables created successfully!")
