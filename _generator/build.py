# -*- coding: utf-8 -*-
"""Build every page. Run from the site root:  python3 _generator/build.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data import BIZ, PILLARS, MATERIALS, PROMISES, PARTNER, DEMO_SCOPE, DEMO_HEADLINE, DIVISION, GALLERY
import chrome as C

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P, PH = BIZ["phone_display"], BIZ["phone_href"]
ASK, ASKNAME = BIZ["ask_for"], BIZ["ask_name"]


def write(name, html):
    with open(os.path.join(ROOT, name), "w", encoding="utf-8") as f:
        f.write(html)
    print("  wrote", name)


def page(name, title, desc, active, body):
    write(name, C.head(title, desc, active) + C.topbar() + C.header(active) + body + C.footer())


def pillars_block():
    out = ['<div class="pillars">']
    for i, (href, h, p) in enumerate(PILLARS, 1):
        out.append(
            f'  <a class="pillar" href="{href}">'
            f'<span class="pill-num">0{i}</span><h3>{h}</h3><p>{p}</p>'
            f'<span class="pill-go">Learn more &rarr;</span></a>'
        )
    out.append("</div>")
    return "\n".join(out) + "\n"


def materials_block(navy=False):
    out = ['<div class="mat-grid">']
    for heading, items in MATERIALS:
        lis = "".join(f"    <li>{i}</li>\n" for i in items)
        out.append(f'  <div class="mat-col">\n    <h3>{heading}</h3>\n    <ul class="mat-list">\n{lis}    </ul>\n  </div>')
    out.append("</div>")
    return "\n".join(out) + "\n"


def demo_scope_block():
    """Categorised list — same treatment as the materials list on what-we-buy."""
    out = ['<div class="mat-grid">']
    for heading, items in DEMO_SCOPE:
        lis = "".join(f"    <li>{i}</li>\n" for i in items)
        out.append(f'  <div class="mat-col">\n    <h3>{heading}</h3>\n    <ul class="mat-list">\n{lis}    </ul>\n  </div>')
    out.append("</div>")
    return "\n".join(out) + "\n"


def demo_headline_block():
    out = ['<div class="cards cards-4">']
    for h, b in DEMO_HEADLINE:
        out.append(f'  <div class="card"><div class="card-ico">&#9670;</div><h3>{h}</h3><p>{b}</p></div>')
    out.append("</div>")
    return "\n".join(out) + "\n"


def division_block():
    """Mid-page lockup for the demolition arm. Deliberately reads as a division of the
    yard, not as a second unrelated company and not as a rename of the parent."""
    D = DIVISION
    return f"""<section class="division">
  <div class="wrap">
    <span class="division-eyebrow">{D["eyebrow"]}</span>
    <div class="division-lockup">
      <span class="division-mark">UR</span>
      <span class="division-name">{D["name"]}</span>
    </div>
    <p class="division-parent">A demolition division of {D["parent"]}</p>
    <p class="division-blurb">{D["blurb"]}</p>
    <div class="btn-row">
      <a class="btn btn-red btn-lg" href="tel:{BIZ["phone_href"]}">Call {BIZ["phone_display"]}</a>
      <a class="btn btn-ghost btn-lg" href="sms:{PH}">Text A Photo</a>
    </div>
  </div>
