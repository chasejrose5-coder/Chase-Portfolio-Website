"""Header, footer, and page shell shared by every Streamlit page."""

from __future__ import annotations

import html
import json
from pathlib import Path

import streamlit as st

from portfolio.content import EMAIL, NAME, PAGE_COPY

ROOT = Path(__file__).resolve().parent.parent
CSS_FILES = (ROOT / "css" / "styles.css", ROOT / "css" / "streamlit.css")
MAIN_JS = ROOT / "js" / "main.js"
FONT_IMPORT = (
    '@import url("https://fonts.googleapis.com/css2?family=Inter+Tight:'
    'ital,wght@0,400;0,500;0,600;1,400;1,500&display=swap");'
)

NAV = (
    ("home", "Home", "/"),
    ("projects", "Projects", "/projects"),
    ("resume", "Resume", "/resume"),
)


def combined_css() -> str:
    """Original portfolio CSS plus the Streamlit bridge, with the font first."""
    body = "\n".join(path.read_text(encoding="utf-8") for path in CSS_FILES)
    # Streamlit drops a <style> sheet that contains a raw "<html" token, even
    # inside a comment in styles.css. The rule itself is unchanged.
    body = body.replace("<html>", "the html element")
    return f"{FONT_IMPORT}\n{body}"


def render_page(
    active: str,
    main_html: str,
    *,
    title: str | None = None,
    description: str | None = None,
) -> None:
    # Style-only HTML is mounted outside the page body. A <style> tag inside
    # the page is stripped, and two separate style elements overwrite each other.
    st.html(f"<style>\n{combined_css()}\n</style>")
    st.html(
        _document(active, main_html, title=title, description=description),
        unsafe_allow_javascript=True,
    )


def _document(
    active: str,
    main_html: str,
    *,
    title: str | None = None,
    description: str | None = None,
) -> str:
    page = PAGE_COPY[active]
    title = title or page["title"]
    description = description or page["description"]
    return (
        f'<a class="skip" href="#main">Skip to content</a>'
        f"{_header(active)}"
        f"{main_html}"
        f"{_footer()}"
        f"{_script(title, description)}"
    )


def _header(active: str) -> str:
    links = []
    for key, label, href in NAV:
        current = ' aria-current="page"' if key == active else ""
        links.append(f'<li><a href="{href}"{current}>{html.escape(label)}</a></li>')
    return (
        '<header class="site-header">'
        '<div class="header-inner wrap">'
        f'<a class="brand" href="/">{html.escape(NAME)}</a>'
        '<input class="nav-check" type="checkbox" id="nav-toggle">'
        '<label class="nav-toggle" for="nav-toggle" aria-expanded="false">'
        '<span class="sr-only">Menu</span>'
        '<span class="bars" aria-hidden="true"></span>'
        "</label>"
        '<nav class="site-nav" aria-label="Primary">'
        f'<ul class="nav-links">{"".join(links)}</ul>'
        "</nav>"
        "</div>"
        "</header>"
    )


def _footer() -> str:
    email = html.escape(EMAIL)
    return (
        '<footer class="site-footer">'
        '<div class="wrap footer-inner">'
        f'<p class="footer-name">{html.escape(NAME)}</p>'
        f'<a href="mailto:{email}">{email}</a>'
        "</div>"
        "</footer>"
    )


def _script(title: str, description: str) -> str:
    boot = f"""
    document.documentElement.lang = "en";
    if (window.matchMedia("(prefers-reduced-motion: no-preference)").matches) {{
      document.documentElement.classList.add("js");
    }}
    (function () {{
      var title = {json.dumps(title)};
      var description = {json.dumps(description)};
      var applyTitle = function () {{
        if (document.title !== title) document.title = title;
      }};
      applyTitle();
      if (window.MutationObserver) {{
        new MutationObserver(applyTitle).observe(document.head, {{
          childList: true,
          characterData: true,
          subtree: true
        }});
      }}
      window.setTimeout(applyTitle, 0);
      window.setTimeout(applyTitle, 250);
      var desc = document.querySelector('meta[name="description"]');
      if (!desc) {{
        desc = document.createElement("meta");
        desc.setAttribute("name", "description");
        document.head.appendChild(desc);
      }}
      desc.setAttribute("content", description);
      var theme = document.querySelector('meta[name="theme-color"]');
      if (!theme) {{
        theme = document.createElement("meta");
        theme.setAttribute("name", "theme-color");
        document.head.appendChild(theme);
      }}
      theme.setAttribute("content", "#FFFFFF");
    }})();
    """
    main = MAIN_JS.read_text(encoding="utf-8")
    return f"<script>{boot}\n{main}</script>"
