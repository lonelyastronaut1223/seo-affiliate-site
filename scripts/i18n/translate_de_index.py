#!/usr/bin/env python3
"""
Translate DE index.astro from EN to German
Keeps the structure identical but translates content and fixes paths
"""

import re
from pathlib import Path

def translate_de_index():
    file_path = Path("src/pages/de/index.astro")
    content = file_path.read_text(encoding="utf-8")
    
    # Fix import path for DE subdirectory
    content = content.replace(
        'import BaseLayout from "../layouts/BaseLayout.astro";',
        'import BaseLayout from "../../layouts/BaseLayout.astro";'
    )
    
    # Title and description
    content = content.replace(
        'title="cameraupick — Camera Reviews, Comparisons & Buying Guides (2026)"',
        'title="Kameraupick — Kamera Testberichte, Vergleiche & Kaufberatung (2026)"'
    )
    content = content.replace(
        'description="Expert camera reviews & buying guides for 2026. Compare 50+ tested cameras from $400-$5000. Find your perfect match for travel, vlog, or professional work."',
        'description="Experten-Kameratests & Kaufberatungen für 2026. Vergleiche 50+ getestete Kameras von 400€-5000€. Finde die perfekte Kamera für Reisen, Vlogs oder professionelle Arbeit."'
    )
    
    # Hero section
    content = content.replace('Find the right camera — faster.', 'Finde die richtige Kamera — schneller.')
    content = content.replace(
        'Honest camera reviews and buying guides for beginners, travelers and',
        'Ehrliche Kamera-Testberichte und Kaufberatungen für Einsteiger, Reisende und'
    )
    content = content.replace('creators.', 'Creator.')
    
    # Camera finder / Quiz section
    content = content.replace('Discover Your Perfect Camera', 'Entdecke deine perfekte Kamera')
    content = content.replace(
        'Answer 3 quick questions to get a personalized recommendation based',
        'Beantworte 3 kurze Fragen für eine persönliche Empfehlung basierend auf'
    )
    content = content.replace('on your needs.', 'deinen Bedürfnissen.')
    content = content.replace('Start the Guide', 'Ratgeber starten')
    
    # Quiz steps
    content = content.replace('1. What will you primarily shoot?', '1. Was möchtest du hauptsächlich aufnehmen?')
    content = content.replace('Select the most important one.', 'Wähle das Wichtigste aus.')
    content = content.replace('>🎥 Video / Vlogs<', '>🎥 Video / Vlogs<')
    content = content.replace('>📸 Photography<', '>📸 Fotografie<')
    content = content.replace('>⚖️ Both (Hybrid)<', '>⚖️ Beides (Hybrid)<')
    
    content = content.replace('2. What is your experience level?', '2. Wie viel Erfahrung hast du?')
    content = content.replace("Be honest, we won't judge!", 'Sei ehrlich, wir urteilen nicht!')
    content = content.replace('>Beginner<', '>Anfänger<')
    content = content.replace('>Enthusiast<', '>Fortgeschritten<')
    content = content.replace('>Pro<', '>Profi<')
    
    content = content.replace('3. What is your budget?', '3. Wie hoch ist dein Budget?')
    content = content.replace('Including a lens.', 'Inklusive Objektiv.')
    content = content.replace('>Under $1,000<', '>Unter 1.000 €<')
    content = content.replace('>$1,000 - $2,500<', '>1.000 € - 2.500 €<')
    content = content.replace('>$2,500+<', '>2.500 € +<')
    
    content = content.replace('We found your match!', 'Wir haben deinen Match gefunden!')
    content = content.replace('Based on your answers, this is the best choice.', 'Basierend auf deinen Antworten ist dies die beste Wahl.')
    content = content.replace('Start Over ↺', 'Von vorne beginnen ↺')
    
    # Buying Guides
    content = content.replace('>Buying Guides<', '>Kaufberatungen<')
    content = content.replace('Start with the picks that fit your budget and how you shoot.', 
                             'Starte mit den Empfehlungen, die zu deinem Budget und Stil passen.')
    
    # Guide cards - titles and meta
    content = content.replace('>Best Camera for Beginners (2026)<', '>Beste Kamera für Einsteiger (2026)<')
    content = content.replace('/guides/best-camera-for-beginners-2026', '/de/ratgeber/beste-kamera-fuer-anfaenger-2026')
    content = content.replace('Safe, easy picks with fast AF, simple menus, solid battery, and',
                             'Sichere, einfache Wahl mit schnellem AF, einfachen Menüs, gutem Akku und')
    content = content.replace('lenses you can grow with.', 'Objektiven zum Wachsen.')
    content = content.replace('>Beginner</div>', '>Einsteiger</div>')
    
    content = content.replace('>Best Travel Camera<', '>Beste Reisekamera<')
    content = content.replace('/guides/best-travel-camera', '/de/ratgeber/beste-reisekamera')
    content = content.replace('Carry-light kits that still deliver stabilized 4K and sharp travel',
                             'Leichte Ausrüstung, die dennoch stabilisiertes 4K und scharfe')
    content = content.replace('photos.', 'Reisefotos liefert.')
    content = content.replace('>Travel</div>', '>Reise</div>')
    
    content = content.replace('>Best Vlog Camera<', '>Beste Vlog-Kamera<')
    content = content.replace('/guides/best-vlog-camera', '/de/ratgeber/beste-vlog-kamera')
    content = content.replace('Fast AF, flip screens, gyro data or IBIS, and clean audio options.',
                             'Schneller AF, Klappbildschirm, Gyro-Daten oder IBIS und saubere Audio-Optionen.')
    content = content.replace('>Video</div>', '>Video</div>')
    
    content = content.replace('>Best Budget Camera Under $800<', '>Beste Budget-Kamera unter 800€<')
    content = content.replace('/guides/best-budget-camera-under-800', '/de/ratgeber/beste-budget-kamera-unter-800')
    content = content.replace('Value picks with reliable AF, decent battery, and affordable lens',
                             'Preiswerte Modelle mit zuverlässigem AF, gutem Akku und günstigem')
    content = content.replace('paths.', 'Objektiv-Pfad.')
    content = content.replace('>Budget</div>', '>Budget</div>')
    
    content = content.replace('>Best Hybrid Camera<', '>Beste Hybrid-Kamera<')
    content = content.replace('/guides/best-hybrid-camera', '/de/ratgeber/beste-hybrid-kamera')
    content = content.replace('Balanced photo-video bodies with 10-bit, dependable AF, and strong',
                             'Ausgewogene Foto-Video-Bodys mit 10-Bit, zuverlässigem AF und')
    content = content.replace('ecosystems.', 'starken Ökosystemen.')
    content = content.replace('>Hybrid</div>', '>Hybrid</div>')
    
    content = content.replace('>Best Full-Frame for Video<', '>Beste Vollformat-Kamera für Video<')
    content = content.replace('/guides/best-full-frame-for-video', '/de/ratgeber/beste-vollformat-fuer-video')
    content = content.replace('Full-frame hybrids with strong codecs, low rolling shutter, and good',
                             'Vollformat-Hybride mit starken Codecs, geringem Rolling Shutter und')
    content = content.replace('IBIS.', 'gutem IBIS.')
    content = content.replace('>Video · Full-frame</div>', '>Video · Vollformat</div>')
    
    content = content.replace('>Best Action & 360 Camera<', '>Beste Action- & 360-Kamera<')
    content = content.replace('/guides/best-action-360-camera', '/de/ratgeber/beste-action-360-kamera')
    content = content.replace('Rugged cams with horizon lock, invisible sticks, and easy reframing.',
                             'Action/360-Cams mit Horizontsperre, unsichtbaren Sticks und einfachem Zuschneiden.')
    content = content.replace('>Action · 360</div>', '>Action · 360</div>')
    
    content = content.replace('>Best Camera for YouTube<', '>Beste Kamera für YouTube<')
    content = content.replace('/guides/best-camera-for-youtube', '/de/ratgeber/beste-kamera-fuer-youtube')
    content = content.replace('Top picks by budget for solo creators: autofocus, flip screens, good audio.',
                             'Top-Empfehlungen nach Budget für Solo-Creator: Autofokus, Klappbildschirm, guter Ton.')
    content = content.replace('>YouTube · Creator</div>', '>YouTube · Creator</div>')
    
    # Latest Reviews
    content = content.replace('>Latest Reviews<', '>Neueste Testberichte<')
    content = content.replace('Hands-on impressions, pros/cons, and clear "who should buy" guidance.',
                             'Praxis-Eindrücke, Vor- und Nachteile sowie klare Kaufempfehlungen.')
    content = content.replace('>All<', '>Alle<')
    content = content.replace('>Other<', '>Andere<')
    
    # Reviews - fix paths from /reviews/* to /de/reviews/*
    content = re.sub(r'href="/reviews/([^"]+)"', r'href="/de/reviews/\1"', content)
    
    # Review card content translations
    content = content.replace('Nikon Z6 III Review', 'Nikon Z6 III Testbericht')
    content = content.replace('Canon R5 Mark II Review', 'Canon R5 Mark II Testbericht')
    content = content.replace('Fujifilm X-S20 Review', 'Fujifilm X-S20 Testbericht')
    content = content.replace('Sony ZV-E10 II Review', 'Sony ZV-E10 II Testbericht')
    content = content.replace('Canon EOS R50 Review', 'Canon EOS R50 Testbericht')
    content = content.replace('Fujifilm X-T50 Review', 'Fujifilm X-T50 Testbericht')
    content = content.replace('OM System OM-1 Mark II Review', 'OM System OM-1 Mark II Testbericht')
    content = content.replace('Sony A7C II Review', 'Sony A7C II Testbericht')
    content = content.replace('Sony A7 IV Review', 'Sony A7 IV Testbericht')
    content = content.replace('Fujifilm X-T5 Review', 'Fujifilm X-T5 Testbericht')
    content = content.replace('Canon EOS R8 Review', 'Canon EOS R8 Testbericht')
    content = content.replace('Sony ZV-E10 Review', 'Sony ZV-E10 Testbericht')
    content = content.replace('Nikon Z8 Quick Take', 'Nikon Z8 Kurz-Test')
    content = content.replace('Panasonic S5 II Quick Take', 'Panasonic S5 II Kurz-Test')
    content = content.replace('DJI Osmo Pocket 3 Quick Take', 'DJI Osmo Pocket 3 Kurz-Test')
    
    # Review descriptions (key phrases)
    content = content.replace('Full-Frame Hybrid', 'Vollformat-Hybrid')
    content = content.replace('Professional Flagship', 'Profi-Flaggschiff')
    content = content.replace('APS-C Hybrid', 'APS-C Hybrid')
    content = content.replace('Compact Full-Frame', 'Kompakte Vollformat')
    content = content.replace('Full-frame · Hybrid', 'Vollformat · Hybrid')
    content = content.replace('APS-C · Photo-first', 'APS-C · Foto-First')
    content = content.replace('Value · Video-friendly', 'Preis-Leistung · Video-freundlich')
    content = content.replace('Vlog · Budget', 'Vlog · Budget')
    content = content.replace('Pro · Hybrid', 'Profi · Hybrid')
    content = content.replace('Vlog · Pocket', 'Vlog · Pocket')
    content = content.replace('Show More Reviews', 'Mehr Testberichte')
    content = content.replace('(1 review)', '(1 Bewertung)')
    
    # Deals section
    content = content.replace('>Current Deals<', '>Aktuelle Angebote<')
    content = content.replace('Limited-time price drops on gear we recommend.', 
                             'Zeitlich begrenzte Preissenkungen für Ausrüstung, die wir empfehlen.')
    content = content.replace('Sony ZV-E10 Kit', 'Sony ZV-E10 Set')
    content = content.replace('Budget vlog camera with flip screen. Includes 16-50mm lens.',
                             'Budget-Vlog-Kamera mit Klappbildschirm. Inklusive 16-50mm Objektiv.')
    content = content.replace('$598', '598 €')
    content = content.replace('was $698', 'statt 698 €')
    content = content.replace('Panasonic S5 II Body', 'Panasonic S5 II Gehäuse')
    content = content.replace('Full-frame hybrid with phase-detect AF. Lowest price ever.',
                             'Vollformat-Hybrid mit Phasen-AF. Niedrigster Preis aller Zeiten.')
    content = content.replace('$1,697', '1.697 €')
    content = content.replace('SanDisk cards, batteries, and more', 'SanDisk-Karten, Akkus und mehr')
    content = content.replace('>View All Deals<', '>Alle Angebote ansehen<')
    content = content.replace('href="/deals"', 'href="/de/angebote"')
    content = content.replace('Accessories, storage, and gear on sale.', 'Zubehör, Speicher und Ausrüstung im Angebot.')
    content = content.replace('>Updated Daily<', '>Täglich aktualisiert<')
    
    # Comparisons section
    content = content.replace('>Comparisons<', '>Vergleiche<')
    content = content.replace('Side-by-side breakdowns for the most common shopping choices.',
                             'Seite-an-Seite-Analysen für die häufigsten Kaufentscheidungen.')
    content = content.replace('href="/compare/', 'href="/de/vergleiche/')
    content = content.replace('Two hybrid favorites compared: AF, stabilization, rolling shutter,',
                             'Zwei Hybrid-Favoriten im Vergleich: AF, Stabilisierung, Rolling Shutter')
    content = content.replace('and lenses.', 'und Objektive.')
    content = content.replace('>Hybrid Comparison</div>', '>Hybrid-Vergleich</div>')
    content = content.replace('Flagship hybrid showdown: AF, rolling shutter, stabilization, and',
                             'Flaggschiff-Hybrid-Showdown: AF, Rolling Shutter, Stabilisierung und')
    content = content.replace('heat.', 'Hitze.')
    content = content.replace('>Comparison</div>', '>Vergleich</div>')
    content = content.replace('Creator-first vs enthusiast APS-C — when to upgrade.',
                             'Creator-First vs Enthusiast APS-C — wann lohnt das Upgrade.')
    content = content.replace('>Upgrade path</div>', '>Upgrade-Pfad</div>')
    content = content.replace('Same lenses, different priorities: video features vs classic',
                             'Gleiche Objektive, andere Prioritäten: Video-Merkmale vs klassische')
    content = content.replace('handling.', 'Handhabung.')
    content = content.replace('>APS-C</div>', '>APS-C</div>')
    
    # Lenses section
    content = content.replace('>Lens Guides<', '>Objektivführer<')
    content = content.replace('Find the perfect glass for your camera system.',
                             'Finde das perfekte Glas für dein Kamerasystem.')
    content = content.replace('href="/lenses/', 'href="/de/objektive/')
    content = content.replace('>Sony E-Mount Lenses<', '>Sony E-Mount Objektive<')
    content = content.replace('The largest lens ecosystem. Budget Sigma primes to premium G Master',
                             'Das größte Objektiv-Ökosystem. Von Budget-Sigma-Festbrennweiten bis Premium-G-Master')
    content = content.replace('glass.', 'Glas.')
    content = content.replace('>Sony · APS-C & Full-Frame</div>', '>Sony · APS-C & Vollformat</div>')
    content = content.replace('>Canon RF Lenses<', '>Canon RF Objektive<')
    content = content.replace('Premium optics with excellent autofocus. Budget picks and L-series',
                             'Premium-Optiken mit exzellentem Autofokus. Budget-Optionen und L-Serie')
    content = content.replace('>Canon · RF & RF-S</div>', '>Canon · RF & RF-S</div>')
    content = content.replace('>Fujifilm X-Mount Lenses<', '>Fujifilm X-Mount Objektive<')
    content = content.replace("Compact, sharp, and stylish. Perfect match for Fuji's retro bodies.",
                             'Kompakt, scharf und stylisch. Perfekte Ergänzung zu Fujis Retro-Bodys.')
    content = content.replace('>Fujifilm · APS-C</div>', '>Fujifilm · APS-C</div>')
    
    # Gear section
    content = content.replace('>Gear & Accessories<', '>Ausrüstung & Zubehör<')
    content = content.replace('Essential accessories we actually use every day.',
                             'Unverzichtbares Zubehör, das wir täglich nutzen.')
    content = content.replace('href="/gear/', 'href="/de/zubehoer/')
    content = content.replace('>Best Tripods<', '>Beste Stative<')
    content = content.replace('From ultralight travel tripods to pro video sticks. Stability',
                             'Von ultraleichten Reisestativen bis Profi-Video-Stativen. Stabilitäts')
    content = content.replace('tested.', 'getestet.')
    content = content.replace('>Travel · Video · Landscape</div>', '>Reise · Video · Landschaft</div>')
    content = content.replace('>Best Camera Bags<', '>Beste Kamerataschen<')
    content = content.replace('Backpacks, slings, and messenger bags. Protection meets style.',
                             'Rucksäcke, Slings und Messenger-Taschen. Schutz trifft auf Stil.')
    content = content.replace('>Travel · Everyday Carry</div>', '>Reise · Everyday Carry</div>')
    content = content.replace('>Best SD Cards<', '>Beste SD-Karten<')
    content = content.replace('Speed matters for 4K video and burst photos. Real-world tested.',
                             'Geschwindigkeit zählt für 4K-Video und Serienbilder. Praxis-getestet.')
    content = content.replace('>Storage · 4K/8K Video</div>', '>Speicher · 4K/8K Video</div>')
    
    # Affiliate section
    content = content.replace('>Affiliate & Ethics<', '>Affiliate & Ethik<')
    content = content.replace('We use affiliate links to keep the site free. You never pay extra,',
                             'Wir nutzen Affiliate-Links, um die Seite kostenlos zu halten. Du zahlst nie extra,')
    content = content.replace('and we only recommend gear we would buy ourselves.',
                             'und wir empfehlen nur Ausrüstung, die wir selbst kaufen würden.')
    content = content.replace('>Independent testing<', '>Unabhängige Tests<')
    content = content.replace('>Transparent pros & cons<', '>Transparente Vor- & Nachteile<')
    content = content.replace('>Updated picks<', '>Aktualisierte Empfehlungen<')
    content = content.replace('>View our top picks<', '>Unsere Top-Empfehlungen<')
    
    # How We Test section
    content = content.replace('>How We Test<', '>Wie wir testen<')
    content = content.replace('Practical reviews focused on real-world shooting.',
                             'Praxisnahe Tests mit Fokus auf reale Aufnahmesituationen.')
    content = content.replace('>Handling & Autofocus<', '>Handhabung & Autofokus<')
    content = content.replace('We check how quickly cameras lock on, track faces, and hold focus in',
                             'Wir prüfen, wie schnell Kameras scharf stellen, Gesichter verfolgen und den Fokus')
    content = content.replace('video.', 'bei Video halten.')
    content = content.replace('>Video Reliability<', '>Video-Zuverlässigkeit<')
    content = content.replace('Heat limits, rolling shutter, stabilization, audio options, and log',
                             'Hitze-Limits, Rolling Shutter, Stabilisierung, Audio-Optionen und')
    content = content.replace('profiles.', 'Log-Profile.')
    content = content.replace('>Lenses & Ecosystem<', '>Objektive & Ökosystem<')
    content = content.replace('Which lenses make sense for beginners, travel, and growth paths.',
                             'Welche Objektive für Einsteiger, Reisen und Wachstum sinnvoll sind.')
    
    # FAQ section
    content = content.replace('>Frequently Asked Questions<', '>Häufig gestellte Fragen<')
    content = content.replace('Common questions about choosing the right camera',
                             'Häufige Fragen zur Wahl der richtigen Kamera')
    content = content.replace('>What is the best camera for beginners?<', '>Was ist die beste Kamera für Anfänger?<')
    content = content.replace('>Do I need a full-frame camera?<', '>Brauche ich eine Vollformatkamera?<')
    content = content.replace('>How do I choose my first lens?<', '>Wie wähle ich mein erstes Objektiv?<')
    content = content.replace(">What's the difference between mirrorless and DSLR?<", 
                             '>Was ist der Unterschied zwischen spiegellosen Kameras und DSLRs?<')
    content = content.replace('>What specs do I need for video?<', '>Welche Spezifikationen brauche ich für Video?<')
    content = content.replace('>What can I get for $1,000?<', '>Was bekomme ich für 1.000 €?<')
    
    # Newsletter section
    content = content.replace('>Stay in the Loop<', '>Bleib auf dem Laufenden<')
    content = content.replace('New reviews, deals, and buying guides — straight to your inbox.',
                             'Neue Testberichte, Angebote und Kaufberatungen — direkt in dein Postfach.')
    content = content.replace('placeholder="your@email.com"', 'placeholder="deine@email.de"')
    content = content.replace('>Subscribe<', '>Abonnieren<')
    content = content.replace('No spam. Unsubscribe anytime.', 'Kein Spam. Jederzeit abbestellbar.')
    
    # Script translations (for no results message)
    content = content.replace('No reviews found for this brand yet.', 'Noch keine Testberichte für diese Marke.')
    
    file_path.write_text(content, encoding="utf-8")
    print(f"✅ Translated and updated: {file_path}")

if __name__ == "__main__":
    translate_de_index()
