"""Visible copy for the Streamlit pages.

Home, the quotes, and the resume are the placeholder text from the static
pages. Project entries are empty slots for the work index and detail pages.
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

# Empty project slots. Titles, dates, and paragraphs are placeholders.
# Detail pages alternate these paragraphs with framed image placeholders.
# Streamlit page paths cannot contain a slash, so each slug is its own route.

_PARAGRAPHS = (
    "I will replace this with a short note about how this started.",
    "I will replace this with what I did next, in a sentence or two.",
    "I will replace this with a constraint, a decision, or a result.",
    "I will replace this with a closing line in my own words.",
)

PROJECTS = (
    {
        "slug": "project-one",
        "title": "Project one",
        "dates": "Month Year – Present",
        "role": "Role",
        "year": "Year",
        "href": "https://example.com",
        "link_label": "Link label",
        "paragraphs": _PARAGRAPHS,
    },
    {
        "slug": "project-two",
        "title": "Project two",
        "dates": "Month Year – Month Year",
        "role": "Role",
        "year": "Year",
        "href": "https://example.com",
        "link_label": "Link label",
        "paragraphs": _PARAGRAPHS,
    },
    {
        "slug": "project-three",
        "title": "Project three",
        "dates": "Year – Year",
        "role": "Role",
        "year": "Year",
        "href": "https://example.com",
        "link_label": "Link label",
        "paragraphs": _PARAGRAPHS,
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
