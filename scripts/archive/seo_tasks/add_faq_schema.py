#!/usr/bin/env python3
"""
Add FAQ Schema to guide pages for richer search results.
Each guide gets relevant camera FAQ questions.
"""

import re
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent

# FAQ data for different guide pages
GUIDE_FAQS = {
    # English Guides
    "best-hybrid-camera.html": [
        ("What is a hybrid camera?", "A hybrid camera excels at both photography and video. Modern hybrids offer 4K+ recording, high-resolution sensors, and features like in-body stabilization that work for both stills and motion."),
        ("Sony or Canon for hybrid shooting?", "Sony offers the best third-party lens ecosystem and value. Canon has superior autofocus and color science. Choose Sony for budget flexibility, Canon for premium results."),
        ("Is full-frame necessary for video?", "Not always. APS-C cameras like Fujifilm X-T5 deliver excellent video. Full-frame shines in low light and shallow depth of field, but costs more for camera and lenses."),
    ],
    "best-vlog-camera.html": [
        ("What's the best camera for YouTube beginners?", "The Sony ZV-E10 is ideal for beginners. It has a flip screen, excellent autofocus, built-in mic, product showcase mode, and costs under $700 with a kit lens."),
        ("Do I need 4K for YouTube?", "Yes, 4K is recommended in 2026. It gives you cropping flexibility in editing and looks sharper even when exported to 1080p. Most modern vlog cameras support 4K30 minimum."),
        ("Is a gimbal necessary for vlogging?", "Not with modern cameras. IBIS (in-body stabilization) and electronic stabilization in cameras like Sony and Panasonic reduce the need for gimbals. A good camera with IBIS is often enough."),
    ],
    
    # German Guides
    "beste-hybrid-kamera.html": [
        ("Was ist eine Hybrid-Kamera?", "Eine Hybrid-Kamera ist sowohl für Fotografie als auch Video optimiert. Moderne Hybride bieten 4K+ Aufnahme, hochauflösende Sensoren und Features wie Bildstabilisierung, die für Fotos und Video funktionieren."),
        ("Sony oder Canon für Hybrid-Aufnahmen?", "Sony bietet das beste Drittanbieter-Objektiv-Ökosystem und Preis-Leistung. Canon hat überlegenen Autofokus und Farbwiedergabe. Wähle Sony für Budget-Flexibilität, Canon für Premium-Ergebnisse."),
        ("Brauche ich Vollformat für Video?", "Nicht unbedingt. APS-C-Kameras wie die Fujifilm X-T5 liefern exzellentes Video. Vollformat glänzt bei Schwachlicht und geringer Schärfentiefe, kostet aber mehr für Kamera und Objektive."),
    ],
    "beste-vlog-kamera.html": [
        ("Welche Kamera ist am besten für YouTube-Anfänger?", "Die Sony ZV-E10 ist ideal für Anfänger. Sie hat einen Klappbildschirm, exzellenten Autofokus, eingebautes Mikrofon, Produkt-Showcase-Modus und kostet unter 700€ mit Kit-Objektiv."),
        ("Brauche ich 4K für YouTube?", "Ja, 4K ist 2026 empfohlen. Es gibt dir Beschnitt-Flexibilität beim Schnitt und sieht schärfer aus, selbst wenn du auf 1080p exportierst. Die meisten modernen Vlog-Kameras unterstützen mindestens 4K30."),
        ("Ist ein Gimbal fürs Vloggen notwendig?", "Nicht mit modernen Kameras. IBIS (Sensor-Stabilisierung) und elektronische Stabilisierung in Kameras wie Sony und Panasonic reduzieren den Bedarf an Gimbals. Eine gute Kamera mit IBIS reicht oft aus."),
    ],
    "beste-reisekamera.html": [
        ("Welche Kamera ist am besten für Reisen?", "Kompakte Kameras wie die Sony A7C II oder Fujifilm X-T5 sind ideal. Sie bieten Vollformat- oder APS-C-Qualität in einem tragbaren Gehäuse mit guter Akkulaufzeit."),
        ("Welches Objektiv für Reisefotografie?", "Ein 24-70mm f/2.8 oder 24-105mm ist vielseitig. Für noch leichteres Gepäck: eine 35mm f/1.8 Festbrennweite deckt die meisten Situationen ab."),
    ],
}

FAQ_SCHEMA_TEMPLATE = '''
  <!-- FAQ Schema -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
{questions}
    ]
  }}
  </script>
'''

QUESTION_TEMPLATE = '''      {{
        "@type": "Question",
        "name": "{question}",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "{answer}"
        }}
      }}'''


def add_faq_schema(file_path: Path) -> bool:
    """Add FAQ Schema to a guide page."""
    filename = file_path.name
    
    if filename not in GUIDE_FAQS:
        return False
    
    print(f"Processing: {filename}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if already has FAQ schema
    if '"@type": "FAQPage"' in content:
        print(f"  - Already has FAQ schema")
        return False
    
    # Generate questions JSON
    questions = []
    for q, a in GUIDE_FAQS[filename]:
        questions.append(QUESTION_TEMPLATE.format(
            question=q.replace('"', '\\"'),
            answer=a.replace('"', '\\"')
        ))
    questions_json = ",\n".join(questions)
    
    # Generate schema
    schema = FAQ_SCHEMA_TEMPLATE.format(questions=questions_json)
    
    # Insert before </head>
    if '</head>' in content:
        content = content.replace('</head>', f'{schema}</head>')
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"  ✓ Added FAQ schema with {len(GUIDE_FAQS[filename])} Q&As")
        return True
    
    return False


def main():
    """Process all guide pages."""
    updated_count = 0
    
    # Process English guides
    en_guides = BASE_DIR / 'guides'
    if en_guides.exists():
        for html_file in en_guides.glob('*.html'):
            if add_faq_schema(html_file):
                updated_count += 1
    
    # Process German guides
    de_guides = BASE_DIR / 'de' / 'ratgeber'
    if de_guides.exists():
        for html_file in de_guides.glob('*.html'):
            if add_faq_schema(html_file):
                updated_count += 1
    
    print(f"\n{'='*60}")
    print(f"FAQ Schema Added")
    print(f"Updated: {updated_count} guide pages")
    print(f"{'='*60}")


if __name__ == '__main__':
    main()
