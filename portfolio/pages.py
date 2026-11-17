"""HTML for Home and Projects."""

from __future__ import annotations

import html
from pathlib import Path

from portfolio.content import (
    BUILDING,
    BUILDING_HEADING,
    COMING_SOON_LABEL,
    CONTACT_HEADING,
    EMAIL,
    FIELD,
    FIELD_HEADING,
    FINISH,
    FUN_FACT_PLACEHOLDERS,
    FUN_FACTS,
    FUN_FACTS_HEADING,
    GITHUB_LINK_LABEL,
    GITHUB_PROFILE,
    HOME_PORTRAIT,
    LAP_MARKS,
    ORIGIN,
    ORIGIN_HEADING,
    PROJECTS,
    QUOTES,
    QUOTES_HEADING,
    RACE_DATE,
    RACE_NAME,
    RACE_ZONE,
    RESUME_LINK_LABEL,
    SCOREBOARD_EVENT,
    SCOREBOARD_RECORDS,
    STORIES_HEADING,
    STORIES_LEAD,
    STORY_LINK_LABEL,
    STORY_PLACEHOLDERS,
    TAGLINE,
    VIDEO_HEADING,
    VIDEO_PLACEHOLDER,
    NAME,
    countdown_parts,
    days_until_race,
)
from portfolio.layout import PORTFOLIO_PATH_JS, ROOT, render_page


def _external_link(href: str, label: str, class_name: str) -> str:
    return (
        f'<a class="{class_name}" href="{html.escape(href, quote=True)}" '
        'target="_blank" rel="noopener noreferrer">'
        f"{html.escape(label)}"
        '<span class="sr-only"> (opens in a new tab)</span></a>'
    )


_RESUME_SUFFIXES = {".pdf", ".doc", ".docx"}


def resume_public_path(root: Path | None = None) -> str | None:
    """Static URL for a resume file under static/, or None when there is no file."""
    root = ROOT if root is None else Path(root)
    static_root = (root / "static").resolve()
    if not static_root.is_dir():
        return None
    found = []
    for path in static_root.rglob("*"):
        if not path.is_file():
            continue
        if path.suffix.lower() not in _RESUME_SUFFIXES:
            continue
        if "resume" not in path.stem.lower():
            continue
        found.append(path)
    if not found:
        return None
    found.sort(key=lambda item: item.as_posix())
    rel = found[0].resolve().relative_to(static_root).as_posix()
    return "app/static/" + rel


def _section(section_id: str, heading: str, body: str) -> str:
    sid = html.escape(section_id, quote=True)
    label = dict(LAP_MARKS).get(section_id, "")
    lap = f' data-lap="{html.escape(label, quote=True)}"' if label else ""
    return (
        f'<section class="story-section reveal" id="{sid}"{lap} aria-labelledby="{sid}-heading">'
        f'<h2 id="{sid}-heading">{html.escape(heading)}</h2>'
        f"{body}"
        "</section>"
    )


def _building_cards() -> str:
    cards = []
    for spec in BUILDING:
        project = _project_by_slug(spec["slug"])
        if project is None:
            continue
        thumb = project.get("thumb") or {}
        mark = " is-mark" if thumb.get("mark") else ""
        slug = html.escape(project["slug"], quote=True)
        countdown = ""
        if spec.get("show_countdown"):
            count, rest = countdown_parts(days_until_race())
            countdown = (
                '<p class="race-countdown" aria-live="polite" '
                f'data-race-date="{html.escape(RACE_DATE, quote=True)}" '
                f'data-race-zone="{html.escape(RACE_ZONE, quote=True)}" '
                f'data-race-name="{html.escape(RACE_NAME, quote=True)}">'
                f'<span class="race-count">{html.escape(count)}</span>'
                f'<span class="race-rest">{html.escape(rest)}</span>'
                "</p>"
            )
        cards.append(
            '<article class="build-card reveal">'
            f'<a class="build-card-link" href="{slug}">'
            f'<span class="build-media{mark}">{_picture(thumb, decorative=True)}</span>'
            f'<span class="build-kicker">{html.escape(spec["kicker"])}</span>'
            f'<h3 class="build-headline">{html.escape(spec["headline"])}</h3>'
            f"{countdown}"
            f'<p class="build-body">{html.escape(spec["body"])}</p>'
            f'<span class="build-more">{html.escape(STORY_LINK_LABEL)}</span>'
            "</a>"
            '<p class="work-linkline">'
            f'{_external_link(project["href"], project["link_label"], "work-link")}'
            f'{_external_link(project["code_href"], project["code_label"], "work-link")}'
            "</p>"
            "</article>"
        )
    return f'<div class="build-grid">{"".join(cards)}</div>'