</section>
"""


def carousel_block(limit=None, heading=True):
    """Scroll-snap carousel of Gus's own photos. No library, no build step — it's a
    horizontal scroller with prev/next buttons and dots, so it degrades to a plain
    swipeable strip if JS never runs."""
    items = GALLERY if limit is None else GALLERY[:limit]
    slides = ""
    for i, (f, title, caption) in enumerate(items):
        slides += (
            f'      <li class="cara-slide" role="group" aria-roledescription="slide" '
            f'aria-label="{i+1} of {len(items)}">\n'
            f'        <figure>\n'
            f'          <img src="assets/img/gallery/{f}" alt="{title} at United Recycling Scrap Metals" '
            f'loading="lazy" width="750" height="1000">\n'
            f'          <figcaption><strong>{title}</strong><span>{caption}</span></figcaption>\n'
            f'        </figure>\n'
            f'      </li>\n'
        )
    dots = "".join(
        f'      <button class="cara-dot" type="button" data-go="{i}" aria-label="Go to slide {i+1}"></button>\n'
        for i in range(len(items))
    )
    return f"""<div class="cara" data-carousel>
  <button class="cara-nav cara-prev" type="button" aria-label="Previous photos">&#8249;</button>
  <div class="cara-viewport">
    <ul class="cara-track">
{slides}    </ul>
  </div>
  <button class="cara-nav cara-next" type="button" aria-label="Next photos">&#8250;</button>
  <div class="cara-dots">
{dots}  </div>
</div>
"""


def partner_block():
    """Referral card for Gus's friend. Deliberately looks like a referral, not a service
    of United Recycling — nobody should think Big Dog is the same company."""
    P_ = PARTNER
    if P_["phone_display"]:
        contact = f'<a class="btn btn-navy" href="tel:{P_["phone_display"]}">Call {P_["name"]}</a>'
    elif P_["url"]:
        contact = f'<a class="btn btn-navy" href="{P_["url"]}" target="_blank" rel="noopener">Visit {P_["name"]}</a>'
    else:
        # No verified number or site for them yet — show the referral without a dead
        # link rather than leaking an internal note onto a live customer-facing page.
        contact = ""
    return f"""<section class="sec-gray">
  <div class="wrap">
    <div class="partner">
      <div class="partner-tag">Who we work with</div>
      <div class="partner-body">
        <h3>Also check out {P_["name"]} &mdash; {P_["city"]}</h3>
        <p>{P_["blurb"]} If your project is bigger than a container and a crew, or you want
        a second set of eyes on a teardown, give them a look. Tell them United Recycling sent you.</p>
        {contact}
      </div>
    </div>
  </div>
</section>
"""


def banner(h1, sub):
    return f"""<section class="banner">
  <div class="wrap">
    <h1>{h1}</h1>
    <p>{sub}</p>
  </div>
</section>
"""


# ---------------------------------------------------------------- HOME
home = f"""<section class="hero">
  <span class="hero-watermark" aria-hidden="true">UR</span>
  <div class="wrap">
    <span class="eyebrow eyebrow-light">Lawrenceville, Georgia &middot; Open to the public</span>
    <h1>Scrap Metal<span>Turned Into Cash</span></h1>
    <p>United Recycling buys all ferrous and non-ferrous metals &mdash; from a truckload of aluminum cans to a plant full of switch gear. We pay more than the local yards, and we pay you the same day.</p>
    <div class="hero-phone">
      <span class="hero-phone-label">Call or text</span>
      <a class="hero-phone-number" href="tel:{PH}">{P}</a>
      <span class="hero-phone-ask">{ASK}</span>
    </div>
    <div class="btn-row">
      <a class="btn btn-red btn-lg" href="tel:{PH}">Call Now</a>
      <a class="btn btn-ghost btn-lg" href="sms:{PH}">Text A Photo</a>
      <a class="btn btn-ghost btn-lg" href="what-we-buy.html">See What We Buy</a>
    </div>
    <p class="hero-note">Picture messages welcome &mdash; snap a photo of your load and we'll price it.</p>
  </div>
</section>

{pillars_block()}

<section class="sec-gray">
  <div class="wrap">
    <div class="sec-head center">
      <span class="eyebrow">Straight from the yard</span>
      <h2>Real Loads, Real Money</h2>
      <p class="lede center" style="margin:0 auto">These are actual loads that came across our
      scale in Lawrenceville. Got something that looks like this? Call or text
      <a href="tel:{PH}">{P}</a> and ask for {ASKNAME}.</p>
    </div>
    {carousel_block(limit=8)}
    <div class="center" style="margin-top:34px">
      <a class="btn btn-navy" href="gallery.html">See The Full Gallery</a>
    </div>
  </div>
</section>

<section>
  <div class="wrap split">
    <div>
      <span class="eyebrow">Who we are</span>
      <h2>A Licensed &amp; Bonded Georgia Scrap Yard</h2>
      <p class="lede">United Recycling Scrap Metals is a licensed and bonded metal recycler on Hurricane Shoals Road in Lawrenceville. We buy from homeowners pulling in with a trunk full of cans and from plant managers decommissioning an entire line &mdash; and everything in between.</p>
      <p>If it's metal, we want it. Copper, brass, aluminum, stainless, steel of any grade, electric motors, transformers, switch gear, machinery working or damaged, appliances, ice boxes, insulated wire, and the specialty material most yards turn away.</p>
      <div class="btn-row">
        <a class="btn btn-navy" href="about.html">About United Recycling</a>
        <a class="btn btn-outline" href="contact.html">Call Or Text Us</a>
      </div>
    </div>
    <div class="split-media"><img src="assets/img/yard-aerial.jpg" alt="Scrap metal recycling yard with material handler sorting ferrous and non-ferrous piles" loading="lazy" width="1200" height="820"></div>
  </div>
