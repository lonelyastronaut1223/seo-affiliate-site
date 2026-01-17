#!/usr/bin/env python3
"""
Add advanced SEO features to German pages:
1. Breadcrumb Schema for all pages
2. FAQ Schema for guide pages
3. Open Graph tags for review/guide pages
"""

import re
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).parent.parent.parent

# German page configurations
GERMAN_PAGES = {
    # Reviews
    'de/bewertungen/sony-a7-iv-testbericht.html': {
        'title': 'Sony A7 IV Testbericht',
        'breadcrumbs': [
            ('Startseite', 'https://cameraupick.com/de/'),
            ('Testberichte', 'https://cameraupick.com/de/#testberichte'),
            ('Sony A7 IV Testbericht', 'https://cameraupick.com/de/bewertungen/sony-a7-iv-testbericht.html')
        ],
        'og_image': 'https://cameraupick.com/assets/images/guides/sony-a7iv.png',
        'og_description': 'Sony A7 IV Testbericht 2026: Bildqualität, Autofokus, Video im Detail. Lohnt sich die Investition?'
    },
    'de/bewertungen/sony-a7c-ii-testbericht.html': {
        'title': 'Sony A7C II Testbericht',
        'breadcrumbs': [
            ('Startseite', 'https://cameraupick.com/de/'),
            ('Testberichte', 'https://cameraupick.com/de/#testberichte'),
            ('Sony A7C II Testbericht', 'https://cameraupick.com/de/bewertungen/sony-a7c-ii-testbericht.html')
        ],
        'og_image': 'https://cameraupick.com/assets/images/guides/sony-a7c-ii.png',
        'og_description': 'Sony A7C II Testbericht: Kompaktes Vollformat mit KI-Autofokus. Perfekt für Reisen.'
    },
    'de/bewertungen/fujifilm-x-t5-testbericht.html': {
        'title': 'Fujifilm X-T5 Testbericht',
        'breadcrumbs': [
            ('Startseite', 'https://cameraupick.com/de/'),
            ('Testberichte', 'https://cameraupick.com/de/#testberichte'),
            ('Fujifilm X-T5 Testbericht', 'https://cameraupick.com/de/bewertungen/fujifilm-x-t5-testbericht.html')
        ],
        'og_image': 'https://cameraupick.com/assets/images/guides/fujifilm-x-t5.png',
        'og_description': 'Fujifilm X-T5 Testbericht: 40MP, Filmsimulationen, klassisches Design. Für Foto-Enthusiasten.'
    },
    'de/bewertungen/canon-eos-r8-testbericht.html': {
        'title': 'Canon EOS R8 Testbericht',
        'breadcrumbs': [
            ('Startseite', 'https://cameraupick.com/de/'),
            ('Testberichte', 'https://cameraupick.com/de/#testberichte'),
            ('Canon EOS R8 Testbericht', 'https://cameraupick.com/de/bewertungen/canon-eos-r8-testbericht.html')
        ],
        'og_image': 'https://cameraupick.com/assets/images/guides/canon-eos-r8.png',
        'og_description': 'Canon EOS R8 Testbericht: Leichtes Vollformat mit Top-Autofokus und Canon-Farben.'
    },
    'de/bewertungen/nikon-z8-testbericht.html': {
        'title': 'Nikon Z8 Testbericht',
        'breadcrumbs': [
            ('Startseite', 'https://cameraupick.com/de/'),
            ('Testberichte', 'https://cameraupick.com/de/#testberichte'),
            ('Nikon Z8 Testbericht', 'https://cameraupick.com/de/bewertungen/nikon-z8-testbericht.html')
        ],
        'og_image': 'https://cameraupick.com/assets/images/guides/nikon-z8.png',
        'og_description': 'Nikon Z8 Testbericht: Profi-Niveau für Foto und Video, 8K-Optionen, starker AF.'
    },
    'de/bewertungen/panasonic-s5-ii-testbericht.html': {
        'title': 'Panasonic S5 II Testbericht',
        'breadcrumbs': [
            ('Startseite', 'https://cameraupick.com/de/'),
            ('Testberichte', 'https://cameraupick.com/de/#testberichte'),
            ('Panasonic S5 II Testbericht', 'https://cameraupick.com/de/bewertungen/panasonic-s5-ii-testbericht.html')
        ],
        'og_image': 'https://cameraupick.com/assets/images/guides/panasonic-s5ii.png',
        'og_description': 'Panasonic S5 II Testbericht: PDAF behebt AF-Probleme, starker IBIS, 6K Open-Gate.'
    },
    'de/bewertungen/sony-zv-e10-testbericht.html': {
        'title': 'Sony ZV-E10 Testbericht',
        'breadcrumbs': [
            ('Startseite', 'https://cameraupick.com/de/'),
            ('Testberichte', 'https://cameraupick.com/de/#testberichte'),
            ('Sony ZV-E10 Testbericht', 'https://cameraupick.com/de/bewertungen/sony-zv-e10-testbericht.html')
        ],
        'og_image': 'https://cameraupick.com/assets/images/guides/sony-zv-e10-original.png',
        'og_description': 'Sony ZV-E10 Testbericht: Beste Budget-Vlogkamera mit Flip-Screen und Mikrofonanschluss.'
    },
    'de/bewertungen/dji-osmo-pocket-3-testbericht.html': {
        'title': 'DJI Osmo Pocket 3 Testbericht',
        'breadcrumbs': [
            ('Startseite', 'https://cameraupick.com/de/'),
            ('Testberichte', 'https://cameraupick.com/de/#testberichte'),
            ('DJI Osmo Pocket 3 Testbericht', 'https://cameraupick.com/de/bewertungen/dji-osmo-pocket-3-testbericht.html')
        ],
        'og_image': 'https://cameraupick.com/assets/images/guides/dji-osmo-pocket-3.png',
        'og_description': 'DJI Osmo Pocket 3 Testbericht: 1-Zoll Gimbal-Kamera, perfekte Stabilisierung für Reise-Vlogs.'
    },
    # Guides
    'de/ratgeber/beste-kamera-fuer-anfaenger-2026.html': {
        'title': 'Beste Kamera für Anfänger 2026',
        'breadcrumbs': [
            ('Startseite', 'https://cameraupick.com/de/'),
            ('Ratgeber', 'https://cameraupick.com/de/#ratgeber'),
            ('Beste Kamera für Anfänger', 'https://cameraupick.com/de/ratgeber/beste-kamera-fuer-anfaenger-2026.html')
        ],
        'og_image': 'https://cameraupick.com/assets/images/guides/beginner.webp',
        'og_description': 'Die besten Kameras für Einsteiger 2026: Sony, Canon, Fujifilm im Vergleich mit Kaufberatung.'
    },
    'de/ratgeber/beste-vlog-kamera.html': {
        'title': 'Beste Vlog Kamera',
        'breadcrumbs': [
            ('Startseite', 'https://cameraupick.com/de/'),
            ('Ratgeber', 'https://cameraupick.com/de/#ratgeber'),
            ('Beste Vlog Kamera', 'https://cameraupick.com/de/ratgeber/beste-vlog-kamera.html')
        ],
        'og_image': 'https://cameraupick.com/assets/images/guides/vlog.webp',
        'og_description': 'Die besten Vlog-Kameras 2026: Schneller AF, Flip-Screen, IBIS und gute Audio-Optionen.'
    },
    'de/ratgeber/beste-reisekamera.html': {
        'title': 'Beste Reisekamera',
        'breadcrumbs': [
            ('Startseite', 'https://cameraupick.com/de/'),
            ('Ratgeber', 'https://cameraupick.com/de/#ratgeber'),
            ('Beste Reisekamera', 'https://cameraupick.com/de/ratgeber/beste-reisekamera.html')
        ],
        'og_image': 'https://cameraupick.com/assets/images/guides/travel.webp',
        'og_description': 'Die besten Reisekameras 2026: Kompakt, leicht, mit stabilisiertem 4K und scharfen Fotos.'
    },
    'de/ratgeber/beste-hybrid-kamera.html': {
        'title': 'Beste Hybridkamera',
        'breadcrumbs': [
            ('Startseite', 'https://cameraupick.com/de/'),
            ('Ratgeber', 'https://cameraupick.com/de/#ratgeber'),
            ('Beste Hybridkamera', 'https://cameraupick.com/de/ratgeber/beste-hybrid-kamera.html')
        ],
        'og_image': 'https://cameraupick.com/assets/images/guides/hybrid.webp',
        'og_description': 'Die besten Hybrid-Kameras 2026: Ausgewogene Foto-Video-Bodies mit 10-bit und zuverlässigem AF.'
    },
    'de/ratgeber/beste-vollformat-fuer-video.html': {
        'title': 'Beste Vollformat für Video',
        'breadcrumbs': [
            ('Startseite', 'https://cameraupick.com/de/'),
            ('Ratgeber', 'https://cameraupick.com/de/#ratgeber'),
            ('Beste Vollformat für Video', 'https://cameraupick.com/de/ratgeber/beste-vollformat-fuer-video.html')
        ],
        'og_image': 'https://cameraupick.com/assets/images/guides/fullframe-video.webp',
        'og_description': 'Die besten Vollformat-Kameras für Video 2026: Starke Codecs, niedriger Rolling Shutter, guter IBIS.'
    },
    'de/ratgeber/beste-budget-kamera-unter-800.html': {
        'title': 'Beste Budget Kamera unter 800€',
        'breadcrumbs': [
            ('Startseite', 'https://cameraupick.com/de/'),
            ('Ratgeber', 'https://cameraupick.com/de/#ratgeber'),
            ('Beste Budget Kamera', 'https://cameraupick.com/de/ratgeber/beste-budget-kamera-unter-800.html')
        ],
        'og_image': 'https://cameraupick.com/assets/images/guides/budget.webp',
        'og_description': 'Die besten Budget-Kameras unter 800€: Zuverlässiger AF, guter Akku, bezahlbare Objektive.'
    },
    'de/ratgeber/beste-action-360-kamera.html': {
        'title': 'Beste Action & 360 Kamera',
        'breadcrumbs': [
            ('Startseite', 'https://cameraupick.com/de/'),
            ('Ratgeber', 'https://cameraupick.com/de/#ratgeber'),
            ('Beste Action & 360 Kamera', 'https://cameraupick.com/de/ratgeber/beste-action-360-kamera.html')
        ],
        'og_image': 'https://cameraupick.com/assets/images/guides/action-360.webp',
        'og_description': 'Die besten Action- und 360-Kameras 2026: Stabilisierung, Horizon Lock, einfaches Reframing.'
    },
}


