# -*- coding: utf-8 -*-
"""Shared page chrome: <head>, top bar, header/nav, CTA band, footer."""
from data import BIZ, NAV, DIVISION

def head(title, desc, active):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="index,follow">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<link rel="stylesheet" href="assets/css/site.css">
<script type="application/ld+json">
{{
  "@context":"https://schema.org",
  "@type":"RecyclingCenter",
  "name":"{BIZ['name']}",
  "telephone":"{BIZ['phone_display']}",
  "email":"{BIZ['email']}",
  "address":{{
    "@type":"PostalAddress",
    "streetAddress":"{BIZ['street']}",
    "addressLocality":"{BIZ['city']}",
    "addressRegion":"{BIZ['state']}",
    "postalCode":"{BIZ['zip']}",
    "addressCountry":"US"
  }}
}}
</script>
</head>
<body>
"""

def topbar():
    return f"""<div class="topbar">
  <div class="wrap">
    <span>{BIZ['street']}, {BIZ['city']}, {BIZ['state']} {BIZ['zip']}</span>
    <span class="tb-note">Text and picture messages accepted &mdash; send us a photo of your load</span>
    <span><a href="tel:{BIZ['phone_href']}">{BIZ['phone_display']}</a></span>
  </div>
</div>
"""

def header(active):
    links = ""
    for href, label in NAV:
        cls = ' class="active"' if href == active else ""
        links += f'    <a href="{href}"{cls}>{label}</a>\n'
    return f"""<header class="site-header">
  <div class="wrap">
    <a class="brand" href="index.html">
      <span class="brand-mark">UR</span>
      <span class="brand-text">
        <span class="brand-name">United Recycling</span>
        <span class="brand-sub">Scrap Metals LLC</span>
      </span>
    </a>
    <button class="nav-toggle" aria-expanded="false" aria-controls="site-nav">Menu</button>
    <nav class="nav" id="site-nav">
{links}      <a class="btn btn-red" href="contact.html">Get a Quote</a>
    </nav>
  </div>
</header>
"""

def strip():
    return f"""<div class="strip">
  <div class="wrap">
    <p>Got a load right now? Text a picture to <a href="tel:{BIZ['phone_href']}">{BIZ['phone_display']}</a> and we'll price it.</p>
  </div>
</div>
"""

def cta(head_txt="Get Paid For Your Scrap Today",
        body="Send us a picture of what you've got, or pull into the yard on Hurricane Shoals Road. Either way you leave with cash."):
    return f"""<section class="cta">
  <div class="wrap">
    <span class="eyebrow eyebrow-light">Open to the public</span>
    <h2>{head_txt}</h2>
    <p>{body}</p>
    <div class="btn-row">
      <a class="btn btn-red btn-lg" href="tel:{BIZ['phone_href']}">Call {BIZ['phone_display']}</a>
      <a class="btn btn-ghost btn-lg" href="contact.html">Get a Quote</a>
    </div>
  </div>
</section>
"""

def footer():
    return f"""<footer class="site-footer">
  <div class="wrap">
    <div class="foot-grid">
      <div class="foot-brand">
        <span class="brand-name">{BIZ['name']}</span>
        <p>{BIZ['tagline']}. Licensed and bonded, open to the public, and paying more than the local yards in Gwinnett County.</p>
        <p class="foot-division">Demolition performed by<br><a href="demolition.html">{DIVISION['name']}</a></p>
      </div>
      <div>
        <h4>What We Buy</h4>
        <ul>
          <li><a href="what-we-buy.html">Ferrous metals</a></li>
          <li><a href="what-we-buy.html">Non-ferrous metals</a></li>
          <li><a href="what-we-buy.html">Electrical &amp; plant equipment</a></li>
          <li><a href="what-we-buy.html">Specialty materials</a></li>
        </ul>
      </div>
      <div>
        <h4>Services</h4>
        <ul>
          <li><a href="drop-off.html">Public drop-off</a></li>
          <li><a href="commercial.html">Commercial accounts</a></li>
          <li><a href="demolition.html">Demolition &amp; roll-offs</a></li>
          <li><a href="vehicles.html">Vehicles &amp; equipment</a></li>
        </ul>
      </div>
      <div>
        <h4>The Yard</h4>
        <ul>
          <li><a href="{BIZ['map_url']}" target="_blank" rel="noopener">{BIZ['street']}<br>{BIZ['city']}, {BIZ['state']} {BIZ['zip']}</a></li>
          <li><a href="tel:{BIZ['phone_href']}">{BIZ['phone_display']}</a></li>
          <li><a href="mailto:{BIZ['email']}">{BIZ['email']}</a></li>
          <li>{BIZ['hours']}</li>
        </ul>
      </div>
    </div>
    <div class="foot-bottom">
      <span>&copy; <span id="yr">2026</span> {BIZ['name']}. All rights reserved.</span>
      <span><a href="credits.html">Photo credits</a> &middot; Site by <a href="https://60minutesites.com" target="_blank" rel="noopener">60 Minute Sites</a></span>
    </div>
  </div>
</footer>
<script>
document.getElementById('yr').textContent = new Date().getFullYear();
var t = document.querySelector('.nav-toggle'), n = document.getElementById('site-nav');
t.addEventListener('click', function(){{
  var open = n.classList.toggle('open');
  t.setAttribute('aria-expanded', open);
}});
</script>
</body>
</html>
"""
