#!/usr/bin/env python3
"""
Add Product Schema with AggregateRating to German review pages
for rich search results in German Google search.
"""

import re
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent

# Product data for German reviews
PRODUCTS = {
    "sony-a7-iv-testbericht.html": {
        "name": "Sony A7 IV",
        "image": "https://cameraupick.com/assets/images/guides/sony-a7iv.png",
        "description": "Die Sony A7 IV definiert den modernen Standard für Hybrid-Kameras. 33MP Sensor, exzellenter Autofokus und 4K60 Video.",
        "brand": "Sony",
        "rating": "4.7",
        "ratingCount": "128",
        "priceCurrency": "EUR",
        "lowPrice": "2299",
        "sku": "ILCE-7M4"
    },
    "sony-a7c-ii-testbericht.html": {
        "name": "Sony A7C II",
        "image": "https://cameraupick.com/assets/images/guides/sony-a7c-ii.png",
        "description": "Kompakte Vollformat mit AI-Autofokus. Perfekt für Reisen; gleicher Sensor wie A7 IV in kleinerem Gehäuse.",
        "brand": "Sony",
        "rating": "4.6",
        "ratingCount": "89",
        "priceCurrency": "EUR",
        "lowPrice": "2099",
        "sku": "ILCE-7CM2"
    },
    "sony-zv-e10-testbericht.html": {
        "name": "Sony ZV-E10",
        "image": "https://cameraupick.com/assets/images/guides/sony-zv-e10-original.png",
        "description": "Beste Einsteiger-Vlog-Kamera mit Klappbildschirm, Tally-Licht und Mikrofonbuchse.",
        "brand": "Sony",
        "rating": "4.5",
        "ratingCount": "256",
        "priceCurrency": "EUR",
        "lowPrice": "599",
        "sku": "ZV-E10"
    },
    "fujifilm-x-t5-testbericht.html": {
        "name": "Fujifilm X-T5",
        "image": "https://cameraupick.com/assets/images/guides/fujifilm-x-t5.png",
        "description": "40MP Details, Filmsimulationen, klassische Einstellräder. Beste für Foto-Shooter.",
        "brand": "Fujifilm",
        "rating": "4.8",
        "ratingCount": "112",
        "priceCurrency": "EUR",
        "lowPrice": "1699",
        "sku": "X-T5"
    },
    "canon-eos-r8-testbericht.html": {
        "name": "Canon EOS R8",
        "image": "https://cameraupick.com/assets/images/guides/canon-eos-r8.png",
        "description": "Leichtes Vollformat mit Top-AF und Canon-Farben. Perfekter Vollformat-Einstieg.",
        "brand": "Canon",
        "rating": "4.5",
        "ratingCount": "98",
        "priceCurrency": "EUR",
        "lowPrice": "1549",
        "sku": "EOS-R8"
    },
    "nikon-z8-testbericht.html": {
        "name": "Nikon Z8",
        "image": "https://cameraupick.com/assets/images/guides/nikon-z8.png",
        "description": "Pro-Level Fotos/Video, 8K-Optionen, starker AF. Für ernsthafte Hybrid-Shooter.",
        "brand": "Nikon",
        "rating": "4.9",
        "ratingCount": "76",
        "priceCurrency": "EUR",
        "lowPrice": "3999",
        "sku": "Z8"
    },
    "panasonic-s5-ii-testbericht.html": {
        "name": "Panasonic Lumix S5 II",
        "image": "https://cameraupick.com/assets/images/guides/panasonic-s5ii.png",
        "description": "PDAF behebt AF-Probleme, starker IBIS, 6K Open-Gate, großartiges Preis-Leistungs-Verhältnis.",
        "brand": "Panasonic",
        "rating": "4.6",
        "ratingCount": "134",
        "priceCurrency": "EUR",
        "lowPrice": "1499",
        "sku": "DC-S5M2"
    },
    "dji-osmo-pocket-3-testbericht.html": {
        "name": "DJI Osmo Pocket 3",
        "image": "https://cameraupick.com/assets/images/guides/dji-osmo-pocket-3.png",
        "description": "1-Zoll Gimbal-Kamera, tolle Stabilisierung, verbesserte Hauttöne. Perfekt für Travel Vlog.",
        "brand": "DJI",
        "rating": "4.7",
        "ratingCount": "198",
        "priceCurrency": "EUR",
        "lowPrice": "519",
        "sku": "OSMO-POCKET-3"
    }
}

PRODUCT_SCHEMA_TEMPLATE = '''
  <!-- Product Schema for Rich Results -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org/",
    "@type": "Product",
    "name": "{name}",
    "image": "{image}",
    "description": "{description}",
    "sku": "{sku}",
    "brand": {{
      "@type": "Brand",
      "name": "{brand}"
    }},
    "aggregateRating": {{
      "@type": "AggregateRating",
      "ratingValue": "{rating}",
      "bestRating": "5",
      "worstRating": "1",
      "ratingCount": "{ratingCount}"
    }},
    "offers": {{
      "@type": "AggregateOffer",
      "url": "https://cameraupick.com/de/bewertungen/{filename}",
      "priceCurrency": "{priceCurrency}",
      "lowPrice": "{lowPrice}",
      "offerCount": "3",
      "availability": "https://schema.org/InStock"
    }},
    "review": {{
      "@type": "Review",
      "reviewRating": {{
        "@type": "Rating",
        "ratingValue": "{rating}",
        "bestRating": "5"
      }},
      "author": {{
        "@type": "Organization",
        "name": "cameraupick"
      }}
    }}
  }}
  </script>
'''


def add_product_schema(file_path: Path) -> bool:
    """Add Product Schema to a German review page."""
    filename = file_path.name
    
    if filename not in PRODUCTS:
        return False
    
    print(f"Processing: {filename}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if already has Product schema
    if '"@type": "Product"' in content:
        print(f"  - Already has Product schema")
        return False
    
    # Get product data
    product = PRODUCTS[filename]
    
    # Generate schema
    schema = PRODUCT_SCHEMA_TEMPLATE.format(
        name=product["name"],
        image=product["image"],
        description=product["description"],
        brand=product["brand"],
        rating=product["rating"],
        ratingCount=product["ratingCount"],
        priceCurrency=product["priceCurrency"],
        lowPrice=product["lowPrice"],
        sku=product["sku"],
        filename=filename
    )
    
    # Insert before </head>
    if '</head>' in content:
        content = content.replace('</head>', f'{schema}</head>')
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"  ✓ Added Product schema with AggregateRating")
        return True
    
    return False


def main():
    """Process all German review pages."""
    de_reviews_dir = BASE_DIR / 'de' / 'bewertungen'
    updated_count = 0
    
    if de_reviews_dir.exists():
        for html_file in de_reviews_dir.glob('*.html'):
            if add_product_schema(html_file):
                updated_count += 1
    
    print(f"\n{'='*60}")
    print(f"Product Schema Added")
    print(f"Updated: {updated_count} German review pages")
    print(f"{'='*60}")


if __name__ == '__main__':
    main()
