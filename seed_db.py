import json
from sqlalchemy.orm import Session
from backend.db import SessionLocal, engine
from backend.models import Base, Event, Restaurant, Attraction

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

attractions_data = [
    {
        "name": "Niagara Falls",
        "address": "Niagara Falls State Park, NY",
        "description": "Experience the breathtaking power and beauty of one of the world's most famous waterfalls.",
        "full_description": "Niagara Falls is not just a waterfall; it's a testament to the raw power of nature. To truly experience its majesty, start your day with the Maid of the Mist boat tour, which takes you right into the heart of the Horseshoe Falls. Afterward, walk through the Cave of the Winds to feel the 'tropical storm' force of the Bridal Veil Falls.\n\nFor a more peaceful experience, explore the miles of hiking trails on Goat Island or enjoy a picnic overlooking the upper rapids. As the sun sets, stay for the nightly illumination where the falls are lit in a rainbow of colors, followed by spectacular fireworks displays during the summer months.",
        "image": "assets/images/niagara-falls.avif",
        "category": "parks family",
        "hours": "Open 24/7",
        "price": "Free Admission",
        "url": "https://www.niagarafallsstatepark.com",
        "badge1": "Natural Wonder",
        "badge2": "Parks & Nature",
        "featured": True
    },
    {
        "name": "Buffalo AKG Art Museum",
        "address": "Delaware Park, Buffalo, NY",
        "description": "World-renowned collection of modern and contemporary art in a newly renovated architectural setting.",
        "full_description": "The Buffalo AKG Art Museum (formerly Albright-Knox) is an architectural and cultural masterpiece. Following its historic expansion, the museum now features the stunning 'Common Sky' installation in the town square. Your visit should begin in the Gundlach Building, where massive skylights illuminate some of the most important modern works in the world.\n\nDon't miss the 1962 building's classic galleries, which house masterpieces by Picasso, Matisse, and Pollock. The museum is perfectly situated at the edge of Delaware Park, making it ideal for a combined day of high culture and nature strolls. Be sure to check their calendar for 'M&T First Fridays' when admission is free for the community.",
        "image": "https://images.unsplash.com/photo-1518998053901-5348d3961a04?w=800",
        "category": "arts museums",
        "hours": "Tue-Sun 10AM-5PM",
        "price": "$15 Adults",
        "url": "https://buffaloakg.org",
        "badge1": "Art",
        "badge2": "Museums",
        "featured": True
    },
    {
        "name": "Buffalo Museum of Science",
        "address": "1020 Humboldt Pkwy, Buffalo, NY 14211",
        "description": "Interactive science studios and exhibits showcasing over 700,000 specimens and artifacts.",
        "full_description": "The Buffalo Museum of Science offers an adventure through time and space for explorers of all ages...",
        "image": "assets/images/museum-of-science.jpg",
        "category": "museums family",
        "hours": "Daily 10AM-4PM",
        "price": "$23 Adults",
        "url": "https://www.sciencebuff.org",
        "badge1": "Museums",
        "badge2": "Family Friendly",
        "featured": True
    },
    {
        "name": "Delaware Park",
        "address": "Buffalo, NY 14214",
        "description": "350-acre centerpiece of Buffalo's park system, designed by Olmsted & Vaux.",
        "full_description": "Designed by the legendary Frederick Law Olmsted, Delaware Park is the crown jewel...",
        "image": "https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=800",
        "category": "parks family",
        "hours": "Dawn to Dusk",
        "price": "Free",
        "url": "https://bfloparks.org/parks/delaware-park/",
        "badge1": "Parks & Nature",
        "badge2": "Family Friendly",
        "featured": True
    },
    {
        "name": "Darwin D. Martin House",
        "address": "125 Jewett Pkwy, Buffalo, NY 14214",
        "description": "Frank Lloyd Wright's masterpiece of Prairie-style architecture.",
        "full_description": "The Darwin D. Martin House is considered one of the most important works...",
        "image": "assets/images/flw.jpg",
        "category": "historic arts",
        "hours": "Tours 10AM-4PM",
        "price": "$25 Tours",
        "url": "https://martinhouse.org",
        "badge1": "Historic Sites",
        "badge2": "Arts & Culture",
        "featured": False
    },
    {
        "name": "Buffalo Zoo",
        "address": "300 Parkside Ave, Buffalo, NY 14214",
        "description": "The third oldest zoo in the US.",
        "full_description": "Located nestled within the historic Delaware Park, the Buffalo Zoo is one of the city's most beloved destinations...",
        "image": "https://images.unsplash.com/photo-1534567153574-2b12153a87f0?w=800",
        "category": "family parks",
        "hours": "Daily 10AM-4PM",
        "price": "$22.50 Adults",
        "url": "https://buffalozoo.org",
        "badge1": "Family Friendly",
        "badge2": "Parks & Nature",
        "featured": False
    },
    {
        "name": "Shea's Performing Arts Center",
        "address": "646 Main St, Buffalo, NY 14202",
        "description": "Historic 1926 theater hosting Broadway tours.",
        "full_description": "Stepping into Shea's Buffalo Theatre is like traveling back to the Gilded Age...",
        "image": "assets/images/sheas.jpg",
        "category": "arts historic",
        "hours": "Performance Times",
        "price": "Varies",
        "url": "https://www.sheas.org",
        "badge1": "Arts & Culture",
        "badge2": "Historic Sites",
        "featured": False
    },
    {
        "name": "Canalside",
        "address": "44 Prime St, Buffalo, NY 14202",
        "description": "Buffalo's revitalized waterfront destination.",
        "full_description": "Canalside is the heart of Buffalo's waterfront renaissance...",
        "image": "assets/images/canalside.jpg",
        "category": "family parks",
        "hours": "Open 24/7",
        "price": "Free Admission",
        "url": "https://buffalowaterfront.com/canalside",
        "badge1": "Family Friendly",
        "badge2": "Parks & Nature",
        "featured": False
    }
]

