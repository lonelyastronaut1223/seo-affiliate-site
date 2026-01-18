#!/usr/bin/env python3
"""
Deep Translation Script for Camera Review Website
Translates full page content from English to German.
"""

import re
from pathlib import Path
from typing import Dict, List, Tuple

BASE_DIR = Path(__file__).parent.parent.parent

# Comprehensive translation dictionary
TRANSLATIONS: Dict[str, str] = {
    # =========================
    # TITLES & HEADINGS
    # =========================
    "Best Hybrid Camera": "Beste Hybrid-Kamera",
    "Best Vlog Camera": "Beste Vlog-Kamera",
    "Best Travel Camera": "Beste Reisekamera",
    "Best Camera for Beginners": "Beste Kamera für Einsteiger",
    "Best Budget Camera Under $800": "Beste Budget-Kamera unter 800€",
    "Best Full-Frame for Video": "Beste Vollformat für Video",
    "Best Action & 360 Camera": "Beste Action- & 360-Kamera",
    "At a Glance: Top 3 Picks": "Auf einen Blick: Top 3 Empfehlungen",
    "At a Glance": "Auf einen Blick",
    "Top Picks": "Top-Empfehlungen",
    "Buying Advice": "Kaufberatung",
    "Hybrid Buying Advice": "Hybrid-Kaufberatung",
    "The Lens Ecosystem": "Das Objektiv-Ökosystem",
    "Quick Specs": "Technische Daten",
    
    # =========================
    # SECTION HEADERS
    # =========================
    "Pros": "Vorteile",
    "Cons": "Nachteile",
    "Overview": "Überblick",
    "Conclusion": "Fazit",
    "Summary": "Zusammenfassung",
    "Key Features": "Hauptmerkmale",
    "Specifications": "Spezifikationen",
    "Who is it for?": "Für wen ist sie geeignet?",
    "Who Should Buy": "Wer sollte kaufen",
    "Final Verdict": "Endgültiges Urteil",
    "The Bottom Line": "Das Fazit",
    
    # =========================
    # TABLE HEADERS
    # =========================
    "Model": "Modell",
    "Best For": "Ideal für",
    "Megapixels": "Megapixel",
    "Video Specs": "Video-Spezifikationen",
    "Price": "Preis",
    "Sensor": "Sensor",
    "Video": "Video",
    "Focus": "Fokus",
    "AF": "AF",
    "Burst": "Serienbildgeschwindigkeit",
    "Cooling": "Kühlung",
    "Card Slots": "Kartensteckplätze",
    "Screen": "Display",
    "Viewfinder": "Sucher",
    "Battery": "Akku",
    "Weight": "Gewicht",
    "Stabilization": "Stabilisierung",
    
    # =========================
    # BUTTONS & CTAs
    # =========================
    "Check Price": "Preis prüfen",
    "Check Price on Amazon": "Preis auf Amazon prüfen",
    "Check Price on Amazon →": "Preis auf Amazon prüfen →",
    "View on Amazon": "Auf Amazon ansehen",
    "Buy Now": "Jetzt kaufen",
    "Learn More": "Mehr erfahren",
    "Read Full Review": "Vollständigen Test lesen",
    "Read Review": "Test lesen",
    "See Deals": "Angebote sehen",
    "Compare": "Vergleichen",
    
    # =========================
    # TAGS & BADGES
    # =========================
    "The Standard": "Der Standard",
    "The Gold Standard": "Der Goldstandard",
    "Value / Video": "Preis-Leistung / Video",
    "Speed / Action": "Geschwindigkeit / Action",
    "Best for Video": "Beste für Video",
    "Best Value": "Bestes Preis-Leistungs-Verhältnis",
    "Editor's Choice": "Empfehlung der Redaktion",
    "Best Overall": "Beste Gesamtwahl",
    "Budget Pick": "Budget-Empfehlung",
    "Fastest": "Schnellste",
    "Beginner": "Einsteiger",
    "Pro": "Profi",
    "Enthusiast": "Enthusiast",
    
    # =========================
    # CAMERA TERMS
    # =========================
    "Full-Frame": "Vollformat",
    "full-frame": "Vollformat",
    "APS-C": "APS-C",
    "Mirrorless": "Spiegellos",
    "mirrorless": "spiegellos",
    "DSLR": "DSLR",
    "autofocus": "Autofokus",
    "Autofocus": "Autofokus",
    "Eye AF": "Augen-AF",
    "Real-time Eye AF": "Echtzeit-Augen-AF",
    "Phase Detect AF": "Phasen-AF",
    "image stabilization": "Bildstabilisierung",
    "Image Stabilization": "Bildstabilisierung",
    "IBIS": "IBIS",
    "in-body image stabilization": "Sensor-Bildstabilisierung",
    "rolling shutter": "Rolling Shutter",
    "Rolling Shutter": "Rolling Shutter",
    "dynamic range": "Dynamikumfang",
    "Dynamic Range": "Dynamikumfang",
    "low light": "Schwachlicht",
    "Low Light": "Schwachlicht",
    "high ISO": "hohe ISO",
    "viewfinder": "Sucher",
    "electronic viewfinder": "elektronischer Sucher",
    "optical viewfinder": "optischer Sucher",
    "flip screen": "Klappbildschirm",
    "Flip Screen": "Klappbildschirm",
    "vari-angle screen": "schwenkbares Display",
    "touchscreen": "Touchscreen",
    "weather sealing": "Wetterdichtung",
    "Weather Sealing": "Wetterdichtung",
    "dual card slots": "zwei Kartensteckplätze",
    "Dual Card Slots": "Zwei Kartensteckplätze",
    "lens mount": "Objektivanschluss",
    "Lens Mount": "Objektivanschluss",
    "kit lens": "Kit-Objektiv",
    "prime lens": "Festbrennweite",
    "zoom lens": "Zoomobjektiv",
    "wide-angle": "Weitwinkel",
    "telephoto": "Tele",
    "macro": "Makro",
    "portrait": "Porträt",
    "landscape": "Landschaft",
    "shutter speed": "Verschlusszeit",
    "aperture": "Blende",
    "ISO": "ISO",
    "exposure": "Belichtung",
    "white balance": "Weißabgleich",
    "color science": "Farbwiedergabe",
    "Color Science": "Farbwiedergabe",
    "film simulation": "Filmsimulation",
    "Film Simulation": "Filmsimulation",
    "log profile": "Log-Profil",
    "Log Profile": "Log-Profil",
    "color grading": "Farbkorrektur",
    "focus peaking": "Fokus-Peaking",
    "focus breathing": "Fokusatmung",
    "Focus Breathing": "Fokusatmung",
    
    # =========================
    # VIDEO TERMS
    # =========================
    "4K": "4K",
    "4K60": "4K60",
    "4K 60p": "4K 60p",
    "4K 30p": "4K 30p",
    "6K": "6K",
    "8K": "8K",
    "Open Gate": "Open Gate",
    "10-bit": "10-Bit",
    "10-bit 4:2:2": "10-Bit 4:2:2",
    "codec": "Codec",
    "bitrate": "Bitrate",
    "frame rate": "Bildrate",
    "slow motion": "Zeitlupe",
    "overheating": "Überhitzung",
    "recording limit": "Aufnahmebegrenzung",
    "recording limits": "Aufnahmebegrenzungen",
    "built-in fan": "integrierter Lüfter",
    "Built-in Fan": "Integrierter Lüfter",
    "unlimited recording": "unbegrenzte Aufnahme",
    "crop": "Crop",
    "no crop": "kein Crop",
    "No Crop": "Kein Crop",
    "1.5x crop": "1,5-facher Crop",
    "S35 Crop": "S35 Crop",
    "gimbal": "Gimbal",
    "stabilization": "Stabilisierung",
    "Active IS": "Active IS",
    "gyro data": "Gyro-Daten",
    
    # =========================
    # COMMON PHRASES
    # =========================
    "One camera to rule them all": "Eine Kamera für alles",
    "The true do-it-all cameras": "Die wahren Alleskönner",
    "This is the camera that defines": "Dies ist die Kamera, die definiert",
    "legendary": "legendär",
    "affordable": "erschwinglich",
    "expensive": "teuer",
    "budget": "Budget",
    "Budget": "Budget",
    "value": "Preis-Leistungs-Verhältnis",
    "Value": "Preis-Leistung",
    "premium": "Premium",
    "professional": "professionell",
    "Professional": "Professionell",
    "beginner-friendly": "anfängerfreundlich",
    "user-friendly": "benutzerfreundlich",
    "easy to use": "einfach zu bedienen",
    "intuitive": "intuitiv",
    "ergonomics": "Ergonomie",
    "Ergonomics": "Ergonomie",
    "build quality": "Verarbeitungsqualität",
    "third-party lenses": "Objektive von Drittanbietern",
    "lens selection": "Objektivauswahl",
    "Lens Selection": "Objektivauswahl",
    "ecosystem": "Ökosystem",
    "Ecosystem": "Ökosystem",
    "battery life": "Akkulaufzeit",
    "Battery Life": "Akkulaufzeit",
    "photos": "Fotos",
    "video": "Video",
    "stills": "Fotos",
    "footage": "Material",
    "content creator": "Content Creator",
    "vlogger": "Vlogger",
    "YouTuber": "YouTuber",
    "filmmaker": "Filmemacher",
    "photographer": "Fotograf",
    "hybrid shooter": "Hybrid-Fotograf",
    "travel": "Reise",
    "street": "Street",
    "sports": "Sport",
    "wildlife": "Wildlife",
    "wedding": "Hochzeit",
    "portrait": "Porträt",
    "landscape": "Landschaft",
    "vlog": "Vlog",
    
    # =========================
    # QUALITY DESCRIPTORS
    # =========================
    "excellent": "ausgezeichnet",
    "Excellent": "Ausgezeichnet",
    "great": "großartig",
    "Great": "Großartig",
    "good": "gut",
    "Good": "Gut",
    "decent": "ordentlich",
    "Decent": "Ordentlich",
    "okay": "okay",
    "poor": "schwach",
    "Poor": "Schwach",
    "best-in-class": "klassenbester",
    "Best-in-Class": "Klassenbester",
    "industry-leading": "branchenführend",
    "top-tier": "erstklassig",
    "reliable": "zuverlässig",
    "Reliable": "Zuverlässig",
    "dependable": "verlässlich",
    "Dependable": "Verlässlich",
    "impressive": "beeindruckend",
    "Impressive": "Beeindruckend",
    "outstanding": "herausragend",
    "Outstanding": "Herausragend",
    "incredible": "unglaublich",
    "Incredible": "Unglaublich",
    "fantastic": "fantastisch",
    "Fantastic": "Fantastisch",
    "superb": "hervorragend",
    "Superb": "Hervorragend",
    
    # =========================
    # MISC UI TEXT
    # =========================
    "Home": "Startseite",
    "Reviews": "Testberichte",
    "Guides": "Ratgeber",
    "Compare": "Vergleiche",
    "Deals": "Angebote",
    "Contact": "Kontakt",
    "About": "Über uns",
    "Privacy": "Datenschutz",
    "© ": "© ",
    "All rights reserved": "Alle Rechte vorbehalten",
    "Updated": "Aktualisiert",
    "Last updated": "Zuletzt aktualisiert",
    "Published": "Veröffentlicht",
    "Written by": "Geschrieben von",
    "Read time": "Lesezeit",
    "min read": "Min. Lesezeit",
    "Skip to content": "Zum Inhalt springen",
}

