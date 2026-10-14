# -*- coding: utf-8 -*-
"""United Recycling Scrap Metals LLC — site content.
Everything the client can change lives here. Edit, then run: python3 _generator/build.py
Source of truth for facts: the printed flyer + phone calls with the client.
The flyer reads "Gus Heart"; the client confirmed by phone on 9/25 that it is
**Gus Harvey**, the son, and that he is who callers should ask for. (see DEMO-NOTES.md)"""

BIZ = {
    "name": "United Recycling Scrap Metals LLC",
    "short": "United Recycling",
    "owner": "Gus Harvey",
    "phone_display": "470-655-9608",
    "phone_href": "+14706559608",
    "street": "621 Hurricane Shoals Rd",
    "city": "Lawrenceville",
    "state": "GA",
    "zip": "30046",
    "map_url": "https://maps.google.com/?q=621+Hurricane+Shoals+Rd+Lawrenceville+GA+30046",
    # TODO(client): confirm real yard hours
    "hours": "Mon–Fri 8:00am – 5:00pm · Sat 8:00am – 12:00pm",
    "tagline": "Ferrous &amp; Non-Ferrous Metal Recycling",
    # NO email and NO forms anywhere on this site — client request 9/25. Phone only.
    # Every phone number is followed by this line. It is the main conversion instruction.
    "ask_name": "Gus Harvey",          # <- change this one line if the name ever changes
    "ask_for": "Ask for Gus Harvey",
    "call_cta": "Call or text &mdash; ask for Gus Harvey",
    "call_note": "Call or text this number and ask for Gus Harvey. Picture messages welcome &mdash; "
                 "send a photo of your load and you'll get a price back.",
}

