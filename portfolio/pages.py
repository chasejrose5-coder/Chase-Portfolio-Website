"""HTML for Home, Projects, and Resume."""

from __future__ import annotations

import html

from portfolio.content import (
    COMING_SOON,
    FUN_FACTS,
    FUN_HEADING,
    GITHUB_PROFILE,
    HOME_PORTRAIT,
    INTRO,
    LEAN_CAPTION,
    LEAN_STILL,
    LEAN_VIDEO,
    NAME,
    NOTICE,
    NOTICE_HEADING,
    ORIGIN,
    ORIGIN_HEADING,
    PROJECTS,
    QUOTES,
    REMEMBER,
    REMEMBER_LABEL,
    RESUME_SECTIONS,
    RESUME_TITLE,
    STORIES,
    STORIES_HEADING,
    TAGLINE,
    YOUNG_STORY,
)
from portfolio.layout import PORTFOLIO_PATH_JS, ROOT, render_page


def _external_link(href: str, label: str, class_name: str) -> str:
    return (
        f'<a class="{class_name}" href="{html.escape(href, quote=True)}" '
        'target="_blank" rel="noopener noreferrer">'
        f"{html.escape(label)}"
        '<span class="sr-only"> (opens in a new tab)</span></a>'
    )


def _soon(text: str) -> str:
    return (
        '<p class="soon-note">'
        f'<span class="soon-label">{html.escape(COMING_SOON)}</span>'
        f"{html.escape(text)}</p>"
    )


def _gun_gate() -> str:
    return (
        '<div class="start-gun" id="start-gun" role="dialog" aria-modal="true" '
        'aria-labelledby="gun-title">'
        "<script>document.documentElement.classList.add('gun-held');</script>"
        '<div class="gun-backdrop"></div>'
        '<canvas class="gun-smoke" id="gun-smoke" aria-hidden="true"></canvas>'
        '<div class="gun-stage">'
        '<p class="gun-kicker" id="gun-title">On your marks</p>'
        '<button class="gun-fire" id="gun-fire" type="button">Go</button>'
        '<p class="gun-hint">Click, or press Enter.</p>'
        "</div></div>"
    )


def _lean_dialog() -> str:
    video = _public_src(LEAN_VIDEO) or ""
    poster = _public_src(LEAN_STILL["src"]) or ""
    return (
        '<dialog class="lean-dialog" id="lean-dialog" aria-labelledby="lean-caption">'
        '<button class="lean-close" type="button" id="lean-close">Close</button>'
        f'<video id="lean-video" loop muted playsinline controls preload="none" '
        f'poster="{html.escape(poster, quote=True)}" '
        f'width="{LEAN_STILL["width"]}" height="{LEAN_STILL["height"]}">'
        f'<source src="{html.escape(video, quote=True)}" type="video/mp4">'
        "</video>"
        f'<p id="lean-caption">{html.escape(LEAN_CAPTION)}</p>'
        "</dialog>"
    )


def _ball() -> str:
    # Streamlit drops an inline svg, so the ball is drawn with CSS only.
    return '<div class="kick-ball" id="kick-ball" aria-hidden="true"></div>'


def show_home() -> None:
    paragraphs = "".join(f'<p class="reveal">{html.escape(text)}</p>' for text in INTRO)
    origin = "".join(f"<p>{html.escape(text)}</p>" for text in ORIGIN)
    portrait = _picture(HOME_PORTRAIT, loading="eager")
    facts = "".join(f"<li>{_soon(text)}</li>" for text in FUN_FACTS)
    stories = "".join(f"<li>{_soon(text)}</li>" for text in STORIES)
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
        '<div class="home-fold">'
        '<section class="hero">'
        f'<h1 class="rise">{html.escape(NAME)}</h1>'
        f'<p class="tagline rise d1">{html.escape(TAGLINE)}</p>'
        '<p class="remember rise d1">'
        f'<span class="remember-label">{html.escape(REMEMBER_LABEL)}</span>'
        f"{html.escape(REMEMBER)}</p>"
        '<button class="lean-mark" id="lean-mark" type="button" '
        'aria-haspopup="dialog" aria-controls="lean-dialog">'
        '<span class="lean-tape" aria-hidden="true"></span>'
        "The lean</button>"
        "</section>"
        '<section class="intro" aria-labelledby="intro-label">'
        '<div class="intro-aside">'
        f'<figure class="home-portrait">{portrait}</figure>'
        '<div class="intro-kicker reveal">'
        '<span class="rule" aria-hidden="true"></span>'
        '<span id="intro-label">Intro</span>'
        "</div>"
        "</div>"
        f'<div class="intro-copy stagger">{paragraphs}</div>'
        "</section>"
        '<div class="scroll-hint" aria-hidden="true">&#8595;</div>'
        "</div>"
        '<div class="home-more">'
        f'<section class="origin" aria-labelledby="origin-heading">'
        f'<h2 id="origin-heading">{html.escape(ORIGIN_HEADING)}</h2>'
        f'<div class="origin-copy">{origin}</div>'
        f"{_soon(YOUNG_STORY)}"
        "</section>"
        f'<section aria-labelledby="notice-heading">'
        f'<h2 id="notice-heading">{html.escape(NOTICE_HEADING)}</h2>'
        f"{_soon(NOTICE)}"
        "</section>"
        f'<section aria-labelledby="facts-heading">'
        f'<h2 id="facts-heading">{html.escape(FUN_HEADING)}</h2>'
        f'<ul class="plain-list">{facts}</ul>'
        "</section>"
        f'<section aria-labelledby="stories-heading">'
        f'<h2 id="stories-heading">{html.escape(STORIES_HEADING)}</h2>'
        f'<ul class="plain-list">{stories}</ul>'
        "</section>"
        "</div>"
        f'<section class="quotes stagger" aria-label="Quotes">{"".join(quotes)}</section>'
        "</div></main>"
        + _ball()
        + _lean_dialog()
    )
    render_page("home", main, before=_gun_gate())


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
        '<p class="resume-contact">'
        f'{_external_link(GITHUB_PROFILE, "github.com/chasejrose5-coder", "resume-github")}'
        "</p>"
        "</div>"
        f'<div class="resume-sections">{"".join(sections)}</div>'
        "</div></main>"
    )
    render_page("resume", main)