</section>

<section class="sec-navy">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow eyebrow-light">What we buy</span>
      <h2>All Ferrous &amp; Non-Ferrous Metals</h2>
      <p class="lede" style="color:#C9D6EE">Here's the short version. If you don't see your material, call anyway &mdash; we buy a lot of things other yards won't touch.</p>
    </div>
    {materials_block(navy=True)}
    <div class="btn-row" style="margin-top:38px">
      <a class="btn btn-red btn-lg" href="what-we-buy.html">Full Material List</a>
    </div>
  </div>
</section>

{C.strip()}

<section class="sec-gray">
  <div class="wrap">
    <div class="sec-head center">
      <span class="eyebrow">Why United Recycling</span>
      <h2>Three Reasons People Drive Past Other Yards</h2>
    </div>
    <div class="cards">
""" + "\n".join(
    f'      <div class="card{" card-red" if i == 1 else ""}"><div class="card-ico">0{i+1}</div><h3>{h}</h3><p>{b}</p></div>'
    for i, (h, b) in enumerate(PROMISES)
) + f"""
    </div>
  </div>
</section>

<section class="photoband">
  <div class="wrap">
    <span class="eyebrow eyebrow-light">Ferrous &amp; non-ferrous</span>
    <h2>Millions Of Pounds, One Load At A Time</h2>
    <p>Whether it's a pickup bed of aluminum cans or a decommissioned production line, it comes across the same scale and gets graded the same honest way.</p>
  </div>
</section>

<section>
  <div class="wrap split">
    <div class="split-media"><img src="assets/img/rolloff-truck.jpg" alt="Roll-off truck setting down an open container for a scrap metal job site" loading="lazy" width="1200" height="620"></div>
    <div>
      <span class="eyebrow">For business</span>
      <h2>Dumpsters, Roll-Offs &amp; Full Demolition</h2>
      <p class="lede">Plant managers and business owners: we don't just buy the metal, we come get it. United Recycling supplies dumpsters and roll-off containers, and we do large-scale commercial demolition &mdash; chemical plants, power plants, refineries, mills, hospitals, campuses and malls.</p>
      <p>One call handles the container, the labor, the haul-off and the check. No coordinating three vendors and hoping the scrap value doesn't disappear into someone else's invoice.</p>
      <div class="btn-row">
        <a class="btn btn-navy" href="commercial.html">Commercial Accounts</a>
        <a class="btn btn-outline" href="demolition.html">Demolition Services</a>
      </div>
    </div>
  </div>
</section>

{C.cta()}
"""
page("index.html",
     f"{BIZ['name']} | Scrap Metal Recycling in Lawrenceville, GA",
     "United Recycling Scrap Metals buys all ferrous and non-ferrous metals in Lawrenceville, GA. Open to the public, licensed and bonded, paying more than local scrap yards.",
     "index.html", home)


# ---------------------------------------------------------------- WHAT WE BUY
wwb = banner("What We Buy",
             "We buy all ferrous and non-ferrous metals. If it isn't on this list, call us anyway &mdash; the list isn't the limit.") + f"""
<section>
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow">Material list</span>
      <h2>Bring It In Or We'll Come Get It</h2>
      <p class="lede">Small loads get weighed and paid at the scale. Large industrial lots get a price, a container, and a scheduled pickup.</p>
    </div>
    {materials_block()}
  </div>
</section>

{C.strip()}

<section class="sec-gray">
  <div class="wrap split">
    <div>
      <span class="eyebrow">Not sure what you have?</span>
      <h2>Send Us A Picture</h2>
      <p class="lede">Most people don't know a motor from a transformer, and that's fine &mdash; that's our job. Take a photo of the pile, text it to {P}, and you'll get a straight answer on whether it's worth hauling and roughly what it's worth.</p>
      <p>Picture messages are welcome at the same number you'd call. No account, no appointment, no runaround.</p>
      <div class="btn-row">
        <a class="btn btn-red" href="tel:{PH}">Text or Call {P}</a>
      </div>
    </div>
    <div class="split-media"><img src="assets/img/nonferrous-bales.jpg" alt="Baled mixed non-ferrous scrap metal stacked at a recycling yard" loading="lazy" width="1200" height="800"></div>
  </div>