# Longer phrase translations (order matters - longer first)
PHRASE_TRANSLATIONS: List[Tuple[str, str]] = [
    # Long descriptive sentences
    ("One camera to rule them all. These hybrid workhorses deliver 33MP+ high-resolution stills for clients and 10-bit 4K video for YouTube, all in a single body.",
     "Eine Kamera für alles. Diese Hybrid-Arbeitstiere liefern 33MP+ hochauflösende Fotos für Kunden und 10-Bit-4K-Video für YouTube, alles in einem Gehäuse."),
    
    ("This is the camera that defines \"modern hybrid.\"",
     "Dies ist die Kamera, die den \"modernen Hybrid\" definiert."),
    
    ("With a 33MP sensor, it offers significantly more cropping room for photos than its 24MP rivals.",
     "Mit einem 33-MP-Sensor bietet sie deutlich mehr Beschnittspielraum für Fotos als die 24-MP-Konkurrenz."),
    
    ("The autofocus is legendary—it tracks eyes like a magnet.",
     "Der Autofokus ist legendär – er verfolgt Augen wie ein Magnet."),
    
    ("It has a huge ecosystem of third-party lenses from Sigma, Tamron, and Samyang, making it the most affordable system to build long-term.",
     "Das riesige Ökosystem an Drittanbieter-Objektiven von Sigma, Tamron und Samyang macht es zum günstigsten System für den langfristigen Aufbau."),
    
    ("Panasonic finally fixed their autofocus.",
     "Panasonic hat endlich ihren Autofokus verbessert."),
    
    ("The S5II uses Phase Detect AF (PDAF), making it reliable for solo shooters.",
     "Die S5II verwendet Phasen-AF (PDAF), was sie für Solo-Shooter zuverlässig macht."),
    
    ("But its superpower is \"Open Gate\" 6K video, which lets you record the full sensor height.",
     "Aber ihre Superkraft ist das \"Open Gate\" 6K-Video, das die volle Sensorhöhe aufnimmt."),
    
    ("It allows you to crop a vertical 9:16 (TikTok) and a horizontal 16:9 (YouTube) video from the same clip without losing quality.",
     "So kannst du aus demselben Clip ein vertikales 9:16 (TikTok) und ein horizontales 16:9 (YouTube) Video schneiden – ohne Qualitätsverlust."),
    
    ("It also has a built-in fan for unlimited recording.",
     "Außerdem hat sie einen integrierten Lüfter für unbegrenzte Aufnahmen."),
    
    ("Need speed?",
     "Brauchst du Geschwindigkeit?"),
    
    ("shoots a blistering 40 frames per second electronically",
     "schießt atemberaubende 40 Bilder pro Sekunde elektronisch"),
    
    ("It's a monster for sports and wildlife.",
     "Sie ist ein Monster für Sport und Wildlife."),
    
    ("The ergonomics are fantastic, and the autofocus sticks to subjects tenaciously.",
     "Die Ergonomie ist fantastisch, und der Autofokus klebt hartnäckig an Motiven."),
    
    ("It's a pure joy to use if you prioritize speed and usability.",
     "Es ist eine pure Freude zu verwenden, wenn du Geschwindigkeit und Bedienbarkeit priorisierst."),
    
    # Pros/Cons common items
    ("Highest resolution in class (33MP)", "Höchste Auflösung der Klasse (33MP)"),
    ("Unmatched lens selection (E-Mount)", "Unübertroffene Objektivauswahl (E-Mount)"),
    ("Focus breathing compensation is great", "Fokusatmungs-Kompensation ist großartig"),
    ("Reliable pro ergonomics", "Zuverlässige Profi-Ergonomie"),
    ("4K 60p has a 1.5x crop (APS-C mode)", "4K 60p hat einen 1,5-fachen Crop (APS-C-Modus)"),
    ("LCD screen quality is just okay", "LCD-Bildschirmqualität ist nur okay"),
    ("Rolling shutter is noticeable in electronic shutter", "Rolling Shutter ist beim elektronischen Verschluss spürbar"),
    ("6K Open Gate is a social media cheat code", "6K Open Gate ist ein Social-Media-Cheatcode"),
    ("Built-in fan = no overheating anxiety", "Integrierter Lüfter = keine Überhitzungsangst"),
    ("Incredible stabilization (gimbal-like)", "Unglaubliche Stabilisierung (gimbal-artig)"),
    ("Built-in LUT support (REAL TIME LUT)", "Integrierte LUT-Unterstützung (ECHTZEIT-LUT)"),
    ("Battery life is shorter than Sony/Canon", "Akkulaufzeit ist kürzer als bei Sony/Canon"),
    ("L-Mount lenses are generally heavier", "L-Mount-Objektive sind generell schwerer"),
    ("Slight crop in 4K60 mode", "Leichter Crop im 4K60-Modus"),
    ("4K 60p with NO crop (rare in this class)", "4K 60p OHNE Crop (selten in dieser Klasse)"),
    ("Insane 40fps burst shooting", "Wahnsinnige 40fps Serienbilder"),
    ("Excellent ergonomics and weather sealing", "Ausgezeichnete Ergonomie und Wetterdichtung"),
    ("False color tools for video exposure", "Falschfarben-Tools für Videobelichtung"),
    ("No third-party autofocus lens options", "Keine Autofokus-Objektive von Drittanbietern"),
    ("Micro-HDMI port (fragile)", "Micro-HDMI-Anschluss (zerbrechlich)"),
    ("Dynamic range slightly lower than Sony", "Dynamikumfang etwas geringer als bei Sony"),
    
    # Advice sections
    ("If you choose Sony, you get cheap third-party lenses. If you choose Canon, you get expensive but brilliant proprietary lenses. Choose the system, not just the body.",
     "Wenn du Sony wählst, bekommst du günstige Drittanbieter-Objektive. Wenn du Canon wählst, bekommst du teure, aber brillante proprietäre Objektive. Wähle das System, nicht nur die Kamera."),
    
    ("24MP is plenty for 4K video and social media. Only pay extra for the Sony A7 IV's 33MP if you crop heavily or print huge billboards.",
     "24MP reicht völlig für 4K-Video und Social Media. Zahle nur extra für die 33MP der Sony A7 IV, wenn du stark beschneidest oder riesige Plakate druckst."),
    
    ("Do you need 33MP?", "Brauchst du 33MP?"),
]


