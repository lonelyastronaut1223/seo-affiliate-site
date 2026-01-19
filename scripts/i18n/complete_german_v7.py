#!/usr/bin/env python3
"""
German Translation Fix - Version 7 (Final Cleanup)
Fixing remaining issues in Canon, Fujifilm, Nikon, Sony reviews
"""

from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent

# ============================================================================
# CANON EOS R8 REVIEW FIXES
# ============================================================================
CANON_FIXES = {
    "Why is the R8 so much cheaper than the R6 II?": "Warum ist die R8 so viel günstiger als die R6 II?",
    "Canon removed IBIS to hit the lower price point.": "Canon hat IBIS entfernt, um den niedrigeren Preispunkt zu erreichen.",
    "It's aimed at photographers who want Vollformat quality without paying for features they don't need.":
        "Sie richtet sich an Fotografen, die Vollformat-Qualität wollen, ohne für Funktionen zu bezahlen, die sie nicht brauchen.",
    "Is the lack of IBIS a deal-breaker?": "Ist das Fehlen von IBIS ein Dealbreaker?",
    "Depends on your shooting style.": "Kommt auf deinen Aufnahmestil an.",
    "For photography, RF lens stabilization is often enough.": "Für Fotografie reicht die RF-Objektiv-Stabilisierung oft aus.",
    "For video, you'll want stabilized lenses or a gimbal.": "Für Video brauchst du stabilisierte Objektive oder einen Gimbal.",
    "How is the Rolling Shutter compared to Sony?": "Wie ist der Rolling Shutter im Vergleich zu Sony?",
    "Slightly worse than Sony A7C II, but fine for most video work.": "Etwas schlechter als Sony A7C II, aber für die meiste Videoarbeit in Ordnung.",
    "Should I invest in RF lenses or use EF with an adapter?": "Sollte ich in RF-Objektive investieren oder EF mit Adapter nutzen?",
    "RF lenses are sharper and smaller, but expensive.": "RF-Objektive sind schärfer und kleiner, aber teuer.",
    "EF lenses work perfectly with the EF-RF adapter.": "EF-Objektive funktionieren perfekt mit dem EF-RF-Adapter.",
    "Is the R8 worth it over the older RP?": "Lohnt sich die R8 gegenüber der älteren RP?",
    "Absolutely. The R8 has a much better sensor, autofocus, and no record limit.":
        "Absolut. Die R8 hat einen viel besseren Sensor, Autofokus und kein Aufnahmelimit.",
}

# ============================================================================
# FUJIFILM X-T5 REVIEW FIXES
# ============================================================================
FUJIFILM_FIXES = {
    "save hours of editing": "spart Stunden der Bearbeitung",
    "For casual clips or interviews, it's more than enough.": "Für Gelegenheitsclips oder Interviews ist es mehr als genug.",
    "quality modes.": "Qualitätsmodi.",
    "Does the X-T5 have gut Autofokus?": "Hat die X-T5 guten Autofokus?",
    "Yes, for photography.": "Ja, für Fotografie.",
    "The Phase-Detection AF is fast and Zuverlässig.": "Der Phasenerkennungs-AF ist schnell und zuverlässig.",
    "For video, it's more limited than Sony.": "Für Video ist er limitierter als Sony.",
    "Is the autofocus as good as Sony?": "Ist der Autofokus so gut wie bei Sony?",
    "For photos, nearly. For video tracking, Sony has an edge.": "Für Fotos, fast. Für Video-Tracking hat Sony einen Vorteil.",
    "Does it have in-body image stabilization?": "Hat sie In-Body-Bildstabilisierung?",
    "Yes, up to 7 stops of stabilization.": "Ja, bis zu 7 Blenden Stabilisierung.",
}

