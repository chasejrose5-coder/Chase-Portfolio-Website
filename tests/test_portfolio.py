"""Story-first portfolio: copy, section order, and what was removed."""

from __future__ import annotations

import tempfile
import unittest
from datetime import date
from pathlib import Path

from portfolio.content import (
    FUN_FACT_PLACEHOLDERS,
    PAGE_COPY,
    PROJECTS,
    QUOTES,
    RACE_DATE,
    STORY_PLACEHOLDERS,
    countdown_parts,
    days_until_race,
)
from portfolio.layout import NAV
from portfolio.content import GHOST_800_PACE_SECONDS
from portfolio.pages import _finish_gate, _gun_opener, home_main_html, project_detail_html, resume_public_path

ROOT = Path(__file__).resolve().parents[1]


class CountdownTests(unittest.TestCase):
    def test_days_until_race(self):
        self.assertEqual(days_until_race(date(2027, 3, 18)), 1)
        self.assertEqual(days_until_race(date(2027, 3, 19)), 0)
        self.assertEqual(days_until_race(date(2027, 3, 20)), -1)
        self.assertGreater(days_until_race(date(2026, 11, 17)), 1)

    def test_countdown_wording(self):
        self.assertEqual(countdown_parts(122), ("122", "days until the Stanford Invitational"))
        self.assertEqual(countdown_parts(1), ("1", "day until the Stanford Invitational"))
        self.assertEqual(countdown_parts(0), ("Today", "is the Stanford Invitational"))
        self.assertEqual(countdown_parts(-1), ("1", "day since the Stanford Invitational"))
        self.assertEqual(countdown_parts(-4), ("4", "days since the Stanford Invitational"))


class HomeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = home_main_html()

    def test_section_order(self):
        ids = [
            "origin-story",
            "building",
            "track-field",
            "fun-facts",
            "stories",
            "video",
            "quotes",
            "contact",
            "blooper",
        ]
        positions = [self.html.index(f'id="{item}"') for item in ids]
        self.assertEqual(positions, sorted(positions))
        self.assertLess(self.html.index("<h1"), positions[0])
        self.assertIn("Chase Rose", self.html)
        self.assertIn("Captain. Researcher. Builder.", self.html)
        self.assertIn("app/static/home/chase-home-photo.jpg", self.html)

    def test_origin_keeps_his_meaning(self):
        self.assertIn("good at running", self.html)
        self.assertIn("their own niche", self.html)
        self.assertIn("proud of", self.html)
        self.assertIn("in control of what I do", self.html)

    def test_building_cards_and_countdown(self):
        self.assertIn("1:55.0", self.html)
        self.assertIn("Stanford Invitational", self.html)
        self.assertIn("3/19/27", self.html)
        self.assertIn('data-race-date="2027-03-19"', self.html)
        self.assertIn('data-race-zone="America/Los_Angeles"', self.html)
        count, rest = countdown_parts(days_until_race())
        self.assertIn(f'class="race-count">{count}<', self.html)
        self.assertIn(rest, self.html)
        self.assertIn("crew of three", self.html)
        self.assertIn('href="rio"', self.html)
        self.assertIn('href="prowash"', self.html)
        self.assertIn("https://www.riorunning.com", self.html)
        self.assertIn("https://github.com/chasejrose5-coder/rio", self.html)
        self.assertIn("https://prowash.streamlit.app", self.html)
        self.assertIn("https://github.com/chasejrose5-coder/prowash-site", self.html)

    def test_track_and_field_uses_existing_facts(self):
        self.assertIn("school records in the 400m and the 800m", self.html)
        self.assertIn("Team MVP in 2025", self.html)
        self.assertIn("NCS finalist", self.html)
        self.assertIn("2× All-League", self.html)
        self.assertIn("League Offensive Player of the Year", self.html)
        self.assertIn("BCL Championship MVP", self.html)
        self.assertEqual(self.html.count("Three-year captain"), 2)

    def test_finish_line_lap_scoreboard_and_flips(self):
        gate = _finish_gate()
        self.assertIn('id="finish-gate"', gate)
        self.assertIn('class="finish-skip"', gate)
        self.assertIn(">Skip<", gate)
        self.assertIn("Break the tape", gate)
        self.assertIn("chase-finish-seen", gate)
        self.assertIn("position:fixed", gate)
        self.assertIn('id="lap"', self.html)
        self.assertIn('id="lap-runner"', self.html)
        self.assertIn("400m 50.9 · 800m 2:02.9", self.html)
        self.assertIn('class="scoreboard', self.html)
        self.assertIn('class="flip"', self.html)
        self.assertGreaterEqual(self.html.count('class="flip"'), 3)
        self.assertIn('aria-pressed="false"', self.html)
        css = (ROOT / "css" / "meet.css").read_text(encoding="utf-8")
        self.assertIn("min-height: 44px", css)
        self.assertIn("min-width: 44px", css)
        self.assertIn("prefers-reduced-motion", css)
        script = (ROOT / "js" / "main.js").read_text(encoding="utf-8")
        self.assertIn("chase-finish-seen", script)
        self.assertIn('event.key === " "', script)
        self.assertIn("prefers-reduced-motion", script)
        self.assertIn("Tuxedo. A boat. The bridge is back there.", self.html)
        self.assertIn("False start. Back on the line.", self.html)
        self.assertIn('id="scoreboard-hit"', self.html)
        self.assertIn('data-goal="1:55.0"', self.html)
        self.assertIn("the short version", self.html)
        gun = _gun_opener()
        self.assertIn('id="start-gun"', gun)
        self.assertIn("On your marks", gun)
        self.assertNotIn(">Skip<", gun)
        self.assertIn("Enter", gun)
        self.assertEqual(self.html.count('class="lane-btn"'), 8)
        self.assertIn('id="run-it"', self.html)
        self.assertIn("New PR!", self.html)
        self.assertIn("Chase still wins", self.html)
        self.assertIn("2:02.9", self.html)
        self.assertEqual(GHOST_800_PACE_SECONDS, 122.9)
        self.assertIn("Leaned so hard the track had to catch me.", self.html)
        self.assertIn("Dad said 54.", self.html)
        self.assertIn("playsinline", self.html)
        self.assertIn("Kobe Bryant, 2009 (reference photo)", self.html)
        self.assertNotIn("THAT WAS ABOUT MY DAD", self.html)
        self.assertIn("Met a gold medalist. Asked for tips. Got a photo.", self.html)
        self.assertIn("Number 5. Bentley black and gold.", self.html)
        self.assertIn("The goal", self.html)
        self.assertIn("The assist", self.html)
        self.assertIn("Eleven crossed it.", self.html)
        self.assertIn("Right wing. Low cross.", self.html)
        self.assertIn('preload="none"', self.html)
        self.assertIn("goal-loop.mp4", self.html)
        self.assertIn("assist-loop.mp4", self.html)
        self.assertIn('id="oval-svg"', self.html)
        self.assertGreater(GHOST_800_PACE_SECONDS, 0)
        meet = (ROOT / "js" / "meet.js").read_text(encoding="utf-8")
        self.assertIn('event.key === "Enter"', meet)
        self.assertIn("smoke-canvas", meet)
        self.assertIn("is-smoking", meet)
        self.assertIn('id="pitch"', self.html)
        self.assertIn('id="goals-count"', self.html)
        self.assertIn('id="whistle"', self.html)
        self.assertIn('id="infield-copy"', self.html)
        self.assertIn("prefers-reduced-motion", meet)
        self.assertIn('id="cursor-pace"', self.html)
        self.assertIn('id="baton-pass"', self.html)
        self.assertIn('id="photo-frame"', self.html)
        self.assertIn("Pass the baton", self.html)
        self.assertIn("Your hand", self.html)
        self.assertIn("showPhoto", meet)

    def test_fun_facts_and_placeholders(self):
        self.assertIn("12-page thesis", self.html)
        self.assertIn("West African soccer academies", self.html)
        self.assertIn("JRP Honorable Mention", self.html)
        self.assertIn("Drew Robinson", self.html)
        self.assertIn("Student Body Treasurer", self.html)
        self.assertIn("student store", self.html)
        self.assertEqual(self.html.count("Fun fact coming soon"), len(FUN_FACT_PLACEHOLDERS))
        self.assertGreaterEqual(len(FUN_FACT_PLACEHOLDERS), 2)
        self.assertLessEqual(len(FUN_FACT_PLACEHOLDERS), 3)
        self.assertIn('class="fun-soon soon', self.html)
        self.assertIn("Coming soon", self.html)

    def test_story_and_video_placeholders(self):
        self.assertEqual(self.html.count("Story coming soon"), len(STORY_PLACEHOLDERS))
        self.assertGreaterEqual(len(STORY_PLACEHOLDERS), 2)
        self.assertLessEqual(len(STORY_PLACEHOLDERS), 3)
        self.assertIn('class="story-card soon', self.html)
        self.assertIn("Video coming soon", self.html)
        self.assertIn('class="video-slot soon', self.html)
        self.assertNotIn("<iframe", self.html)
        self.assertNotIn("youtube", self.html.lower())

    def test_quotes_and_contact(self):
        for quote in QUOTES:
            self.assertIn(quote["attribution"], self.html)
        self.assertIn("Chasejrose5@gmail.com", self.html)
        self.assertIn("mailto:Chasejrose5@gmail.com", self.html)
        self.assertIn("https://github.com/chasejrose5-coder", self.html)
        self.assertNotIn("Download resume", self.html)

    def test_removed_resume_material(self):
        banned = (
            "GPA",
            "AP Physics",
            "Food Bank",
            "Lamorinda",
            "community service",
            "Education",
            ">Resume<",
        )
        for phrase in banned:
            self.assertNotIn(phrase, self.html)
        self.assertIsNone(__import__("re").search(r"\bSAT\b", self.html))
        self.assertNotIn("resume", PAGE_COPY["home"]["description"].lower())
        self.assertNotIn("resume", {item[0] for item in NAV})
        labels = [item[1] for item in NAV]
        self.assertEqual(labels, ["Home", "Projects"])