def _finish_gate() -> str:
    """Full-screen finish tape. JS shows it once per session."""
    skip = html.escape(FINISH["skip"])
    title = html.escape(FINISH["title"])
    kicker = html.escape(FINISH["kicker"])
    action = html.escape(FINISH["action"])
    hint = html.escape(FINISH["hint"])
    return (
        '<div class="finish-gate" id="finish-gate" role="dialog" aria-modal="true" '
        'aria-labelledby="finish-title">'
        "<script>(function(){try{if(sessionStorage.getItem('chase-finish-seen')==='1')"
        "{document.getElementById('finish-gate').classList.add('is-done');}}catch(e){}})();</script>"
        f'<a class="finish-skip" id="finish-skip" href="#main">{skip}</a>'
        '<div class="finish-stage">'
        f'<p class="finish-kicker">{kicker}</p>'
        f'<h2 id="finish-title">{title}</h2>'
        '<button class="finish-break" id="finish-break" type="button">'
        '<span class="finish-lane" aria-hidden="true">'
        '<span class="finish-ribbon">'
        '<span class="finish-half is-left"><span>FINISH</span></span>'
        '<span class="finish-half is-right"><span>FINISH</span></span>'
        "</span></span>"
        f'<span class="finish-cta">{action}</span>'
        "</button>"
        f'<p class="finish-hint">{hint}</p>'
        "</div></div>"
    )


def _scoreboard() -> str:
    count, _rest = countdown_parts(days_until_race())
    return (
        '<div class="scoreboard reveal" data-race-date="'
        f'{html.escape(RACE_DATE, quote=True)}" data-race-zone="'
        f'{html.escape(RACE_ZONE, quote=True)}" data-race-name="'
        f'{html.escape(RACE_NAME, quote=True)}">'
        f'<p class="scoreboard-event">{html.escape(SCOREBOARD_EVENT)}</p>'
        '<p class="scoreboard-digits" aria-live="polite">'
        f'<span class="race-count">{html.escape(count)}</span>'
        '<span class="scoreboard-unit" data-race-unit>DAYS</span>'
        "</p>"
        f'<p class="scoreboard-records">{html.escape(SCOREBOARD_RECORDS)}</p>'
        "</div>"
    )


def _lap_nav() -> str:
    marks = []
    for section_id, label in LAP_MARKS:
        sid = html.escape(section_id, quote=True)
        name = html.escape(label)
        marks.append(
            f'<a class="lap-mark" href="#{sid}" data-lap-target="{sid}" '
            f'aria-label="{name}"><span class="lap-dot" aria-hidden="true"></span>'
            f'<span class="lap-name">{name}</span></a>'
        )
    return (
        '<nav class="lap" id="lap" aria-label="Page progress">'
        '<div class="lap-track">'
        '<span class="lap-oval" aria-hidden="true"></span>'
        '<span class="lap-runner" id="lap-runner" aria-hidden="true"></span>'
        f'{"".join(marks)}'
        "</div></nav>"
    )