</section>

{C.cta("Turn That Pile Into A Check")}
"""
page("what-we-buy.html",
     f"What We Buy | Ferrous &amp; Non-Ferrous Metals | {BIZ['short']}",
     "Full list of metals United Recycling buys in Lawrenceville GA: copper, brass, aluminum, stainless, steel, electric motors, transformers, switch gear, MRI magnets and more.",
     "what-we-buy.html", wwb)


# ---------------------------------------------------------------- DROP OFF
drop = banner("Public Drop-Off",
              "We are open to the public. No account, no minimum load, no appointment &mdash; pull in, get weighed, get paid.") + f"""
<section>
  <div class="wrap split">
    <div>
      <span class="eyebrow">Homeowners &amp; haulers</span>
      <h2>Cans, Wire, Motors, Ice Boxes</h2>
      <p class="lede">Cleaning out a garage, a basement, a rental property or a job-site trailer? Bring it to the yard on Hurricane Shoals Road. Aluminum cans, copper wire, electric motors, old appliances and ice boxes, lawn equipment, radiators, pipe, sheet metal &mdash; it all has value.</p>
      <p>We pay more than local scrap yards. If another yard gave you a ticket, bring it with you and let us beat it.</p>
      <div class="btn-row">
        <a class="btn btn-navy" href="what-we-buy.html">What We Buy</a>
        <a class="btn btn-outline" href="{BIZ['map_url']}" target="_blank" rel="noopener">Get Directions</a>
      </div>
    </div>
    <div class="split-media"><img src="assets/img/baled-cans.jpg" alt="Bales of crushed beverage cans stacked at a recycling facility" loading="lazy" width="1200" height="900"></div>
  </div>
</section>

<section class="sec-gray">
  <div class="wrap">
    <div class="sec-head center">
      <span class="eyebrow">How it works</span>
      <h2>Three Steps, Same Day Cash</h2>
    </div>
    <div class="cards">
      <div class="card"><div class="card-ico">01</div><h3>Pull In &amp; Weigh</h3><p>Drive onto the scale at {BIZ['street']}. Our crew sorts and grades your material with you standing there &mdash; nothing happens out of sight.</p></div>
      <div class="card card-red"><div class="card-ico">02</div><h3>See Your Numbers</h3><p>You see the weight and the price per pound for every grade in your load before anything is settled.</p></div>
      <div class="card"><div class="card-ico">03</div><h3>Get Paid</h3><p>Walk out the same day with your money. Bring a valid ID &mdash; Georgia law requires it on every scrap transaction.</p></div>
    </div>
  </div>
</section>

{C.strip()}
{C.cta("The Yard Is Open To The Public")}
"""
page("drop-off.html",
     f"Public Scrap Drop-Off in Lawrenceville, GA | {BIZ['short']}",
     "Open to the public scrap metal drop-off in Lawrenceville, GA. Bring cans, copper wire, electric motors, appliances and ice boxes. Same-day cash, we pay more than local yards.",
     "drop-off.html", drop)


# ---------------------------------------------------------------- COMMERCIAL
comm = banner("Commercial &amp; Industrial Accounts",
              "ATTN: Plant Manager / Business Owner &mdash; we buy the equipment, the surplus and the scrap your operation generates.") + f"""
<section>
  <div class="wrap split">
    <div>
      <span class="eyebrow">For plants &amp; contractors</span>
      <h2>Your Scrap Stream, Handled</h2>
      <p class="lede">United Recycling works directly with plant managers, electrical contractors, facility teams and business owners across Gwinnett County and North Georgia. We buy switch gear, MCCs, breakers, panels, disconnects, electric motors, transformers, heat exchangers, chillers and machinery &mdash; working or damaged.</p>
      <p>We handle surplus electrical inventory nobody else wants to grade, and specialty material like tantalum, high-temp alloys, nickel-cobalt, carbide and sludge, MRI magnets, X-ray film and litho negatives.</p>
      <div class="btn-row">
        <a class="btn btn-red" href="tel:{PH}">Call {P}</a>
        <a class="btn btn-outline" href="what-we-buy.html">Full Material List</a>
      </div>
    </div>
    <div class="split-media"><img src="assets/img/switchgear.jpg" alt="Row of industrial electrical switch gear cabinets and motor control centers" loading="lazy" width="1200" height="900"></div>
  </div>
</section>