def generate_breadcrumb_schema(breadcrumbs):
    """Generate BreadcrumbList JSON-LD schema."""
    items = []
    for i, (name, url) in enumerate(breadcrumbs, 1):
        items.append({
            "@type": "ListItem",
            "position": i,
            "name": name,
            "item": url
        })
    
    schema = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": items
    }
    
    # Convert to JSON string with proper formatting
    import json
    return json.dumps(schema, ensure_ascii=False, indent=2)


def generate_og_tags(title, description, url, image):
    """Generate Open Graph and Twitter Card meta tags."""
    return f'''  <!-- Open Graph / Twitter -->
  <meta property="og:type" content="article">
  <meta property="og:site_name" content="cameraupick">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{image}">
  <meta property="og:locale" content="de_DE">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{description}">
  <meta name="twitter:image" content="{image}">
'''


def add_schema_to_page(file_path, config):
    """Add breadcrumb schema and OG tags to a page."""
    print(f"Processing: {file_path}")
    
    full_path = BASE_DIR / file_path
    if not full_path.exists():
        print(f"  ⚠ File not found")
        return False
    
    with open(full_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    
    # Check if breadcrumb schema already exists
    if '"BreadcrumbList"' not in content:
        breadcrumb_json = generate_breadcrumb_schema(config['breadcrumbs'])
        breadcrumb_script = f'''
  <!-- Breadcrumb Schema -->
  <script type="application/ld+json">
  {breadcrumb_json}
  </script>
'''
        # Insert before </head>
        content = content.replace('</head>', f'{breadcrumb_script}</head>')
        modified = True
        print(f"  ✓ Added Breadcrumb Schema")
    else:
        print(f"  - Breadcrumb Schema already exists")
    
    # Check if OG tags exist
    if 'og:type' not in content:
        url = f"https://cameraupick.com/{file_path}"
        og_tags = generate_og_tags(
            config['title'],
            config['og_description'],
            url,
            config['og_image']
        )
        # Insert after theme-color meta or before title
        if '<meta name="theme-color"' in content:
            content = re.sub(
                r'(<meta name="theme-color"[^>]*>)',
                r'\1\n\n' + og_tags,
                content
            )
        else:
            content = content.replace('<title>', og_tags + '\n  <title>')
        modified = True
        print(f"  ✓ Added Open Graph tags")
    else:
        print(f"  - Open Graph tags already exist")
    
    if modified:
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    
    return False


def main():
    """Main execution."""
    updated_count = 0
    
    for page_path, config in GERMAN_PAGES.items():
        if add_schema_to_page(page_path, config):
            updated_count += 1
    
    print(f"\n{'='*60}")
    print(f"SEO Enhancement Complete")
    print(f"Updated: {updated_count} pages")
    print(f"{'='*60}")


if __name__ == '__main__':
    main()
