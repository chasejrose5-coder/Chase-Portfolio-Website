"""Visible copy for the portfolio pages.

Home and Resume use Chase's wording. Projects is still the scaffold text
from projects.html.
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

PROJECTS_TITLE = "My Projects"
PROJECTS_KICKER = "(both serious and fun!)"

PROJECTS = (
    {
        "title": "Field Guide",
        "role": "Founder, Editor",
        "href": "https://github.com",
        "label": "Visit Website",
        "paragraphs": (
            "Replace this with what the project is. Say who it is for, when it started, and why it exists. One short paragraph is the right length.",
            "Use a second paragraph for your role now. Mention what you edit, design, or keep running.",
        ),
    },
    {
        "title": "Listening Notes",
        "role": "Music project",
        "href": "https://www.instagram.com",
        "label": "Visit Account",
        "paragraphs": (
            "A sample side project. Describe a personal account, channel, or hobby you share in public, and what got you started.",
            "Then say what someone will find if they follow the link: songs, notes, videos, or a list you keep up to date.",
        ),
    },
    {
        "title": "Name That Tune",
        "role": "Creator",
        "href": "https://codepen.io",
        "label": "View Project",
        "paragraphs": (
            "A sample for a small game, tool, or experiment. Explain the premise in plain language so a new reader gets it immediately.",
            "Add one result if you have it: people who used it, something you learned, or why you still keep it online.",
        ),
    },
    {
        "title": "Studio Markup",
        "role": "Website design",
        "href": "https://github.com",
        "label": "GitHub",
        "paragraphs": (
            "A sample client or collaboration project. Name who you worked with and what you were asked to make.",
            "Close with what the site includes and where the work lives now. Swap the button label if “GitHub” is not the right word.",
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
