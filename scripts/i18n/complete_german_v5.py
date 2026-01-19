#!/usr/bin/env python3
"""
German Translation Fix - Version 5 (Final)
Addresses remaining review page content and FAQ schemas
"""

from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent

# ============================================================================
# REMAINING FAQ SCHEMA TRANSLATIONS
# ============================================================================
FAQ_FIXES = {
    # Canon R8
    '"Does the R8 have Stabilisierung?"': '"Hat die R8 Stabilisierung?"',
    '"text": "No. The R8 relies on lens-based image stabilization (IS).': '"text": "Nein. Die R8 verlässt sich auf objektivbasierte Bildstabilisierung (IS).',
    
    # Fujifilm X-T5
    '"Does the X-T5 have gut Autofokus?"': '"Hat die X-T5 guten Autofokus?"',
    '"text": "Yes, for photography. The Phase-Detection AF is fast and Zuverlässig.': '"text": "Ja, für Fotografie. Der Phasenerkennungs-AF ist schnell und zuverlässig.',
    
    # Nikon Z8
    '"Is the Nikon Z8 gut for Wildlife photography?"': '"Ist die Nikon Z8 gut für Wildlife-Fotografie?"',
    '"Nikon Z8 vs Sony A1: Which is better?"': '"Nikon Z8 vs Sony A1: Welche ist besser?"',
    
    # Sony A7C II
    '"For Reise and hobbyists, no. For paid Hochzeits, maybe—bring a backup memory or an extra Kamera."':
        '"Für Reisen und Hobbyisten: nein. Für bezahlte Hochzeitsaufträge vielleicht – nimm einen Backup-Speicher oder eine Extra-Kamera mit."',
    
    # Sony ZV-E10
    '"Should I get the ZV-E10 or ZV-E10 II?"': '"Sollte ich die ZV-E10 oder ZV-E10 II kaufen?"',
}

# ============================================================================
# DJI OSMO POCKET 3 REVIEW TRANSLATIONS
# ============================================================================
DJI_TRANSLATIONS = {
    "screen that fits in your pocket":
        "Bildschirm, der in deine Tasche passt",
    "The DJI Osmo Pocket 3 is a masterpiece of engineering. It packs":
        "Der DJI Osmo Pocket 3 ist ein Meisterwerk der Ingenieurskunst. Er packt",
    "into a tiny Gimbal handle":
        "in einen winzigen Gimbal-Griff",
    "a large 1-inch sensor":
        "einen großen 1-Zoll-Sensor",
    "It's insane how stabilized":
        "Es ist verrückt, wie stabilisiert",
    "The rotating OLED touchscreen":
        "Der drehbare OLED-Touchscreen",
    "makes vlogging incredibly easy":
        "macht Vlogging unglaublich einfach",
    "flip it forward for selfies":
        "dreh ihn nach vorne für Selfies",
    "this thing produces":
        "dieses Ding produziert",
    "The audio is surprisingly good too":
        "Der Ton ist überraschend gut auch",
    "It's not a replacement for a full camera":
        "Er ist kein Ersatz für eine vollwertige Kamera",
    "but for quick content":
        "aber für schnelle Inhalte",
    "it's unbeatable":
        "ist er unschlagbar",
}

# ============================================================================
# PANASONIC S5 II REVIEW TRANSLATIONS
# ============================================================================
PANASONIC_TRANSLATIONS = {
    "At 1.997 €, the S5 II offers unglaublich":
        "Mit 1.997 € bietet die S5 II unglaubliches",
    "with klassenführender Video":
        "mit klassenführendem Video",
    "finally reliable Autofokus":
        "endlich zuverlässigem Autofokus",
    "the best IBIS on the market":
        "der besten IBIS auf dem Markt",
    "It's the swiss army knife for hybrid shooters while remaining unter 2.000 €":
        "Sie ist das Schweizer Taschenmesser für Hybrid-Filmer und bleibt unter 2.000 €",
    "The S5 II fixed everything that was wrong with Panasonic cameras":
        "Die S5 II hat alles behoben, was an Panasonic-Kameras falsch war",
    "It now has phase-detection autofocus that actually works":
        "Sie hat jetzt Phasenerkennungs-Autofokus, der tatsächlich funktioniert",
    "plus the best stabilization":
        "plus die beste Stabilisierung",
    "The Open Gate 6K recording is genius":
        "Die Open Gate 6K-Aufnahme ist genial",
}

