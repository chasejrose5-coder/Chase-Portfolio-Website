"""Visible copy for the Streamlit pages.

Home and Resume use Chase's wording. Projects lists RIO and
ProWash & Detail Co. Screenshots live under assets/projects/.
"""

from __future__ import annotations

NAME = "Chase Rose"
EMAIL = "Chasejrose5@gmail.com"

PAGE_COPY = {
    "home": {
        "title": "Chase Rose",
        "description": "Personal portfolio of Chase Rose. Introduction, projects, and resume.",
    },
    "projects": {
        "title": "Projects — Chase Rose",
        "description": "Selected projects by Chase Rose.",
    },
    "resume": {
        "title": "Resume — Chase Rose",
        "description": "Resume of Chase Rose. Education, experience, leadership, and skills.",
    },
}

TAGLINE = "Captain. Researcher. Builder. Chasing excellence on the track, the pitch, and beyond."

INTRO = (
    "I’m Chase Rose, a senior at Bentley Upper School in Lafayette, California, where I have served as a three-year captain of both the track & field and soccer teams. I have set school records in both the 400m and 800m, earned multiple All-League honors, and was named Team MVP in both sports as well as All league MVP in the 2026 soccer season. Aside from sports, I participate in student government, paper research, and building programs to fix issues that help athletes.",
    "Outside of sports I founded a local mobile detailing business, wrote a research thesis on West African soccer academies (JRP Honorable Mention), and am currently building an 800m training app. I care about leadership that actually shows up, whether that’s being part of a relay, managing a student store and its inventory, interviewing nationally recognized figures on stage, or organizing community service. I’m looking to carry that same standard into college and beyond.",
)

QUOTES = (
    {
        "text": "I thought I’d solved a problem when really I was creating new ones by taking the path of least resistance.",
        "attribution": "David Goggins, Can’t Hurt Me: Master Your Mind and Defy the Odds",
    },
    {
        "text": (
            "Those times when you get up early and you work hard; those times when you stay up late "
            "and you work hard; those times when you don’t feel like working, you’re too tired, you "
            "don’t want to push yourself, but you do it anyway; that is actually the dream. That’s the "
            "dream. It’s not the destination, it’s the journey."
        ),
        "attribution": "Kobe Bryant",
    },
    {
        "text": "The mind is everything. What you think you become.",
        "attribution": "Buddha",
    },
)

# Streamlit page paths cannot contain a slash, so each slug is its own route.
# Detail pages place a straight frame after each paragraph that has one.

PROJECTS = (
    {
        "slug": "rio",
        "title": "RIO",
        "dates": "2025 – Present",
        "role": "Founder",
        "year": "2025–Present",
        "href": "https://riotraining.streamlit.app",
        "link_label": "Open RIO",
        "thumb": {
            "src": "assets/projects/rio/thumb.webp",
            "alt": "RIO splash screen",
            "width": 960,
            "height": 600,
        },
        "hero": {
            "src": "assets/projects/rio/hero.webp",
            "alt": "RIO splash screen: Your Race, Your Plan, Your Result",
            "width": 1280,
            "height": 900,
        },
        "frames": (
            {
                "src": "assets/projects/rio/home.webp",
                "alt": "RIO home screen, 150 days from a 1:55 goal",
                "width": 1600,
                "height": 893,
            },
            {
                "src": "assets/projects/rio/blocks.webp",
                "alt": "Chase Rose driving out of the blocks",
                "width": 1600,
                "height": 1067,
            },
            {
                "src": "assets/projects/rio/plan.webp",
                "alt": "RIO plan page with the season calendar",
                "width": 1440,
                "height": 1100,
            },
            {
                "src": "assets/projects/rio/session.webp",
                "alt": "RIO start-session screen for a Thursday speed workout",
                "width": 1600,
                "height": 893,
            },
        ),
        "paragraphs": (
            "RIO is the 800m training app I’m building for runners. Plans, hard-day scoring, and insights sit in one place.",
            "I built it while chasing 1:55.0 at the Stanford Invitational, with the goal set around March 2027.",
            "It connects to Strava, scores the session after a planned hard day, and Home shows where the season stands.",
            "I’m still shipping it while I train. The product and the training move together.",
        ),
        "mobile_preview": {
            "src": "assets/projects/rio/phone.webp",
            "alt": "RIO Start session screen, cropped inside a phone frame",
            "width": 700,
            "height": 893,
            "kicker": "Mobile preview",
            "note": "Coming to mobile. This is the Start session screen, cropped into a phone. Not shipped, and not on the App Store.",
        },
    },
    {
        "slug": "prowash",
        "title": "ProWash & Detail Co.",
        "dates": "Present",
        "role": "Founder & Managing Partner",
        "year": "Present",
        "href": "https://prowash.streamlit.app",
        "link_label": "Open ProWash",
        "thumb": {
            "src": "assets/projects/prowash/thumb.webp",
            "alt": "ProWash & Detail Co.",
            "width": 960,
            "height": 600,
        },
        "hero": {
            "src": "assets/projects/prowash/hero.webp",
            "alt": "ProWash & Detail Co. site header",
            "width": 1400,
            "height": 397,
        },
        "frames": (
            {
                "src": "assets/projects/prowash/services.webp",
                "alt": "ProWash services: car detailing, power washing, solar panel cleaning, and trash can cleaning",
                "width": 1392,
                "height": 1484,
            },
            {
                "src": "assets/projects/prowash/booking.webp",
                "alt": "ProWash booking form",
                "width": 1400,
                "height": 1888,
            },
            {
                "src": "assets/projects/prowash/calendar.webp",
                "alt": "ProWash calendar of open appointment times",
                "width": 1392,
                "height": 965,
            },
        ),
        "paragraphs": (
            "I founded ProWash & Detail Co., a local mobile detailing and power washing business.",
            "We detail cars, power wash, clean solar panels, and clean trash cans. Clients book online.",
            "I managed the schedule, the equipment, and a small crew of about three people.",
            "I built the booking site so a request lands in one place instead of getting lost in texts.",
        ),
    },
)

