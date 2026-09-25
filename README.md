# United Recycling Scrap Metals LLC

Static site for a Lawrenceville, GA scrap metal yard. Built for 60 Minute Sites.

- **Design reference:** sarecycling.com (navy / red / white, bold uppercase, quadrant tiles)
- **Business model reference:** abcrecycling.com (public drop-off · commercial · demolition · vehicles)

## Build

All page content lives in `_generator/`. Edit there, then regenerate:

```bash
python3 _generator/build.py
```

- `_generator/data.py` — business facts, nav, pillars, material list, gallery. Start here.
  `BIZ["ask_for"]` / `BIZ["call_cta"]` drive the "Ask for Gus" line that sits next to
  every phone number — the single most important instruction on the site.
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

**There is no contact form and no email address on this site** — the client asked for
phone and text only (9/25). Do not add Netlify Forms, a mailto link, or an email field
back in without asking him first.

## Custom domain

`unitedrecyclingdemolition.com` (Namecheap) → this Netlify site.

Namecheap → Domain List → Manage → **Advanced DNS**. Host records should be exactly:

| Type | Host | Value | TTL |
|---|---|---|---|
| ALIAS Record | `@` | `united-recycling.netlify.app` | Automatic |
| CNAME Record | `www` | `united-recycling.netlify.app` | Automatic |

Delete the default `CNAME www → parkingpage.namecheap.com` and the
`URL Redirect Record @` first — those are Namecheap's parking page and they will
override the site. Then add the domain in Netlify under Domain management so it can
issue the Let's Encrypt certificate.

See `DEMO-NOTES.md` for open questions and the photo shot list.
