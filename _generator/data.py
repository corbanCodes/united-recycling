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
     "Power plants, chemical plants, mills, malls and campuses — torn down and hauled out."),
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

# What he'll actually tear down. Straight from Gus, 8/17.
# Commercial and industrial structures only — no single-family houses.
# He specifically lights up about chemical plants and big power generation.
DEMO_SCOPE = [
    ("Power &amp; Energy", [
        "Power plants &amp; energy facilities",
        "Nuclear plants",
        "Coal-fired power stations",
        "Gas-fired power plants",
        "Hydroelectric dams",
        "Substations &amp; switchyards",
    ]),
    ("Heavy Industry", [
        "Chemical plants",
        "Refineries &amp; petrochemical plants",
        "Steel mills &amp; manufacturing complexes",
        "Paper mills",
        "Automotive manufacturing plants",
        "Tanks, vats, silos &amp; pressure vessels",
    ]),
    ("Institutional &amp; Public", [
        "Major hospitals",
        "Universities &amp; campus buildings",
        "Large school districts",
        "Prisons &amp; correctional complexes",
        "Military installations",
        "Convention centers",
    ]),
    ("Commercial &amp; Large Structure", [
        "Shopping malls &amp; mini-malls",
        "Office towers",
        "Data centers",
        "Stadiums &amp; arenas",
        "Airports &amp; airport terminals",
        "Apartment &amp; multifamily complexes",
        "Industrial warehouses &amp; distribution centers",
        "Bridges &amp; large infrastructure",
    ]),
]

# The handful he'll bring up first on a call.
DEMO_HEADLINE = [
    ("Chemical Plants", "The work this yard is built around. Process piping, reactors, tank farms, structural steel and every pound of alloy in them."),
    ("Power Generation", "Nuclear, coal-fired, gas-fired and hydro &mdash; turbine halls, boiler houses, switchyards and the copper that runs through them."),
    ("Refineries &amp; Mills", "Petrochemical plants, steel mills, paper mills and automotive manufacturing complexes."),
    ("Big Public Structures", "Malls, stadiums, airports, hospitals, campuses and correctional complexes."),
]
