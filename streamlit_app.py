"""Chase Rose portfolio, served as a Streamlit multipage app."""

import streamlit as st

from portfolio.content import PROJECTS
from portfolio.layout import ROOT
from portfolio.pages import show_project

st.set_page_config(
    page_title="Chase Rose",
    page_icon=str(ROOT / "favicon.svg"),
    layout="wide",
    initial_sidebar_state="collapsed",
)


def _project_page(slug: str):
    def run() -> None:
        show_project(slug)

    run.__name__ = "project_" + slug.replace("-", "_")
    return run


navigation = st.navigation(
    [
        st.Page("pages/home.py", title="Chase Rose", default=True),
        st.Page(
            "pages/projects.py",
            title="Projects — Chase Rose",
            url_path="projects",
        ),
        *[
            st.Page(
                _project_page(project["slug"]),
                title=f"{project['title']} — Chase Rose",
                url_path=project["slug"],
            )
            for project in PROJECTS
        ],
        st.Page(
            "pages/resume.py",
            title="Resume — Chase Rose",
            url_path="resume",
        ),
    ],
    position="hidden",
)

navigation.run()
