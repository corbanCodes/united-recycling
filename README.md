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

Netlify → import from GitHub → publish directory is the repo root (no build command
needed; run `build.py` locally and commit the HTML). The contact form is wired for
Netlify Forms (`data-netlify="true"`, posts to `thank-you.html`).

See `DEMO-NOTES.md` for open questions and the photo shot list.
