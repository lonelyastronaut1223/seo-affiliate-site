#!/usr/bin/env python3
"""
German Translation Fix - Version 11 (Absolute Final)
Fixes all remaining true English content
"""

from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent

# ============================================================================
# SONY A7C II - FAQ SCHEMA FIX
# ============================================================================
A7C_FAQ = {
    '"text": "For Reise and hobbyists, no. For paid Hochzeits, maybe."':
        '"text": "Für Reisen und Hobbyisten, nein. Für bezahlte Hochzeiten, vielleicht."',
    '"text": "Better than the A7C, but compact bodies do get warm in 4K60."':
        '"text": "Besser als die A7C, aber kompakte Gehäuse werden in 4K60 warm."',
}

# ============================================================================
# SONY A7 V vs CANON R6 III - REMAINING FIX
# ============================================================================
A7V_VS_R6III = {
    "Both ausgezeichnet; Canon is stickier for humans/animals. Sony strong across varied subjects and lenses.":
        "Beide ausgezeichnet; Canon ist hartnäckiger bei Menschen/Tieren. Sony stark bei verschiedenen Motiven und Objektiven.",
}

# ============================================================================
# FUJIFILM X-S20 vs X-T5 - REMAINING FIX
# ============================================================================
XS20_VS_XT5 = {
    "you're okay with a tilt screen.":
        "du mit einem Neigungsbildschirm einverstanden bist.",
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
    print("🇩🇪 German Translation Fix v11 (Absolute Final)\n")
    de_dir = BASE_DIR / 'de'
    total = 0
    
    translations = [
        (de_dir / 'bewertungen' / 'sony-a7c-ii-testbericht.html', A7C_FAQ, "Sony A7C II FAQ"),
        (de_dir / 'vergleiche' / 'sony-a7-v-vs-canon-r6-iii.html', A7V_VS_R6III, "A7V vs R6 III"),
        (de_dir / 'vergleiche' / 'fujifilm-x-s20-vs-fujifilm-x-t5.html', XS20_VS_XT5, "X-S20 vs X-T5"),
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
