# United Recycling Scrap Metals LLC — client notes

> **STATUS: SIGNED 9/25/2026 — $50/mo.** Haggled the setup fee down. Live client, not a demo.

**Client:** Gus Heart · United Recycling Scrap Metals LLC
**Yard:** 621 Hurricane Shoals Rd, Lawrenceville, GA 30046
**Phone:** 470-655-9608 (text + picture messages accepted)
**Email:** unitedelectricalsurplus@yahoo.com
**Existing domain:** unitedelectricalsurplus.com

## The brief

- **Look and feel:** sarecycling.com — navy (`#102759` / `#0A1837`), red (`#D11242`), white,
  big uppercase headlines, dark photo-overlay hero with an oversized logo watermark,
  four colored quadrant tiles under the hero.
- **Business model:** abcrecycling.com — four pillars, which map straight onto Gus's flyer:
  1. Public drop-off (open to the public — cans, wire, electric motors, ice boxes/appliances)
  2. Commercial & industrial (the flyer's "ATTN: Plant Manager / Business Owner")
  3. Demolition & cleanouts + dumpsters and roll-offs (commercial/industrial only)
  4. Vehicles & heavy equipment (flyer: "Company Vehicles", "Machinery — working or damaged")

Every material on the printed flyer is on the site, regrouped into
Ferrous / Non-Ferrous / Electrical & Plant Equipment / Specialty.

## Pages

| File | Purpose |
|---|---|
| `index.html` | Hero, 4 pillars, about strip, material list, 3 promises, commercial strip, CTA |
| `what-we-buy.html` | Full material list + "send us a picture" |
| `drop-off.html` | Open-to-the-public drop-off, 3-step how-it-works |
| `commercial.html` | Plant managers / business owners, what-you-get grid |
| `demolition.html` | Demolition, dumpsters, roll-offs, plant cleanouts |
| `vehicles.html` | Company vehicles, heavy equipment, machinery, parts/cores |
| `about.html` | Who he is, licensed & bonded, service area tags |
| `contact.html` | Quote form (Netlify) + full contact block |
| `thank-you.html`, `404.html` | Form success + fallback |

## Entity names — CONFIRM THIS ONE

Two names are now in play, and the site treats them as parent + division:

- **United Recycling Scrap Metals LLC** — the yard. This is what's on the printed flyer,
  it owns the phone number and address, and it stays in the header, the footer brand and
  the schema markup on every page.
- **United Recycling Demolition Metals LLC** — the demolition arm. Gus called this "the
  official name of the website" on 8/17 while also saying he wanted it as "a sub-serviced
  type thing," not the company name. So it fronts `demolition.html` (page title + a full
  lockup band mid-page reading "A demolition division of United Recycling Scrap Metals LLC")
  and gets a "Demolition performed by" line in the footer sitewide.

**Ask him to confirm that split.** If he actually wants Demolition Metals to be the primary
brand everywhere, it's a one-line change in `_generator/data.py` (`BIZ["name"]`) plus a
rebuild — but don't do it without hearing him say so, because the flyer, the yard and the
scrap side all trade under Scrap Metals. Also worth asking whether Demolition Metals LLC is
actually registered with the GA Secretary of State, since the site now says "LLC" in public.

## ⚠️ NAME CONFLICT — RESOLVE BEFORE ANYONE SEES THIS

The printed flyer says **Gus Heart**. On 9/25 Corban wrote **"gus harvey, his son."**
Heart vs Harvey — one of them is wrong, and a wrong surname on a live site is the kind
of thing a client notices immediately.

**So the site says "Ask for Gus" everywhere and never prints a surname.** That satisfies
the instruction (call/text and ask for the son), reads naturally, and carries zero risk.
Get the correct spelling from him and it's a one-line change to `BIZ["ask_for"]` +
`BIZ["call_cta"]` in `_generator/data.py`.

Also worth pinning down: the flyer's "Gus Heart" is the contact on the phone number, and
Corban's note says the son is who you ask for. Are they the same person, or is the dad
on the flyer and the son answering now? `BIZ["owner"]` is still "Gus Heart".

## 9/25 change set — NO EMAIL, NO FORMS

Client isn't tech literate and doesn't want an inbox he'll miss. Stripped completely:

- Contact form deleted. `contact.html` is now one big tap-to-call number + "Ask for Gus"
  + a "Text A Photo" (`sms:`) button.
- `thank-you.html` deleted — it only existed as the form's target.
- Every `mailto:` link and the email address itself are gone from the pages, the footer,
  and the `RecyclingCenter` schema. `BIZ["email"]` is deleted from `data.py`.
- All "Get a Quote" CTAs now say Call / Text, and the header button is the phone number
  itself with a `tel:` link.
- Netlify Forms attributes removed. **Do not re-enable form detection in Netlify.**

Verified after build: 0 `mailto:`, 0 `<form>`, 0 `data-netlify`, 0 email-shaped strings
anywhere in the generated HTML.

**"Ask for Gus" appears on all 11 pages** — top bar, footer, contact page, and next to
every phone number.

## Photo gallery (his own photos)

12 photos from `client-provided-photos/` are live at `assets/img/gallery/`. They arrived
as texted screenshots (750x1624, black letterbox bars top and bottom, and two had an
iPhone home-indicator line at the bottom). All cropped to the real 750x1000 content
region, so they're uniform 3:4 — `magick -crop 750x1000+0+312`.

