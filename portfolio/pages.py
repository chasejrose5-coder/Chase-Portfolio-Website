"""HTML for Home, Projects, and Resume, using the static site's class names."""

from __future__ import annotations

import html

from portfolio.content import (
    INTRO,
    PROJECTS,
    PROJECTS_KICKER,
    PROJECTS_TITLE,
    QUOTES,
    RESUME_SECTIONS,
    RESUME_TITLE,
    TAGLINE,
    NAME,
)
from portfolio.layout import render_page


def show_home() -> None:
    paragraphs = "".join(f'<p class="reveal">{html.escape(text)}</p>' for text in INTRO)
    quotes = []
    for quote in QUOTES:
        quotes.append(
            '<figure class="quote reveal">'
            "<blockquote>"
            f"<p>&ldquo;{html.escape(quote['text'])}&rdquo;</p>"
            "</blockquote>"
            f"<figcaption>{html.escape(quote['attribution'])}</figcaption>"
            "</figure>"
        )
    main = (
        '<main id="main"><div class="wrap">'
        '<section class="hero">'
        f'<h1 class="rise">{html.escape(NAME)}</h1>'
        f'<p class="tagline rise d1">{html.escape(TAGLINE)}</p>'
        "</section>"
        '<section class="intro" aria-labelledby="intro-label">'
        '<div class="intro-kicker reveal">'
        '<span class="rule" aria-hidden="true"></span>'
        '<span id="intro-label">Intro</span>'
        "</div>"
        f'<div class="intro-copy stagger">{paragraphs}</div>'
        "</section>"
        f'<section class="quotes stagger" aria-label="Quotes">{"".join(quotes)}</section>'
        "</div></main>"
    )
    render_page("home", main)


def show_projects() -> None:
    articles = []
    for project in PROJECTS:
        body = "".join(f"<p>{html.escape(text)}</p>" for text in project["paragraphs"])
        articles.append(
            '<article class="project reveal">'
            '<div class="project-meta">'
            f"<h2>{html.escape(project['title'])}</h2>"
            f'<p class="role">{html.escape(project["role"])}</p>'
            f'<a class="text-btn" href="{html.escape(project["href"], quote=True)}" '
            'target="_blank" rel="noopener noreferrer">'
            f'{html.escape(project["label"])}'
            '<span class="sr-only"> (opens in a new tab)</span></a>'
            "</div>"
            f'<div class="project-body">{body}</div>'
            "</article>"
        )
    main = (
        '<main id="main"><div class="wrap">'
        '<header class="page-head">'
        f'<h1 class="page-title rise">{html.escape(PROJECTS_TITLE)}</h1>'
        f'<p class="page-kicker rise d1">{html.escape(PROJECTS_KICKER)}</p>'
        "</header>"
        f'<div class="project-list">{"".join(articles)}</div>'
        "</div></main>"
    )
    render_page("projects", main)


def show_resume() -> None:
    sections = []
    for section in RESUME_SECTIONS:
        entries = []
        for entry in section["entries"]:
            title = (
                f"<h3>{html.escape(entry['title'])}</h3>" if entry["title"] else ""
            )
            degree = (
                f'<p class="degree">{html.escape(entry["degree"])}</p>'
                if entry["degree"]
                else ""
            )
            bullets = "".join(
                f'<li class="reveal">{html.escape(item)}</li>' for item in entry["bullets"]
            )
            entries.append(
                '<article class="entry">'
                f"{title}{degree}"
                f'<ul class="stagger">{bullets}</ul>'
                "</article>"
            )
        sections.append(
            f'<section class="resume-section" aria-labelledby="{html.escape(section["id"], quote=True)}">'
            f'<h2 id="{html.escape(section["id"], quote=True)}" class="reveal">{html.escape(section["heading"])}</h2>'
            f'{"".join(entries)}'
            "</section>"
        )
    main = (
        '<main id="main"><div class="wrap resume-layout">'
        '<div class="resume-title">'
        f'<h1 class="page-title rise">{html.escape(RESUME_TITLE)}</h1>'
        "</div>"
        f'<div class="resume-sections">{"".join(sections)}</div>'
        "</div></main>"
    )
    render_page("resume", main)
