# Chase Rose

Personal portfolio, run as a Streamlit app. Home, Projects, and Resume use the copy and layout from the static site.

## Run locally

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

Open the URL Streamlit prints (usually http://localhost:8501).

- Home is `/`
- Projects is `/projects`
- Resume is `/resume`

The original static files (`index.html`, `projects.html`, `resume.html`, `css/styles.css`, `js/main.js`, `favicon.svg`) are still in the repo. The app loads that CSS, script, and favicon. Edit the visible copy in `portfolio/content.py`. The bio, project, and resume sections are still the placeholder text from the HTML.
