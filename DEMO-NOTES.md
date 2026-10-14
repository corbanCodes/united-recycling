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

## Name — RESOLVED 9/25

The printed flyer reads "Gus Heart". **Confirmed by phone on 9/25: it is Gus Harvey**,
the son, and he is who callers should ask for. The site now says "Ask for Gus Harvey"
next to every phone number.

Single source of truth: `BIZ["ask_name"]` in `_generator/data.py`. Change that one line
and every page follows — nothing is hardcoded any more.

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

## 10/6 — two locations + travel area

Added to **this site only**:

- **Second yard: 1901 Peachtree Industrial Blvd, Buford, GA 30518** (newly rented).
  Both addresses now appear on the home page, About, Contact, the footer and the
  JSON-LD schema. Lawrenceville stays primary and keeps the phone number.
- **States/metros travelled**, from the expansion list. Framed as *"We Haul Across The
  Southeast — where we travel for large loads"*, **not** as office locations, because
  claiming branches that don't exist is false advertising and generates calls nobody
  can service. GA, TN, AL, FL, NC, TX, LA, OK + Atlanta, Charlotte, Nashville,
  Birmingham, Dallas, Houston, OKC, Baton Rouge, New Orleans.

**CONFIRM WITH HIM:** does he actually run tractors/trailers to Louisiana, Oklahoma and
Texas today, or is that where he *wants* locations? If it's aspirational, cut the list
back to what he can really service — one unanswerable call from Houston costs more
goodwill than the listing earns. Edit `SERVICE_AREA` / `SERVICE_CITIES` in
`_generator/data.py`.

**Buford hours** are unknown. The site shows one set of hours for both yards, which is
very likely wrong for a brand-new building. Still the top open question.

## NOT on this site — parked from the 10/6 notes

The 10/6 notes covered three businesses. Only the two addresses and the travel area
belong to United Recycling. Everything below is **not built and not in this repo**:

- **Ann / SA Metals Recycling LLC** — her own website, her hours of operation, her second
  address. Separate build.
- **Vinnie (the son)** — United Electrical, `unitedelectricalsurplus.com`. Wants to leave
  his current web guy and get a new site: Google Business page, Facebook page, **forms**,
  "paying more than anyone else for electrical equipment", tractors/trailers and large
  equipment pickup, remove the existing photos. **Real number: 404-831-3600** (the
  404-830-3600 in the earlier note was wrong). He is an electrical buyer, not a scrap
  recycler — different positioning entirely.
- **Both** want Google review links and SEO / Google Business Maps work.
- "Huge cranes, 40,000 lbs+" capability — good proof copy, but I don't know yet which
  business it belongs to. Ask before putting it on any site.

## 10/14 — 12 new yard photos + Christmas lights

Gus texted 13 HEICs (`client-provided-photos-10-14-2026/`). Twelve are real yard
material and are now in the gallery carousel and grid: bare bright copper, copper coils
on pallets, insulated building wire, heavy jacketed cable, brass valves, faucets and
fixtures, aluminum radiators, lead-acid batteries, lead sheet, brake rotors and two of
Christmas lights. The 13th (IMG_5948) is the "Rich Uncle" logo cartoon off his flyer,
not a yard photo, so it was left out of the gallery.

The new bare-bright shot landed on the same filename as the September one — kept both,
the new one is `bare-bright-copper-2.jpg`.

**Christmas lights is a new seasonal buy line.** His words: businesses, property
managers, churches and light installers dump pallets of old strings every January, and
he buys them because they're insulated copper wire. There's now a red-bordered section
on what-we-buy, plus the line item in the materials list. **Worth re-running this as a
push every December/January** — it's a genuinely uncontested search term for a scrap
yard and nobody thinks to call one about Christmas lights.

Still outstanding: he said he has more photos coming, and a yard-from-the-road shot is
still the one that would do the most work.

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

## LIVE — and no internal notes render any more

Live at **https://unitedrecyclingdemolition.com** (Netlify + Namecheap ALIAS/CNAME,
Let's Encrypt cert issued 9/25). www and http both 301 to the canonical https apex.

Six `TODO(client)` notes used to render **on the page** — fine for a demo, not fine on a
paying client's own domain. One of them literally read "confirm yard hours before this
goes in front of customers" while sitting in front of customers. All removed from the
rendered output on 9/25. **Every question they raised is preserved below — nothing was
dropped, just moved off the public page.**

### Answers still needed (previously shown on-page)

1. **Yard hours** — still the placeholder Mon–Fri 8–5, Sat 8–12 in `BIZ["hours"]`.
   This one is public and wrong until he confirms it. Highest priority.
2. **Drop-off**: ID requirements, payment method (cash / check / card), and any material
   he can't take from the public.
3. **Demolition**: service area, insurance limits, bonding capacity, and whether the
   roll-offs are owned or subcontracted.
4. **Vehicles**: title/paperwork requirements, and whether he tows.
5. **Service area**: how far out he'll actually run containers and demolition crews.
6. **Big Dog Demolition**: still no verified phone or website. The referral card now
   renders with no button at all rather than a dead link — get the real details and fill
   in `PARTNER` in `_generator/data.py` and the button comes back automatically.

## Placeholders in the code

## Build

Content lives in `_generator/data.py`. Chrome (header/footer/CTA) in `_generator/chrome.py`.
Page bodies in `_generator/build.py`.

```bash
python3 _generator/build.py
```

Never hand-edit the generated `.html` — it gets overwritten.
