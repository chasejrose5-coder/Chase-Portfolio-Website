# Chase Rose

Personal portfolio, run as a Streamlit app. Home is a short story: origin, what Chase is building, the track and the field, fun facts, stories, a video slot, quotes, and contact. Projects lists RIO and ProWash & Detail Co.

## Run locally

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

Open the URL Streamlit prints (usually http://localhost:8501).

- Home is `/`
- Projects is `/projects`
- RIO is `/rio`
- ProWash is `/prowash`

Edit the visible copy in `portfolio/content.py`.

Home opens on a finish-line tape (once per session; Skip, click, or space breaks it; reduced motion skips the snap). A small track follows the scroll, a scoreboard counts down to Stanford and names the 400m and 800m school records, and the fun facts flip.

## Placeholders Chase still needs to fill

These are marked “Coming soon” on the home page:

- Three fun-fact lines (`Fun fact coming soon`)
- Three story cards (`Story coming soon`)
- One video slot (`Video coming soon`). There is no embed yet.

No resume file is in the repo, so Contact does not show a download link. Add a `.pdf`, `.doc`, or `.docx` whose filename contains `resume` under `static/` and the link appears.

## Earlier static files

`index.html`, `projects.html`, `css/styles.css`, `js/main.js`, and `favicon.svg` remain from the first static version. The app loads that CSS, script, and favicon. Streamlit does not serve the HTML files.
