
# To run this script from the root directory, use the command: python -m seed_data.seed_article_table 

from sqlalchemy.orm import Session
from backend.db import SessionLocal, engine
from backend.models import Base, Article
from datetime import datetime

# Initialize DB
Base.metadata.create_all(bind=engine)


articles_data = [

    # =========================
    # APRIL 2026 (LATEST FIRST)
    # =========================

    {
        "name": "Sustainable Eating for a Happy Planet",
        "image": "https://images.pexels.com/photos/3737696/pexels-photo-3737696.jpeg",
        "description": "Learn how simple food choices can improve your health while reducing your impact on the planet.",
        "full_description": """
<p>Earth Day is a reminder to all that we need to consider the impact of our everyday decisions on the world around us. Of those decisions, the way we choose to eat is particularly a strong one. Sustainable eating is not just about rules and perfection. It is all about the conscious choices that feed your body and your world.</p>

<h3>Lower Carbon Footprint</h3>
<p>Farm-to-plate food has an environmental effect. Greenhouse gas emissions are caused by industrial agriculture, transportation and packaging. By consuming foods that use fewer resources, especially plant-based options, you will cut down on your carbon footprint without significantly altering your way of life.</p>

<h3>Healthier Body, Happier Mind</h3>
<p>The food we consume and our mood are closely associated. Heavy consumption of whole foods, such as fruits, vegetables and grains, can help maintain physical well-being as well as enhance mood and energy. Feel good in your body; your mind will follow the suit.</p>

<h3>Reducing Food Waste</h3>
<p>One can easily forget about the quantity of food that is not eaten at home. Food items left in the refrigerator or excessive purchase of food will lead to a global waste menace on a low profile. Eating in moderation and scheduling meals not only helps to save money, but also to save important resources, such as water and energy.</p>

<h3>Embrace Plant-Based Foods</h3>
<p>Vegetarian lifestyles are not mandatory but can embrace some good qualities. Make a great impact by adding a few plant-based meals per week to your diet and lowering the environmental impact. Consider lentil curries, vegetable stir-fries or chickpea salads. These meals are simple, satisfying and sustainable.</p>

<h3>Select Locally Grown Foods</h3>
<p>Purchasing local is a way to help support your local farmers, and it also lessens the length of the journey that your food must travel. Fresh food, less pollution and increased local economy is a win at several levels. Going to farmers markets or buying local vendors can bring you back into the close up of where your food is produced.</p>

<h3>Go Organic When You Can</h3>
<p>Farming organic foods is done without synthetic pesticides and fertilizers and contributes to the preservation of soil health and biodiversity. Although you cannot always go completely organic, even minimal changes such as switching to organic fruits or vegetables, can have a significant impact in the long run.</p>

<h3>Sustainable Eating and Contributions to Happiness</h3>
<p>Sustainable eating is a physical, environmental and emotional choice. It is satisfying knowing what you eat can make you healthy. Home kitchen meals, picking local products and fewer disposals may bring some sense of purpose and mindfulness to everyday life.</p>

<p>In addition, making and sharing a well-cooked home meal together can cement relationships with loved ones. Food is no longer fuel; it is now a profoundly caring, perceptive and deliberate experience.</p>

<h3>Little Things to Big Things</h3>
<p>Sustainable eating does not mean that one needs to make an overhaul of your lifestyle. It starts with small actions, like picking meatless meals, purchasing local foods, or just watching the amount of waste one produces. These decisions would eventually create an effective ripple effect on the planet and your health.</p>

<p>Use your plate to honor this Earth Day. When you eat well, you are eating sustainably. You are not only feeding yourself, but you are feeding a healthier and much happier world.</p>
""",
        "author": "Usman Mehmood",
        "minutes": 6,
        "category": "happiness",
        "badge1": "Sustainability",
        "badge2": "Lifestyle",
        "sort_order": 100,
        "featured": True
    },

    {
        "name": "How Financial Stress Affects Our Mental Health",
        "image": "https://images.pexels.com/photos/5900136/pexels-photo-5900136.jpeg",
        "description": "Explore how money anxiety affects mental health and how awareness can help break the cycle.",
        "full_description": """
<p>There is a certain type of silence after economic anxiety. It appears in the middle of the night, when no one can hear, yet you know what to think. You start to reason, re-reason, and find out every decision; what you used to spend, what you saved, and what you will not have tomorrow. This is money anxiety, and to many individuals, it is not merely about money. It is a very emotional, overwhelming and strongly relatable situation to the well-being of our minds.</p>

<p>Financial stress will slip into daily life. It begins in an insidious manner, with indecisiveness before buying a product. It can be a lingering feeling of guilt after spending money or being in constant comparison with others. It may eventually develop into persistent anxiety. You may check your bank balance several times a day, or you may even avoid talking about money. This is an indicator that your mental health is being impacted.</p>

<p>Money anxiety is an uncertain feeling of control. The feeling of insecurity which arises due to the instability of finances can cause stress responses, like any other anxiety. The brain views financial threat through real danger and it triggers a loop of worry that may result in sleep problems, irritability, headaches and fatigue. It is more difficult to concentrate, more difficult to relax, and more difficult to be present.</p>

<p>The invisibility of money anxiety is also what makes it a difficult phenomenon to counter. Unlike other stress factors, financial struggles can be a secret. Social expectations and stigma may cause one to find it hard to open up, and such individuals are found to suffer in silence. This alienation further increases the emotional weight, and it becomes heavier than it is.</p>

<p>However, the relationship between money and mental health is not a one-way relationship. The same way financial stress may change your mood, may also influence the way you spend money. Anxiety can also be avoided, bills ignored, decisions postponed or overspent as a means of coping with emotions. It turns into a vicious cycle in which stress incites behavior and which behavior strengthens stress.</p>

<p>To end this cycle, it is necessary to change your point of view. It does not mean that one will get the perfect financial tune within a short time but instead develop a healthier relationship with money. Small actions with purpose may go a long way. Uncertainty can be minimized by creating a simple budget, creating realistic goals or achieving an understanding of your financial situation. Fear of the unknown starts to pass once you are aware of where you are.</p>

<p>It is also crucial to take care of the emotional side of money. Having a conversation with a friend, a relative, or someone you trust about financial stress may relieve. You understand that you are not only alone, but there are other individuals who are going through the same challenges though they do not discuss them openly.</p>

<p>Even mindfulness can be of help. Rather than letting the thoughts about money get out of control, simply being in the present moment can lessen anxiety. Ask yourself, what can I do today? The solution is often so much easier than the fears that control you.</p>

<p>It is true that money will never leave your life. It does not need to dominate your mind. This is because when you recognize money anxiety and deal with it both practically and emotionally, you establish some space of equilibrium. Within that moment, you start to shake off fear and become calm and controlled instead of stressed.</p>
""",
        "author": "Usman Mehmood",
        "minutes": 6,
        "category": "wealth",
        "badge1": "Mental Health",
        "badge2": "Finance",
        "sort_order": 99,
        "featured": True
    },

    {
        "name": "Stress Awareness: Digital Overwhelm and Triggers",
        "image": "https://images.pexels.com/photos/36697936/pexels-photo-36697936.jpeg",
        "description": "A closer look at how constant phone use and notifications quietly increase daily stress.",
        "full_description": """
<p>You probably don’t think twice before reaching for your phone. But did you know that our phones may be one of our biggest sources of stress? At the start of the technology era, we used social media and the internet as a way to access an abundance of information, connect with others, and pass time. Now, it has become the norm for people to be somewhat addicted to their phones, often causing significant stress on our bodies without us even realizing it.</p>

<p>One of the clearest examples is bedtime procrastination. Staying up far past your bedtime just to scroll on your phone a little longer creates a much larger stress trigger than we think. Not only does it disrupt our sleep, but the blue light emitted from our phones also interferes with melatonin production. Melatonin is a hormone that plays a crucial role in regulating sleep. When melatonin levels are disrupted, our circadian rhythm shifts, which can prevent us from reaching deep, restorative sleep. This may explain why many of us feel groggy and tired the morning after a night of doomscrolling.</p>

<p>A study sited from UC Health Today suggests that the average American unlocks their phone 100 to 150 times a day. Without conscious thought, our hands instinctively reach for our phones. This addiction to distraction is causing more physiological and cognitive stress than we realize. For example, every time we hear a phone notification, it can cause a cognitive slowdown of about seven seconds. Depending on how many notifications you receive, this delay can quickly add up. In addition, the sound of a notification can increase heart rate and trigger dopamine release. With the constant urge to check our phones and the effects of repeated notifications, both our minds and bodies remain continuously stimulated, ultimately leading to stress.</p>

<p>So, the next time you reach for your phone for a quick laugh or to check notifications, take a moment for yourself. Researchers and neuroscientists suggest replacing screen time with other activities or even starting small by physically distancing yourself from your phone, such as placing it in another room. It's best to sometimes remind ourselves that the biggest trigger for our stress can be sitting right in our pocket.</p>
""",
        "author": "Hana Dawood",
        "minutes": 4,
        "category": "happiness",
        "badge1": "Digital Detox",
        "badge2": "Awareness",
        "sort_order": 98,
        "featured": False
    },

    {
        "name": "Healthy Alternatives to Soda",
        "image": "https://images.pexels.com/photos/12851556/pexels-photo-12851556.jpeg",
        "description": "Simple drink swaps that can help reduce sugar intake and support healthier everyday habits.",
        "full_description": """
<p>Cutting back on soda is one of the simplest changes one can make to improve overall health and well-being. From a preventive care perspective, the goal isn’t perfection but rather making small and realistic swaps that can help support better lifestyle habits over time. Choosing alternatives to soda a few times a week can reduce sugar intake, lower exposure to acidic drinks, and help create a healthier daily routine without feeling too overly restrictive. The good news is that there are many alternatives that can make the transition easier. Here are some great options that you could swap instead the regular soda route:</p>

<ol>
<li><strong>Infused water</strong><br>
This is one of the simplest options. Adding fruit such as berries, lemon, limes or cucumber can give water a refreshing flavor without added sugars. A great option for those who want something more interesting than simply plain water.</li>

<li><strong>Sparkling water</strong><br>
Another excellent swap if you miss the carbonation of pop drinks. It offers the same fizzy feeling without the heavy sugar load of traditional soft drinks. Unsweetened flavored sparkling waters can be especially helpful for people trying to reduce soda while still enjoying variety.</li>

<li><strong>Herbal tea (iced or hot)</strong><br>
Many herbal teas naturally have a mild sweetness or refreshing taste without the need for added sugar. Depending on the flavor, they can feel soothing, energizing, or cooling, making them a versatile option for many times of day.</li>

<li><strong>Prebiotic sodas</strong><br>
Brands like Poppi and Olipop have become increasingly popular as a “better” soda alternative. These drinks are designed to offer a familiar taste and feel of soda, but typically with less sugar and added ingredients meant to support gut health, such as prebiotic fiber. For people who want something that feels closer to a traditional soda, this might be a good transition option.</li>
</ol>

<p>That said, prebiotic sodas which support gut health are best viewed as an occasional alternative rather than a health drink. Some types still have added sugars or sweeteners, and while the added fiber may sound appealing, these beverages should not replace water or whole-food sources of fiber in the diet. They may be a better choice than regular soda for some people, but it is still important to read the nutrition label and consider moderation.</p>

<p>In the end, replacing soda does not have to mean giving up enjoyment. Small changes, such as choosing infused water, sparkling water, or an occasional lower-sugar soda alternative, can support healthier habits over time. Preventive care is often built on these everyday choices, and even simple swaps can make a meaningful difference at the end of the day.</p>
""",
        "author": "Ayesha Khan",
        "minutes": 5,
        "category": "health",
        "badge1": "Nutrition",
        "badge2": "Lifestyle",
        "sort_order": 97,
        "featured": False
    },

    {
        "name": "How to Design a Sensory-Safe Home for Children",
        "image": "https://images.pexels.com/photos/8709244/pexels-photo-8709244.jpeg",
        "description": "Practical ways to create a calmer, more sensory-friendly home for children with autism.",
        "full_description": """
<p>With each generation, we have made significant strides in our abilities to care for our children. The collective efforts of mothers and medical providers have allowed us to provide an informed, structured environment to help any child flourish. April is Autism Awareness Month, which provides an opportunity to educate ourselves and recognize the needs of those who have Autism Spectrum Disorder (ASD). No matter where you are on your parenting journey, it is important to understand and know the signs of Autism to help better support yourself and others. With this knowledge, you can also make your home environment safer and more sensory friendly for every child.</p>

<p>Autism is best described on https://www.autismspeaks.org/what-autism as “a broad range of conditions characterized by challenges with social skills, repetitive behaviors, speech and nonverbal communication.” Often people think of the spectrum as linear, but the spectrum is actually more circular in that the diagnosed person could have any combination of symptoms with different levels of severity. Those with ASD have symptoms that range from barely detectable and maskable to those that are very apparent and require special assistance throughout different phases of their life.</p>

<p>Though the symptoms can vary dramatically, there are some common symptoms that indicate a child may be on the spectrum. AutismSpeaks.org defines them into 2 major categories: Challenges with socialization and having repetitive, restrictive behaviors. The early noticeable symptoms are:</p>

<ul>
<li>Limited eye contact or lack of response to their name by 9-12 months</li>
<li>Delayed speech or lack of babbling by 12 months</li>
<li>Repetitive behaviors such as hand-flapping, rocking, or spinning objects</li>
<li>Preference for playing alone or difficulty engaging with others</li>
<li>Unusual reactions to sensory stimuli, such as being overly sensitive to sounds or textures</li>
</ul>

<p>If your child shows any of these symptoms, it's important not to panic! Remember that every child develops differently, so contact their physician to see if an evaluation is necessary. Early intervention can make a huge impact on your child’s future development with ASD. The sooner you catch it, the sooner you can take advantage of the nutritionists, therapists, and support groups available.</p>

<p>Many other families navigate having a child with ASD successfully. Small changes and adjustments can help everyone thrive. Your home is a great place to start creating an accommodating space. With a few mindful adjustments, you can build a more sensory safe environment.</p>

<p>We have all experienced sensory overload. With the television blaring, toys going off, multiple conversations, and the clatter in the kitchen, the home can be full of noise. This can be particularly harder to navigate when you have different sensory needs. Those with autism may experience sounds, lights, textures, or smells more intensely. Everyday items in the household, such as appliances, lighting, and crowded areas, can feel very overwhelming.</p>

<p>The home should be a place where children can regulate and decompress. Reducing sensory stimulation provides space for emotional comfort and daily routine. By limiting sensory stressors, we can support better focus, sleep, and relaxation. With these adjustments, everyone can benefit from a more sensory-friendly environment, not just the child!</p>

<p>Making these changes does not have to be expensive or complicated! In fact, creating a sensory-safe home can often be made with 4 simple adjustments:</p>

<ol>
<li>Address the lighting. Replace blaring white overhead light with soft yellow lightbulbs. Allow natural light to flood the room whenever possible to help balance natural circadian rhythms. Lamps and dimmers also are a great way to control the lighting in each room.</li>
<li>Focusing on sound is also very important. Try to keep background noise at a controlled volume. Use noisy appliances routinely so they can be anticipated and allow preparation. Having soft rugs, curtains, or quiet play areas can also help absorb sound.</li>
<li>Create a calm corner for grounding and support. Include soft pillows, weighted blankets, favorite comfort items, or calming sensory toys. Having access to comfortable textures outside of the calming space wherever appropriate can also help.</li>
<li>Most importantly, stay organized. All children, with ASD or not, thrive in a predictable environment where toys and materials are stored in neat, consistent places.</li>
</ol>

<p>As always, follow your child’s lead. There is no standard way to have the perfect home for you and your family. Every child is unique and experiences sensory input differently. Try and change things slowly and take note of what works best for your child. It doesn’t all have to happen at once. Small adjustments over time can make a huge difference.</p>

<p>Creating a safe, sensory environment is about paying attention to your family’s specific needs. By observing and making thoughtful adjustments, you can build a space where your child can feel understood, supported, and at ease. Every child is unique and special and deserves to feel safe and loved. Just know that you are doing great and are not alone! Autismspeaks.org has multitudes of resources to connect you with physicians, other professionals, and resource guides for events and support within your community. For local support, The Buffalo Autism Project has events centered around those with autism and introduces people to the resources available in Buffalo, NY. Check out their Facebook and Instagram pages for more information.</p>

<p>(https://www.facebook.com/BuffaloAutismProject IG: @buffaloautismproject)</p>
""",
        "author": "Victoria H",
        "minutes": 8,
        "category": "spirit",
        "badge1": "Parenting",
        "badge2": "Awareness",
        "sort_order": 96,
        "featured": False
    },

    {
        "name": "Mental Fitness for Founders: Rebuilding Focus",
        "image": "https://images.pexels.com/photos/19856609/pexels-photo-19856609.jpeg",
        "description": "A reflective piece on focus, creativity, and the mental well-being of entrepreneurs.",
        "full_description": """
<p>The first question an entrepreneur should ask is not how to stay productive, but why does the mind so often slip into exhaustion in the first place? Why do we push ourselves until clarity becomes cloudy? What does focus truly mean for a founder? And where does creativity come from, if not from the deeper reservoirs of our inner life?</p>

<p>When we speak about “mental fitness,” we often imagine it as a separate domain. We see it as something to carve time out for, something to manage like an errand on a list. Yet this division implies a boundary between the mind at work and the mind at rest, as if an entrepreneur can place their thoughts on a shelf to preserve energy like spare parts.</p>

<p>But the founders are not machines. We are not cogs that run smoothly only when oiled. We are human beings, thinking and feeling at once, carrying vision, fear, excitement, and responsibility in the same breath. So rather than imagining the mind as something to control, perhaps we should try to reconnect with it and acknowledge it as part of an inseparable whole.</p>

<p>As one quarter closes and another begins, Q2 offers a chance to revisit these connections. The many pressures of Q1, such as launching projects, hitting numbers, and reestablishing pace, pull at our mental space. They create a sense that focus is something we must chase. But focus is not a target outside of ourselves. It comes from alignment, from returning to the center of who we are before we attempt to build what we want.</p>

<p>Founders often forget that creativity is not born out of relentless motion. It emerges when we pause, in the conversations that spark a new thought, in the quiet walk that clears away mental clutter, and in the moments where the mind is allowed simply to be. When entrepreneurs permit themselves to rest, they aren’t stepping back from business; they are stepping into the deeper place where new ideas form.</p>

<p>As spring arrives, let your mental landscape follow the season. Allow space for clarity to return. Invite creativity to bloom. Recognize that your business is an extension of your mind’s ability to imagine and build. And just as every tree grows from a single root, your leadership grows from your well-being.</p>

<p>Your mind is not a liability to manage, but an origin of everything you hope to create.</p>
""",
        "author": "Faizan Haq",
        "minutes": 5,
        "category": "spirit",
        "badge1": "Entrepreneurship",
        "badge2": "Mindset",
        "sort_order": 95,
        "featured": True
    },

    {
        "name": "Day of Silence: Resilience for LGBTQ+ Individuals",
        "image": "https://images.pexels.com/photos/9588017/pexels-photo-9588017.jpeg",
        "description": "A look at the meaning, history, and impact of Day of Silence for LGBTQ+ individuals.",
        "full_description": """
<p>In 1996, voices from the University of Virginia stood forth and took action to the unacceptable and hurtful behavior towards the LGBTQ+ community. Today, this campaign is celebrated every April to shed light on what many of these individuals experience every day of their lives.</p>

<p>According to National Today, Day of Silence broke through to the public nationally one year after its visibility was recognized. In 2000, the Gay, Lesbian & Straight Education Network, also known by GLSEN, adopted this as one of their official projects. In modern times, many students from diverse backgrounds participate in this day. Individuals choose to wear tape over their mouth or Xs on their hands to call further attention to the movement. At the end of the day, the silence is typically broken with a rally or some type of public speaking event, allowing all participants to end the vow in unison. Today, there are over 10,000 institutions registered as participants in this day, including all 50 states and several countries. As this day continues to grow, we remember how and why we celebrate it, all together.</p>

<p>Actions speak louder than words, and this campaign shows significance to a community that feels hatred on a daily basis. We live in a world filled with diversity, love and equality. Unfortunately, we also live in a world filled with hate, shame and encouraged hostilities that causes those influenced to take their feelings out on innocent lives. I wholeheartedly believe we deserve to live in a world where people can live peacefully among those we love and care for.</p>

<p>Love is love, and it has always existed in numerous spheres beyond that which some see as traditional. As humans, we deserve the right to freely express ourselves and who we have chosen to spend our lives with. The hate I see in modern times towards the LGBTQ+ community is absolutely crippling, and nobody deserves to live their life in fear. We all deserve to live in a diverse world where people accept those differences and live a life in ever-growing care and joy. If you are a student, I highly encourage you to participate in Day of Silence on Friday, April 10, 2026. You will not only make somebody’s day, you might even change their whole perspective on life, all together.</p>
""",
        "author": "Katy Defazio",
        "minutes": 5,
        "category": "happiness",
        "badge1": "Awareness",
        "badge2": "Equality",
        "sort_order": 94,
        "featured": False
    },

    {
        "name": "Media Corner: Review of Arc Raiders",
        "image": "https://images.pexels.com/photos/9069300/pexels-photo-9069300.jpeg",
        "description": "A review of Arc Raiders covering gameplay, player culture, and why it stands out.",
        "full_description": """
<p>Some years ago I got into a video game called Sea of Thieves. It was my first time playing an ‘extraction’ game, where other players can steal all your hard work. There were things I loved about it, and things I absolutely hated. But apparently there was more love than hate because I hung around for a couple of years and did essentially everything there was to do. But fundamentally, I could never escape the feeling that this game incentivized a practice known as griefing; playing the game for the purpose of making other players miserable.</p>

<p>I eventually lost interest as time rolled on. Other extraction games came into vogue and I had no desire to play them. I didn’t want to steal other player’s loot, and I didn’t want anyone stealing mine. So when Arc Raiders became the breakout hit of 2025, I had no intention of paying for it or playing it. But my brother wanted it, so I got it for him for Christmas. He retaliated by getting it for me as well, at which point it seemed rude not to at least try it.</p>

<p>A few weeks later I realized that essentially every scrap of my free time had been poured into this new addiction and, as much as that definitely needed to stop…I was clearly wrong about this game.</p>

<p>Yes, people can kill you and steal your stuff…but most of them refuse to do so. Mostly they’ll leave you alone or help you out. The player community overwhelmingly condemns hunting other players, and refers to people who do so as rats. I can reliably count on someone I’ve never met before giving me a health item if I need one, and I always carry extras so I can do the same. It’s just a video game, but it created a legitimate esprit de corps. It was refreshing, highly addictive, and it made me feel like video games could be a pro-social force, which is something I haven’t experienced for years.</p>

<p>The game itself is very well designed. Gameplay mechanics are simple to learn but take time to master. You’re given quests but they’re entirely optional and you can go wherever you want and do whatever you want. Players feel well rewarded for taking big risks, and they can grind low-risk activities and still get a meaningful payoff. The game includes a mechanism where the player can (optionally) retire their existing character and start a new one with some additional perks during a weeklong window that comes around every 2 months.</p>

<p>On the down side: this game needs more maps to play on. They have 5 at present, and various ‘conditions’ go into effect from time to time making the map a different experience. But after a while the rewarding feeling of mastering a map starts to fade. The developers have a road map which promises several new maps a year and this will certainly help, but it’s not hard to see a massive drop-off in player activity over the next few months until this starts to happen.</p>

<p>In any case, Arc Raiders is worth your time and money if you enjoy a challenge with the risk of occasionally getting your stuff stolen by other players.</p>
""",
        "author": "Alex Tilton",
        "minutes": 6,
        "category": "happiness",
        "badge1": "Gaming",
        "badge2": "Review",
        "sort_order": 93,
        "featured": False
    },

    {
        "name": "Get Your Mind and Body Ready for Spring",
        "image": "https://images.pexels.com/photos/7578504/pexels-photo-7578504.jpeg",
        "description": "Tips for supporting brain and body health through springtime habits and preventive care.",
        "full_description": """
<p>With the arrival of Spring, it is time to exercise both our body and our brain. Healthy eating is significant to both our mental and physical well-being. The freshest fruits and vegetables are available in grocery stores, and days are getting longer. Various nutrients including Omega 3, nuts and vitamins will help support brain health.</p>

<p>It is important to get outdoors this time of the year. Participating in leisurely activities like gardening, talking, and bike riding can send oxygen-rich blood to our brain cells. Other activities include outdoor yoga at the park, or even an outdoor concert event. Just don’t forget your ear plugs. All these activities are patiently waiting for us, so it is crucial to get out and become one with Mother Nature. Your body and brain will thank you for it.</p>

<p>It is crucial to keep up with your mind and body by seeing all necessary doctors and physicians for your long-term health. If there is something wrong with your health, your body will make that clear. Be in tune with yourself and take note of when it is the right time to see your doctor.</p>

<p>We live in a tech savvy world, and we should rely on medical professionals to help us resolve our health concerns; I cannot emphasize that enough. Remember, before undertaking any new activities or changes in lifestyle, please consult a medical professional. The staff at WNY Medical, PC can recommend dietary advice to improve the power and strength of your brain and body. To schedule an appointment, visit wnymedical.com, or call our office at 716-923-4380. Your health matters!</p>
""",
        "author": "Dr. Riffat Sadiq",
        "minutes": 5,
        "category": "health",
        "badge1": "Wellness",
        "badge2": "Spring",
        "sort_order": 92,
        "featured": False
    }

]

def seed_articles():
    db = SessionLocal()
    try:
        db.query(Article).delete()
        db.commit()

        for a in articles_data:
            db.add(Article(
                name=a["name"],
                image=a["image"],
                description=a["description"],
                full_description=a["full_description"],
                author=a.get("author"),
                minutes=a["minutes"],
                category=a["category"],
                badge1=a.get("badge1"),
                badge2=a.get("badge2"),
                sort_order=a.get("sort_order", 0),
                featured=a.get("featured", False)
            ))

        db.commit()
        print("Articles seeded successfully!")
    except Exception as e:
        import traceback
        print(f"Error seeding articles: {e}")
        traceback.print_exc()
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed_articles()