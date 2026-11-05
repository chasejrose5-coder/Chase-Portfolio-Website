"""Visible copy ported from the static pages.

Nothing here is invented. Placeholder sentences are the text already in
index.html, projects.html, and resume.html.
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

TAGLINE = "A short tagline about what you do."

INTRO = (
    "Write a short paragraph about where you are from and what you care about. "
    "Two or three sentences is enough. This is the first thing people read after your name.",
    "Use this second paragraph for school, the work you want, or what you are focused on right now. "
    "Then delete these sentences and add your own.",
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
                "title": "Your University — Class of 20XX",
                "degree": "Bachelor of Arts in Your Major",
                "bullets": (
                    "Add a GPA, honor, or concentration.",
                    "Add a second detail if you want one.",
                ),
            },
            {
                "title": "Another School — Class of 20XX",
                "degree": "Degree or program name",
                "bullets": ("A course, award, or activity worth listing.",),
            },
        ),
    },
    {
        "id": "experience",
        "heading": "Work Experience",
        "entries": (
            {
                "title": "Role Title @ Company Name | City, ST (Month Year – Present)",
                "degree": None,
                "bullets": (
                    "Describe a responsibility or a result in one line.",
                    "Add another bullet the way you would on a resume.",
                ),
            },
            {
                "title": "Earlier Role @ Earlier Company | City, ST (Month Year – Month Year)",
                "degree": None,
                "bullets": (
                    "What you worked on, who it was for, or what changed because of it.",
                    "A tool, team, or skill this role used.",
                ),
            },
        ),
    },
    {
        "id": "leadership",
        "heading": "Leadership & Extracurriculars",
        "entries": (
            {
                "title": "Organization Name, Your Role (Year – Year)",
                "degree": None,
                "bullets": (
                    "What you led, built, or showed up for.",
                    "A result, a team size, or a thing you are proud of.",
                ),
            },
            {
                "title": "Club or Team, Role (Year – Year)",
                "degree": None,
                "bullets": ("One concrete detail is better than a long list of duties.",),
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
                    "Design tool or software you actually use",
                    "A writing, research, or technical skill",
                    "Another tool or strength to swap in",
                ),
            },
        ),
    },
)
