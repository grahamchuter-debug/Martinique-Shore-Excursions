#!/usr/bin/env python3
"""Generate index.html page shells for martiniqueshoreexcursions.com."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOMAIN = "https://martiniqueshoreexcursions.com"

HOME_FAQS = [
    ("Is Martinique good for cruise passengers?", "Yes. Martinique rewards cruise passengers who want more than a beach break. French Caribbean culture, volcanic scenery, rum heritage and compact north or south routes make it one of the more distinctive Lesser Antilles port calls."),
    ("Where do cruise ships dock in Martinique?", "Most ships use Pointe Simon in downtown Fort-de-France. Some vessels anchor in the bay and tender passengers to La Tourelles. Both are close to taxis, tour pickups and the city centre."),
    ("Can you visit Mount Pelée from a cruise ship?", "Yes, on a north Martinique shore excursion. Tours typically reach viewpoints and interpretive stops rather than summit hikes. Expect roughly 45–60 minutes driving from Fort-de-France."),
    ("Is Saint-Pierre worth visiting?", "Absolutely. Saint-Pierre — known as the Pompeii of the Caribbean — was destroyed by Mount Pelée's 1902 eruption. It is a highlight of most north Martinique cruise excursions."),
    ("Are Martinique shore excursions suitable for families?", "Yes. South Martinique tours with beach stops work well for families. North tours suit curious older kids and teens interested in volcanoes and history."),
    ("Do Martinique tours return to the ship on time?", "Reputable Martinique shore excursion operators track ship schedules and plan routes with buffer time. Always confirm your all aboard time at booking."),
    ("Should I choose north or south Martinique?", "Choose north for Mount Pelée, Saint-Pierre and rainforest scenery. Choose south for beaches, Diamond Rock views and a more relaxed pace."),
    ("Is Martinique French-speaking?", "Yes. French is the official language. Tour guides on Martinique cruise excursions typically speak English, and tourist areas around Fort-de-France accommodate international visitors."),
    ("Can you visit a rum distillery on a cruise stop?", "Yes. Northern Martinique tours often include a rhum agricole distillery stop such as Depaz or J.M. Visits are usually 30–45 minutes."),
]

EXCURSIONS_FAQS = [
    ("Should I choose north or south Martinique?", "North for volcanoes, Saint-Pierre and rum. South for beaches and a relaxed pace. With one port day, pick one direction."),
    ("Do Martinique tours return to the ship on time?", "Licensed operators running Fort-de-France cruise port tours track ship schedules. Confirm your all aboard time when booking."),
    ("Are Martinique shore excursions suitable for families?", "South tours with beach time are the easiest fit for families. North tours work for older children interested in history."),
    ("Can you visit a rum distillery on a cruise stop?", "Yes — north Martinique tours commonly include Depaz, J.M. or similar rhum agricole distilleries."),
    ("How much time do I need for a Martinique excursion?", "Plan on 4–5 hours for either north or south highlights, plus 1–2 hours of buffer before all aboard."),
]

NORTH_FAQS = [
    ("Can you visit Mount Pelée from a cruise ship?", "Yes. North Martinique shore excursions reach Pelée viewpoints by road. Summit hikes require a full day and are not part of standard cruise tours."),
    ("Is Saint-Pierre worth visiting?", "Saint-Pierre is the centrepiece of most north tours — a haunting French Caribbean town preserved by volcanic tragedy."),
    ("Do north Martinique tours return to the ship on time?", "Reputable operators plan north routes with return buffers. Confirm your all aboard time at booking."),
    ("Can you visit a rum distillery on this tour?", "Many north tours include a rhum agricole distillery such as Depaz or J.M."),
]

SOUTH_FAQS = [
    ("Are south Martinique tours good for families?", "Yes. Beach stops, easy walking and shorter drives make south tours among the most family-friendly Martinique shore excursions."),
    ("Should I choose south over north Martinique?", "Choose south if beaches and swimming are your priority. Choose north for Mount Pelée, Saint-Pierre and rum distilleries."),
    ("Do south tours return to the ship on time?", "Shorter distances give south tours excellent return-to-ship reliability."),
    ("Can I swim on a south Martinique excursion?", "Most south tours include a beach or snorkel stop at Les Anses-d'Arlet or nearby coves."),
]

PORT_FAQS = [
    ("Where do cruise ships dock in Martinique?", "Pointe Simon in downtown Fort-de-France or La Tourelles via tender."),
    ("Is Martinique French-speaking?", "Yes. French is the official language. English is common on organised Martinique shore excursions."),
    ("Is Martinique good for cruise passengers?", "Martinique offers French culture, volcanoes, rum and beaches within reach of Fort-de-France on a single shore excursion."),
]

ONE_DAY_FAQS = [
    ("How much time do I need in Martinique port?", "Most ships allow 5–9 hours ashore. A 4–5 hour north or south excursion uses the bulk of that time comfortably."),
    ("Should I choose north or south Martinique?", "North for Pelée, Saint-Pierre and rum. South for beaches and Diamond Rock."),
    ("Can you visit a rum distillery on a cruise stop?", "Yes — north Martinique tours often include a distillery visit."),
]

SAINT_PIERRE_FAQS = [
    ("Is Saint-Pierre worth visiting?", "Yes — it is one of the most memorable stops on any Martinique cruise excursion."),
    ("Can you visit Mount Pelée from Saint-Pierre?", "Pelée viewpoints are a short drive above Saint-Pierre. North Martinique tours typically include both."),
    ("How long do you need in Saint-Pierre?", "60–90 minutes covers the museum and waterfront within a 4–5 hour north route."),
]

RUM_FAQS = [
    ("Can you visit a rum distillery on a cruise stop?", "Yes. North Martinique shore excursions from Fort-de-France commonly include Depaz, J.M. or similar distilleries."),
    ("What is rhum agricole?", "Rhum agricole is made from fresh-pressed sugarcane juice. Martinique's version has AOC protected status."),
    ("How long does a distillery visit take?", "Plan on 30–45 minutes including a guided tour and optional tasting."),
]


def faq_schema(faqs):
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": a},
            }
            for q, a in faqs
        ],
    }


def website_schema():
    return {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "name": "Martinique Shore Excursions",
        "url": f"{DOMAIN}/",
        "description": "Planning guide for Martinique cruise shore excursions from Fort-de-France",
    }


PAGES = [
    {
        "path": "index.html",
        "depth": 0,
        "page": "home",
        "hero": "partials/hero-home.html",
        "content": "content/home.html",
        "trust": True,
        "title": "Martinique Shore Excursions | Fort-de-France Cruise Tours",
        "description": "Discover the best Martinique shore excursions from Fort-de-France, including Mount Pelée, Saint-Pierre, rum distilleries, rainforest scenery and French Caribbean culture.",
        "canonical": "/",
        "preload": "images/hero-home.jpg",
        "og_image": "/images/hero-home.jpg",
        "schemas": [website_schema(), faq_schema(HOME_FAQS)],
    },
    {
        "path": "excursions/index.html",
        "depth": 1,
        "page": "excursions",
        "hero": "partials/hero-excursions.html",
        "content": "content/excursions.html",
        "trust": True,
        "title": "Best Martinique Shore Excursions",
        "description": "Compare the best Martinique shore excursions for cruise passengers, from island sightseeing and volcano views to rum tasting, beaches and cultural tours.",
        "canonical": "/excursions/",
        "preload": "images/hero-excursions.jpg",
        "og_image": "/images/hero-excursions.jpg",
        "schemas": [faq_schema(EXCURSIONS_FAQS)],
    },
    {
        "path": "excursions/north-martinique-tour/index.html",
        "depth": 2,
        "page": "north",
        "hero": "partials/hero-north.html",
        "content": "content/north-martinique-tour.html",
        "trust": True,
        "title": "North Martinique Shore Excursion | Mount Pelée & Saint-Pierre",
        "description": "Explore northern Martinique with a cruise-friendly shore excursion featuring Mount Pelée views, Saint-Pierre history, rainforest scenery and French Caribbean culture.",
        "canonical": "/excursions/north-martinique-tour/",
        "preload": "images/north-martinique.jpg",
        "og_image": "/images/north-martinique.jpg",
        "schemas": [faq_schema(NORTH_FAQS)],
    },
    {
        "path": "excursions/south-martinique-tour/index.html",
        "depth": 2,
        "page": "south",
        "hero": "partials/hero-south.html",
        "content": "content/south-martinique-tour.html",
        "trust": True,
        "title": "South Martinique Shore Excursion | Beaches, Villages & Island Views",
        "description": "Discover southern Martinique with beaches, coastal villages, island viewpoints and relaxed French Caribbean scenery on a cruise-friendly shore excursion.",
        "canonical": "/excursions/south-martinique-tour/",
        "preload": "images/south-martinique.jpg",
        "og_image": "/images/south-martinique.jpg",
        "schemas": [faq_schema(SOUTH_FAQS)],
    },
    {
        "path": "martinique-cruise-port-guide/index.html",
        "depth": 1,
        "page": "port",
        "hero": "partials/hero-port-guide.html",
        "content": "content/martinique-cruise-port-guide.html",
        "trust": True,
        "title": "Martinique Cruise Port Guide | Fort-de-France",
        "description": "A practical guide to Fort-de-France cruise port, including what to expect, how to choose a shore excursion and what cruise passengers can see in one day.",
        "canonical": "/martinique-cruise-port-guide/",
        "preload": "images/cruise-port.jpg",
        "og_image": "/images/cruise-port.jpg",
        "schemas": [faq_schema(PORT_FAQS)],
    },
    {
        "path": "one-day-in-martinique-from-cruise-ship/index.html",
        "depth": 1,
        "page": "one-day",
        "hero": "partials/hero-one-day.html",
        "content": "content/one-day-in-martinique-from-cruise-ship.html",
        "trust": True,
        "title": "One Day in Martinique From a Cruise Ship",
        "description": "Plan one day in Martinique from a cruise ship with ideas for sightseeing, beaches, rum distilleries, Saint-Pierre, Mount Pelée and Fort-de-France.",
        "canonical": "/one-day-in-martinique-from-cruise-ship/",
        "preload": "images/one-day.jpg",
        "og_image": "/images/one-day.jpg",
        "schemas": [faq_schema(ONE_DAY_FAQS)],
    },
    {
        "path": "saint-pierre-martinique-cruise-guide/index.html",
        "depth": 1,
        "page": "saint-pierre",
        "hero": "partials/hero-saint-pierre.html",
        "content": "content/saint-pierre-martinique-cruise-guide.html",
        "trust": True,
        "title": "Saint-Pierre Martinique Cruise Guide | Pompeii of the Caribbean",
        "description": "Learn why Saint-Pierre is known as the Pompeii of the Caribbean and why it is one of the most interesting places to visit on a Martinique shore excursion.",
        "canonical": "/saint-pierre-martinique-cruise-guide/",
        "preload": "images/saint-pierre.jpg",
        "og_image": "/images/saint-pierre.jpg",
        "schemas": [faq_schema(SAINT_PIERRE_FAQS)],
    },
    {
        "path": "martinique-rum-distillery-guide/index.html",
        "depth": 1,
        "page": "rum",
        "hero": "partials/hero-rum.html",
        "content": "content/martinique-rum-distillery-guide.html",
        "trust": True,
        "title": "Martinique Rum Distillery Guide for Cruise Passengers",
        "description": "Discover Martinique's famous rum heritage, distillery visits and what cruise passengers should know before choosing a rum-focused shore excursion.",
        "canonical": "/martinique-rum-distillery-guide/",
        "preload": "images/rum-distillery.jpg",
        "og_image": "/images/rum-distillery.jpg",
        "schemas": [faq_schema(RUM_FAQS)],
    },
]


def rel(depth, asset):
    if depth == 0:
        return asset
    prefix = "../" * depth
    return f"{prefix}{asset}"


def render_page(p):
    depth = p["depth"]
    base = "../" * depth
    data_base = base.rstrip("/") if depth else ""
    data_base_attr = f'  data-base="{data_base}"\n' if depth else '  data-base=""\n'

    schema_blocks = "\n".join(
        f'  <script type="application/ld+json">\n{json.dumps(s, indent=2)}\n  </script>'
        for s in p["schemas"]
    )

    trust_attr = ""
    if p["trust"]:
        trust_attr = '  data-trust-strip="partials/trust-strip.html"\n'

    canonical_url = DOMAIN + (p["canonical"] if p["canonical"] != "/" else "/")
    og_image_url = DOMAIN + p["og_image"]

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />

  <title>{p['title']}</title>
  <meta name="description" content="{p['description']}" />
  <meta name="keywords" content="Martinique shore excursions, Fort-de-France cruise port, Martinique cruise excursions, things to do in Martinique from a cruise ship" />
  <link rel="canonical" href="{canonical_url}" />
  <link rel="preload" as="image" href="{rel(depth, p['preload'])}" fetchpriority="high" />

  <meta property="og:type" content="website" />
  <meta property="og:url" content="{canonical_url}" />
  <meta property="og:title" content="{p['title']}" />
  <meta property="og:description" content="{p['description']}" />
  <meta property="og:image" content="{og_image_url}" />
  <meta property="og:site_name" content="Martinique Shore Excursions" />
  <meta name="twitter:card" content="summary_large_image" />

{schema_blocks}

  <script src="https://cdn.tailwindcss.com"></script>
  <script src="{rel(depth, 'js/tailwind-config.js')}"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="{rel(depth, 'css/site.css')}" />
</head>
<body
  class="bg-white text-gray-800 antialiased"
  data-page="{p['page']}"
{data_base_attr}  data-hero="{p['hero']}"
{trust_attr}  data-content="{p['content']}"
>
  <div id="site-nav"></div>
  <div id="page-hero"></div>
  <div id="page-trust-strip"></div>
  <main id="page-content"></main>
  <div id="site-footer"></div>
  <script src="{rel(depth, 'js/site.js')}"></script>
</body>
</html>
"""


def main():
    for p in PAGES:
        out = ROOT / p["path"]
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(render_page(p), encoding="utf-8")
        print(f"Created {p['path']}")


if __name__ == "__main__":
    main()