def _contact_links() -> str:
    email = html.escape(EMAIL)
    github = html.escape(GITHUB_PROFILE, quote=True)
    links = [
        f'<a class="contact-link" href="mailto:{email}">{email}</a>',
        (
            f'<a class="contact-link" href="{github}" target="_blank" rel="noopener noreferrer">'
            f"{html.escape(GITHUB_LINK_LABEL)}"
            '<span class="sr-only"> (opens in a new tab)</span></a>'
        ),
    ]
    resume = resume_public_path()
    if resume:
        href = html.escape(resume, quote=True)
        links.append(
            f'<a class="contact-link" href="{href}" download>'
            f"{html.escape(RESUME_LINK_LABEL)}</a>"
        )
    return f'<p class="contact-links reveal">{"".join(links)}</p>'


def home_main_html() -> str:
    portrait = _picture(HOME_PORTRAIT, loading="eager")
    origin = "".join(f"<p>{html.escape(text)}</p>" for text in ORIGIN)
    facts = []
    for fact in FUN_FACTS:
        facts.append(
            '<li>'
            '<button class="flip" type="button" aria-pressed="false">'
            '<span class="flip-inner">'
            '<span class="flip-face flip-front">'
            f'<span class="flip-kicker">Fun fact</span>'
            f'<span class="flip-hook">{html.escape(fact["front"])}</span>'
            "</span>"
            '<span class="flip-face flip-back" aria-hidden="true">'
            f'<span class="flip-copy">{html.escape(fact["back"])}</span>'
            "</span>"
            "</span></button></li>"
        )
    for text in FUN_FACT_PLACEHOLDERS:
        facts.append(
            '<li class="fun-soon soon reveal">'
            f'<span class="soon-label">{html.escape(COMING_SOON_LABEL)}</span>'
            f'<span class="soon-text">{html.escape(text)}</span>'
            "</li>"
        )
    stories = []
    for story in STORY_PLACEHOLDERS:
        stories.append(
            '<article class="story-card soon reveal">'
            f'<span class="soon-label">{html.escape(COMING_SOON_LABEL)}</span>'
            f'<h3>{html.escape(story["title"])}</h3>'
            f'<p>{html.escape(story["text"])}</p>'
            "</article>"
        )
    columns = []
    for item in FIELD:
        columns.append(
            '<article class="field-card reveal">'
            f'<h3>{html.escape(item["title"])}</h3>'
            f'<p>{html.escape(item["text"])}</p>'
            "</article>"
        )
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
    video = (
        '<div class="video-slot soon reveal">'
        f'<span class="soon-label">{html.escape(COMING_SOON_LABEL)}</span>'
        f"<p>{html.escape(VIDEO_PLACEHOLDER)}</p>"
        "</div>"
    )
    return (
        f"{_finish_gate()}"
        '<main id="main"><div class="wrap">'
        '<div class="home-fold" id="hero" data-lap="Start">'
        '<section class="hero">'
        f'<h1 class="rise">{html.escape(NAME)}</h1>'
        f'<p class="tagline rise d1">{html.escape(TAGLINE)}</p>'
        f'<figure class="home-portrait">{portrait}</figure>'
        "</section>"
        '<div class="scroll-hint" aria-hidden="true">&#8595;</div>'
        "</div>"
        f'{_section("origin-story", ORIGIN_HEADING, f"<div class=\"story-copy stagger\">{origin}</div>")}'
        f'{_section("building", BUILDING_HEADING, _scoreboard() + _building_cards())}'
        f'{_section("track-field", FIELD_HEADING, f"<div class=\"field-grid\">{"".join(columns)}</div>")}'
        f'{_section("fun-facts", FUN_FACTS_HEADING, f"<ul class=\"fun-facts\">{"".join(facts)}</ul>")}'
        + _section(
            "stories",
            STORIES_HEADING,
            f'<p class="story-lead reveal">{html.escape(STORIES_LEAD)}</p>'
            f'<div class="story-grid">{"".join(stories)}</div>',
        )
        + _section("video", VIDEO_HEADING, video)
        + _section("quotes", QUOTES_HEADING, f'<div class="quotes stagger">{"".join(quotes)}</div>')
        + _section("contact", CONTACT_HEADING, _contact_links())
        + "</div></main>"
        + _lap_nav()
    )


def show_home() -> None:
    render_page("home", home_main_html())