`gallery.html` has a scroll-snap carousel (4 up on desktop, 2 on tablet, 1 on phone,
swipeable, with prev/next + dots) plus a full 12-photo grid. The homepage carries an
8-photo carousel above the "who we are" section. No JS library — it degrades to a plain
horizontal scroller if the script never runs.

**These are far better than the Wikimedia stand-ins.** Next step: swap the remaining
stock photos (hero, yard-aerial, switchgear, demolition, vehicles) for his own as he
sends more, then delete `credits.html` and its footer link. Still need: the yard from
the road, the scale/drive-in lane, and a shot of Gus or the crew.

## Open questions for Gus — ASK ON THE CALL

1. **Yard hours.** Placeholder is Mon–Fri 8–5, Sat 8–12. Need the real ones.
2. **Payment.** Cash, check, or card? Any dollar threshold where it becomes a check?
3. **ID requirements.** Georgia scrap law — what does a walk-in need to bring?
4. **Anything he *won't* take** from the public (sealed units, tanks, propane, etc.).
5. **Photos — THE BIG ONE.** The site now has real, freely-licensed stand-in photos
   (Wikimedia Commons, CC0/PD/CC BY/CC BY-SA — no iStock comps, sources listed on
   `credits.html`). They're generic scrap-yard shots, not his yard. Replace with his
   own as soon as possible; phone photos beat stock badly for this business. Shot list:
   - the yard from the road (this is the money shot — proves he's real and local)
   - the public drive-in lane and the scale
   - mixed non-ferrous on the scale
   - a switch gear / MCC lineup or a plant lot he's bought
   - a roll-off being dropped or picked up
   - a demolition or cleanout job in progress
   - Gus and/or the crew
   When his photos go in, delete `credits.html` and the footer link to it.
6. **Demolition service area**, insurance limits and bonding capacity — how far will he
   send a crew? Confirmed with Gus 8/17: demolition is a real service line, **commercial
   and industrial only — no single-family houses**. Full scope he named on 8/17, all live
   on the site: power plants & energy facilities, nuclear, coal-fired, gas-fired, hydroelectric
   dams, refineries & petrochemical, **chemical plants (his favorite — it leads the section)**,
   steel mills, paper mills, automotive manufacturing plants, airports & terminals, major
   hospitals, universities & campus buildings, large school districts, shopping malls,
   office towers, data centers, stadiums & arenas, convention centers, prisons & correctional
   complexes, military installations, bridges & large infrastructure, industrial warehouses
   & distribution centers, apartment & multifamily complexes.
   Note apartments ARE in scope (multifamily = commercial); single-family houses are not.
7. **Roll-offs** — does he own the containers or subcontract?
8. **Vehicles** — title/paperwork requirements, and does he tow?
9. **Big Dog Demolition (Atlanta, GA)** — Gus's friend, and he wants them promoted on the
   demolition page. The referral card is live at the bottom of `demolition.html`, but it has
   **no working link or phone yet**. `bigdogdemo.com` is a parked GoDaddy lander and
   `bigdogdemolition.com` doesn't resolve, so nothing was linked rather than guess and send
   his friend's traffic to the wrong business. Get the real number/site from Gus and fill in
   `PARTNER` in `_generator/data.py` — the card wires itself up once those fields are set.
   Also worth asking: does Big Dog want to reciprocate and send scrap back to the yard?
10. **Domain.** Keep `unitedelectricalsurplus.com` or move to something like
   `unitedrecyclingga.com`? The current domain says "electrical surplus" but the
   business is a full scrap yard — the name is costing him public drop-off traffic.
11. **Logo.** He has no real mark; the site uses a "UR" badge lockup. Offer a simple one.
12. **Price list?** ABC and a lot of yards post current prices per pound. Big trust lever
    if he's willing — big maintenance burden if he isn't. Ask before promising it.

## Photography currently in place

| File | Used on | License |
|---|---|---|
| `hero-scrapyard.jpg` | home hero | CC BY-SA 3.0 |
| `yard-aerial.jpg` | home — "who we are" | CC BY 4.0 |
| `rolloff-truck.jpg` | home — commercial strip | CC BY-SA 3.0 |
| `nonferrous-bales.jpg` | what-we-buy | CC BY 2.0 |
| `baled-cans.jpg` | drop-off | CC BY-SA 2.5 |
| `switchgear.jpg` | commercial | Public domain |
| `demolition.jpg` | demolition | CC BY-SA 2.0 |
| `vehicles.jpg` | vehicles | CC BY 2.0 |
| `yard-piles.jpg` | about + CTA bands | CC0 |
| `texture-bales.jpg` | interior page banners, photo band | CC BY 2.0 |

Attribution is generated from `_generator/credits.json` onto `credits.html`.
Several strong-looking candidates were **rejected on inspection**: two had competitor
branding in frame (Veolia, Waste Management), one "aluminum cans" result was actually a
garbage truck full of cardboard, one "truck scale" result was a Chinese freight yard with
no scale in it, and one "motor control center" result was a man drilling a concrete wall
with a date stamp burned into the corner. Worth knowing that image search titles lie.

## Placeholders / TODOs in the code

Search for `TODO(client)` — they're on drop-off, demolition, vehicles, about, contact.

## Build

Content lives in `_generator/data.py`. Chrome (header/footer/CTA) in `_generator/chrome.py`.
Page bodies in `_generator/build.py`.

```bash
python3 _generator/build.py
```

Never hand-edit the generated `.html` — it gets overwritten.