<section class="sec-navy">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow eyebrow-light">What you get</span>
      <h2>One Vendor, One Number, One Check</h2>
    </div>
    <div class="cards cards-4">
      <div class="card"><div class="card-ico">&#9670;</div><h3>Containers On Site</h3><p>Dumpsters and roll-offs staged where your crew actually works, swapped on your schedule.</p></div>
      <div class="card card-red"><div class="card-ico">&#9670;</div><h3>Scheduled Pickup</h3><p>Regular routes for ongoing production scrap, or one-time pulls for a shutdown.</p></div>
      <div class="card"><div class="card-ico">&#9670;</div><h3>Graded Fairly</h3><p>Every grade priced separately. No dumping your copper in with the sheet iron.</p></div>
      <div class="card"><div class="card-ico">&#9670;</div><h3>Clean Paperwork</h3><p>Licensed and bonded, with the documentation your accounting and compliance people need.</p></div>
    </div>
    <div class="promise" style="margin-top:56px">
      <div><strong>Open To The Public</strong><span>No account required &mdash; but commercial accounts get pricing and pickup.</span></div>
      <div><strong>We Pay More</strong><span>Consistently above local scrap yard pricing on ferrous and non-ferrous.</span></div>
      <div><strong>Text A Photo</strong><span>Picture message the lot to {P} for a fast read.</span></div>
    </div>
  </div>
</section>

{C.cta("Let's Price Your Lot", "Send photos, a list, or just tell us what's sitting in the back of the plant. We'll tell you what it's worth and how fast we can be there.")}
"""
page("commercial.html",
     f"Commercial &amp; Industrial Metal Recycling | {BIZ['short']}",
     "Industrial scrap metal buyer for plant managers and business owners in Georgia. Switch gear, MCCs, breakers, motors, transformers, machinery, surplus electrical inventory.",
     "commercial.html", comm)


# ---------------------------------------------------------------- DEMOLITION
demo = banner("Commercial &amp; Industrial Demolition",
              "Power plants, chemical plants, refineries, mills, hospitals, campuses, malls, "
              "stadiums and apartment complexes &mdash; torn down, hauled out and paid for.") + f"""
<section>
  <div class="wrap split">
    <div>
      <span class="eyebrow">This is a service we run, not a sideline</span>
      <h2>We Tear It Down And Take It Away</h2>
      <p class="lede">United Recycling does demolition &mdash; the big stuff. Power plants,
      chemical plants, refineries, steel and paper mills, hospitals, universities, stadiums,
      airports, malls, office towers, apartment complexes and the distribution centers behind them.
      Not container drops and scrap pickups. Actual teardowns.</p>
      <p>Because we are the metal buyer and the demolition crew, the scrap value comes straight
      off your project cost instead of disappearing into a middleman's invoice. That is the
      whole advantage, and it is a big one on a job with real tonnage in it.</p>
      <p class="scope-note"><strong>Commercial and industrial only.</strong> No single-family
      houses or garages. This crew is set up for power plants, chemical plants, mills, campuses,
      malls, apartment complexes and anything else with real tonnage in it.</p>
      <div class="btn-row">
        <a class="btn btn-red" href="tel:{PH}">Call {P}</a>
        <a class="btn btn-outline" href="tel:{PH}">Call {P}</a>
      </div>
    </div>
    <div class="split-media"><img src="assets/img/demolition.jpg" alt="Excavators with demolition shears tearing down an industrial building" loading="lazy" width="1200" height="675"></div>
  </div>
</section>

<section class="sec-navy">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow eyebrow-light">What he goes after</span>
      <h2>The Big Ones</h2>
      <p class="lede" style="color:#C9D6EE">These are the jobs United Recycling is built for &mdash;
      heavy structures with serious tonnage and serious alloy content in them.</p>
    </div>
    {demo_headline_block()}
  </div>
</section>

{division_block()}

<section>
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow">Full scope</span>
      <h2>What We'll Take Down</h2>
      <p class="lede">Commercial and industrial structures only. If it's a big building coming down
      and there's metal in it, it's on the list &mdash; and if it isn't listed, call anyway,
      it probably still is.</p>
    </div>
    {demo_scope_block()}
  </div>
</section>

