"""Visible copy for the Streamlit pages.

Home is a short story. Projects lists RIO and ProWash & Detail Co.
Screenshots live in static/projects/, the folder Streamlit serves.
"""

from __future__ import annotations

from datetime import date, datetime
from zoneinfo import ZoneInfo

NAME = "Chase Rose"
EMAIL = "Chasejrose5@gmail.com"
GITHUB_PROFILE = "https://github.com/chasejrose5-coder"

# Chase's own portrait. Served from static/ like the project screenshots.
HOME_PORTRAIT = {
    "src": "static/home/chase-home-photo.jpg",
    "alt": "Chase Rose in a tuxedo on a boat at night, with the San Francisco skyline and a bridge behind him",
    "width": 3448,
    "height": 3389,
    # Display size is about 23.5rem. These are the 1x / 2x / 3x files.
    "sizes": "(max-width: 860px) min(19.25rem, 80vw), (max-height: 740px) min(17rem, 72vw), 23.5rem",
    "srcset": (
        {"src": "static/home/chase-home-photo-352.jpg", "width": 352},
        {"src": "static/home/chase-home-photo-704.jpg", "width": 704},
        {"src": "static/home/chase-home-photo-1056.jpg", "width": 1056},
    ),
}

PAGE_COPY = {
    "home": {
        "title": "Chase Rose",
        "description": "Personal portfolio of Chase Rose. An origin story, what he is building, and life on the track and the field.",
    },
    "projects": {
        "title": "Projects — Chase Rose",
        "description": "Selected projects by Chase Rose.",
    },
}

TAGLINE = "Captain. Researcher. Builder."

FINISH = {
    "kicker": "Finish line",
    "title": "Break the tape",
    "action": "Break the tape",
    "hint": "Click, tap, or press space",
    "skip": "Skip",
}

# One lap around the page. The ids match the home sections.
LAP_MARKS = (
    ("hero", "Start"),
    ("origin-story", "Origin"),
    ("building", "Build"),
    ("track-field", "Track"),
    ("fun-facts", "Facts"),
    ("stories", "Stories"),
    ("video", "Video"),
    ("quotes", "Quotes"),
    ("contact", "Contact"),
)

SCOREBOARD_EVENT = "Stanford Invitational"
SCOREBOARD_RECORDS = "400m · 800m school records"

ORIGIN_HEADING = "Origin story"

# Lightly polished from Chase's own words. Two short paragraphs.
ORIGIN = (
    "I was always good at running, and being good at something made me feel like I fit in. Everyone I knew had their own niche.",
    "What pushed me to build things was wanting to have something to show about myself that I would be proud of. I also want to be in control of what I do in life, so I built my own things.",
)

BUILDING_HEADING = "What I'm building"

# Home cards. Detail pages keep the longer story. slugs match PROJECTS.
BUILDING = (
    {
        "slug": "rio",
        "kicker": "RIO",
        "headline": "I'm building my own 800m training app while chasing 1:55.0 at the Stanford Invitational on 3/19/27.",
        "body": "The plan is not fixed. It adapts to what I actually run, and I am building it in the middle of that training.",
        "show_countdown": True,
    },
    {
        "slug": "prowash",
        "kicker": "ProWash & Detail Co.",
        "headline": "I started ProWash & Detail Co. with a crew of three.",
        "body": "Early 2026. We detail cars, power wash, and clean solar panels and trash cans. I built the booking site so a request lands in one place instead of getting lost in texts, and I keep the work local so each job gets personal attention.",
    },
)

STORY_LINK_LABEL = "Read the story"

# Stanford Invitational. The countdown uses Pacific time, where the meet is.
RACE_DATE = "2027-03-19"
RACE_NAME = "Stanford Invitational"
RACE_ZONE = "America/Los_Angeles"

FIELD_HEADING = "On the track and the field"

FIELD = (
    {
        "title": "Track",
        "text": "Three-year captain. I hold the school records in the 400m and the 800m. Team MVP in 2025–26, NCS finalist, and 2× All-League in the 400m and the 4×100m.",
    },
    {
        "title": "Soccer",
        "text": "Three-year captain. In 2026 I was League Offensive Player of the Year and BCL Championship MVP.",
    },
)

FUN_FACTS_HEADING = "Fun facts"

# Front is the hook. Back is the fact already on the page. Nothing new.
FUN_FACTS = (
    {
        "front": "12-page thesis",
        "back": "Wrote a 12-page thesis on West African soccer academies (JRP Honorable Mention).",
    },
    {
        "front": "Drew Robinson",
        "back": "Interviewed former MLB player Drew Robinson live on stage.",
    },
    {
        "front": "Student store",
        "back": "Student Body Treasurer who ran the student store.",
    },
)

COMING_SOON_LABEL = "Coming soon"

FUN_FACT_PLACEHOLDERS = (
    "Fun fact coming soon",
    "Fun fact coming soon",
    "Fun fact coming soon",
)

STORIES_HEADING = "Stories"

STORIES_LEAD = "Crazy and fun stories will go here."

STORY_PLACEHOLDERS = (
    {
        "title": "Story coming soon",
        "text": "A story will go here.",
    },
    {
        "title": "Story coming soon",
        "text": "A story will go here.",
    },
    {
        "title": "Story coming soon",
        "text": "A story will go here.",
    },
)

