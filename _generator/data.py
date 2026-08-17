# -*- coding: utf-8 -*-
"""United Recycling Scrap Metals LLC — site content.
Everything the client can change lives here. Edit, then run: python3 _generator/build.py
Source of truth for facts: Gus Heart's printed flyer (see DEMO-NOTES.md)."""

BIZ = {
    "name": "United Recycling Scrap Metals LLC",
    "short": "United Recycling",
    "owner": "Gus Heart",
    "phone_display": "470-655-9608",
    "phone_href": "+14706559608",
    "email": "unitedelectricalsurplus@yahoo.com",
    "street": "621 Hurricane Shoals Rd",
    "city": "Lawrenceville",
    "state": "GA",
    "zip": "30046",
    "map_url": "https://maps.google.com/?q=621+Hurricane+Shoals+Rd+Lawrenceville+GA+30046",
    # TODO(client): confirm real yard hours
    "hours": "Mon–Fri 8:00am – 5:00pm · Sat 8:00am – 12:00pm",
    "tagline": "Ferrous &amp; Non-Ferrous Metal Recycling",
}

NAV = [
    ("index.html", "Home"),
    ("what-we-buy.html", "What We Buy"),
    ("drop-off.html", "Drop Off"),
    ("commercial.html", "Commercial"),
    ("demolition.html", "Demolition"),
    ("vehicles.html", "Vehicles"),
    ("about.html", "About"),
]

# The four ABC-style pillars
PILLARS = [
    ("drop-off.html", "Public Drop-Off",
     "Open to the public. Cans, wire, motors, ice boxes, old appliances — pull in, get weighed, get paid."),
    ("commercial.html", "Commercial &amp; Industrial",
     "Plant managers and business owners: switch gear, MCCs, breakers, motors, transformers, machinery."),
    ("demolition.html", "Demolition &amp; Cleanouts",
     "We do demolition for industrial plants, schools and malls — and haul every pound of it out."),
    ("vehicles.html", "Vehicles &amp; Equipment",
     "Company vehicles, fleet trucks, heavy equipment and machinery — working or damaged."),
]

MATERIALS = [
    ("Ferrous Metals", [
        "Steel — any grade",
        "Structural steel &amp; beams",
        "Cast iron",
        "Machinery — working or damaged",
        "Appliances &amp; ice boxes",
        "Pipe, fittings &amp; valves",
        "Stainless containers, tanks &amp; vats",
        "Company vehicles &amp; equipment",
    ]),
    ("Non-Ferrous Metals", [
        "Copper",
        "Brass",
        "Aluminum",
        "Aluminum cans",
        "Stainless steel",
        "Lead",
        "Nickel &amp; cobalt",
        "Tantalum",
        "High temp alloys",
        "Carbide &amp; carbide sludge",
        "Radiators",
        "Precious metals",
    ]),
    ("Electrical &amp; Plant Equipment", [
        "Electric equipment &amp; switch gear",
        "MCCs, breakers &amp; panels",
        "Disconnects",
        "Electric motors",
        "Transformers",
        "Electrical &amp; insulated wire",
        "Heat exchangers",
        "Chillers",
    ]),
    ("Specialty &amp; Hard-to-Place", [
        "M.R.I. magnets",
        "X-ray film",
        "Litho film negatives",
        "Surplus electrical inventory",
    ]),
]

PROMISES = [
    ("We Pay More", "We pay more than local scrap yards. Bring us a ticket from another yard and we'll beat it."),
    ("Licensed &amp; Bonded", "A licensed and bonded Georgia company — paperwork done right, every load."),
    ("Text Us a Photo", "Text or picture-message your pile to " + BIZ["phone_display"] + " and get a number back."),
]

# Referral partner — Gus's friend. He does the heavy demolition side.
# TODO(client): get the real phone + web address from Gus. bigdogdemo.com is a parked
# GoDaddy lander and bigdogdemolition.com does not resolve, so nothing is linked yet.
PARTNER = {
    "name": "Big Dog Demolition",
    "city": "Atlanta, GA",
    "blurb": "A longtime friend of the yard and the crew we hand the biggest teardowns to.",
    "phone_display": "",   # TODO(client)
    "url": "",             # TODO(client)
}

# What he'll actually tear down. Straight from Gus.
DEMO_SCOPE = [
    ("Power Plants", "Generating stations, boiler houses, turbine halls and the switchyards attached to them."),
    ("Industrial Plants", "Manufacturing facilities, processing lines, foundries and full production floors."),
    ("Big Commercial Plants", "The whole building down to the slab &mdash; structural steel, roof deck, walls, footings."),
    ("Schools &amp; Mini-Malls", "Institutional and retail demolition, including selective interior strip-outs."),
    ("Warehouses &amp; Distribution", "Racking, mezzanines, dock equipment, conveyor and clear-span structures."),
    ("Substations &amp; Switchyards", "Transformers, breakers, bus work, switch gear and the copper that goes with it."),
    ("Tanks &amp; Vessels", "Stainless and carbon steel tanks, vats, silos, pressure vessels and piping."),
    ("Plant Decommissioning", "Retired lines cut out, rigged, hauled and paid for &mdash; without stopping the rest of the plant."),
]
