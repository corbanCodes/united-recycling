# United Recycling Scrap Metals LLC

Static site for a Lawrenceville, GA scrap metal yard. Built for 60 Minute Sites.

- **Design reference:** sarecycling.com (navy / red / white, bold uppercase, quadrant tiles)
- **Business model reference:** abcrecycling.com (public drop-off · commercial · demolition · vehicles)

## Build

All page content lives in `_generator/`. Edit there, then regenerate:

```bash
python3 _generator/build.py
```

- `_generator/data.py` — business facts, nav, pillars, material list. Start here.
- `_generator/chrome.py` — top bar, header/nav, CTA band, footer.
- `_generator/build.py` — page bodies.

Generated HTML at the repo root is **overwritten on every build** — don't hand-edit it.

## Local preview

```bash
python3 -m http.server 5075
```

## Deploy

Netlify, from GitHub. There is **no build step** — `build.py` runs locally and the
generated HTML is committed, so Netlify just serves the repo root.

Build settings must be:

| Field | Value |
|---|---|
| Base directory | *(empty)* |
| Build command | *(empty)* |
| Publish directory | `.` |

`netlify.toml` at the repo root pins the publish directory and sets cache headers.

**If a deploy fails at "Reading and parsing configuration files"**, the Base directory
is pointing at a folder that doesn't exist in this repo — most likely `united-recycling`,
which is only the local folder name on the Mac. Inside the repo, those files *are* the
root. Clear that field and redeploy. Netlify looks for `netlify.toml` relative to the
base directory, so while that field is wrong this file won't even be read.

The contact form is wired for Netlify Forms (`data-netlify="true"`, posts to
`thank-you.html`). Enable form detection on the site after the first successful deploy.

See `DEMO-NOTES.md` for open questions and the photo shot list.