VIDEO_HEADING = "Video"

VIDEO_PLACEHOLDER = "Video coming soon"

QUOTES_HEADING = "Quotes"

CONTACT_HEADING = "Contact"

GITHUB_LINK_LABEL = "GitHub"

RESUME_LINK_LABEL = "Download resume"

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
        "blurb": "An 800m training app that adapts the plan to what you actually run.",
        "href": "https://www.riorunning.com",
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
            {
                "src": "static/projects/rio/about.jpg",
                "alt": "A stadium during a track meet, the photograph on RIO’s About page",
                "width": 1600,
                "height": 1070,
            },
            None,
            {
                "src": "static/projects/rio/goal.png",
                "alt": "Goal: 1:55.0 around the Stanford Invitational, March 2027",
                "width": 1600,
                "height": 760,
            },
            {
                "src": "static/projects/rio/blocks.webp",
                "alt": "Chase Rose driving out of the blocks",
                "width": 1600,
                "height": 1067,
            },
        ),
        "paragraphs": (
            "Rio is a distance training app for runners, initially focused on the 800m. The name is Runner Intelligence Owned. I wanted a plan that belonged to the athlete running it, not one handed down from the outside. It is built by a runner, for a runner. Your race, your plan, your result.",
            "The biggest part of RIO is that the workout plan is not fixed. It auto-adapts as you progress through the season. Most plans tell you what to run. RIO shows you why, and it adjusts when the season does not go to script.",
            "I am chasing 1:55.0 at the Stanford Invitational on March 19, 2027. I am building the app in the middle of that training.",
            "The workouts did not come from a template I found. I read the physiology and the training ideas behind an 800, then used that, and the code, to build the workout logic and the classifiers that read a session. The product and the training move together.",
        ),
        "ahead": {
            "title": "Where I want RIO to go",
            "lead": "I am still shipping RIO, and I am building it while I train toward the Stanford Invitational on March 19, 2027. Here is what the app already does, and where I want it to go.",
            "groups": (
                {
                    "label": "Shipped now",
                    "items": (
                        "It connects to Strava.",
                        "After a planned hard day, it scores the session.",
                        "Plan lays the season out by phase.",
                        "Start session runs the workout, and the debrief follows.",
                    ),
                },
                {
                    "label": "Next",
                    "items": (
                        "Deeper adaptation, with the why shown on every session as the plan changes.",
                        "A fuller Insights view, beyond the note that appears after a hard day.",
                        "Sharper session classifiers, so the app gets better at reading what a workout was and what that means for the next one.",
                    ),
                },
                {
                    "label": "Later",
                    "items": (
                        "I want to leave Strava and connect instead to key health-data figures, like Apple Health or Garmin.",
                        "A goal-completion probability: a clear read on how likely the athlete is to hit their goal time. For me that is 1:55.0, and the read should move as the season goes.",
                        "A language model that can explain the season and the sessions in plain language, and that an athlete can talk back and forth with if they choose to.",
                        "Support for different kinds of 800m runners, a speedier 800 and a more endurance-oriented 800. I also want to include other race events spanning from the 400m dash to the 3200m.",
                    ),
                },
            ),
        },
    },
    {
        "slug": "prowash",
        "title": "ProWash & Detail Co.",
        "dates": "Early 2026 – Present",
        "role": "Founder & Managing Partner",
        "year": "Early 2026 – Present",
        "blurb": "A local mobile detailing and power-washing business with online booking.",
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
            None,
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
            {
                "src": "static/projects/prowash/book.jpg",
                "alt": "ProWash booking form",
                "width": 1423,
                "height": 1838,
            },
            {
                "src": "static/projects/prowash/calendar.jpg",
                "alt": "Public calendar showing open appointment times.",
                "width": 1420,
                "height": 1300,
            },
        ),
        "paragraphs": (
            "I founded ProWash & Detail Co. in early 2026. It is a local mobile detailing and power washing business. We detail cars, power wash, clean solar panels, and clean trash cans. I built the booking site for the business I run.",
            "Car detailing and power washing are the jobs at the curb.",
            "Solar panel cleaning and trash can cleaning are the rest of the property.",
            "Clients book open times online, and my crew of three gets a private page to accept jobs and manage shifts. I built the site so a request lands in one place instead of getting lost in texts.",
            "The public calendar shows open appointment times. That is the public view: when we can come.",
            "That is a crew of about three, plus me. The jobs live on that page instead of in a string of texts. I keep the work local so each job gets personal attention.",
        ),
    },
)


def days_until_race(today: date | None = None) -> int:
    """Whole days from a Pacific calendar date until the Stanford Invitational."""
    if today is None:
        today = datetime.now(ZoneInfo(RACE_ZONE)).date()
    return (date.fromisoformat(RACE_DATE) - today).days


def countdown_parts(days: int, race_name: str = RACE_NAME) -> tuple[str, str]:
    """Return the big count and the words beside it.

    The JavaScript countdown in js/main.js uses the same four cases.
    """
    if days > 1:
        return str(days), f"days until the {race_name}"
    if days == 1:
        return "1", f"day until the {race_name}"
    if days == 0:
        return "Today", f"is the {race_name}"
    ago = abs(days)
    unit = "day" if ago == 1 else "days"
    return str(ago), f"{unit} since the {race_name}"
