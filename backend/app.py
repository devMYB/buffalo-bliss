from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from .db import engine, get_db, SessionLocal
from .models import Base, Event, AdvertisingRequest, Subscriber, Restaurant, Attraction, Recipe, Article, Magazine
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
        
@app.get("/api/attractions")
def get_attractions(category: Optional[str] = None, db: Session = Depends(get_db)):
    query = db.query(Attraction)
    if category:
        query = query.filter(Attraction.category.contains(category))
    return query.all()

@app.get("/api/attractions/{attraction_id}")
def get_attraction(attraction_id: int, db: Session = Depends(get_db)):
    attraction = db.query(Attraction).filter(Attraction.id == attraction_id).first()
    if not attraction:
        raise HTTPException(status_code=404, detail="Attraction not found")
    return attraction

@app.get("/api/recipes")
def get_recipes(category: Optional[str] = None, db: Session = Depends(get_db)):
    query = db.query(Recipe)

    if category:
        query = query.filter(Recipe.category.contains(category))

    return query.order_by(Recipe.sort_order, Recipe.id).all()


@app.get("/api/recipes/{id}")
def get_recipe(id: int, db: Session = Depends(get_db)):
    recipe = db.query(Recipe).filter(Recipe.id == id).first()

    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")

    return recipe

@app.get("/api/articles")
def get_articles(category: Optional[str] = None, featured: Optional[bool] = None, db: Session = Depends(get_db)):
    query = db.query(Article)
    if category:
        query = query.filter(Article.category == category)
    if featured is not None:
        query = query.filter(Article.featured == featured)
    return query.order_by(Article.sort_order.desc(), Article.id.desc()).all()

@app.get("/api/articles/{article_id}")
def get_article(article_id: int, db: Session = Depends(get_db)):
    article = db.query(Article).filter(Article.id == article_id).first()
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    return article

@app.get("/api/magazines")
def get_magazines(db: Session = Depends(get_db)):
    return db.query(Magazine).order_by(Magazine.created_at.desc()).all()

@app.get("/api/magazines/{magazine_id}")
def get_magazine(magazine_id: int, db: Session = Depends(get_db)):
    magazine = db.query(Magazine).filter(Magazine.id == magazine_id).first()
    if not magazine:
        raise HTTPException(status_code=404, detail="Magazine not found")
    return magazine

@app.get("/api/health")
def health_check():
    return {"status": "healthy"}