recipes_data = [
    {
        "id": 1,
        "name": "Chocolate Lava Cake",
        "image": "https://images.getrecipekit.com/20250325120225-how-20to-20make-20chocolate-20molten-20lava-20cake-20in-20the-20microwave.png?width=650&quality=90&",
        "description": "A rich and decadent chocolate dessert with a molten center.",
        "full_description": "Ingredients:\n- Dark chocolate\n- Butter\n- Eggs\n- Sugar\n\nInstructions:\nMelt chocolate and butter together. Mix eggs and sugar separately, combine with chocolate, and bake until the center remains soft and gooey.\n\nServe warm with vanilla ice cream for the best experience.",
        "category": "dessert",
        "badge1": "Dessert",
        "badge2": "Indulgent",
        "featured": True,
        "sort_order": 1
    },
    {
        "id": 2,
        "name": "Vegan Lentil Soup",
        "image": "https://cdn.apartmenttherapy.info/image/upload/f_jpg,q_auto:eco,c_fill,g_auto,w_1500,ar_1:1/k%2FPhoto%2FRecipes%2F2024-10-red-lentil-soup%2Fred-lentil-soup-180",
        "description": "A hearty, protein-rich soup perfect for a healthy meal.",
        "full_description": "Ingredients:\n- Lentils\n- Carrots\n- Celery\n- Garlic\n\nInstructions:\nCook lentils with vegetables and spices. Simmer until soft and flavorful.\n\nThis dish is perfect for meal prep and keeps well for several days.",
        "category": "vegan dinner",
        "badge1": "Vegan",
        "badge2": "Healthy",
        "featured": True,
        "sort_order": 2
    },
    {
        "id": 3,
        "name": "Stuffed Zucchini Boats",
        "image": "https://hips.hearstapps.com/hmg-prod/images/stuffed-zucchini-recipe-3-1656619330.jpg?crop=1.00xw:1.00xh;0,0&resize=1200:*",
        "description": "A light and flavorful vegetable-based dish.",
        "full_description": "Ingredients:\n- Zucchini\n- Bell peppers\n- Cheese\n\nInstructions:\nSlice zucchini, scoop the center, and fill with sautéed vegetables. Bake until tender.\n\nGreat as a light lunch or side dish.",
        "category": "lunch vegetarian",
        "badge1": "Vegetarian",
        "badge2": "Healthy",
        "featured": True,
        "sort_order": 3
    },
    {
        "id": 4,
        "name": "Avocado Toast Deluxe",
        "image": "https://www.allrecipes.com/thmb/H1mSgOExKFdto3PWLfC9aTgJmlI=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/11699506-avocado-toast-4x3-ea45b882fb0c454a9ca31647d4fd3c01.jpg",
        "description": "A nutritious and quick breakfast option.",
        "full_description": "Ingredients:\n- Bread\n- Avocado\n- Lemon\n\nInstructions:\nToast bread, mash avocado with lemon juice, spread evenly, and top with chili flakes.\n\nPerfect for a quick morning meal.",
        "category": "breakfast",
        "badge1": "Breakfast",
        "badge2": "Quick",
        "featured": False,
        "sort_order": 4
    },
    {
        "id": 5,
        "name": "Meal Prep Chicken Bowls",
        "image": "https://healthyfitnessmeals.com/wp-content/uploads/2018/08/Grilled-chicken-burrito-bowls-10.jpg",
        "description": "Balanced meals perfect for weekly prep.",
        "full_description": "Ingredients:\n- Chicken\n- Rice\n- Vegetables\n\nInstructions:\nCook chicken and portion with rice and veggies into containers.\n\nIdeal for busy weekdays.",
        "category": "meal-prep dinner",
        "badge1": "Meal Prep",
        "badge2": "High Protein",
        "featured": False,
        "sort_order": 5
    },
    {
        "id": 6,
        "name": "Classic Pancakes",
        "image": "https://img.delicious.com.au/EyhPamCD/del/2023/06/easy-pancake-191698-2.jpg",
        "description": "Fluffy pancakes for a perfect breakfast.",
        "full_description": "Ingredients:\n- Flour\n- Milk\n- Eggs\n\nInstructions:\nMix ingredients into a batter and cook on a skillet until golden brown.\n\nServe with syrup and butter.",
        "category": "breakfast",
        "badge1": "Breakfast",
        "badge2": "Comfort Food",
        "featured": False,
        "sort_order": 6
    },
    {
        "id": 7,
        "name": "Quinoa Buddha Bowl",
        "image": "https://www.eatwell101.com/wp-content/uploads/2021/02/Healthy-Chickpea-Quinoa-Salad-recipe-1.jpg",
        "description": "A nutritious bowl packed with plant-based goodness.",
        "full_description": "Ingredients:\n- Quinoa\n- Chickpeas\n- Vegetables\n\nInstructions:\nCook quinoa and assemble with roasted vegetables and dressing.\n\nHealthy and filling.",
        "category": "vegan lunch",
        "badge1": "Vegan",
        "badge2": "Balanced",
        "featured": False,
        "sort_order": 7
    },
    {
        "id": 8,
        "name": "Chocolate Chip Cookies",
        "image": "https://mojo.generalmills.com/api/public/content/_pLFRXFETcuXWg_Z0MhZPw_gmi_hi_res_jpeg.jpeg?v=693b292b&t=466b54bb264e48b199fc8e83ef1136b4",
        "description": "Classic cookies with a soft and chewy texture.",
        "full_description": "Ingredients:\n- Flour\n- Sugar\n- Chocolate chips\n\nInstructions:\nMix ingredients, shape dough, and bake until golden.\n\nPerfect for dessert or snacks.",
        "category": "dessert",
        "badge1": "Dessert",
        "badge2": "Classic",
        "featured": False,
        "sort_order": 8
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

def seed_attractions():
    db = SessionLocal()
    try:
        db.query(Attraction).delete()
        db.commit()

        for a in attractions_data:
            attraction = Attraction(
                name=a["name"],
                address=a["address"],
                image=a["image"],
                url=a.get("url"),
                description=a["description"],
                full_description=a["full_description"],
                category=a["category"],
                hours=a["hours"],
                price=a["price"],
                badge1=a.get("badge1"),
                badge2=a.get("badge2"),
                featured=a.get("featured", False)
            )
            db.add(attraction)

        db.commit()
        print("Attractions seeded successfully!")

    except Exception as e:
        import traceback
        print(f"Error seeding attractions: {e}")
        traceback.print_exc()
        db.rollback()
    finally:
        db.close()

def seed_recipes():
    db = SessionLocal()
    try:
        from backend.models import Recipe

        db.query(Recipe).delete()
        db.commit()

        for r in recipes_data:
            db.add(Recipe(
                id=r["id"],
                name=r["name"],
                image=r["image"],
                description=r["description"],
                full_description=r["full_description"],
                category=r["category"],
                badge1=r.get("badge1"),
                badge2=r.get("badge2"),
                featured=r.get("featured", False),
                sort_order=r.get("sort_order", 0)
            ))

        db.commit()
        print("Recipes seeded successfully!")

    except Exception as e:
        import traceback
        print(f"Error seeding recipes: {e}")
        traceback.print_exc()
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed_events()
    seed_restaurants()
    seed_attractions()
    seed_recipes()