RESUME_TITLE = "My Resume"

RESUME_SECTIONS = (
    {
        "id": "education",
        "heading": "Education",
        "entries": (
            {
                "title": "Bentley Upper School, Lafayette, CA — Class of 2027",
                "degree": "High School Diploma / College Preparatory Program",
                "bullets": (
                    "3.92 unweighted / 4.42 weighted GPA",
                    "Junior Research Program (JRP) Honorable Mention; 400m/800m school record holder",
                ),
            },
        ),
    },
    {
        "id": "leadership",
        "heading": "Leadership & Extracurriculars",
        "entries": (
            {
                "title": "Bentley Track & Field — Team Captain (Grades 10–12)",
                "degree": None,
                "bullets": (
                    "Team MVP (2025–26); 2× All-League (400m, 4×100m); 400m/800m school record holder; NCS finalist",
                    "Led workouts, pacing, and relays as 3-year captain; 400m/800m specialist",
                ),
            },
            {
                "title": "Bentley Soccer — Varsity Team Captain (Grades 10–12), Striker",
                "degree": None,
                "bullets": (
                    "2026 League Offensive Player of the Year; 2026 BCL Championship MVP; Team MVP (’24–’25); 2× All-League (’24, ’25); Phoenix Award (’23–’24)",
                    "3-year captain",
                ),
            },
            {
                "title": "Student Body Treasurer (former Class President & Ambassador)",
                "degree": None,
                "bullets": (
                    "Managed the student store (inventory restocking + revenue tracking); organized class spirit events; led campus tours.",
                ),
            },
            {
                "title": "ProWash & Detail Co. — Founder & Managing Partner",
                "degree": None,
                "bullets": (
                    "Founded a local mobile detailing & power washing business; managed 3 employees, client scheduling, and equipment.",
                ),
            },
            {
                "title": "800m Training App — Creator / Coder / Researcher",
                "degree": None,
                "bullets": (
                    "Building an 800m training app; researched physiological and neurological body systems while utilizing a coding agent to build workout algorithms and classifier algorithms for athlete session data.",
                ),
            },
            {
                "title": "Bentley Junior Research Program — Independent Student Researcher",
                "degree": None,
                "bullets": (
                    "Wrote a 12-page thesis on colonial origins & labor migration in West African soccer academies; awarded JRP Honorable Mention.",
                ),
            },
            {
                "title": "Bentley Student Life & Mental Wellness Programming — Co-Facilitator & Stage Moderator",
                "degree": None,
                "bullets": (
                    "Co-facilitated mental health assembly; led live onstage interview with former MLB player Drew Robinson.",
                ),
            },
            {
                "title": "Alameda County Community Food Bank — Community Volunteer",
                "degree": None,
                "bullets": (
                    "Sorted, weighed, and boxed produce/dry goods; Supported East Bay residents.",
                ),
            },
            {
                "title": "Lamorinda Orthopedics and Sport PT — Volunteer Service Worker",
                "degree": None,
                "bullets": (
                    "Assisted PTs with rehab setups, cleaning, and equipment prep; I also helped by guiding patients through exercises",
                ),
            },
        ),
    },
    {
        "id": "skills",
        "heading": "Skills",
        "entries": (
            {
                "title": None,
                "degree": None,
                "bullets": (
                    "Leadership & Team Captaining",
                    "Public Speaking / On-stage Moderation",
                    "Event Organization & Campus Tours",
                    "Student Store Operations / Basic Revenue Tracking",
                    "Small Business Operations (scheduling, employees, marketing, equipment)",
                    "Research Writing & Thesis Development",
                    "Coding / App Development (workout algorithms, athlete data classification)",
                    "Physiological & Training Knowledge (track/soccer)",
                    "Inventory Management & Logistics",
                    "Community Service & Patient Interaction Support",
                ),
            },
        ),
    },
)