<section class="photoband photoband--yard">
  <div class="wrap">
    <span class="eyebrow eyebrow-light">Licensed &amp; bonded</span>
    <h2>One Crew, One Number, One Check</h2>
    <p>The container, the labor, the haul-off and the payment for the metal &mdash; all of it
    through United Recycling. No coordinating three vendors and hoping the scrap value survives.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head center">
      <span class="eyebrow">Also available</span>
      <h2>Dumpsters, Roll-Offs &amp; Cleanouts</h2>
    </div>
    <div class="cards">
      <div class="card"><div class="card-ico">&#9670;</div><h3>Dumpsters &amp; Roll-Offs</h3><p>Containers staged for job sites, plants and cleanouts. Fill it with metal and the container works for you instead of against you.</p></div>
      <div class="card card-red"><div class="card-ico">&#9670;</div><h3>Selective Demolition</h3><p>Interior strip-outs and single-line removals where the rest of the building keeps operating around us.</p></div>
      <div class="card"><div class="card-ico">&#9670;</div><h3>Plant Cleanouts</h3><p>Decommissioned lines, retired equipment and years of accumulated surplus &mdash; cleared out and turned into a check.</p></div>
    </div>
  </div>
</section>

{partner_block()}
{C.strip()}
{C.cta("Talk To Us About A Teardown", "Call or text <b>" + P + "</b> and ask for " + ASKNAME + ". Tell us what's coming down and roughly what's in it &mdash; we'll price the demolition and the metal together.")}
"""
page("demolition.html",
     f"{DIVISION['name']} | Commercial &amp; Industrial Demolition",
     "Large-scale commercial and industrial demolition in Georgia: power plants, nuclear and coal-fired stations, chemical plants, refineries, steel and paper mills, hospitals, universities, malls, stadiums, airports and apartment complexes. Scrap value applied against project cost.",
     "demolition.html", demo)


# ---------------------------------------------------------------- VEHICLES
veh = banner("Vehicles &amp; Heavy Equipment",
             "Company vehicles, fleet trucks, machinery and heavy equipment &mdash; working or damaged.") + f"""
<section>
  <div class="wrap split">
    <div>
      <span class="eyebrow">End of life</span>
      <h2>That Truck Still Has Value</h2>
      <p class="lede">Retired company vehicles, box trucks, service vans, trailers, forklifts, loaders and production machinery all carry real metal value &mdash; whether they still run or haven't turned over in years.</p>
      <p>Tell us what you've got and where it's sitting. We'll price it and arrange the pickup.</p>
      <div class="btn-row">
        <a class="btn btn-red" href="tel:{PH}">Call {P}</a>
        <a class="btn btn-outline" href="tel:{PH}">Call {P}</a>
      </div>
    </div>
    <div class="split-media"><img src="assets/img/vehicles.jpg" alt="End-of-life vehicle in a scrap yard awaiting processing" loading="lazy" width="1200" height="800"></div>
  </div>
</section>

<section class="sec-navy">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow eyebrow-light">What we take</span>
      <h2>Rolling Stock &amp; Machinery</h2>
    </div>
    <div class="cards cards-4">
      <div class="card"><div class="card-ico">&#9670;</div><h3>Company Vehicles</h3><p>Trucks, vans, trailers and fleet units at the end of their service life.</p></div>
      <div class="card card-red"><div class="card-ico">&#9670;</div><h3>Heavy Equipment</h3><p>Forklifts, loaders, compressors and yard equipment.</p></div>
      <div class="card"><div class="card-ico">&#9670;</div><h3>Machinery</h3><p>Production machinery working or damaged, including full lines.</p></div>
      <div class="card"><div class="card-ico">&#9670;</div><h3>Parts &amp; Cores</h3><p>Radiators, motors, transmissions, catalytic material and non-ferrous cores.</p></div>
    </div>
  </div>
</section>

{C.cta("Tell Us What You're Retiring")}
"""
page("vehicles.html",
     f"Vehicle &amp; Heavy Equipment Recycling | {BIZ['short']}",
     "United Recycling buys company vehicles, fleet trucks, heavy equipment and machinery, working or damaged, in Lawrenceville GA and across North Georgia.",
     "vehicles.html", veh)


# ---------------------------------------------------------------- ABOUT
about = banner("About United Recycling",
               "A licensed and bonded Georgia scrap metal company on Hurricane Shoals Road in Lawrenceville.") + f"""
