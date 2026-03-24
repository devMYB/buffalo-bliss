import json
from sqlalchemy.orm import Session
from backend.db import SessionLocal, engine
from backend.models import Base, Event, Restaurant

# Initialize database
Base.metadata.create_all(bind=engine)

events_data = [
    {
        "id": 1,
        "name": "Music is Art",
        "description": "Live music featuring local and international artists across multiple genres.",
        "image": "https://images.unsplash.com/photo-1533174072545-7a4b6ad7a6c3?w=1200",
        "category": "music food entertainment",
        "badges": "Music, Festival",
        "month": "Feb",
        "time": "~06:30 PM",
        "location": "Canalside, Buffalo, NY",
        "price": "$25",
        "url": "https://www.musicisart.org",
        "featured": True
    },
    {
        "id": 2,
        "name": "Buffalo Holiday Spring Market",
        "description": "Outdoor spring artisan market featuring crafts, food vendors, and seasonal activities.",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ-GiKqbyBlf8HUmwkrmlkD-iWDlLHGw9V4hw&s",
        "category": "food",
        "badges": "Food",
        "month": "March - April",
        "time": "11:00 AM – 5:00 PM",
        "location": "Buffalo RiverWorks, Buffalo, NY",
        "price": "Free",
        "url": "https://www.buffaloholidaymarket.com/spring",
        "featured": True
    },
    {
        "id": 3,
        "name": "Buffalo Cherry Blossom Festival",
        "description": "Japanese cultural celebration with music, performances, and blooming cherry trees.",
        "image": "https://www.buffalorising.com/wp-content/uploads/2024/04/Cherry-Blossom-Festival-2048x1536-1.jpg",
        "category": "cultural art",
        "badges": "Cultural, Sakura",
        "month": "April",
        "time": "11:00 AM – 3:00 PM",
        "location": "Buffalo History Museum & Japanese Garden, Buffalo, NY",
        "price": "Free",
        "url": "https://www.buffalocherryblossomfestival.org/",
        "featured": True
    },
    {
        "id": 4,
        "name": "Dyngus Day Buffalo",
        "description": "Massive Polish-American celebration with parades, polka bands, and food.",
        "image": "https://substackcdn.com/image/fetch/$s_!Ssni!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F16873293-b1bd-48a7-89ca-d7551095377c_1500x1000.jpeg",
        "category": "cultural music religion",
        "badges": "Cultural, Music",
        "month": "April",
        "time": "~12:00 PM – 8:00 PM",
        "location": "Broadway Market District, Buffalo, NY",
        "price": "Varies",
        "url": "https://www.dyngusday.com/",
        "featured": False
    },
    {
        "id": 5,
        "name": "Explore Buffalo Walking Tours",
        "description": "Guided architectural tours exploring Buffalo’s historic neighborhoods.",
        "image": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/29/ae/e5/7b/explore-buffalo-including.jpg?w=800&h=-1&s=1",
        "category": "cultural art",
        "badges": "History, Explore",
        "month": "March - April",
        "time": "~10:00 AM – 12:00 PM",
        "location": "Various locations, Buffalo, NY",
        "price": "Free",
        "url": "https://explorebuffalo.org/",
        "featured": False
    },
    {
        "id": 6,
        "name": "Buffalo Marathon Spring Training Group",
        "description": "Community running training program preparing runners for major races.",
        "image": "https://stepoutbuffalo.com/wp-content/uploads/2026/01/image000000-1-1024x576.jpg",
        "category": "fitness wellness sports",
        "badges": "Fitness, Wellness",
        "month": "March–May",
        "time": "~Tuesdays 6:00 PM / Sundays 8:30 AM",
        "location": "Various training locations around Buffalo & Hamburg, NY",
        "price": "$103",
        "url": "https://runsignup.com/Race/Info/NY/Hamburg/BuffaloSpringTrainingGroup",
        "featured": False
    },
    {
        "id": 7,
        "name": "M&T Fourth Friday Art Walk",
        "description": "Monthly gallery walk with exhibitions, music, and local art showcases.",
        "image": "https://www.buffaloartsstudio.org/wp-content/uploads/2025/09/52743900497_c5348d8fcb_o-2-scaled.jpg",
        "category": "art",
        "badges": "Art",
        "month": "April–December",
        "time": "~6:00 PM – 9:00 PM",
        "location": "Downtown galleries (Buffalo Arts Studio area), Buffalo, NY",
        "price": "Free",
        "url": "https://www.buffaloartsstudio.org/",
        "featured": False
    },
    {
        "id": 8,
        "name": "Nickel City Comic Con",
        "description": "Major comic book and pop-culture convention featuring artists, panels, and cosplay.",
        "image": "https://pbs.twimg.com/profile_images/1631049115969769472/OTK073Pj_400x400.jpg",
        "category": "entertainment",
        "badges": "Pop-culture, Comics",
        "month": "May",
        "time": "~10:00 AM – 6:00 PM",
        "location": "Buffalo Niagara Convention Center, Buffalo, NY",
        "price": "Varies",
        "url": "https://www.nickelcitycon.com/",
        "featured": False
    },
    {
        "id": 9,
        "name": "Himalayan Institute Buffalo Yoga & Meditation",
        "description": "Yoga and meditation classes focused on mindfulness and self-awareness.",
        "image": "https://images.momence.com/h/41307/session-template-banner/659a6408-17ca-4277-a4c4-44eb2dae84bb.jpg",
        "category": "health wellness spirituality",
        "badges": "Yoga",
        "month": "Year-round",
        "time": "~6:30 AM – 7:30 AM (various sessions)",
        "location": "Himalayan Institute Buffalo, Buffalo, NY",
        "price": "$17",
        "url": "https://hibuffalo.org/",
        "featured": False
    },
    {
        "id": 10,
        "name": "Outer Harbor Live Concert Series",
        "description": "Outdoor waterfront concerts featuring touring rock and indie bands.",
        "image": "https://www.buffalorising.com/wp-content/uploads/2025/02/3856fb5d-db69-302e-c42c-8ce237b58fdf.jpg",
        "category": "music entertainment",
        "badges": "Rock, Indie",
        "month": "May–August",
        "time": "~6:00 PM – 10:00 PM",
        "location": "Outer Harbor Terminal B, Buffalo, NY",
        "price": "Varies",
        "url": "https://buffalowaterfront.com/concerts",
        "featured": False
    },
    {
        "id": 11,
        "name": "Flex Yoga Community Classes",
        "description": "Community yoga classes focusing on strength, mindfulness, and balance.",
        "image": "https://flexyogabuffalo.com/cdn/shop/files/IMG_3672.jpg?v=1742830879&width=3840",
        "category": "health wellness spirituality",
        "badges": "Yoga",
        "month": "Year-round",
        "time": "~6:00 PM – 7:00 PM (varies by class)",
        "location": "Flex Yoga Studio, Buffalo, NY",
        "price": "Varies",
        "url": "https://flexyogabuffalo.com/",
        "featured": False
    },
    {
        "id": 12,
        "name": "Lewiston Garden Fest",
        "description": "Large gardening festival with plant vendors, landscaping ideas, and artisan booths.",
        "image": "https://nebula.wsimg.com/648bde0d366a501497a79d16920f6f6e?AccessKeyId=3D51FAE985CE87BF7A06&disposition=0&alloworigin=1",
        "category": "art",
        "badges": "Nature",
        "month": "May",
        "time": "~10:00 AM – 5:00 PM",
        "location": "Center Street, Lewiston, NY",
        "price": "Free",
        "url": "http://www.lewistongardenfest.com/",
        "featured": False
    },
    {
        "id": 13,
        "name": "Food Truck Tuesdays",
        "description": "Weekly event featuring dozens of food trucks and live music.",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR_s3qzE0G_hlQms1w4L7F319D2zNHLMibhBA&s",
        "category": "music food entertainment",
        "badges": "Food, Live Music",
        "month": "May–September",
        "time": "~5:00 PM – 9:00 PM",
        "location": "Larkin Square, Buffalo, NY",
        "price": "Free",
        "url": "https://larkinsquare.com/",
        "featured": False
    },
    {
        "id": 14,
        "name": "Juneteenth Festival of Buffalo",
        "description": "One of the largest Juneteenth celebrations in the U.S. with music and cultural events.",
        "image": "https://scontent-iad3-2.xx.fbcdn.net/v/t39.30808-6/489415174_1223880813076000_2011125519899232488_n.jpg?_nc_cat=111&ccb=1-7&_nc_sid=7b2446&_nc_ohc=y2419QGy5JUQ7kNvwGhr702&_nc_oc=AdnniQteUr24WvmA4QcgfAExd-yGIRlTVBrHLmW7OKN799bEsEAV6Ln8cjaIftUbukw&_nc_zt=23&_nc_ht=scontent-iad3-2.xx&_nc_gid=-GUolAlYwWFUFCorD59NJg&_nc_ss=8&oh=00_Afw1fdCGeroIOtAgu3nd1KKV3i97bvJ0SRJTGF0ZHH70GQ&oe=69B628F3",
        "category": "cultural",
        "badges": "Juneteenth, Cultural",
        "month": "June",
        "time": "~11:00 AM – 8:00 PM",
        "location": "Martin Luther King Jr. Park, Buffalo, NY",
        "price": "Varies",
        "url": "https://www.buffalojuneteenth.com/",
        "featured": False
    },
    {
        "id": 15,
        "name": "Allentown First Fridays",
        "description": "Monthly art gallery walk with exhibits and live performances.",
        "image": "https://pbs.twimg.com/media/F47WQcaXQAA5bfR.jpg",
        "category": "art music entertainment",
        "badges": "Music, Art",
        "month": "Monthly",
        "time": "~6:00 PM – 9:00 PM",
        "location": "Allentown Arts District, Buffalo, NY",
        "price": "Varies",
        "url": "https://www.allentown.org/",
        "featured": False
    },
    {
        "id": 16,
        "name": "Elmwood Village Farmers Market",
        "description": "Weekly farmers market featuring local produce, baked goods, and crafts.",
        "image": "https://assets.simpleviewinc.com/simpleview/image/upload/c_fill,h_334,q_75,w_579/v1/crm/newyorkstate/Elmwood-Bidwell-Farmers-Market_b25721a0-f8a9-bc91-3190ce4c01e83c28.jpg",
        "category": "food",
        "badges": "Farmers market",
        "month": "May–November",
        "time": "~8:00 AM – 1:00 PM",
        "location": "Bidwell Parkway, Buffalo, NY",
        "price": "Free",
        "url": "https://www.elmwoodmarket.org/",
        "featured": False
    },
    {
        "id": 17,
        "name": "WNY Muslim Community Events",
        "description": "Religious, cultural, and community gatherings organized by the local Muslim community.",
        "image": "https://pbs.twimg.com/profile_images/558284968112046080/24SWU3ee_400x400.jpeg",
        "category": "faith religion",
        "badges": "Community",
        "month": "Year round",
        "time": "~10:00 AM – 3:00 PM",
        "location": "Various locations, Buffalo, NY",
        "price": "Varies",
        "url": "https://www.wnymuslims.org/events",
        "featured": False
    },
    {
        "id": 18,
        "name": "Buffalo Greek Festival",
        "description": "Festival featuring Greek food, music, and cultural traditions.",
        "image": "https://farm4.static.flickr.com/3303/3474474448_bbcf1a34ba.jpg",
        "category": "cultural faith religion",
        "badges": "Greek, food, music",
        "month": "June",
        "time": "~11:00 AM – 11:00 PM",
        "location": "Annunciation Greek Orthodox Church, Buffalo, NY",
        "price": "$3",
        "url": "https://www.buffalogreekfest.org/",
        "featured": False
    },
    {
        "id": 19,
        "name": "Buffalo Marathon Weekend",
        "description": "Major running event featuring a full marathon, half marathon, 5K, and family races.",
        "image": "https://www.thebuffalomarathon.com/wp-content/uploads/2026/01/buffalo-marathon-and-25th-lockup.jpg",
        "category": "fitness health sports",
        "badges": "Marathon",
        "month": "May",
        "time": "~6:30 AM – 2:00 PM",
        "location": "Downtown Buffalo (various start locations), Buffalo, NY",
        "price": "Varies",
        "url": "https://www.thebuffalomarathon.com/",
        "featured": False
    }
]


