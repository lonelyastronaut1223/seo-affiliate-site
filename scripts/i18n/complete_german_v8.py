#!/usr/bin/env python3
"""
German Translation Fix - Version 8 (FAQ Schema Complete Rewrite)
Fixes all remaining English in FAQ Schema JSON-LD blocks
"""

from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent

# ============================================================================
# PANASONIC S5 II - FAQ SCHEMA COMPLETE TRANSLATION
# ============================================================================
PANASONIC_FAQ = {
    # Question 1 Answer
    '"text": "Absolutely! Mit 1.997 € bietet die S5 II unglaubliches Preis-Leistungs-Verhältnis with Vollformat sensor, phase-detect AF (finally!), 4K60, and ausgezeichnet Stabilisierung. It\'s 500 € cheaper than Sony A7 IV while offering similar performance, especially for Video. The main trade-off is a smaller Objektiv Ökosystem."':
        '"text": "Absolut! Mit 1.997 € bietet die S5 II unglaubliches Preis-Leistungs-Verhältnis mit Vollformat-Sensor, Phasenerkennungs-AF (endlich!), 4K60 und ausgezeichneter Stabilisierung. Sie ist 500 € günstiger als die Sony A7 IV bei vergleichbarer Leistung, besonders für Video. Der Hauptnachteil ist ein kleineres Objektiv-Ökosystem."',
    
    # Question 2
    '"name": "Panasonic S5 II vs Sony A7 IV: Which is better?"':
        '"name": "Panasonic S5 II vs Sony A7 IV: Welche ist besser?"',
    '"text": "S5 II costs 500 € less (1.997 € vs 2.498 €) with better Video specs (6K open gate, no Crop 4K60) and superior IBIS. Sony A7 IV has better AF, more Megapixel (33MP vs 24MP), and much larger Objektivauswahl. Choose S5 II for Video and Preis-Leistungs-Verhältnis, Sony for photography and Ökosystem."':
        '"text": "S5 II kostet 500 € weniger (1.997 € vs 2.498 €) mit besseren Video-Specs (6K Open Gate, kein Crop bei 4K60) und überlegener IBIS. Sony A7 IV hat besseren AF, mehr Megapixel (33MP vs 24MP) und eine viel größere Objektivauswahl. Wähle die S5 II für Video und Preis-Leistung, Sony für Fotografie und Ökosystem."',
    
    # Question 3
    '"name": "Does the S5 II have gut Autofokus now?"':
        '"name": "Hat die S5 II jetzt guten Autofokus?"',
    '"text": "Yes! The S5 II finally has phase-detect AF, a huge upgrade from contrast-detect. It\'s zuverlässig for most situations, though Sony and Canon still edge it out for tracking fast erratic movement. For Video AF and general photography, it\'s ausgezeichnet."':
        '"text": "Ja! Die S5 II hat endlich Phasenerkennungs-AF, ein riesiges Upgrade vom Kontrast-AF. Sie ist zuverlässig für die meisten Situationen, obwohl Sony und Canon bei der Verfolgung schneller, unberechenbarer Bewegungen leicht vorne liegen. Für Video-AF und allgemeine Fotografie ist sie ausgezeichnet."',
}

# ============================================================================
# NIKON Z8 - FAQ SCHEMA COMPLETE TRANSLATION
# ============================================================================
NIKON_FAQ = {
    # Question 1 Answer
    '"text": "Z8 offers 95% of Z9 performance for 2.000 € less (3.996 € vs 5.996 €). Main differences: Z9 has built-in vertical grip and dual CFexpress slots. Z8 is smaller, lighter, and uses EN-EL15c batteries. Choose Z8 unless you need the integrated grip or shoot Hochzeits/Sport requiring zwei Kartensteckplätze."':
        '"text": "Z8 bietet 95% der Z9-Leistung für 2.000 € weniger (3.996 € vs 5.996 €). Hauptunterschiede: Z9 hat integrierten Hochformatgriff und duale CFexpress-Slots. Z8 ist kleiner, leichter und nutzt EN-EL15c-Akkus. Wähle die Z8, es sei denn, du brauchst den integrierten Griff oder fotografierst Hochzeiten/Sport, die zwei Kartensteckplätze erfordern."',
    
    # Question 2 Answer
    '"text": "Ausgezeichnet! Die Z8 ist eine der besten Wildlife-Kameras with 45MP resolution, unglaublich AF (subject detection for birds, animals), 20fps bursts, and deep buffer. Der einzige potenzielle Nachteil ist the smaller Z-mount Objektivauswahl compared to Canon, though key Wildlife lenses exist."':
        '"text": "Ausgezeichnet! Die Z8 ist eine der besten Wildlife-Kameras mit 45MP-Auflösung, unglaublichem AF (Motiverkennung für Vögel, Tiere), 20fps-Serienbildern und tiefem Puffer. Der einzige potenzielle Nachteil ist die kleinere Z-Mount-Objektivauswahl im Vergleich zu Canon, obwohl wichtige Wildlife-Objektive existieren."',
    
    # Question 3 Answer
    '"text": "Both are flagship hybrids. Z8 costs less (3.996 € vs 6.498 €), has better Ergonomie, and superior Video specs. Sony A1 has faster readout (less Rolling Shutter), 30fps bursts, and more lenses. Choose Z8 for Preis-Leistungs-Verhältnis and Video. Choose A1 for ultimate speed and Objektivauswahl."':
        '"text": "Beide sind Flaggschiff-Hybride. Z8 kostet weniger (3.996 € vs 6.498 €), hat bessere Ergonomie und überlegene Video-Specs. Sony A1 hat schnelleres Auslesen (weniger Rolling Shutter), 30fps-Serienbilder und mehr Objektive. Wähle die Z8 für Preis-Leistung und Video. Wähle die A1 für ultimative Geschwindigkeit und Objektivauswahl."',
}

