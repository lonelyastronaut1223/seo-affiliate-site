#!/usr/bin/env python3
"""
German Translation Fix - Version 14 (Title, Meta, FAQ UI Final)
Complete translation of titles, meta descriptions, and FAQ UI content
"""

from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent

# ============================================================================
# SONY ZV-E10 - TITLE, META, FAQ UI FIXES
# ============================================================================
ZVE10_FINAL = {
    # Title - "Under" -> "Unter"
    "Sony ZV-E10 Testbericht 2026: Beste Budget Vlog Kamera Under 700 €?":
        "Sony ZV-E10 Testbericht 2026: Beste Budget Vlog Kamera unter 700 €?",
    
    # Meta description
    "Sony ZV-E10 Testbericht 2026: Beste vlogging Kamera for 698 €? Flip screen, ausgezeichnet AF, compact design tested. Honest pros & cons. Aktualisiert Jan 2026.":
        "Sony ZV-E10 Testbericht 2026: Beste Vlogging-Kamera für 698 €? Klappbildschirm, ausgezeichneter AF, kompaktes Design getestet. Ehrliche Vor- & Nachteile. Aktualisiert Jan 2026.",
    
    # FAQ Question 2 - "or" -> "oder"
    "Sollte ich die ZV-E10 or ZV-E10 II?":
        "Sollte ich die ZV-E10 oder ZV-E10 II kaufen?",
    
    # FAQ Answer 2 - Full translation
    "If you can afford it, get the ZV-E10 II. It adds in-body Stabilisierung, better Akkulaufzeit, and AI":
        "Wenn du es dir leisten kannst, nimm die ZV-E10 II. Sie bietet sensorbasierte Stabilisierung, bessere Akkulaufzeit und KI-",
    "Autofokus. Aber die originale ZV-E10 ist immer noch ausgezeichnet und kostet jetzt 200 €-300 weniger. For":
        "Autofokus. Aber die originale ZV-E10 ist immer noch ausgezeichnet und kostet jetzt 200 €-300 weniger. Für",
    "tripod work or":
        "Stativ-Arbeit oder",
    
    # FAQ Schema - Question names
    '"name": "Sony ZV-E10 vs ZV-1: Which is better for vlogging?"':
        '"name": "Sony ZV-E10 vs ZV-1: Welche ist besser für Vlogging?"',
    '"name": "Can the ZV-E10 shoot 4K Video?"':
        '"name": "Kann die ZV-E10 4K-Video aufnehmen?"',
    
    # FAQ Answer 5 - "Yes" -> "Ja"
    "Yes, using the USB-C port with Sony's Imaging Edge Webcam software (free). It works perfectly with OBS,":
        "Ja, über den USB-C-Anschluss mit Sonys Imaging Edge Webcam-Software (kostenlos). Es funktioniert perfekt mit OBS,",
    "Zoom, and YouTube Live. The Kamera can run off USB power indefinitely, so Akkulaufzeit isn't a concern":
        "Zoom und YouTube Live. Die Kamera kann unbegrenzt mit USB-Strom laufen, daher ist Akkulaufzeit kein Problem",
}

# ============================================================================
# OTHER REVIEW PAGES - SIMILAR FIXES
# ============================================================================
OTHER_FIXES = {
    # Common "Under" typo
    "Under 700": "unter 700",
    "Under 800": "unter 800",
    "Under 1000": "unter 1000",
    
    # Common FAQ starts
    "Yes! It's": "Ja! Sie ist",
    "Yes, if": "Ja, wenn",
    "No, the": "Nein, die",
    
    # Common transitions
    "However,": "Jedoch",
    "Therefore,": "Daher",
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
    print("🇩🇪 German Translation Fix v14 (Title, Meta, FAQ UI Final)\n")
    de_dir = BASE_DIR / 'de'
    total = 0
    
    # ZV-E10 specific fixes
    c = apply_translations(de_dir / 'bewertungen' / 'sony-zv-e10-testbericht.html', ZVE10_FINAL)
    if c: print(f"✅ sony-zv-e10-testbericht.html: {c} translations")
    total += c
    
    # Apply common fixes to all review pages
    for review_file in (de_dir / 'bewertungen').glob('*.html'):
        c = apply_translations(review_file, OTHER_FIXES)
        if c: 
            print(f"✅ {review_file.name}: {c} translations")
            total += c
    
    print(f"\n{'='*50}")
    print(f"✨ Total: {total} translations applied")

if __name__ == '__main__':
    main()
