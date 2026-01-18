#!/usr/bin/env python3
"""
Add missing Open Graph and Twitter meta tags to pages
"""

from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

# Configuration for pages
PAGES = {
    # English utility pages
    'about.html': {
        'title': 'About Us — Cameraupick',
        'desc': 'Our mission is to help you find the perfect camera through honest, unbiased reviews and guides.',
        'image': 'assets/images/team-avatar.webp'
    },
    'contact.html': {
        'title': 'Contact Us — Cameraupick',
        'desc': 'Get in touch with the Cameraupick team. We love hearing from fellow photographers and creators.',
        'image': 'assets/images/team-avatar.webp'
    },
    'deals.html': {
        'title': 'Camera Deals & Discounts — Cameraupick',
        'desc': 'The best current deals on cameras, lenses, and accessories. Updated daily.',
        'image': 'assets/images/guides/Vlog.jpg'
    },
    'privacy.html': {
        'title': 'Privacy Policy — Cameraupick',
        'desc': 'How we collect, use, and protect your data.',
        'image': 'assets/images/logo.png'
    },
    '404.html': {
        'title': 'Page Not Found — Cameraupick',
        'desc': 'Oops! The page you are looking for seems to have moved or does not exist.',
        'image': 'assets/images/logo.png'
    },
    
    # German pages
    'de/uber-uns.html': {
        'title': 'Über Uns — Cameraupick',
        'desc': 'Unsere Mission ist es, dir durch ehrliche, unvoreingenommene Testberichte und Ratgeber zu helfen.',
        'image': 'assets/images/team-avatar.webp',
        'locale': 'de_DE'
    },
    'de/kontakt.html': {
        'title': 'Kontakt — Cameraupick',
        'desc': 'Nimm Kontakt mit dem Kameraupick-Team auf. Wir freuen uns, von dir zu hören.',
        'image': 'assets/images/team-avatar.webp',
        'locale': 'de_DE'
    },
    'de/angebote.html': {
        'title': 'Kamera-Angebote & Deals — Cameraupick',
        'desc': 'Die besten aktuellen Angebote für Kameras, Objektive und Zubehör. Täglich aktualisiert.',
        'image': 'assets/images/guides/Vlog.jpg',
        'locale': 'de_DE'
    },
    'de/datenschutz.html': {
        'title': 'Datenschutzerklärung — Cameraupick',
        'desc': 'Wie wir deine Daten sammeln, verwenden und schützen.',
        'image': 'assets/images/logo.png',
        'locale': 'de_DE'
    },
    'de/404.html': {
        'title': 'Seite nicht gefunden — Cameraupick',
        'desc': 'Hoppla! Die gesuchte Seite scheint verschoben worden zu sein oder existiert nicht.',
        'image': 'assets/images/logo.png',
        'locale': 'de_DE'
    },
    
    # German comparison pages
    'de/vergleiche/fujifilm-x-s20-vs-fujifilm-x-t5.html': {
        'title': 'Fujifilm X-S20 vs X-T5 Vergleich (2026)',
        'desc': 'Detaillierter Vergleich zwischen der hybriden X-S20 und der foto-fokussierten X-T5. Welche ist die Richtige für dich?',
        'image': 'assets/images/guides/fujifilm-x-t5.png',
        'locale': 'de_DE'
    },
    'de/vergleiche/sony-a7-v-vs-canon-r6-iii.html': {
        'title': 'Sony A7 V vs Canon EOS R6 III Vergleich (2026)',
        'desc': 'Der ultimative Hybrid-Showdown. Autofokus, Video-Specs und Low-Light-Performance im Vergleich.',
        'image': 'assets/images/guides/sony-a7iv.png',
        'locale': 'de_DE'
    },
    'de/vergleiche/sony-zv-e10-vs-sony-a6700.html': {
        'title': 'Sony ZV-E10 vs Sony A6700 Vergleich',
        'desc': 'Lohnt sich das Upgrade? Vergleich der besten Budget-Vlog-Kamera gegen das APS-C Flaggschiff.',
        'image': 'assets/images/guides/sony-zv-e10-original.png',
        'locale': 'de_DE'
    }
}

def inject_meta_tags(file_path: Path, config: dict):
    """Inject OG tags into head"""
    content = file_path.read_text(encoding='utf-8')
    
    if '<meta property="og:title"' in content:
        print(f"skipping {file_path.name} (already has OG tags)")
        return False
    
    # Construct base URL
    rel_path = file_path.relative_to(BASE_DIR)
    url = f"https://cameraupick.com/{rel_path}"
    
    # Image URL (fix relative header paths for German pages if needed, but best to use absolute)
    img_url = f"https://cameraupick.com/{config['image']}"
    
    locale = config.get('locale', 'en_US')
    
    tags = f"""
  <!-- Open Graph / Twitter -->
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Kameraupick">
  <meta property="og:title" content="{config['title']}">
  <meta property="og:description" content="{config['desc']}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{img_url}">
  <meta property="og:locale" content="{locale}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{config['title']}">
  <meta name="twitter:description" content="{config['desc']}">
  <meta name="twitter:image" content="{img_url}">
"""
    
    # Insert before </head> or <link rel="stylesheet"
    if '<link rel="stylesheet"' in content:
        # Try to insert before stylesheet for cleaner grouping
        head_end = content.find('<link rel="stylesheet"')
        insert_pos = head_end
    elif '</head>' in content:
        insert_pos = content.find('</head>')
    else:
        print(f"❌ Could not find head tag in {file_path}")
        return False
        
    new_content = content[:insert_pos] + tags + content[insert_pos:]
    file_path.write_text(new_content, encoding='utf-8')
    return True

def main():
    print("🏷️  Adding missing OG Tags...\n")
    count = 0
    
    for rel_path, config in PAGES.items():
        file_path = BASE_DIR / rel_path
        if not file_path.exists():
            print(f"⚠️  File not found: {rel_path}")
            continue
            
        if inject_meta_tags(file_path, config):
            print(f"✅ Updated {rel_path}")
            count += 1
            
    print(f"\n✨ Added tags to {count} pages")

if __name__ == '__main__':
    main()