# ============================================================================
# NIKON Z8 REVIEW FIXES
# ============================================================================
NIKON_FIXES = {
    "Both are flagship hybrids. Z8 costs less (3.996 € vs 5.499 €) but has a smaller body and battery.":
        "Beide sind Flaggschiff-Hybride. Z8 kostet weniger (3.996 € vs 5.499 €), hat aber ein kleineres Gehäuse und Akku.",
    "Z9 is for professional sports shooters, Z8 is for traveling pros.":
        "Z9 ist für professionelle Sportfotografen, Z8 für reisende Profis.",
    "Is the Nikon Z8 gut for Wildlife photography?": "Ist die Nikon Z8 gut für Wildlife-Fotografie?",
    "Excellent. Fast continuous shooting, reliable tracking, and deep buffers.":
        "Ausgezeichnet. Schnelle Serienaufnahmen, zuverlässiges Tracking und große Puffer.",
    "Nikon Z8 vs Sony A1: Which is better?": "Nikon Z8 vs Sony A1: Welche ist besser?",
    "A1 costs 2.000 € more. Z8 wins on value. A1 wins on speed and global shutter.":
        "A1 kostet 2.000 € mehr. Z8 gewinnt beim Preis-Leistungs-Verhältnis. A1 gewinnt bei Geschwindigkeit und Global Shutter.",
}

# ============================================================================
# SONY ZV-E10 REVIEW FIXES
# ============================================================================
ZVE10_FIXES = {
    "Autofokus. But the original ZV-E10 is still ausgezeichnet and": "Autofokus. Aber die originale ZV-E10 ist immer noch ausgezeichnet und",
    "For a Brand neu budget, the original is perfect.": "Für ein brandneues Budget ist die originale perfekt.",
    "should I get the ZV-E10 or ZV-E10 II?": "Sollte ich die ZV-E10 oder ZV-E10 II kaufen?",
    "The Mark II has better screen, improved video, and updated AF.": "Die Mark II hat einen besseren Bildschirm, verbessertes Video und aktualisierten AF.",
    "for creators who want great video on a budget.": "für Creator, die großartiges Video mit kleinem Budget wollen.",
    "entry-point for creators.": "Einstiegspunkt für Creator.",
    "✨ Beste Preis-Leistung": "✨ Beste Preis-Leistung",
}

# ============================================================================
# HYBRID GUIDE REMAINING FIXES
# ============================================================================
HYBRID_FINAL = {
    "Brauchst du Geschwindigkeit? The R6 Mark II schießt atemberaubende 40 Bilder pro Sekunde": 
        "Brauchst du Geschwindigkeit? Die R6 Mark II schießt atemberaubende 40 Bilder pro Sekunde",
    "elektronisch. It's a monster for Sport and Wildlife.": "elektronisch. Sie ist ein Monster für Sport und Wildlife.",
    "For Video, it's the only Kamera in this price range that shoots 4K 60p":
        "Für Video ist sie die einzige Kamera in dieser Preisklasse, die 4K 60p aufnimmt",
}

# ============================================================================
# COMPARISON PAGE FINAL FIXES
# ============================================================================
COMPARISON_FINAL = {
    "you're okay with a tilt screen": "du mit einem Neigungsbildschirm zufrieden bist",
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
    print("🇩🇪 German Translation Fix v7 (Final Cleanup)\n")
    de_dir = BASE_DIR / 'de'
    total = 0
    
    all_fixes = [
        (de_dir / 'bewertungen' / 'canon-eos-r8-testbericht.html', CANON_FIXES),
        (de_dir / 'bewertungen' / 'fujifilm-x-t5-testbericht.html', FUJIFILM_FIXES),
        (de_dir / 'bewertungen' / 'nikon-z8-testbericht.html', NIKON_FIXES),
        (de_dir / 'bewertungen' / 'sony-zv-e10-testbericht.html', ZVE10_FIXES),
        (de_dir / 'ratgeber' / 'beste-hybrid-kamera.html', HYBRID_FINAL),
    ]
    
    for file_path, fixes in all_fixes:
        c = apply_all(file_path, fixes)
        if c:
            print(f"✅ {file_path.name}: {c} translations")
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
