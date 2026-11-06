"""Visible copy for the Streamlit pages.

Home and Resume use Chase's wording. Projects lists RIO and
ProWash & Detail Co. Screenshots live in static/projects/, the folder
Streamlit serves.
"""

from __future__ import annotations

NAME = "Chase Rose"
EMAIL = "Chasejrose5@gmail.com"
GITHUB_PROFILE = "https://github.com/chasejrose5-coder"

# Chase's own portrait. Served from static/ like the project screenshots.
HOME_PORTRAIT = {
    "src": "static/home/chase-home-photo.jpg",
    "alt": "Chase Rose in a tuxedo on a boat at night, with the San Francisco skyline and a bridge behind him",
    "width": 3448,
    "height": 3389,
}

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
    "My name is Chase Rose. I am a senior at Bentley Upper School in Lafayette, CA. My primary focus is on entrepreneurship and leadership. I have served as a three-year captain of both the track & field and soccer teams. I have set school records in both the 400m and 800m, earned multiple All-League honors, and was named Team MVP in both sports as well as All-League MVP in the 2026 soccer season. Aside from sports, I participate in student government, paper research, and building programs to solve problems.",
    "I founded a local mobile detailing business, wrote a research thesis on West African soccer academies, and am currently building a runner training app named RIO. I care about leadership that is forward-thinking and intentional, whether that’s being part of a relay, managing a student store and its inventory, interviewing nationally recognized figures on stage, or organizing community service. I’m looking to carry that same standard into college and beyond.",
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
        "dates": "Early 2026 – Present",
        "role": "Founder",
        "year": "Early 2026 – Present",
        "href": "https://riotraining.streamlit.app",
        "link_label": "Open RIO",
        "code_href": "https://github.com/chasejrose5-coder/rio",
        "code_label": "GitHub",
        "thumb": {
            "src": "static/projects/rio/first-screen.jpg",
            "alt": "RIO first screen: Your Race, Your Plan, Your Result, over the track",
            "width": 1600,
            "height": 1000,
        },
        "hero": {
            "src": "static/projects/rio/first-screen.jpg",
            "alt": "RIO first screen: Your Race, Your Plan, Your Result, over the track",
            "width": 1600,
            "height": 1000,
        },
        "frames": (
            None,
            None,
            None,
            {
                "src": "static/projects/rio/blocks.webp",
                "alt": "Chase Rose driving out of the blocks",
                "width": 1600,
                "height": 1067,
            },
            {
                "src": "static/projects/rio/goal.png",
                "alt": "1:55.0 at the Stanford Invitational, March 2027",
                "width": 1600,
                "height": 760,
            },
            None,
            {
                "src": "static/projects/rio/about.jpg",
                "alt": "A stadium during a track meet, the photograph on RIO’s About page",
                "width": 1600,
                "height": 1070,
            },
        ),
        "paragraphs": (
            "RIO is the 800m training app I am building while I train. The name is Runner Intelligence Owned. I wanted a plan that belonged to the athlete running it, not one handed down from the outside. Built by a runner, for runners. Your race, your plan, your result.",
            "The biggest part of RIO is that the workout plan is not fixed. It auto-adapts as you progress through the season. Most plans tell you what to run. RIO shows you why, and it adjusts when the season does not go to script. After a hard session, the app reads how the day went, and the later weeks can change instead of staying frozen from week one.",
            "Home is where the season stands. RIO connects to Strava. After a planned hard day it scores the session, and Home shows this week, the current phase, and the insights that come back once the workout is done.",
            "I am chasing 1:55.0. The goal sits around the Stanford Invitational in March 2027. I am building the app in the middle of that training, so the product and the racing share a calendar.",
            "Plan is the season laid out. The phases sit on the weeks as they actually fall. I can see where this week lives in the longer build toward March.",
            "Start session is the workout itself: the reps, the rest, and what the session is for. Afterward the debrief is the point, what the day was meant to be and what it was. Profile keeps the goal on the page, a Goal 800m time.",
            "The workouts did not come from a template I found. I read the physiology and the training ideas behind an 800, then used that, and the code, to build the workout logic and the classifiers that read a session. The product and the training move together.",
        ),
        "ahead": {
            "title": "Where I want RIO to go",
            "lead": "I am still shipping RIO, and I am building it while I train toward March. Here is where I want the app to go:",
            "items": (
                "The plan should keep adapting more deeply as the season unfolds, so later weeks rewrite themselves from what actually happened, not from a sheet written in week one.",
                "A fuller Insights place to read the season back, beyond the note that appears after a hard day.",
                "A clearer picture of whether the training is on track for 1:55.0 at the Stanford Invitational, updated as hard days are done.",
                "Sharper session classifiers, so the app gets better at understanding what a workout really was and what that means for the next one.",
                "A stronger why on every session. Every rep has a reason, and that reason should stay visible as the plan changes.",
                "Tighter use of Strava, so what you actually ran feeds the next version of the plan.",
                "Smarter handling when a hard day goes off script, instead of the rest of the season pretending nothing changed.",
                "Week-to-week explanations of how this block sits in the longer build.",
                "Keep the product and the racing on the same calendar through the Stanford Invitational in March 2027.",
                "I want a goal-completion probability: a clear read on how likely the athlete is to hit their goal time. For me that is 1:55.0, and the read should move as the season goes. It is not a number I show the public yet.",
                "I want a language model in the program, so the app can explain the season, the sessions, and what comes next in plain language, not as a dump of raw data.",
                "I want the plan and the logic to work for different kinds of 800m runners, a speedier 800 and a more endurance-oriented 800.",
                "I want a lot of other events beyond the 800m, with the plan, the scoring, and the adaptation working for those events too.",
            ),
        },
    },
    {
        "slug": "prowash",
        "title": "ProWash & Detail Co.",
        "dates": "Early 2026 – Present",
        "role": "Founder & Managing Partner",
        "year": "Early 2026 – Present",
        "href": "https://prowash.streamlit.app",
        "link_label": "Open ProWash",
        "code_href": "https://github.com/chasejrose5-coder/prowash-site",
        "code_label": "GitHub",
        "thumb": {
            "src": "static/projects/prowash/mark.png",
            "alt": "PW&D, the ProWash & Detail Co. mark",
            "width": 1139,
            "height": 385,
            "mark": True,
        },
        "hero": {
            "src": "static/projects/prowash/mark.png",
            "alt": "PW&D, the ProWash & Detail Co. mark",
            "width": 1139,
            "height": 385,
            "mark": True,
        },
        "frames": (
            {
                "src": "static/projects/prowash/work.png",
                "alt": "The work: car detailing, power washing, solar panel cleaning, and trash can cleaning",
                "width": 1600,
                "height": 980,
            },
            {
                "src": "static/projects/prowash/curb.png",
                "alt": "Car detailing and power washing",
                "width": 1600,
                "height": 460,
            },
            {
                "src": "static/projects/prowash/property.png",
                "alt": "Solar panel cleaning and trash can cleaning",
                "width": 1600,
                "height": 460,
            },
            None,
            None,
            None,
        ),
        "paragraphs": (
            "I founded ProWash & Detail Co. in early 2026. It is a local mobile detailing and power washing business. We detail cars, power wash, clean solar panels, and clean trash cans. The mark is PW&D, short enough to sit next to the work.",
            "Car detailing and power washing are the jobs at the curb.",
            "Solar panel cleaning and trash can cleaning are the rest of the property.",
            "Clients book online. I built the site so a request lands in one place instead of getting lost in texts. The public calendar shows open appointment times. That is the whole view: when we can come, not who else is booked.",
            "The staff side is how the crew actually runs. Visitors get a Staff sign-in. Once someone is signed in, they see the appointments: pending requests waiting for a yes, and the times that have been accepted show as booked on the public calendar.",
            "Mason, Luke, Noah, and I each have a schedule page, and there is a Completed archive. Staff can search and filter the jobs, accept or decline a request, and claim a shift. Names, shifts, and blackout dates stay on those pages. This page is separate from the public site. Visitors never see this list.",
            "That is a crew of about three, plus me. The jobs live there instead of in a string of texts. I would rather keep the work local and careful than pretend the business is bigger than it is.",
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
                    "SAT: 700 English · 780 Math",
                    "Selected coursework: AP Physics C: Mechanics, AP Calculus BC, AP Computer Science, AP Statistics, Honors Engineering, and additional honors courses",
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
                "title": "RIO Training App — Creator / Coder / Researcher",
                "degree": None,
                "bullets": (
                    "Building a Distance training app; researched physiological and neurological body systems while utilizing a coding agent to build workout algorithms and classifier algorithms for athlete session data.",
                ),
            },
            {
                "title": "Bentley Junior Research Program — Independent Student Researcher",
                "degree": None,
                "bullets": (
                    "12-page thesis on colonial origins & labor migration in West African soccer academies; awarded JRP Honorable Mention.",
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
                    "Community Service & Rehabilitation patient support",
                ),
            },
        ),
    },
)