# ============================================================================
# SONY ZV-E10 REVIEW TRANSLATIONS  
# ============================================================================
ZVE10_TRANSLATIONS = {
    "Rode Wireless Go II — plugs right into the mic jack":
        "Rode Wireless Go II – steckt direkt in die Mikrofon-Buchse",
    "Should I get the":
        "Sollte ich die",
    "or wait for the newer model":
        "kaufen oder auf das neuere Modell warten",
    "The perfect starter camera for content creators":
        "Die perfekte Einsteigerkamera für Content Creator",
    "Incredible value for money":
        "Unglaubliches Preis-Leistungs-Verhältnis",
}

# ============================================================================
# HYBRID GUIDE REMAINING FIXES
# ============================================================================
HYBRID_REMAINING = {
    "Brauchst du Geschwindigkeit? The R6 Mark II schießt atemberaubende 40 Bilder pro Sekunde elektronisch. It's a monster for\n              Sport and Wildlife. For Video, it's the only Kamera in this price range that shoots 4K 60p using the\n              <em>full width</em> of the sensor (no Crop).":
        "Brauchst du Geschwindigkeit? Die R6 Mark II schießt atemberaubende 40 Bilder pro Sekunde elektronisch. Sie ist ein Monster für Sport und Wildlife. Für Video ist sie die einzige Kamera in dieser Preisklasse, die 4K 60p mit der <em>vollen Breite</em> des Sensors aufnimmt (kein Crop).",
    "you prioritize speed and usability":
        "du Geschwindigkeit und Bedienbarkeit priorisierst",
}

# ============================================================================
# COMPARISON PAGE REMAINING FIXES
# ============================================================================
COMPARISON_REMAINING = {
    "you're okay with a tilt screen":
        "du mit einem Neigungsbildschirm zufrieden bist",
    "Canon is stickier for humans/animals. Sony is faster for objects":
        "Canon ist hartnäckiger bei Menschen/Tieren. Sony ist schneller bei Objekten",
}

def apply_all(file_path: Path, translations: dict) -> int:
    if not file_path.exists():
        return 0
    content = file_path.read_text(encoding='utf-8')
    original = content
    count = 0
    for en, de in translations.items():
        if en in content:
            content = content.replace(en, de)
            count += 1
    if content != original:
        file_path.write_text(content, encoding='utf-8')
        return count
    return 0

def main():
    print("🇩🇪 German Translation Fix v5 (Final Round)\n")
    de_dir = BASE_DIR / 'de'
    total = 0
    
    # Apply FAQ fixes to all review pages
    for review_file in (de_dir / 'bewertungen').glob('*.html'):
        c = apply_all(review_file, FAQ_FIXES)
        c += apply_all(review_file, DJI_TRANSLATIONS)
        c += apply_all(review_file, PANASONIC_TRANSLATIONS)
        c += apply_all(review_file, ZVE10_TRANSLATIONS)
        if c: print(f"✅ bewertungen/{review_file.name}: {c} translations")
        total += c
    
    # Hybrid guide remaining
    c = apply_all(de_dir / 'ratgeber' / 'beste-hybrid-kamera.html', HYBRID_REMAINING)
    if c: print(f"✅ ratgeber/beste-hybrid-kamera.html: {c} translations")
    total += c
    
    # Comparison pages remaining
    for comp_file in (de_dir / 'vergleiche').glob('*.html'):
        c = apply_all(comp_file, COMPARISON_REMAINING)
        if c: print(f"✅ vergleiche/{comp_file.name}: {c} translations")
        total += c
    
    print(f"\n{'='*50}")
    print(f"✨ Total: {total} translations applied")

if __name__ == '__main__':
    main()
