#!/usr/bin/env python3
"""
German Translation Fix - Version 15 (Complete Comparison Pages)
Full translation of all comparison pages
"""

from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent

# ============================================================================
# SONY A7 V vs CANON R6 III - COMPLETE TRANSLATION
# ============================================================================
A7V_R6III = {
    # TL;DR section
    "TL;DR picks": "Auf einen Blick",
    "Pick": "Empfehlung",
    "Runner-up": "Zweite Wahl",
    "Budget": "Budget",
    "Cleaner Rolling Shutter, stronger IBIS, großartig AF for action and handheld Video.":
        "Saubererer Rolling Shutter, stärkere IBIS, großartiger AF für Action und freihand Video.",
    "Massive Objektiv Ökosystem, flexible color tools, improved thermals and AF variety.":
        "Riesiges Objektiv-Ökosystem, flexible Farbwerkzeuge, verbesserte Wärmeableitung und AF-Vielfalt.",
    "Still ausgezeichnet hybrids if you don't need the latest Codecs and Rolling Shutter gains.":
        "Immer noch ausgezeichnete Hybride, wenn du nicht die neuesten Codecs und Rolling-Shutter-Verbesserungen brauchst.",
    "Nachteileider A7 IV / R6 II": "Alternativ: A7 IV / R6 II",
    
    # Quick comparison
    "Schnell comparison": "Schnellvergleich",
    "Category": "Kategorie",
    "Hybrid, Objektiv flexibility": "Hybrid, Objektiv-Flexibilität",
    "Hybrid/action, handheld Video": "Hybrid/Action, freihand Video",
    "4K60 HQ, 10-Bit, better Rolling Shutter than A7 IV": "4K60 HQ, 10-Bit, besserer Rolling Shutter als A7 IV",
    "4K60 oversampled, strong motion handling": "4K60 Oversampled, starke Bewegungshandhabung",
    "IBIS stronger for handheld": "IBIS stärker für freihand",
    "Großartig subject variety, improved tracking": "Großartige Motivvielfalt, verbessertes Tracking",
    "Improved heat handling": "Verbesserte Wärmeableitung",
    "Huge E-mount options": "Riesige E-Mount-Auswahl",
    "RF lenses pricier, fewer third-party": "RF-Objektive teurer, weniger Drittanbieter",
    
    # Scores
    "Scores": "Bewertungen",
    "Overall (R6 III)": "Gesamt (R6 III)",
    "Photo (A7 V)": "Foto (A7 V)",
    "Video (R6 III)": "Video (R6 III)",
    
    # Key differences
    "Key differences": "Hauptunterschiede",
    "A7 V improves over A7 IV but R6 III remains cleaner for fast motion and pans.":
        "A7 V verbessert sich gegenüber A7 IV, aber R6 III bleibt sauberer für schnelle Bewegungen und Schwenks.",
    "R6 III IBIS better for handheld Video; Sony Active helps but crops.":
        "R6 III IBIS besser für freihand Video; Sony Active hilft, beschneidet aber.",
    "Heat": "Wärme",
    "Both improved; Canon still zuverlässig for longer 4K sessions. Sony better than older A7 IV.":
        "Beide verbessert; Canon immer noch zuverlässig für längere 4K-Sessions. Sony besser als ältere A7 IV.",
    "Sony: massive third-party and native options. Canon RF: großartig glass but pricier, fewer third-party AF":
        "Sony: massive Drittanbieter- und native Optionen. Canon RF: großartiges Glas, aber teurer, weniger Drittanbieter-AF-",
    "choices.": "Auswahl.",
    
    # Choose sections
    "Choose Sony A7 V if…": "Wähle Sony A7 V wenn…",
    "Choose Canon R6 III if…": "Wähle Canon R6 III wenn…",
    "You want the deepest Objektiv Ökosystem, flexible color options, and improved thermals over A7 IV. Ideal for":
        "Du das größte Objektiv-Ökosystem, flexible Farboptionen und verbesserte Wärmeableitung gegenüber A7 IV willst. Ideal für",
    "Hybrid-Fotografs who mix talking heads, events, and photo work.":
        "Hybrid-Fotografen, die Talking Heads, Events und Fotoarbeit mischen.",
    "You shoot fast-moving subjects, need strong IBIS for handheld Video, and want cleaner Rolling Shutter. Großartig":
        "Du schnell bewegende Motive aufnimmst, starke IBIS für freihand Video brauchst und saubereren Rolling Shutter willst. Großartig",
    "for Hochzeits, documentary, and action hybrids.":
        "für Hochzeiten, Dokumentationen und Action-Hybride.",
    
    # Fazit
    "A7 V wins on lenses and flexibility; R6 III wins on motion handling and IBIS. Pick based on your subjects and":
        "A7 V gewinnt bei Objektiven und Flexibilität; R6 III gewinnt bei Bewegungshandhabung und IBIS. Wähle basierend auf deinen Motiven und",
    "whether you want Objektiv variety or the cleanest handheld Video.":
        "ob du Objektiv-Vielfalt oder das sauberste freihand Video willst.",
    
    # Affiliate
    "Affiliate note": "Partner-Hinweis",
}

# ============================================================================
# FUJIFILM X-S20 vs X-T5 - REMAINING TRANSLATIONS
# ============================================================================
XS20_XT5 = {
    "TL;DR picks": "Auf einen Blick",
    "Pick": "Empfehlung",
    "Photo-first": "Foto-fokussiert",
    "Key differences": "Hauptunterschiede",
    "Body & handling": "Gehäuse & Handhabung",
    "Affiliate note": "Partner-Hinweis",
    "4K60, better thermals, Vlog mode": "4K60, bessere Wärmeableitung, Vlog-Modus",
    "6.2K open-gate, more Rolling Shutter": "6.2K Open-Gate, mehr Rolling Shutter",
}

# ============================================================================
# SONY A7 IV vs CANON R6 II - TRANSLATIONS
# ============================================================================
A7IV_R6II = {
    "TL;DR picks": "Auf einen Blick",
    "Pick": "Empfehlung",
    "Runner-up": "Zweite Wahl",
    "Key differences": "Hauptunterschiede",
    "Scores": "Bewertungen",
    "Affiliate note": "Partner-Hinweis",
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
    print("🇩🇪 German Translation Fix v15 (Complete Comparison Pages)\n")
    de_dir = BASE_DIR / 'de' / 'vergleiche'
    total = 0
    
    translations = [
        (de_dir / 'sony-a7-v-vs-canon-r6-iii.html', A7V_R6III, "A7V vs R6 III"),
        (de_dir / 'fujifilm-x-s20-vs-fujifilm-x-t5.html', XS20_XT5, "X-S20 vs X-T5"),
        (de_dir / 'sony-a7-iv-vs-canon-r6-ii.html', A7IV_R6II, "A7 IV vs R6 II"),
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
