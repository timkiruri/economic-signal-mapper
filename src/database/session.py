from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# You can change this to PostgreSQL, MySQL, etc later
DATABASE_URL = "sqlite:///economic-signal-mapper.db"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)