_FILLS = ("#eef1f4", "#f4f0ea", "#eef3f1")


def _placeholder(label: str, decorative: bool = False) -> str:
    name = html.escape(label)
    if decorative:
        return (
            '<span class="ph" aria-hidden="true">'
            '<span class="ph-label">Image</span></span>'
        )
    return (
        f'<span class="ph" role="img" aria-label="{name}">'
        '<span class="ph-label" aria-hidden="true">Image</span></span>'
    )


def _public_src(path: str | None) -> str | None:
    """URL for a file in the app's static/ directory.

    Streamlit serves that directory at ``<app-root>/app/static/``. Each project
    route is one path segment under the app root (``/projects``, ``/rio``,
    ``/prowash``). A relative URL with no leading slash replaces that segment,
    so it still points at the app root when the app is mounted under a prefix.

    Community Cloud mounts the server at ``/~/+/``. From ``/~/+/projects``,
    ``../app/static/...`` climbs out of that prefix and 404s. A root-absolute
    ``/app/static/...`` skips the prefix the same way. ``app/static/...`` stays
    inside it, and at a host root it still resolves to ``/app/static/...``.
    """
    if not path:
        return None
    root = ROOT.resolve()
    file_path = (root / path).resolve()
    static_root = (root / "static").resolve()
    if not file_path.is_file():
        return None
    try:
        rel = file_path.relative_to(static_root).as_posix()
    except ValueError:
        return None
    return "app/static/" + rel


def _picture(image: dict | None, *, decorative: bool = False, loading: str = "lazy") -> str:
    src = _public_src(image.get("src")) if image else None
    if not src:
        label = (image or {}).get("alt") or "Image"
        return _placeholder(label, decorative=decorative)
    alt = "" if decorative else html.escape(image.get("alt") or "", quote=True)
    width = int(image["width"])
    height = int(image["height"])
    extra = ""
    srcset_parts = []
    for item in image.get("srcset") or ():
        url = _public_src(item.get("src"))
        if not url:
            continue
        srcset_parts.append(
            f"{html.escape(url, quote=True)} {int(item['width'])}w"
        )
    if srcset_parts:
        extra += f' srcset="{", ".join(srcset_parts)}"'
        sizes = image.get("sizes")
        if sizes:
            extra += f' sizes="{html.escape(sizes, quote=True)}"'
    return (
        f'<img src="{html.escape(src, quote=True)}" alt="{alt}" '
        f'width="{width}" height="{height}"{extra} loading="{loading}" decoding="async">'
    )


def _project_by_slug(slug: str) -> dict | None:
    for project in PROJECTS:
        if project["slug"] == slug:
            return project
    return None


def projects_index_html() -> str:
    rows = []
    for index, project in enumerate(PROJECTS):
        slug = html.escape(project["slug"], quote=True)
        fill = _FILLS[index % len(_FILLS)]
        thumb = project.get("thumb") or {}
        mark = " is-mark" if thumb.get("mark") else ""
        blurb = project.get("blurb") or ""
        blurb_html = (
            f'<span class="work-row-blurb">{html.escape(blurb)}</span>' if blurb else ""
        )
        live = (
            '<span class="work-live">Live app</span>' if project.get("href") else ""
        )
        rows.append(
            f'<a class="work-row" href="{slug}" data-project-path="/{slug}">'
            f'<span class="work-thumb{mark}" style="--ph-fill:{fill}">'
            f"{_picture(thumb, decorative=True, loading='eager')}"
            "</span>"
            '<span class="work-row-main">'
            '<span class="work-row-heading">'
            f'<span class="work-row-title">{html.escape(project["title"])}</span>'
            f'<span class="work-row-dates">{html.escape(project["dates"])}</span>'
            "</span>"
            f"{blurb_html}{live}"
            "</span>"
            "</a>"
        )
    return (
        '<main id="main">'
        '<div class="work-column">'
        '<h1 class="work-kicker">Projects</h1>'
        f'<div class="work-list">{"".join(rows)}</div>'
        "</div></main>"
    )


