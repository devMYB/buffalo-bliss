from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text, JSON, Float
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
    month = Column(String(100), nullable=False)      # e.g. "Feb 3-23, 2026"
    time = Column(String(100), nullable=False)       # e.g. "06:30 PM"
    location = Column(String(500), nullable=False)   # e.g. "Canalside, Buffalo, NY"
    price = Column(String(50), nullable=False)       # e.g. "$25" or "Free"
    url = Column(String(500), nullable=True)         # External ticket/info URL
    featured = Column(Boolean, default=False)
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

class Restaurant(Base):
    __tablename__ = "restaurants"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)
    address = Column(String(500), nullable=False)
    catchy_phrase = Column(String(200), nullable=False)   # e.g. "Hidden Oasis"
    image = Column(String(500), nullable=False)
    description = Column(Text, nullable=False)            # Full description paragraphs
    website_url = Column(String(500), nullable=True)      # Official website link
    badge1 = Column(String(100), nullable=True)           # e.g. "Queer-Owned"
    badge2 = Column(String(100), nullable=True)           # e.g. "Coffee & Cocktails"
    sort_order = Column(Integer, default=0)               # Controls display order
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Attraction(Base):
    __tablename__ = "attractions"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)
    address = Column(String(500), nullable=False)
    image = Column(String(500), nullable=False)
    url = Column(String(500), nullable=True)
    description = Column(Text, nullable=False)
    full_description = Column(Text, nullable=False)
    category = Column(String(500), nullable=False)
    hours = Column(String(500), nullable=False)
    price = Column(String(50), nullable=False)
    badge1 = Column(String(100), nullable=True)
    badge2 = Column(String(100), nullable=True)
    featured = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)
    image = Column(String(500), nullable=False)
    description = Column(Text, nullable=False)         # short preview
    full_description = Column(Text, nullable=False)    # full blog-style content
    category = Column(String(200), nullable=False)     # e.g. "vegan breakfast"
    badge1 = Column(String(100), nullable=True)
    badge2 = Column(String(100), nullable=True)
    featured = Column(Boolean, default=False)
    sort_order = Column(Integer, default=0)            # controls display order
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)
    image = Column(String(500), nullable=False)
    description = Column(Text, nullable=False)
    full_description = Column(Text, nullable=False)
    minutes = Column(Integer, nullable=False)
    category = Column(String(100), nullable=False)  # health, wealth, spirit, happiness
    badge1 = Column(String(100), nullable=True)
    badge2 = Column(String(100), nullable=True)
    sort_order = Column(Integer, default=0)
    featured = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)