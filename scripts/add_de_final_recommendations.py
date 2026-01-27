#!/usr/bin/env python3
"""
Add German Final Recommendation (Abschließende Empfehlung) sections to DE review pages.
"""

import os
import re

REVIEWS_DIR = "src/pages/de/reviews"

# German Final Recommendation content for each camera
RECOMMENDATIONS = {
    "nikon-z8-review.astro": {
        "summary": """Die Nikon Z8 liefert Z9-Leistung in einem kompakteren Gehäuse.
          Mit 45,7 MP, 8K-Video und professionellem Autofokus ist sie die Flaggschiff-Kamera
          für Fotografen, die maximale Leistung ohne Gewicht wollen.""",
        "buy_if": """Sie Flaggschiff-Leistung in einem kompakten Gehäuse benötigen.
          Perfekt für Wildlife, Sport, Hochzeiten und kommerzielle Arbeit.""",
        "skip_if": """Sie auf Budget achten (Z6 III betrachten) oder die extremen
          Auflösungs- und Video-Spezifikationen nicht benötigen."""
    },
    "panasonic-s5-ii-review.astro": {
        "summary": """Die Panasonic S5 II bringt endlich Phasen-Autofokus zu Panasonic
          Vollformat-Kameras. Kombiniert mit unglaublichen Video-Funktionen und unbegrenzter
          Aufnahme ist sie ein Traum für Filmemacher zum vernünftigen Preis.""",
        "buy_if": """Sie Videoqualität und -funktionen über alles andere stellen.
          Perfekt für Dokumentarfilme, Interviews und Indie-Filmproduktion.""",
        "skip_if": """Sie erstklassigen Autofokus für schnelle Action benötigen
          (Sony/Canon sind besser), oder hauptsächlich Fotos machen."""
    },
    "fujifilm-x-t5-review.astro": {
        "summary": """Die Fujifilm X-T5 ist durch und durch eine Fotografen-Kamera.
          Mit 40 MP Auflösung, klassischen Bedienelementen und Fujifilms legendärer
          Farbwissenschaft erfasst sie Bilder mit einzigartigem Charakter.""",
        "buy_if": """Sie den fotografischen Prozess lieben und eine Kamera wollen,
          die Kreativität inspiriert. Perfekt für Street und Portrait.""",
        "skip_if": """Sie fortgeschrittene Video-Funktionen benötigen (X-S20 oder X-H2S)
          oder moderne Touchscreen-Interfaces bevorzugen."""
    },
    "canon-eos-r8-review.astro": {
        "summary": """Die Canon EOS R8 bringt R5-Level Autofokus in ein unglaublich
          erschwingliches Vollformat-Gehäuse. Für Fotografen, die AF-Leistung über
          Video-Spezifikationen priorisieren, ist sie ein außergewöhnlicher Wert.""",
        "buy_if": """Sie erstklassigen Autofokus ohne Flaggschiff-Preis wollen.
          Perfekt für Portraits, Events und Reisen.""",
        "skip_if": """Sie professionelle Video-Funktionen benötigen (R6 III),
          Wetterschutz oder duale Kartenschächte."""
    },
    "dji-osmo-pocket-3-review.astro": {
        "summary": """Die DJI Osmo Pocket 3 ist der ultimative Vlogging-Begleiter.
          Mit 1-Zoll-Sensor, drehbarem Bildschirm und 3-Achsen-Gimbal-Stabilisierung
          erfasst sie professionelle Inhalte in Ihrer Tasche.""",
        "buy_if": """Sie unterwegs Content erstellen und Portabilität über alles schätzen.
          Perfekt für Vlogger, Reise-Creator und alle, die Gimbal-Glätte wollen.""",
        "skip_if": """Sie Wechselobjektive benötigen, maximale Low-Light-Leistung
          oder professionelles Audio ohne Adapter."""
    },
    "sony-a7-v-review.astro": {
        "summary": """Die Sony A7 V repräsentiert den Höhepunkt der Allround-Kameras.
          Mit KI-gestütztem Autofokus, exzellentem 4K-Video und der raffiniertesten
          Ergonomie der A7-Reihe meistert sie jede Aufnahmesituation souverän.""",
        "buy_if": """Sie eine Alleskönner-Kamera wollen, die bei Fotos und Video
          glänzt. Perfekt für Profis, die Zuverlässigkeit und KI-AF benötigen.""",
        "skip_if": """Sie mit der A7 IV zufrieden sind und die KI-AF-Verbesserungen
          nicht benötigen, oder auf Budget achten."""
    },
    "sony-a7c-ii-review.astro": {
        "summary": """Die Sony A7C II beweist, dass kompakt nicht Kompromiss bedeutet.
          Mit A7 IV-Level Bildqualität im Messsucherstil-Gehäuse ist sie der perfekte
          Reise- und Street-Photography-Begleiter.""",
        "buy_if": """Sie Portabilität priorisieren, aber keine Vollformat-Bildqualität
          opfern wollen. Perfekt für Reise und Street Photography.""",
        "skip_if": """Sie die Ergonomie eines traditionellen Griffs für schwere
          Objektive benötigen, oder duale Kartenschächte für Backup."""
    },
    "sony-zv-e10-review.astro": {
        "summary": """Die Sony ZV-E10 demokratisiert Content-Erstellung. Mit exzellentem
          Autofokus, Produktpräsentationsmodus und Creator-freundlichen Funktionen
          macht sie professionelles Video für jeden zugänglich.""",
        "buy_if": """Sie Ihre Content-Creation-Reise beginnen und Wechselobjektive
          wollen. Perfekt für YouTube, Streaming und Social Media.""",
        "skip_if": """Sie fortgeschrittene Stabilisierung benötigen (ZV-E10 II),
          einen EVF für traditionelles Fotografieren oder Wetterschutz."""
    },
    "om-system-om-1-ii-review.astro": {
        "summary": """Die OM System OM-1 Mark II maximiert, was Micro Four Thirds
          erreichen kann. Mit unglaublichen Berechnungsfunktionen, blitzschnellem
          Shooting und legendärer Wetterdichtung glänzt sie unter Bedingungen.""",
        "buy_if": """Sie Portabilität und Wetterfestigkeit für Outdoor-Abenteuer
          schätzen. Perfekt für Wildlife, Vogelfotografie und Reisen.""",
        "skip_if": """Sie maximale Low-Light-Leistung oder die geringe Schärfentiefe
          benötigen, die nur größere Sensoren bieten."""
    },
    "canon-r5-ii-review.astro": {
        "summary": """Die Canon EOS R5 Mark II ist die ultimative professionelle
          Hybrid-Kamera. Mit 8K-Video, revolutionärem Eye Control AF und Canons
          legendärer Zuverlässigkeit ist sie für Kompromisslose konzipiert.""",
        "buy_if": """Sie das Beste in Foto und Video verlangen. Perfekt für
          kommerzielle Arbeit, Hochzeiten und High-End Content-Produktion.""",
        "skip_if": """Sie auf Budget achten (EOS R6 III betrachten), kein 8K
          benötigen oder mit Ihrem aktuellen Setup zufrieden sind."""
    },
    "fujifilm-x-s20-review.astro": {
        "summary": """Die Fujifilm X-S20 ist das ultimative Preis-Leistungs-Angebot
          bei APS-C-Kameras. Sie liefert Flaggschiff-Video, exzellenten Autofokus
          und Fujifilms geliebte Farbwissenschaft in einem kompakten Paket.""",
        "buy_if": """Sie professionelle Video-Funktionen (6,2K, Vlog-Modus) mit
          atemberaubenden Fujifilm-Farben wollen. Perfekt für YouTuber und Reise.""",
        "skip_if": """Sie maximale Auflösung für Druck benötigen (X-T5) oder
          schnellste Serienbildgeschwindigkeit für Sport (X-H2S)."""
    },
    "sony-a7-iv-review.astro": {
        "summary": """Die Sony A7 IV repräsentiert die vernünftige Wahl bei
          Vollformat-Kameras. Sie jagt keine extremen Spezifikationen—stattdessen
          liefert sie ein ausgewogenes, zuverlässiges Paket für Foto und Video.""",
        "buy_if": """Sie eine professionelle Hybrid-Kamera mit exzellenter Ergonomie,
          dualen Kartenschächten und zuverlässigem 4K-Video benötigen.""",
        "skip_if": """Sie Portabilität priorisieren (A7C II), maximale Auflösung
          für Landschaften (A7R V) oder extreme Geschwindigkeit für Sport (A9 III)."""
    },
    "nikon-z6-iii-review.astro": {
        "summary": """Die Nikon Z6 III ist die Hybrid-Kamera, die Nikon-Nutzer
          angefordert haben. Sie liefert praktische, nutzbare Funktionen, die
          das Fotografieren im Alltag einfacher und produktiver machen.""",
        "buy_if": """Sie ein Hybrid-Shooter sind, der Video-Qualität, Ergonomie
          und Zuverlässigkeit schätzt. Perfekt für Hochzeiten, Events und Content.""",
        "skip_if": """Sie hauptsächlich Fotos machen und maximale Auflösung für
          extreme Ausschnitte benötigen—Z8 oder Z9 sind bessere Wahlen."""
    },
}

