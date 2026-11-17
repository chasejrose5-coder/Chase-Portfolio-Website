"""The lighter home page keeps the original shell and drops the race times."""

from __future__ import annotations

import unittest

import portfolio.pages as pages
from portfolio.content import ORIGIN, RESUME_SECTIONS


class LightHomeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        got = {}

        def fake(active, main, **kwargs):
            got["active"] = active
            got["html"] = kwargs.get("before", "") + main

        original = pages.render_page
        pages.render_page = fake
        try:
            pages.show_home()
        finally:
            pages.render_page = original
        cls.html = got["html"]

    def test_gun_ball_and_origin(self):
        self.assertIn('id="start-gun"', self.html)
        self.assertIn("On your marks", self.html)
        self.assertIn('id="kick-ball"', self.html)
        self.assertIn("Where it started", self.html)
        self.assertIn("always been good at", self.html)
        self.assertIn("I make my own things.", self.html)
        self.assertIn("A story from when I was young.", self.html)
        self.assertIn("What I want you to remember", self.html)
        self.assertIn('id="lean-dialog"', self.html)
        self.assertIn("400m-fall-loop.mp4", self.html)
        self.assertIn("Leaned so hard the track had to catch me.", self.html)

    def test_times_and_education_stay_out(self):
        self.assertNotIn("50.9", self.html)
        self.assertNotIn("2:02.9", self.html)
        self.assertNotIn(">Education<", self.html)
        ids = {section["id"] for section in RESUME_SECTIONS}
        self.assertNotIn("education", ids)


if __name__ == "__main__":
    unittest.main()
