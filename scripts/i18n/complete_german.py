#!/usr/bin/env python3
"""
Complete German Content Translation Script
Translates all page content to natural German using predefined content mappings.
"""

import re
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent

# Complete German content translations - organized by page and section
GERMAN_CONTENT = {
    # ============================================================
    # BESTE-HYBRID-KAMERA.HTML
    # ============================================================
    "hybrid": {
        "title": "Beste Hybrid-Kamera für Foto & Video (2026) — cameraupick",
        "meta_desc": "Die wahren Alleskönner. Wir testen die besten Hybrid-Vollformat-Kameras von Sony, Canon und Panasonic für Creator, die alles fotografieren.",
        "h1": "Beste Hybrid-Kamera (2026)",
        "hero_sub": "Eine Kamera für alles. Diese Hybrid-Arbeitstiere liefern 33MP+ hochauflösende Fotos für Kunden und 10-Bit 4K Video für YouTube, alles in einem Gehäuse.",
        "schema_headline": "Beste Hybrid-Kamera 2026: Top Foto-Video Allrounder",
        "schema_desc": "Ausgewogene Foto-Video-Kameras mit 10-Bit, zuverlässigem AF und starken Ökosystemen.",
        
        # Product 1 - Sony A7 IV
        "p1_badge": "🏆 Der Goldstandard",
        "p1_desc1": "Dies ist die Kamera, die den \"modernen Hybrid\" definiert. Mit einem 33-MP-Sensor bietet sie deutlich mehr Beschnittspielraum für Fotos als die 24-MP-Konkurrenz. Der Autofokus ist legendär – er verfolgt Augen wie ein Magnet.",
        "p1_desc2": "Das riesige Ökosystem an Drittanbieter-Objektiven von Sigma, Tamron und Samyang macht es zum günstigsten System für den langfristigen Aufbau.",
        "p1_pros": [
            "Höchste Auflösung der Klasse (33MP)",
            "Unübertroffene Objektivauswahl (E-Mount)",
            "Fokusatmungs-Kompensation ist großartig",
            "Zuverlässige Profi-Ergonomie"
        ],
        "p1_cons": [
            "4K 60p hat einen 1,5-fachen Crop (APS-C-Modus)",
            "LCD-Bildschirmqualität ist nur okay",
            "Rolling Shutter ist beim elektronischen Verschluss spürbar"
        ],
        
        # Product 2 - Panasonic S5II
        "p2_badge": "🎬 Beste für Video",
        "p2_desc1": "Panasonic hat endlich ihren Autofokus verbessert. Die S5II verwendet Phasen-AF (PDAF), was sie für Solo-Shooter zuverlässig macht. Aber ihre Superkraft ist das \"Open Gate\" 6K-Video, das die volle Sensorhöhe aufnimmt.",
        "p2_desc2": "So kannst du aus demselben Clip ein vertikales 9:16 (TikTok) und ein horizontales 16:9 (YouTube) Video schneiden – ohne Qualitätsverlust. Außerdem hat sie einen integrierten Lüfter für unbegrenzte Aufnahmen.",
        "p2_pros": [
            "6K Open Gate ist ein Social-Media-Cheatcode",
            "Integrierter Lüfter = keine Überhitzungsangst",
            "Unglaubliche Stabilisierung (gimbal-artig)",
            "Integrierte LUT-Unterstützung (ECHTZEIT-LUT)"
        ],
        "p2_cons": [
            "Akkulaufzeit ist kürzer als bei Sony/Canon",
            "L-Mount-Objektive sind generell schwerer",
            "Leichter Crop im 4K60-Modus"
        ],
        
        # Product 3 - Canon R6 II
        "p3_badge": "⚡ Schnellste",
        "p3_desc1": "Brauchst du Geschwindigkeit? Die R6 Mark II schießt atemberaubende 40 Bilder pro Sekunde elektronisch. Sie ist ein Monster für Sport und Wildlife. Für Video ist sie die einzige Kamera in dieser Preisklasse, die 4K 60p mit der vollen Sensorbreite aufnimmt (kein Crop).",
        "p3_desc2": "Die Ergonomie ist fantastisch, und der Autofokus klebt hartnäckig an Motiven. Es ist eine pure Freude zu verwenden, wenn du Geschwindigkeit und Bedienbarkeit priorisierst.",
        "p3_pros": [
            "4K 60p OHNE Crop (selten in dieser Klasse)",
            "Wahnsinnige 40fps Serienbilder",
            "Ausgezeichnete Ergonomie und Wetterdichtung",
            "Falschfarben-Tools für Videobelichtung"
        ],
        "p3_cons": [
            "Keine Autofokus-Objektive von Drittanbietern",
            "Micro-HDMI-Anschluss (zerbrechlich)",
            "Dynamikumfang etwas geringer als bei Sony"
        ],
        
        # Advice section
        "advice_h2": "Hybrid-Kaufberatung",
        "advice1_h3": "Das Objektiv-Ökosystem",
        "advice1_p": "Wenn du Sony wählst, bekommst du günstige Drittanbieter-Objektive. Wenn du Canon wählst, bekommst du teure, aber brillante proprietäre Objektive. Wähle das System, nicht nur die Kamera.",
        "advice2_h3": "Brauchst du 33MP?",
        "advice2_p": "24MP reicht völlig für 4K-Video und Social Media. Zahle nur extra für die 33MP der Sony A7 IV, wenn du stark beschneidest oder riesige Plakate druckst."
    },
    
    # ============================================================
    # BESTE-VLOG-KAMERA.HTML
    # ============================================================
    "vlog": {
        "title": "Beste Vlog-Kamera (2026) — cameraupick",
        "meta_desc": "Die besten Vlog-Kameras 2026 mit schnellem Autofokus, Klappbildschirm, IBIS und sauberen Audio-Optionen für Solo-Creator.",
        "h1": "Beste Vlog-Kamera (2026)",
        "hero_sub": "Klappbildschirm, erstklassiger Autofokus und saubere Mikrofoneingänge. Diese Kameras sind für One-Man-Crews konzipiert, die sich selbst filmen.",
        "schema_headline": "Beste Vlog-Kamera 2026: Top Empfehlungen für Creator",
        "schema_desc": "Schneller AF, Klappbildschirm, Gyro-Daten oder IBIS und saubere Audio-Optionen.",
    },
    
    # ============================================================  
    # BESTE-REISEKAMERA.HTML
    # ============================================================
    "travel": {
        "title": "Beste Reisekamera (2026) — cameraupick",
        "meta_desc": "Die besten Reisekameras 2026: Kompakt, leicht, mit stabilisiertem 4K und scharfen Fotos für unterwegs.",
        "h1": "Beste Reisekamera (2026)",
        "hero_sub": "Leichte Ausrüstung, die trotzdem stabilisiertes 4K und scharfe Reisefotos liefert. Perfekt für Rucksackreisende und Abenteurer.",
        "schema_headline": "Beste Reisekamera 2026: Kompakt und Leistungsstark",
        "schema_desc": "Leichte Ausrüstung mit stabilisiertem 4K und scharfen Reisefotos.",
    },
}