def seed_events():
    db = SessionLocal()
    try:
        db.query(Event).delete()
        db.commit()

        for event in events_data:
            db.add(Event(
                id=event["id"],
                name=event["name"],
                description=event["description"],
                image=event["image"],
                category=event["category"],
                badges=event.get("badges"),
                month=event["month"],
                time=event["time"],
                location=event["location"],
                price=event.get("price", "Free"),
                url=event.get("url"),
                featured=event.get("featured", False)
            ))

        db.commit()
        print("Events seeded successfully!")
    except Exception as e:
        import traceback
        print(f"Error seeding events: {e}")
        traceback.print_exc()
        db.rollback()
    finally:
        db.close()

restaurants_data = [
    {
        "name": "Cafe Bewilderment",
        "address": "1235 Hertel Ave, Buffalo",
        "catchy_phrase": "Hidden Oasis",
        "image": "https://cafebewilderment.com/wp-content/uploads/2024/12/cafe_3_optimized.jpg",
        "description": "A true hidden gem nestled inside the lower level of The Monocle on Hertel Avenue, Cafe Bewilderment is a queer-owned \"ethereal escape\" that draws inspiration from the raw beauty of the forest. This isn't just a coffee shop; it's a sanctuary for the curious and the connected.\n\nLocated within a beautifully renovated former Jewish synagogue at 1235 Hertel Ave, the space is shared with a boutique furniture store, a barber studio, and a design hub. Here, nature's magic meets the warmth of community. You can savor the artistry of locally sourced dishes, sip on handcrafted cocktails, or enjoy high-end Stumptown coffee in a woodsy, inclusive vibe that feels worlds away from the city bustle.",
        "website_url": "https://cafebewilderment.com/",
        "badge1": "Queer-Owned",
        "badge2": "Coffee & Cocktails",
        "sort_order": 1
    },
    {
        "name": "Blueberry Treehouse Farm",
        "address": "1897 Davis Rd, West Falls",
        "catchy_phrase": "Forest Adventure",
        "image": "https://thevillagerny.com/wp-content/uploads/2025/06/Dining.jpg",
        "description": "Just a short drive south of Buffalo in West Falls lies a family-friendly destination that feels like a childhood dream brought to life. Blueberry Treehouse Farm has transformed a historic 35-year-old organic blueberry farm into a vibrant, modern community space.\n\nThe centerpiece is undoubtedly the \"Treehouse Cafe,\" an architectural marvel perched in the woods that invites you to experience nature from a different perspective. Whether you're there for the organic U-pick berries in the summer, wandering the local trails, or catching an outdoor concert under the stars, this farm offers a unique blend of rural charm and creative vision that makes it an essential hidden gem for families and explorers alike.",
        "website_url": "https://www.blueberrytreehousefarm.com/",
        "badge1": "Family Friendly",
        "badge2": "Unique Architecture",
        "sort_order": 2
    },
    {
        "name": "The Original Tea House",
        "address": "392 Pearl Street, Buffalo",
        "catchy_phrase": "Cultural Haven",
        "image": "https://www.buffalorising.com/wp-content/uploads/2024/04/Teas-Buffalo-3-scaled.jpg",
        "description": "A haven for tea and coffee enthusiasts, The Original Tea House immerses downtown Buffalo in culturally authentic flavors from around the globe. From the delicate Japanese matcha to the spicy, warming Kashmiri Kahwa, every cup tells a story of tradition.\n\nThe space is designed for lingering, with an aesthetic tea/coffee bar island and comfortable seating surrounded by art from local creators. It's a perfect spot to unplug with a book, engage in board games with friends, or indulge in their legendary homemade desserts like Sabaya and the beehive (Khaliat Al-nahl). It's an inviting, aesthetic space that proves some of the city's best experiences are found just off the main drag.",
        "website_url": "https://theoriginalteahouse.com/",
        "badge1": "Authentic",
        "badge2": "Tea Culture",
        "sort_order": 3
    },
    {
        "name": "Mokha Reserve",
        "address": "1207 Hertel Ave, Buffalo",
        "catchy_phrase": "Yemeni Heritage",
        "image": "https://s3-media0.fl.yelpcdn.com/bphoto/6VN99jDnCL2ycBH3EWn3Zg/348s.jpg",
        "description": "Buffalo's premier authentic Yemeni coffee shop, Mokha Reserve, brings a unique cultural experience to Hertel Avenue. Focusing on the rich traditions of Arabic coffee and gourmet pastries, this shop offers a taste profile that is distinct and deeply rooted in heritage.\n\nThe experience here goes beyond the caffeine; it's about the meticulously prepared coffee and the inviting atmosphere that fosters connection. Praised for its traditional flavors and warm environment, it's a place where you can discover the true origins of coffee culture right in Western New York.",
        "website_url": "https://mokhareserve.com/",
        "badge1": "Arabic Coffee",
        "badge2": "Cultural Gem",
        "sort_order": 4
    },
    {
        "name": "RISE Community Coffeehouse",
        "address": "1643 Hertel Avenue, Buffalo",
        "catchy_phrase": "Purpose Driven",
        "image": "https://images.squarespace-cdn.com/content/v1/65af14ccd3cbe1113172e4af/f5340ff9-250c-4ab1-ac4e-5ab2648c0f4d/Attach0%281%29+copy.jpg",
        "description": "More than just a place for a morning brew, RISE Community Coffeehouse is a mission-driven hub on Hertel Avenue that pours hope and relief into the WNY community. They operate on a unique \"pay-what-you-can\" model for hot beverages, ensuring that everyone has access to a great cup of coffee regardless of their financial situation.\n\nBut the impact goes even deeper—RISE serves as a home base for a multi-tiered work readiness program, providing individuals from underserved backgrounds with hands-on job training. It is a cozy, welcoming space that brings together people from all walks of life, proving that a coffee house can truly be the heart of a community.",
        "website_url": "https://www.riseofwny.org/",
        "badge1": "Pay-What-You-Can",
        "badge2": "Community Impact",
        "sort_order": 5
    }
]

def seed_restaurants():
    db = SessionLocal()
    try:
        for r in restaurants_data:
            existing = db.query(Restaurant).filter(Restaurant.name == r["name"]).first()
            if not existing:
                new_restaurant = Restaurant(
                    name=r["name"],
                    address=r["address"],
                    catchy_phrase=r["catchy_phrase"],
                    image=r["image"],
                    description=r["description"],
                    website_url=r.get("website_url"),
                    badge1=r.get("badge1"),
                    badge2=r.get("badge2"),
                    sort_order=r.get("sort_order", 0)
                )
                db.add(new_restaurant)
        db.commit()
        print("Restaurants seeded successfully!")
    except Exception as e:
        import traceback
        print(f"Error seeding restaurants: {e}")
        traceback.print_exc()
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed_events()
    seed_restaurants()
