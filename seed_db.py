import json
from sqlalchemy.orm import Session
from backend.db import SessionLocal, engine
from backend.models import Base, Event

# Initialize database
Base.metadata.create_all(bind=engine)

events_data = [
    {
        "id": "yoga-park",
        "name": "Yoga in the Park",
        "description": "Join us for a rejuvenating outdoor yoga session suitable for all levels.",
        "image": "https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=1200",
        "category": "fitness health wellness",
        "badges": ["Fitness", "Wellness"],
        "date": "Jan 25, 2026",
        "time": "09:00 AM",
        "location": "Delaware Park, Buffalo, NY",
        "price": "Free",
        "featured": False,
        "month": "Jan",
        "day": "25"
    },
    {
        "id": "buffalo-music-fest",
        "name": "Buffalo Music Festival 2026",
        "description": "Live music featuring local and international artists across multiple genres.",
        "image": "https://images.unsplash.com/photo-1492684223066-81342ee5ff30?w=1200",
        "category": "music food entertainment",
        "badges": ["Music", "Festival"],
        "date": "Feb 3-23, 2026",
        "time": "06:30 PM",
        "location": "Canalside, Buffalo, NY",
        "price": "$25",
        "url": "https://www.musicisart.org",
        "featured": True,
        "month": "Feb",
        "day": "3-23"
    },
    {
        "id": "desi-culture-fair",
        "name": "Desi Food & Culture Fair",
        "description": "A vibrant celebration of South Asian food, music, dance, and traditional crafts.",
        "image": "https://images.unsplash.com/photo-1533174072545-7a4b6ad7a6c3?w=1200",
        "category": "food entertainment",
        "badges": ["Desi", "Food"],
        "date": "March 15, 2026",
        "time": "12:00 PM",
        "location": "Niagara Square, Buffalo, NY",
        "price": "Free",
        "url": "https://allevents.in/buffalo",
        "featured": True,
        "month": "Mar",
        "day": "15"
    },
    {
        "id": "bollywood-night",
        "name": "Bollywood Night",
        "description": "A night of dance, music, and celebration of Bollywood culture.",
        "image": "https://images.unsplash.com/photo-1514525253344-f24672a230c5?w=1200",
        "category": "entertainment",
        "badges": ["Desi", "Dance"],
        "date": "March 22, 2026",
        "time": "07:00 PM",
        "location": "Buffalo Convention Center, NY",
        "price": "Free",
        "featured": False,
        "month": "Mar",
        "day": "22"
    },
    {
        "id": "holi-fest",
        "name": "Holi Festival of Colors",
        "description": "Celebrate the arrival of spring with the traditional festival of colors.",
        "image": "https://images.unsplash.com/photo-1463138541530-50d4f13426e2?w=1200",
        "category": "cultural entertainment desi",
        "badges": ["Cultural", "Desi", "Spring"],
        "date": "April 12, 2026",
        "time": "11:00 AM",
        "location": "Outer Harbor, Buffalo, NY",
        "price": "Free",
        "featured": False,
        "month": "Apr",
        "day": "12"
    },
    {
        "id": "pride-buffalo",
        "name": "Pride Buffalo Festival",
        "description": "A vibrant celebration of diversity and inclusion at the Buffalo waterfront.",
        "image": "https://images.unsplash.com/photo-1533174072545-7a4b6ad7a6c3?w=1200",
        "category": "cultural community entertainment",
        "badges": ["Cultural", "Community"],
        "date": "June 15-17, 2026",
        "time": "12:00 PM",
        "location": "Canalside, Buffalo, NY",
        "price": "$45",
        "featured": False,
        "month": "Jun",
        "day": "15-17"
    },
    {
        "id": "spiritual-workshop",
        "name": "Spiritual Awakening Workshop",
        "description": "Explore inner peace and mindfulness in this guided spiritual journey.",
        "image": "https://images.unsplash.com/photo-1506126613408-eca07ce68773?w=1200",
        "category": "faith spirituality wellness",
        "badges": ["Spirituality", "Wellness"],
        "date": "May 20, 2026",
        "time": "10:00 AM",
        "location": "North Park Theatre, Buffalo, NY",
        "price": "$15",
        "featured": False,
        "month": "May",
        "day": "20"
    },
    {
        "id": "shakespeare-park",
        "name": "Shakespeare in Delaware Park",
        "description": "One of the largest free outdoor Shakespeare festivals in the country.",
        "image": "https://images.unsplash.com/photo-1507676184212-d03ab07a01bf?w=1200",
        "category": "art cultural",
        "badges": ["Art", "Theater", "Free"],
        "date": "June 20 - Aug 20, 2026",
        "time": "07:30 PM",
        "location": "Delaware Park, Buffalo, NY",
        "price": "Free",
        "featured": False,
        "month": "Jun",
        "day": "20"
    },
    {
        "id": "taste-of-buffalo",
        "name": "Taste of Buffalo Celebration",
        "description": "Celebrates many cuisines and cultures with restaurants, food trucks, and wineries.",
        "image": "https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=1200",
        "category": "cultural food entertainment",
        "badges": ["Food", "Desi"],
        "date": "July 11-12, 2026",
        "time": "11:00 AM",
        "location": "Niagara Square, Downtown Buffalo, NY",
        "url": "https://www.tasteofbuffalo.com",
        "featured": True,
        "month": "Jul",
        "day": "11-12"
    }
]

def seed():
    db = SessionLocal()
    try:
        for event in events_data:
            # Check if event already exists
            existing = db.query(Event).filter(Event.name == event["name"]).first()
            if not existing:
                new_event = Event(
                    name=event["name"],
                    description=event["description"],
                    image=event["image"],
                    category=event["category"],
                    badges=", ".join(event["badges"]) if isinstance(event.get("badges"), list) else event.get("badges"),
                    date=event["date"],
                    time=event["time"],
                    location=event["location"],
                    price=event.get("price", "Free"),
                    url=event.get("url"),
                    featured=event.get("featured", False),
                    month=event.get("month"),
                    day=event.get("day")
                )
                db.add(new_event)
        db.commit()
        print("Database seeded successfully!")
    except Exception as e:
        import traceback
        print(f"Error seeding database: {e}")
        traceback.print_exc()
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed()
