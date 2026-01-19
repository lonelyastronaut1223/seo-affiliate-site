#!/usr/bin/env python3
"""
German Translation Fix - Version 13 (FAQ Schema & Complete Review Content)
Complete translation of all remaining English content in review pages
"""

from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent

# ============================================================================
# SONY ZV-E10 - FAQ SCHEMA COMPLETE TRANSLATION
# ============================================================================
ZVE10_FAQ = {
    '"text": "Yes! The ZV-E10 is one of the best Kameras for beginner Vloggers. Its simple menu, Klappbildschirm, ausgezeichnet AF, and creator-focused features (Product Showcase, Background Defocus button) make it very benutzerfreundlich. At 698 €, it offers exceptional Preis-Leistungs-Verhältnis."':
        '"text": "Ja! Die ZV-E10 ist eine der besten Kameras für Einsteiger-Vlogger. Das einfache Menü, der Klappbildschirm, der ausgezeichnete AF und die creator-fokussierten Funktionen (Produkt-Präsentation, Hintergrundunschärfe-Taste) machen sie sehr benutzerfreundlich. Mit 698 € bietet sie ein außergewöhnliches Preis-Leistungs-Verhältnis."',
    
    '"text": "ZV-E10 has interchangeable lenses, larger APS-C sensor, and better image quality for 698 €. ZV-1 is more compact with built-in Zoomobjektiv but smaller 1\\" sensor for 748 €. Choose ZV-E10 if you want flexibility and better quality. Choose ZV-1 for ultimate portability."':
        '"text": "Die ZV-E10 hat Wechselobjektive, größeren APS-C-Sensor und bessere Bildqualität für 698 €. Die ZV-1 ist kompakter mit eingebautem Zoomobjektiv, aber kleinerem 1\\"-Sensor für 748 €. Wähle die ZV-E10 für Flexibilität und bessere Qualität. Wähle die ZV-1 für ultimative Tragbarkeit."',
    
    '"text": "Yes, the ZV-E10 shoots 4K30fps Video with ausgezeichnet quality. However, it has a 1.22x Crop in 4K mode and lacks in-body Stabilisierung, so you\'ll need a Gimbal or stabilized lenses for smooth Material while walking."':
        '"text": "Ja, die ZV-E10 nimmt 4K30fps-Video in ausgezeichneter Qualität auf. Sie hat jedoch einen 1,22x Beschnitt im 4K-Modus und keine sensorbasierte Stabilisierung, also brauchst du einen Gimbal oder stabilisierte Objektive für flüssiges Material beim Gehen."',
    
    '"reviewBody": "The best Budget vlogging Kamera with Klappbildschirm, product showcase mode, and exceptional Autofokus."':
        '"reviewBody": "Die beste Budget-Vlogging-Kamera mit Klappbildschirm, Produkt-Präsentationsmodus und außergewöhnlichem Autofokus."',
}

# ============================================================================
# CANON R8 - FAQ SCHEMA COMPLETE TRANSLATION
# ============================================================================
CANON_FAQ = {
    '"text": "Yes, if you want Vollformat on a Budget. At 1.299 €, the R8 offers flagship AF from the R6 II, 24MP sensor, and compact design. Trade-offs include single SD card slot, no IBIS, and 1.6x Crop in 4K60. Beste for Fotografs upgrading from APS-C who prioritize AF and Vollformat over features."':
        '"text": "Ja, wenn du Vollformat mit Budget willst. Mit 1.299 € bietet die R8 Flaggschiff-AF der R6 II, 24MP-Sensor und kompaktes Design. Kompromisse sind: einzelner SD-Steckplatz, kein IBIS und 1,6x Beschnitt in 4K60. Beste für Fotografen, die von APS-C upgraden und AF sowie Vollformat über Features priorisieren."',
    
    '"text": "R8 (1.299 €): Budget Vollformat, großartig AF, no IBIS. R6 II (2.499 €): Professionell hybrid, IBIS, zwei Kartensteckplätze, uncropped 4K60. R7 (1.499 €): APS-C, 32MP, 30fps, better for Wildlife/Sport. Choose R8 for Budget Vollformat, R6 II for pro work, R7 for Tele reach."':
        '"text": "R8 (1.299 €): Budget-Vollformat, großartiger AF, kein IBIS. R6 II (2.499 €): Professioneller Hybrid, IBIS, zwei Kartensteckplätze, unbeschnittenes 4K60. R7 (1.499 €): APS-C, 32MP, 30fps, besser für Wildlife/Sport. Wähle R8 für Budget-Vollformat, R6 II für Profi-Arbeit, R7 für Tele-Reichweite."',
    
    '"text": "No, the R8 lacks in-body Stabilisierung (IBIS). You must use IS lenses (most Canon RF lenses have it) or accept more Kamera shake. For Video, electronic Stabilisierung helps but crops the image. This is the main trade-off for the low price."':
        '"text": "Nein, der R8 fehlt sensorbasierte Stabilisierung (IBIS). Du musst IS-Objektive verwenden (die meisten Canon RF-Objektive haben sie) oder mehr Kamera-Verwacklung akzeptieren. Für Video hilft elektronische Stabilisierung, beschneidet aber das Bild. Das ist der Hauptkompromiss für den niedrigen Preis."',
    
    "Absolutely. The R8 has much better Autofokus (Dual Pixel II vs old system), 4K60p Video (RP maxes at":
        "Absolut. Die R8 hat viel besseren Autofokus (Dual Pixel II vs altes System), 4K60p-Video (RP macht maximal",
    "4K25p), and faster burst shooting. The RP is now heavily discounted but feels outdated. For only 200 €-300":
        "4K25p) und schnellere Serienbildaufnahmen. Die RP ist jetzt stark reduziert, fühlt sich aber veraltet an. Für nur 200 €-300",
}

