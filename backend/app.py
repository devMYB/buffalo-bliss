from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from .db import engine, get_db, SessionLocal
from .models import Base, Event, AdvertisingRequest, Subscriber, Restaurant
from .admin import setup_admin
from .admin_auth import authentication_backend
from pydantic import BaseModel, EmailStr, Field
from typing import Optional
import os

# Initialize database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Buffalo Bliss Content API")

# Setup Admin UI
setup_admin(app, engine, authentication_backend)

# Allow local frontend to call the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Schemas ---
class AdRequestSchema(BaseModel):
    full_name: str = Field(..., min_length=2, max_length=120)
    email: EmailStr
    business_name: str = Field(..., min_length=2, max_length=120)
    sector: str = Field(..., min_length=2, max_length=60)
    other_sector: Optional[str] = Field(default=None, max_length=120)
    company_link: Optional[str] = Field(default=None, max_length=500)
    message: str = Field(..., min_length=1, max_length=2000)

class SubscriberSchema(BaseModel):
    email: EmailStr

# --- Routes ---

@app.get("/")
def root():
    return {"message": "Buffalo Bliss Content API is running"}

@app.get("/api/events")
def get_events(category: Optional[str] = None, db: Session = Depends(get_db)):
    query = db.query(Event)
    if category:
        query = query.filter(Event.category.contains(category))
    return query.all()

@app.get("/api/events/{event_id}")
def get_event(event_id: int, db: Session = Depends(get_db)):
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event

@app.get("/api/restaurants")
def get_restaurants(db: Session = Depends(get_db)):
    return db.query(Restaurant).order_by(Restaurant.sort_order, Restaurant.id).all()

@app.get("/api/restaurants/{restaurant_id}")
def get_restaurant(restaurant_id: int, db: Session = Depends(get_db)):
    restaurant = db.query(Restaurant).filter(Restaurant.id == restaurant_id).first()
    if not restaurant:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    return restaurant

@app.post("/api/advertising-request")
async def create_request(payload: AdRequestSchema, db: Session = Depends(get_db)):
    try:
        new_request = AdvertisingRequest(
            full_name=payload.full_name,
            email=payload.email,
            business_name=payload.business_name,
            sector=payload.sector,
            other_sector=payload.other_sector,
            company_link=payload.company_link,
            message=payload.message
        )
        db.add(new_request)
        db.commit()
        return {"ok": True, "message": "Request submitted successfully"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/subscribe")
async def subscribe(payload: SubscriberSchema, db: Session = Depends(get_db)):
    # Check if subscriber already exists
    existing = db.query(Subscriber).filter(Subscriber.email == payload.email).first()
    if existing:
        return {"ok": True, "message": "Already subscribed"}
    
    try:
        new_subscriber = Subscriber(email=payload.email)
        db.add(new_subscriber)
        db.commit()
        return {"ok": True, "message": "Subscribed successfully"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/health")
def health_check():
    return {"status": "healthy"}