def add_final_recommendation(filepath):
    """Add German Final Recommendation section before Author Box."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    filename = os.path.basename(filepath)
    
    if filename not in RECOMMENDATIONS:
        print(f"○ No recommendation data: {filename}")
        return False
    
    if "Abschließende Empfehlung" in content or "Final Recommendation" in content:
        print(f"○ Already has recommendation: {filename}")
        return False
    
    rec = RECOMMENDATIONS[filename]
    
    recommendation_html = f'''
    <!-- Abschließende Empfehlung -->
    <section class="section">
      <div class="final-verdict">
        <h2>Abschließende Empfehlung</h2>
        <p>
          {rec["summary"]}
        </p>
        <p>
          <strong>Kaufen Sie, wenn:</strong> {rec["buy_if"]}
        </p>
        <p>
          <strong>Überspringen Sie, wenn:</strong> {rec["skip_if"]}
        </p>
      </div>
    </section>

'''
    
    # Insert before Author Box or footer
    patterns = [
        r'(\s*<!-- Author Box -->)',
        r'(\s*<section class="section author-box")',
        r'(\s*</main>\s*</BaseLayout>)',
    ]
    
    for pattern in patterns:
        if re.search(pattern, content):
            content = re.sub(pattern, recommendation_html + r'\1', content, count=1)
            break
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✓ Added recommendation: {filename}")
    return True

def main():
    added_count = 0
    for filename in RECOMMENDATIONS.keys():
        filepath = os.path.join(REVIEWS_DIR, filename)
        if os.path.exists(filepath):
            if add_final_recommendation(filepath):
                added_count += 1
        else:
            print(f"✗ Not found: {filename}")
    
    print(f"\n✓ Added {added_count} German Abschließende Empfehlung sections")

if __name__ == "__main__":
    main()