NAV = [
    ("index.html", "Home"),
    ("what-we-buy.html", "What We Buy"),
    ("drop-off.html", "Drop Off"),
    ("commercial.html", "Commercial"),
    ("demolition.html", "Demolition"),
    ("vehicles.html", "Vehicles"),
    ("gallery.html", "Gallery"),
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
        "Christmas &amp; holiday light strings",
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

# The demolition arm, branded as its own entity. Gus's wording on 8/17:
# "United Recycling Demolition Metals LLC" — a sub-service, NOT a rename of the yard.
# The header/footer brand stays United Recycling Scrap Metals LLC (that's the flyer,
# the yard and the phone number). This name fronts the demolition page.
DIVISION = {
    "name": "United Recycling Demolition Metals LLC",
    "short": "United Recycling Demolition Metals",
    "eyebrow": "Demolition performed by",
    "parent": "United Recycling Scrap Metals LLC",
    "blurb": "The demolition division of the yard on Hurricane Shoals Road. Same crew, "
             "same scale, same check &mdash; pointed at buildings instead of pickup beds.",
}

# Gus's own photos of material that came across the scale. Shot on his phone and
# texted over, so they arrived letterboxed — cropped to the 750x1000 content region.
# These replace the Wikimedia stand-ins wherever a real photo does the job better.
GALLERY = [
    ("bare-bright-copper.jpg",     "Bare bright copper wire",      "Bundled bare bright copper — our top-paying grade."),
    ("wire-red-coils.jpg",         "Insulated copper wire",        "Coils of insulated copper wire, sorted by grade."),
    ("brass-valves-fittings.jpg",  "Brass valves &amp; fittings",  "Red brass, yellow brass, valves and plumbing fittings."),
    ("copper-pipe-fittings.jpg",   "Copper pipe &amp; fittings",   "Copper tube, pipe and fittings out of a plumbing tear-out."),
    ("alternators-motors.jpg",     "Alternators &amp; motors",     "Alternators, starters and small electric motors."),
    ("circuit-boards.jpg",         "Circuit boards &amp; e-scrap", "Boards, power supplies and heat sinks — we grade these too."),
    ("heavy-cable.jpg",            "Heavy cable",                  "Heavy gauge insulated cable off a commercial job."),
    ("insulated-wire-black.jpg",   "Insulated wire",               "Black jacketed wire, ready for the scale."),
    ("insulated-wire-blue.jpg",    "Communications wire",          "Blue and yellow data and comms wire."),
    ("insulated-wire-colors.jpg",  "Mixed colored wire",           "Mixed low-voltage and control wire."),
    ("insulated-wire-mixed.jpg",   "Mixed wire load",              "A mixed wire load straight out of a contractor's truck."),
    ("stripped-wire.jpg",          "Aluminum &amp; stripped wire", "Stripped and aluminum wire, graded separately."),
    ("insulated-building-wire.jpg","Insulated Building Wire",   "THHN and low-voltage wire in every color and gauge."),
    ("heavy-jacketed-cable.jpg",  "Heavy Jacketed Cable",       "Large gauge jacketed cable off commercial and industrial jobs."),
    ("copper-coils-pallets.jpg",  "Copper Coils On Pallets",    "Coiled copper and bare bright staged for pickup."),
    ("bare-bright-copper-2.jpg",  "Bare Bright, Sorted",        "Clean bare bright copper &mdash; the grade that pays the most."),
    ("brass-valves.jpg",          "Brass Valves &amp; Fittings","Red and yellow brass valve bodies and plumbing stock."),
    ("faucets-fixtures.jpg",      "Faucets &amp; Fixtures",     "Chrome, stainless and brass fixtures from commercial tear-outs."),
    ("aluminum-radiators.jpg",    "Aluminum Radiators",         "Aluminum and alloy radiators, graded on their own."),
    ("lead-acid-batteries.jpg",   "Lead-Acid Batteries",        "Automotive and industrial batteries bought by the pallet."),
    ("lead-sheet.jpg",            "Lead Sheet &amp; Plate",     "Sheet lead, plate and lead-bearing material."),
    ("brake-rotors.jpg",          "Rotors &amp; Cast Iron",     "Brake rotors and heavy cast iron, paid by weight."),
    ("christmas-lights.jpg",      "Christmas Light Strings",    "Yes, really &mdash; we buy holiday lights by the box."),
    ("christmas-lights-bulk.jpg", "Holiday Lights In Bulk",     "Pallet and gaylord loads from businesses and installers."),
]

# Two real yard locations (10/6/26). The Buford building is newly rented.
# LOCATIONS[0] stays the primary — it owns the phone number and the schema address.
LOCATIONS = [
    {
        "name": "Lawrenceville Yard",
        "label": "Main yard &amp; public drop-off",
        "street": "621 Hurricane Shoals Rd",
        "city": "Lawrenceville", "state": "GA", "zip": "30046",
        "map_url": "https://maps.google.com/?q=621+Hurricane+Shoals+Rd+Lawrenceville+GA+30046",
    },
    {
        "name": "Buford Location",
        "label": "Second location",
        "street": "1901 Peachtree Industrial Blvd",
        "city": "Buford", "state": "GA", "zip": "30518",
        "map_url": "https://maps.google.com/?q=1901+Peachtree+Industrial+Blvd+Buford+GA+30518",
    },
]

# Where the trucks actually travel for large commercial and industrial loads.
# NOTE(10/6): these came from the client's expansion list, which mixed cities and states.
# They are presented as "where we travel for large loads", NOT as office locations —
# claiming branches that don't exist would be false advertising and would generate calls
# nobody can service. Confirm he really runs equipment to all of these. See DEMO-NOTES.md.
SERVICE_AREA = [
    "Georgia", "Tennessee", "Alabama", "Florida",
    "North Carolina", "Texas", "Louisiana", "Oklahoma",
]
SERVICE_CITIES = [
    "Atlanta", "Charlotte", "Nashville", "Birmingham",
    "Dallas", "Houston", "Oklahoma City", "Baton Rouge", "New Orleans",
]

# Seasonal buy, from Gus 10/14/26: "after the holidays people get rid of a lot of
# Christmas lights, large big businesses commercial — I buy Christmas lights."
HOLIDAY = {
    "kicker": "Seasonal &mdash; after the holidays",
    "heading": "We Buy Christmas Lights",
    "body": "Every January, businesses, property managers, churches and light installers "
            "throw out pallets of old holiday light strings. Don't pay to dump them. Those "
            "strings are insulated copper wire, and we buy them by weight &mdash; burnt out, "
            "tangled or broken makes no difference to us.",
    "points": [
        "Commercial and bulk quantities &mdash; boxes, pallets and gaylords",
        "Burnt out, tangled, broken or mixed in with extension cords is fine",
        "No sorting, no cutting the ends off, no testing required",
        "Installers and property managers: call before you pay a dumpster fee",
    ],
    "photo": "christmas-lights.jpg",
}
