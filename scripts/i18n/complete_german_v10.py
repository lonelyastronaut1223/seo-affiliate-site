#!/usr/bin/env python3
"""
German Translation Fix - Version 10 (Final Polish)
Fixes all remaining true English content and updates whitelist
"""

from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent

# ============================================================================
# CANON R8 - FINAL FIXES
# ============================================================================
CANON_FINAL = {
    "Fotos, just keep your Verschlusszeit above 1/focal length and you'll be fine.":
        "Fotos, halte einfach deine Verschlusszeit über 1/Brennweite und du wirst keine Probleme haben.",
    "Canon cut costs by removing IBIS, the second card slot, Wetterdichtung, and the top LCD. The R8 uses a":
        "Canon hat Kosten gespart durch Entfernung von IBIS, dem zweiten Kartensteckplatz, Wetterdichtung und dem Top-LCD. Die R8 verwendet ein",
    "plastic build instead of magnesium alloy. However, it has the same 24MP sensor and AF system as the R6 II,":
        "Plastikgehäuse statt Magnesiumlegierung. Sie hat jedoch den gleichen 24MP-Sensor und das AF-System wie die R6 II,",
    "so image quality is nearly identical.": "sodass die Bildqualität nahezu identisch ist.",
    "Only if you shoot slow Verschlusszeits handheld or use non-stabilized lenses. Most modern RF lenses have":
        "Nur wenn du langsame Verschlusszeiten freihand aufnimmst oder nicht-stabilisierte Objektive verwendest. Die meisten modernen RF-Objektive haben",
    "IS (Bildstabilisierung), which works großartig with the R8. For Video, enable digital IS in Kamera. For":
        "IS (Bildstabilisierung), die großartig mit der R8 funktioniert. Für Video aktiviere digitale IS in der Kamera. Für",
    "The R8 has more Rolling Shutter than the A7 IV due to the slower sensor readout. Fast pans and quick":
        "Die R8 hat mehr Rolling Shutter als die A7 IV wegen der langsameren Sensor-Auslesung. Schnelle Schwenks und schnelle",
    "movements can show some wobble. It's not terrible, but noticeable if you're coming from a Sony or doing a":
        "Bewegungen können etwas wackeln. Es ist nicht schlimm, aber bemerkbar wenn du von Sony kommst oder viel",
    "lot of handheld Video. The R6 II is better in this regard.":
        "freihand Video machst. Die R6 II ist in dieser Hinsicht besser.",
    "This is where Canon shines. The Dual Pixel CMOS AF II tracks people, animals, and vehicles with uncanny":
        "Hier glänzt Canon. Der Dual Pixel CMOS AF II verfolgt Menschen, Tiere und Fahrzeuge mit unheimlicher",
    "accuracy. It's \"point and shoot\" simplicity with professionell results.":
        "Genauigkeit. Es ist \"Point and Shoot\"-Einfachheit mit professionellen Ergebnissen.",
    "Unlike many competitors that Crop 4K60, the R8 gives you the full sensor width. This is huge for Weitwinkel":
        "Anders als viele Konkurrenten, die 4K60 beschneiden, gibt dir die R8 die volle Sensorbreite. Das ist enorm für Weitwinkel-",
    "vlogging or slow-motion B-roll. Just watch out for Rolling Shutter in fast pans.":
        "Vlogging oder Zeitlupen-B-Roll. Achte nur auf Rolling Shutter bei schnellen Schwenks.",
    "It feels like an entry-level Rebel DSLR but shoots like a pro spiegellos. The lack of a joystick is":
        "Sie fühlt sich an wie eine Einsteiger-Rebel-DSLR, fotografiert aber wie eine Profi-Spiegellose. Das Fehlen eines Joysticks wird",
    'mitigated by the ausgezeichnet "touch and drag" AF on the screen.':
        'durch den ausgezeichneten \"Touch and Drag\"-AF auf dem Bildschirm ausgeglichen.',
}

# ============================================================================
# SONY ZV-E10 - FINAL FIXES
# ============================================================================
ZVE10_FINAL = {
    "Quality is far better than any webcam.": "Die Qualität ist weit besser als jede Webcam.",
    "using the USB-C port with Sony's Imaging Edge Webcam software (free). It works perfectly with OBS,":
        "über den USB-C-Anschluss mit Sonys Imaging Edge Webcam-Software (kostenlos). Es funktioniert perfekt mit OBS,",
    "Zoom, and YouTube Live. The Kamera can run off USB power indefinitely, so Akkulaufzeit isn't a concern":
        "Zoom und YouTube Live. Die Kamera kann unbegrenzt mit USB-Strom laufen, also ist Akkulaufzeit kein Problem",
    "during streams.": "während Streams.",
    "Aber die originale ZV-E10 ist immer noch ausgezeichnet und now costs 200 €-300 less.":
        "Aber die originale ZV-E10 ist immer noch ausgezeichnet und kostet jetzt 200 €-300 weniger.",
}

# ============================================================================
# SONY A7C II - FAQ FIX
# ============================================================================
A7C_FINAL = {
    '"text": "For Reise and hobbyists, no. For paid Hochzeits, maybe—bring a backup memory or an extra Kamera."':
        '"text": "Für Reisen und Hobbyisten: nein. Für bezahlte Hochzeitsaufträge vielleicht – nimm einen Backup-Speicher oder eine Extra-Kamera mit."',
}

# ============================================================================
# COMPARISON PAGE FINAL - SONY A7V VS CANON R6 III
# ============================================================================
SONY_VS_CANON_FINAL = {
    "Both ausgezeichnet; Canon is stickier for humans/animals. Sony is faster for objects.":
        "Beide ausgezeichnet; Canon ist hartnäckiger bei Menschen/Tieren. Sony ist schneller bei Objekten.",
}

# ============================================================================
# FUJIFILM X-S20 VS X-T5 - REMAINING
# ============================================================================
FUJI_COMPARE_FINAL = {
    "you're okay with a tilt screen": "du mit einem Neigungsbildschirm einverstanden bist",
}

def apply_translations(file_path: Path, translations: dict) -> int:
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
    print("🇩🇪 German Translation Fix v10 (Final Polish)\n")
    de_dir = BASE_DIR / 'de'
    total = 0
    
    translations = [
        (de_dir / 'bewertungen' / 'canon-eos-r8-testbericht.html', CANON_FINAL, "Canon R8"),
        (de_dir / 'bewertungen' / 'sony-zv-e10-testbericht.html', ZVE10_FINAL, "Sony ZV-E10"),
        (de_dir / 'bewertungen' / 'sony-a7c-ii-testbericht.html', A7C_FINAL, "Sony A7C II"),
        (de_dir / 'vergleiche' / 'sony-a7-v-vs-canon-r6-iii.html', SONY_VS_CANON_FINAL, "Sony A7V vs Canon R6 III"),
        (de_dir / 'vergleiche' / 'fujifilm-x-s20-vs-fujifilm-x-t5.html', FUJI_COMPARE_FINAL, "Fuji X-S20 vs X-T5"),
    ]
    
    for file_path, fixes, name in translations:
        c = apply_translations(file_path, fixes)
        if c:
            print(f"✅ {name}: {c} translations")
            total += c
    
    print(f"\n{'='*50}")
    print(f"✨ Total: {total} translations applied")

if __name__ == '__main__':
    main()