def translate_content(html_content: str) -> str:
    """Translate HTML content from English to German."""
    result = html_content
    
    # First apply phrase translations (longer phrases first)
    for en, de in PHRASE_TRANSLATIONS:
        result = result.replace(en, de)
    
    # Then apply word/short phrase translations
    for en, de in TRANSLATIONS.items():
        # Use word boundary matching for short words
        if len(en) <= 4:
            # For very short words, be careful with boundaries
            result = re.sub(r'\b' + re.escape(en) + r'\b', de, result)
        else:
            result = result.replace(en, de)
    
    return result


def translate_file(file_path: Path) -> bool:
    """Translate a single HTML file."""
    print(f"Translating: {file_path.name}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if already translated (look for German-specific words)
    german_indicators = ["Vorteile", "Nachteile", "Preis prüfen", "Auf einen Blick"]
    if any(indicator in content for indicator in german_indicators):
        print(f"  ⚠ Already translated (skipping)")
        return False
    
    translated = translate_content(content)
    
    if translated != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(translated)
        print(f"  ✓ Translated successfully")
        return True
    else:
        print(f"  - No changes needed")
        return False


def main():
    """Main execution - translate all German pages."""
    de_dir = BASE_DIR / 'de'
    
    translated_count = 0
    
    # Translate all HTML files in de/ directory
    for html_file in de_dir.rglob('*.html'):
        if translate_file(html_file):
            translated_count += 1
    
    print(f"\n{'='*60}")
    print(f"Deep Translation Complete")
    print(f"Translated: {translated_count} pages")
    print(f"{'='*60}")


if __name__ == '__main__':
    main()