<section>
  <div class="wrap split">
    <div>
      <span class="eyebrow">Who you're dealing with</span>
      <h2>Straight Weights, Straight Prices</h2>
      <p class="lede">United Recycling Scrap Metals LLC is run by {BIZ['owner']} out of the yard at {BIZ['street']} in {BIZ['city']}. We buy all ferrous and non-ferrous metals from the public, from contractors, and from industrial plants across North Georgia.</p>
      <p>The whole business runs on one idea: pay more than the yard down the road, grade honestly in front of the customer, and answer the phone. That's why most of our volume comes from people who came once and kept coming back.</p>
      <p>We are a licensed and bonded company, and we are open to the public.</p>
      <div class="btn-row">
        <a class="btn btn-navy" href="contact.html">Call Or Text Us</a>
        <a class="btn btn-outline" href="drop-off.html">Visit The Yard</a>
      </div>
    </div>
    <div class="split-media"><img src="assets/img/yard-piles.jpg" alt="Scrap metal piles and a material handler at the recycling yard" loading="lazy" width="1200" height="900"></div>
  </div>
</section>

<section class="sec-gray">
  <div class="wrap">
    <div class="sec-head center">
      <span class="eyebrow">Service area</span>
      <h2>Lawrenceville &amp; All Of North Georgia</h2>
      <p class="lede center" style="margin:0 auto">Public drop-off at the Lawrenceville yard. Container service, pickups and demolition throughout the metro.</p>
    </div>
    <div class="center">
      <span class="tag">Lawrenceville</span><span class="tag">Duluth</span><span class="tag">Suwanee</span>
      <span class="tag">Buford</span><span class="tag">Norcross</span><span class="tag">Snellville</span>
      <span class="tag">Lilburn</span><span class="tag">Dacula</span><span class="tag">Grayson</span>
      <span class="tag">Loganville</span><span class="tag">Sugar Hill</span><span class="tag">Winder</span>
      <span class="tag">Gainesville</span><span class="tag">Athens</span><span class="tag">Atlanta Metro</span>
    </div>
  </div>
</section>

{C.strip()}
{C.cta()}
"""
page("about.html",
     f"About {BIZ['name']} | Lawrenceville, GA",
     "United Recycling Scrap Metals LLC is a licensed and bonded scrap metal recycler in Lawrenceville, Georgia, open to the public and serving industrial accounts across North Georgia.",
     "about.html", about)


# ---------------------------------------------------------------- CONTACT
# No form and no email anywhere on this site (client request 9/25 — he isn't tech
# literate and doesn't want an inbox to miss). Phone and text only, and the page's
# whole job is to get someone to call or text and ask for Gus.
contact = banner("Call Or Text Us",
                 "No forms, no email. Pick up the phone or send a text &mdash; "
                 "and ask for " + ASKNAME + ".") + f"""
<section>
  <div class="wrap">
    <div class="callbox">
      <span class="callbox-eyebrow">Call or text</span>
      <a class="callbox-number" href="tel:{PH}">{P}</a>
      <p class="callbox-ask">{ASK}</p>
      <p class="callbox-note">Picture messages welcome. Send a photo of what you've got and
      you'll get a price back &mdash; it's the fastest way to find out what your load is worth.</p>
      <div class="btn-row">
        <a class="btn btn-red btn-lg" href="tel:{PH}">Call {P}</a>
        <a class="btn btn-outline btn-lg" href="sms:{PH}">Text A Photo</a>
      </div>
    </div>
  </div>
</section>

<section class="sec-gray">
  <div class="wrap split">
    <div>
      <span class="eyebrow">The yard</span>
      <h2>{BIZ['name']}</h2>
      <ul class="contact-list">
        <li><span class="cl-label">Call or text</span>
            <span class="cl-value"><a href="tel:{PH}">{P}</a></span>
            <span class="cl-sub">{ASK} &mdash; picture messages welcome</span></li>
        <li><span class="cl-label">Address</span>
            <span class="cl-value"><a href="{BIZ['map_url']}" target="_blank" rel="noopener">{BIZ['street']}<br>{BIZ['city']}, {BIZ['state']} {BIZ['zip']}</a></span></li>
        <li><span class="cl-label">Hours</span>
            <span class="cl-value" style="font-size:1rem">{BIZ['hours']}</span></li>
      </ul>
    </div>
    <div class="split-media"><img src="assets/img/gallery/brass-valves-fittings.jpg" alt="Brass valves and fittings brought in to the yard" loading="lazy" width="750" height="1000"></div>
  </div>
</section>