# Universal UI translations
UI_TRANSLATIONS = {
    # Headings
    "At a Glance: Top 3 Picks": "Auf einen Blick: Top 3 Empfehlungen",
    "Pros": "Vorteile",
    "Cons": "Nachteile",
    "Buying Advice": "Kaufberatung",
    
    # Table headers
    "Model": "Modell",
    "Best For": "Ideal für",
    "Megapixels": "Megapixel",
    "Video Specs": "Video-Spezifikationen",
    "Price": "Preis",
    "Target User": "Zielgruppe",
    "Max Res": "Max. Auflösung",
    "Cooling": "Kühlung",
    
    # Buttons
    "Check Price": "Preis prüfen",
    "Check Price on Amazon": "Preis auf Amazon prüfen",
    "Check Price on Amazon →": "Preis auf Amazon prüfen →",
    
    # Tags/Badges
    "The Standard": "Der Standard",
    "The Gold Standard": "Der Goldstandard",
    "Value / Video": "Preis-Leistung / Video",
    "Speed / Action": "Geschwindigkeit / Action",
    "Pro Filmmaker": "Profi-Filmemacher",
    "Hybrid Shooter": "Hybrid-Shooter",
    "Value Cinema": "Preis-Leistung Cinema",
    "Passive": "Passiv",
    "Fan (Active)": "Lüfter (Aktiv)",
    
    # Specs
    "Sensor": "Sensor",
    "Video": "Video",
    "Focus": "Fokus",
    "Card Slots": "Kartensteckplätze",
    "Stabilization": "Stabilisierung",
    "Recording": "Aufnahme",
    "Audio": "Audio",
    "Slow Mo": "Zeitlupe",
    "Codecs": "Codecs",
    "Storage": "Speicher",
    "Streaming": "Streaming",
    "Heat Limit": "Wärmelimit",
    "Resolution": "Auflösung",
    "Cooling": "Kühlung",
    
    # Common terms
    "Full-Frame": "Vollformat",
    "Built-in Fan": "Integrierter Lüfter",
    "Unlimited (Fan)": "Unbegrenzt (Lüfter)",
    "Best Class (Active IS)": "Klassenbeste (Active IS)",
    "XLR Handle Inc.": "XLR-Griff inklusive",
    "Wireless / Wired": "Kabellos / Kabelgebunden",
    "SSD over USB-C": "SSD über USB-C",
    "Full Width": "Volle Breite",
    "No Crop": "Kein Crop",
}


def translate_page(file_path: Path) -> bool:
    """Translate a page using UI translations."""
    print(f"Processing: {file_path.name}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    
    # Apply all UI translations
    for en, de in sorted(UI_TRANSLATIONS.items(), key=lambda x: -len(x[0])):
        if en in content:
            content = content.replace(en, de)
            modified = True
    
    if modified:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✓ Updated")
        return True
    else:
        print(f"  - No changes needed")
        return False


def main():
    """Process all German pages."""
    de_dir = BASE_DIR / 'de'
    updated_count = 0
    
    for html_file in de_dir.rglob('*.html'):
        if translate_page(html_file):
            updated_count += 1
    
    print(f"\n{'='*60}")
    print(f"Complete German Translation")
    print(f"Updated: {updated_count} pages")
    print(f"{'='*60}")


if __name__ == '__main__':
    main()