# ============================================================================
# DJI OSMO POCKET 3 - FAQ SCHEMA COMPLETE TRANSLATION
# ============================================================================
DJI_FAQ = {
    '"text": "Ordentlich but not großartig. The 1\\" sensor is larger than phones but smaller than APS-C/Vollformat Kameras. In gut light, it\'s ausgezeichnet. In Schwachlicht, expect some noise above ISO 1600. For nighttime vlogging, Kameras with larger sensors like ZV-E10 or A7 IV perform better."':
        '"text": "Ordentlich, aber nicht großartig. Der 1\\"-Sensor ist größer als bei Handys, aber kleiner als APS-C/Vollformat-Kameras. Bei gutem Licht ist es ausgezeichnet. Bei Schwachlicht, erwarte etwas Rauschen über ISO 1600. Für nächtliches Vlogging bieten Kameras mit größeren Sensoren wie ZV-E10 oder A7 IV bessere Leistung."',
    
    '"text": "Yes, for specific professionell use cases (vlogs, real estate tours, Reise content, social media). The built-in Gimbal, compact size, and ease of use make it ideal for run-and-gun shooting. However, for commercial productions requiring maximum quality, use a larger sensor Kamera."':
        '"text": "Ja, für bestimmte professionelle Anwendungsfälle (Vlogs, Immobilientouren, Reise-Content, Social Media). Der eingebaute Gimbal, die kompakte Größe und die einfache Bedienung machen sie ideal für Run-and-Gun-Aufnahmen. Für kommerzielle Produktionen, die maximale Qualität erfordern, verwende eine Kamera mit größerem Sensor."',
    
    '"text": "Pocket 3 is incredibly compact with built-in Gimbal for perfect Stabilisierung (519 €). ZV-E10 has larger APS-C sensor, interchangeable lenses, and better low-light (698 €). Choose Pocket 3 for ultimate portability and smooth Material. Choose ZV-E10 for better image quality and flexibility."':
        '"text": "Die Pocket 3 ist unglaublich kompakt mit eingebautem Gimbal für perfekte Stabilisierung (519 €). Die ZV-E10 hat größeren APS-C-Sensor, Wechselobjektive und besseres Schwachlicht (698 €). Wähle die Pocket 3 für ultimative Tragbarkeit und flüssiges Material. Wähle die ZV-E10 für bessere Bildqualität und Flexibilität."',
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
    print("🇩🇪 German Translation Fix v13 (FAQ Schema Complete)\n")
    de_dir = BASE_DIR / 'de' / 'bewertungen'
    total = 0
    
    translations = [
        (de_dir / 'sony-zv-e10-testbericht.html', ZVE10_FAQ, "Sony ZV-E10 FAQ"),
        (de_dir / 'canon-eos-r8-testbericht.html', CANON_FAQ, "Canon R8 FAQ"),
        (de_dir / 'dji-osmo-pocket-3-testbericht.html', DJI_FAQ, "DJI Pocket 3 FAQ"),
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