class ResumeFileTests(unittest.TestCase):
    def test_absent_until_a_file_exists(self):
        self.assertIsNone(resume_public_path())
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            static = root / "static"
            static.mkdir()
            (static / "notes.pdf").write_bytes(b"%PDF")
            self.assertIsNone(resume_public_path(root))
            (static / "Chase-Resume.pdf").write_bytes(b"%PDF")
            self.assertEqual(resume_public_path(root), "app/static/Chase-Resume.pdf")


class RioDetailTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        rio = next(project for project in PROJECTS if project["slug"] == "rio")
        cls.html = project_detail_html(rio, 0)

    def test_story_and_roadmap_without_the_screen_tour(self):
        self.assertIn("Runner Intelligence Owned", self.html)
        self.assertIn("March 19, 2027", self.html)
        self.assertIn("Shipped now", self.html)
        self.assertIn(">Next<", self.html)
        self.assertIn(">Later<", self.html)
        self.assertIn("blocks.webp", self.html)
        self.assertIn("goal.png", self.html)
        self.assertIn("about.jpg", self.html)
        for phrase in (
            "Home is where the season stands",
            "Plan is the season laid out",
            "Start session is the workout itself",
            "Profile keeps the goal",
        ):
            self.assertNotIn(phrase, self.html)
        self.assertIn("https://www.riorunning.com", self.html)
        self.assertIn("https://github.com/chasejrose5-coder/rio", self.html)


class AppShellTests(unittest.TestCase):
    def test_streamlit_entrypoint_has_no_resume_route(self):
        source = (ROOT / "streamlit_app.py").read_text(encoding="utf-8")
        self.assertNotIn("resume", source.lower())
        self.assertFalse((ROOT / "pages" / "resume.py").exists())
        self.assertFalse((ROOT / "resume.html").exists())
        script = (ROOT / "js" / "main.js").read_text(encoding="utf-8")
        self.assertIn(".race-countdown", script)
        self.assertIn("days until the ", script)
        self.assertEqual(RACE_DATE, "2027-03-19")


if __name__ == "__main__":
    unittest.main()
