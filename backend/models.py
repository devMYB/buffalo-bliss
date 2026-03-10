from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text, JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)
    description = Column(Text, nullable=False)
    image = Column(String(500), nullable=False)
    category = Column(String(500), nullable=False)  # Space-separated categories/tags
    badges = Column(String(200), nullable=True)     # Comma-separated or space-separated e.g. "Music, Festival"
    date = Column(String(100), nullable=False)       # e.g. "Feb 3-23, 2026"
    time = Column(String(100), nullable=False)       # e.g. "06:30 PM"
    location = Column(String(500), nullable=False)   # e.g. "Canalside, Buffalo, NY"
    price = Column(String(50), nullable=True)       # e.g. "$25" or "Free"
    url = Column(String(500), nullable=False)        # External ticket/info URL
    featured = Column(Boolean, default=False)
    month = Column(String(10), nullable=True)       # e.g. "Feb"
    day = Column(String(20), nullable=True)         # e.g. "3-23"
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class AdvertisingRequest(Base):
    __tablename__ = "advertising_requests"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(120), nullable=False)
    email = Column(String(120), nullable=False)
    business_name = Column(String(120), nullable=False)
    sector = Column(String(60), nullable=False)
    other_sector = Column(String(120), nullable=True)
    company_link = Column(String(500), nullable=True)
    message = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

class Subscriber(Base):
    __tablename__ = "subscribers"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(120), nullable=False, unique=True)
    created_at = Column(DateTime, default=datetime.utcnow)