{C.strip()}
"""
page("contact.html",
     f"Call Or Text {BIZ['short']} | Lawrenceville, GA",
     f"Call or text United Recycling Scrap Metals in Lawrenceville GA at {P} and ask for {ASKNAME}. Picture messages welcome — send a photo of your scrap and get a price back.",
     "contact.html", contact)

# ---------------------------------------------------------------- GALLERY
gal = banner("Our Yard &amp; Material",
             "Real loads that came across our scale &mdash; photographed at the yard on "
             "Hurricane Shoals Road.") + f"""
<section>
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow">Photo gallery</span>
      <h2>This Is What We Buy</h2>
      <p class="lede">Copper, brass, wire, motors, boards and fittings &mdash; graded, weighed and
      paid for the same day. If you've got something that looks like any of this, call or text
      <a href="tel:{PH}">{P}</a> and ask for {ASKNAME}.</p>
    </div>
    {carousel_block()}
  </div>
</section>

<section class="sec-gray">
  <div class="wrap">
    <div class="sec-head center">
      <span class="eyebrow">All photos</span>
      <h2>Every Load, Up Close</h2>
    </div>
    <div class="gal-grid">
""" + "\n".join(
    f'      <figure class="gal-item"><img src="assets/img/gallery/{f}" alt="{t} at United Recycling Scrap Metals" loading="lazy" width="750" height="1000"><figcaption>{t}</figcaption></figure>'
    for f, t, c in GALLERY
) + f"""
    </div>
  </div>
</section>

{C.strip()}
{C.cta("Got Something That Looks Like This?")}
"""
page("gallery.html",
     f"Photo Gallery | {BIZ['name']}",
     "Photos of real scrap metal loads bought at United Recycling Scrap Metals in Lawrenceville, GA — bare bright copper, brass, insulated wire, motors, circuit boards and fittings.",
     "gallery.html", gal)


# ---------------------------------------------------------------- 404
# thank-you.html is gone with the form — nothing posts anywhere any more.
nf = f"""<section class="banner">
  <div class="wrap">
    <h1>Page Not Found</h1>
    <p>That page isn't here &mdash; but the metal still is. Call or text {P} and ask for {ASKNAME}.</p>
    <div class="btn-row" style="margin-top:26px">
      <a class="btn btn-red btn-lg" href="tel:{PH}">Call {P}</a>
      <a class="btn btn-ghost btn-lg" href="index.html">Home</a>
      <a class="btn btn-ghost btn-lg" href="what-we-buy.html">What We Buy</a>
    </div>
  </div>
</section>
"""
page("404.html", f"Page Not Found | {BIZ['short']}", "Page not found.", "", nf)


# ---------------------------------------------------------------- PHOTO CREDITS
import json as _json
_cred_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "credits.json")
_rows = ""
if os.path.exists(_cred_path):
    for c in _json.load(open(_cred_path)):
        lic = c["license"]
        lic_html = f'<a href="{c["license_url"]}" target="_blank" rel="noopener">{lic}</a>' if c.get("license_url") else lic
        _rows += (f'        <li><strong>{c["file"]}</strong> &mdash; &ldquo;{c["source_file"]}&rdquo; '
                  f'by {c["artist"]}, {lic_html}, via '
                  f'<a href="{c["commons"]}" target="_blank" rel="noopener">Wikimedia Commons</a>.</li>\n')

cred = banner("Photo Credits",
              "Placeholder photography used on this site, with source and license for each image.") + f"""
<section>
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow">Attribution</span>
      <h2>Image Sources</h2>
      <p class="lede">These are freely-licensed stand-in photos, not pictures of {BIZ['name']}. They get replaced with the yard's own photography before or shortly after launch &mdash; at which point this page goes away.</p>
    </div>
    <ul class="credits">
{_rows}    </ul>
  </div>
</section>
"""
page("credits.html", f"Photo Credits | {BIZ['short']}",
     "Image sources and licenses for photography used on this site.", "", cred)


# ---------------------------------------------------------------- robots / sitemap
write("robots.txt", "User-agent: *\nAllow: /\n")
pages = ["index.html","what-we-buy.html","drop-off.html","commercial.html",
         "demolition.html","vehicles.html","gallery.html","about.html","contact.html"]
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for p in pages:
    loc = "" if p == "index.html" else p
    sm += f"  <url><loc>https://unitedelectricalsurplus.com/{loc}</loc></url>\n"
sm += "</urlset>\n"
write("sitemap.xml", sm)

print("\nBuild complete.")