def project_detail_html(project: dict, index: int) -> str:
    fill = _FILLS[index % len(_FILLS)]
    slug = html.escape(project["slug"], quote=True)
    blocks = []
    paragraphs = project["paragraphs"]
    frames = project.get("frames") or ()
    for step, text in enumerate(paragraphs):
        blocks.append(f'<p class="reveal">{html.escape(text)}</p>')
        frame = frames[step] if step < len(frames) else None
        if not frame:
            continue
        blocks.append(
            '<figure class="work-frame reveal">'
            '<div class="work-print">'
            f"{_picture(frame)}"
            "</div></figure>"
        )
    hero = project.get("hero") or {}
    hero_mark = " is-mark" if hero.get("mark") else ""
    return (
        "<main id=\"main\">"
        f"<script>{PORTFOLIO_PATH_JS}"
        "(function(){try{var raw=sessionStorage.getItem('project-morph');"
        "if(!raw)return;"
        "if(window.matchMedia('(prefers-reduced-motion: reduce)').matches)return;"
        "var data=JSON.parse(raw);"
        "if(!data||portfolioPath(data.path)!==portfolioPath(location.pathname))return;"
        "if(typeof data.t==='number'&&Date.now()-data.t>15000)return;"
        "document.documentElement.classList.add('project-morphing');"
        "}catch(e){}})();"
        "</script>"
        f'<article class="work-column work-detail" style="--ph-fill:{fill}" data-project-path="/{slug}">'
        '<p class="work-backline"><a class="work-back" href="projects">Projects</a></p>'
        f'<div class="work-hero{hero_mark}" data-morph="hero" style="--ph-fill:{fill}">'
        f"{_picture(hero, loading='eager')}"
        "</div>"
        f'<h1 class="work-title">{html.escape(project["title"])}</h1>'
        f'<p class="work-meta">{html.escape(project["role"])} · {html.escape(project["year"])}</p>'
        '<p class="work-linkline">'
        f'{_external_link(project["href"], project["link_label"], "work-link")}'
        f'{_external_link(project["code_href"], project["code_label"], "work-link")}'
        "</p>"
        f'<div class="work-story">{"".join(blocks)}</div>'
        f"{_ahead_html(project)}"
        "</article></main>"
    )


def _ahead_html(project: dict) -> str:
    ahead = project.get("ahead")
    if not ahead:
        return ""
    slug = html.escape(project["slug"], quote=True)
    groups = ahead.get("groups")
    if groups:
        blocks = []
        for index, group in enumerate(groups):
            gid = f"{slug}-ahead-{index}"
            items = "".join(f"<li>{html.escape(item)}</li>" for item in group["items"])
            blocks.append(
                f'<h3 id="{gid}">{html.escape(group["label"])}</h3>'
                f'<ul aria-labelledby="{gid}">{items}</ul>'
            )
        body = "".join(blocks)
    else:
        items = "".join(f"<li>{html.escape(item)}</li>" for item in ahead.get("items") or ())
        body = f"<ul>{items}</ul>"
    return (
        f'<section class="work-ahead" aria-labelledby="{slug}-ahead">'
        f'<h2 id="{slug}-ahead">{html.escape(ahead["title"])}</h2>'
        f'<p>{html.escape(ahead["lead"])}</p>'
        f"{body}"
        "</section>"
    )


def show_projects() -> None:
    render_page("projects", projects_index_html())


def show_project(slug: str) -> None:
    project = _project_by_slug(slug)
    if project is None:
        missing = (
            '<main id="main"><div class="work-column">'
            '<p class="work-backline"><a class="work-back" href="projects">Projects</a></p>'
            "<p>This project placeholder is not in the list.</p>"
            "</div></main>"
        )
        render_page("projects", missing, title="Projects — Chase Rose")
        return
    index = next(i for i, item in enumerate(PROJECTS) if item["slug"] == slug)
    render_page(
        "projects",
        project_detail_html(project, index),
        title=f"{project['title']} — Chase Rose",
        description=project["paragraphs"][0],
    )