# ============================================================================
# SONY A7C II - FAQ SCHEMA TRANSLATION
# ============================================================================
SONY_A7C_FAQ = {
    '"text": "For Reise and hobbyists, no. For paid Hochzeits, maybe—bring a backup memory or an extra Kamera."':
        '"text": "Für Reisen und Hobbyisten: nein. Für bezahlte Hochzeitsaufträge vielleicht – nimm einen Backup-Speicher oder eine Extra-Kamera mit."',
}

# ============================================================================
# SONY ZV-E10 - REMAINING FIXES
# ============================================================================
ZVE10_REMAINING = {
    "Can I livestream with the ZV-E10?": "Kann ich mit der ZV-E10 livestreamen?",
    "Gimbal use, the original is a smart Budget pick": "Gimbal-Nutzung ist die originale eine kluge Budget-Wahl",
}

# ============================================================================
# FUJIFILM X-T5 - REMAINING FIXES
# ============================================================================
FUJIFILM_REMAINING = {
    "For casual clips or interviews, it's more than enough.": "Für Gelegenheitsclips oder Interviews ist es mehr als genug.",
    "but with limitations": "aber mit Einschränkungen",
}

# ============================================================================
# CANON R8 - REMAINING FIXES  
# ============================================================================
CANON_REMAINING = {
    "Fotos, just keep your Verschlusszeit above 1/focal length and you're fine.":
        "Fotos, halte einfach deine Verschlusszeit über 1/Brennweite und du bist gut.",
    "more, the R8 is a significant upgrade": "mehr, die R8 ist ein signifikantes Upgrade",
}

# ============================================================================
# COMPARISON PAGES - FINAL FIXES
# ============================================================================
COMPARISON_FINAL = {
    "you're okay with a tilt screen": "du mit einem Neigungsbildschirm einverstanden bist",
    "Both ausgezeichnet; Canon is stickier for humans/animals. Sony is faster for objects.":
        "Beide ausgezeichnet; Canon ist hartnäckiger bei Menschen/Tieren. Sony ist schneller bei Objekten.",
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
    print("🇩🇪 German Translation Fix v8 (FAQ Schema Complete Rewrite)\n")
    de_dir = BASE_DIR / 'de'
    total = 0
    
    translations = [
        (de_dir / 'bewertungen' / 'panasonic-s5-ii-testbericht.html', PANASONIC_FAQ, "Panasonic S5 II FAQ Schema"),
        (de_dir / 'bewertungen' / 'nikon-z8-testbericht.html', NIKON_FAQ, "Nikon Z8 FAQ Schema"),
        (de_dir / 'bewertungen' / 'sony-a7c-ii-testbericht.html', SONY_A7C_FAQ, "Sony A7C II FAQ"),
        (de_dir / 'bewertungen' / 'sony-zv-e10-testbericht.html', ZVE10_REMAINING, "Sony ZV-E10"),
        (de_dir / 'bewertungen' / 'fujifilm-x-t5-testbericht.html', FUJIFILM_REMAINING, "Fujifilm X-T5"),
        (de_dir / 'bewertungen' / 'canon-eos-r8-testbericht.html', CANON_REMAINING, "Canon R8"),
    ]
    
    for file_path, fixes, name in translations:
        c = apply_all(file_path, fixes)
        if c:
            print(f"✅ {name}: {c} translations")
            total += c
    
    # Comparison pages
    for comp_file in (de_dir / 'vergleiche').glob('*.html'):
        c = apply_all(comp_file, COMPARISON_FINAL)
        if c:
            print(f"✅ {comp_file.name}: {c} translations")
            total += c
    
    print(f"\n{'='*50}")
    print(f"✨ Total: {total} translations applied")

if __name__ == '__main__':
    main()
