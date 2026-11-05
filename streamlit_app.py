"""Chase Rose portfolio, served as a Streamlit multipage app."""

import streamlit as st

from portfolio.layout import ROOT

st.set_page_config(
    page_title="Chase Rose",
    page_icon=str(ROOT / "favicon.svg"),
    layout="wide",
    initial_sidebar_state="collapsed",
)

navigation = st.navigation(
    [
        st.Page("pages/home.py", title="Chase Rose", default=True),
        st.Page(
            "pages/projects.py",
            title="Projects — Chase Rose",
            url_path="projects",
        ),
        st.Page(
            "pages/resume.py",
            title="Resume — Chase Rose",
            url_path="resume",
        ),
    ],
    position="hidden",
)

navigation.run()
