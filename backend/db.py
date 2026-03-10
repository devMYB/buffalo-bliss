from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

# Use a separate DB for content if preferred, or the same requests.db
# Let's use content.db for consistency with the plan
DB_URL = "sqlite:///./content.db"

engine = create_engine(DB_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
