#!/usr/bin/env python3
"""
German Translation Script v6 - New Review Pages
Translates the 10 newly added review pages from EN to DE
"""

from pathlib import Path
import re

BASE_DIR = Path(__file__).parent.parent.parent

# Base translations for ALL review pages
COMMON_TRANS  = {
    # Import paths
    'import BaseLayout from "../../layouts/BaseLayout.astro";':
        'import BaseLayout from "../../../layouts/BaseLayout.astro";',
    'import ProductSchema from "../../components/ProductSchema.astro";':
        'import ProductSchema from "../../../components/ProductSchema.astro";',
    'import AuthorBio from "../../components/AuthorBio.astro";':
        'import AuthorBio from "../../../components/AuthorBio.astro";',
    'import "../../styles/review-page.css";':
        'import "../../../styles/review-page.css";',
    
    # Common UI elements
    'Check Price on Amazon →':
        'Preis auf Amazon prüfen →',
    'The Verdict': 'Das Urteil',
    'What We Like': 'Was uns gefällt',
    'Trade-offs': 'Die Nachteile',
    'Final Recommendation': 'Abschließende Empfehlung',
    'Buy it if:': 'Kaufe sie, wenn:',
    'Skip it if:': 'Überspringe sie, wenn:',
    
    # Common tech terms
    'priceCurrency="USD"': 'priceCurrency="EUR"',
    'url="/reviews/': 'url="/de/reviews/',
    'name: "': 'name: "',  # Keep product names
}

# Individual review page translations
INSTA360_X4 = {
    'title="Insta360 X4 Review 2026: Best 360 Camera?"':
        'title="Insta360 X4 Testbericht 2026: Beste 360-Kamera?"',
    'description="Insta360 X4 review: 8K 360 video, invisible selfie stick, AI reframing tested. Worth $499? Full specs & verdict for content creators."':
        'description="Insta360 X4 Testbericht: 8K 360-Video, unsichtbarer Selfie-Stick, KI-Neurahmung getestet. Lohnt sich 499 €? Vollständige Spezifikationen für Content Creator."',
    '360 Camera · $499': '360-Kamera · 499 €',
    'Insta360 X4 Review': 'Insta360 X4 Testbericht',
    'The Insta360 X4 solves the biggest problem':
        'Die Insta360 X4 löst das größte Problem',
    '👑 360 King': '👑 360-König',
    'Video': 'Video',
    'Features': 'Funktionen',
    'Build': 'Gehäuse',
    'Waterproof': 'Wasserdicht',
    'Screen': 'Bildschirm',
    'Battery': 'Akku',
    'Storage': 'Speicher',
    'Weight': 'Gewicht',
}

GOPRO_HERO13 = {
    'title="GoPro Hero 13 Black Review 2026: Still the Best Action Cam?"':
        'title="GoPro Hero 13 Black Testbericht 2026: Immer noch die beste Action-Kamera?"',
    'description="GoPro Hero 13 Black review: New magnetic mounting, improved battery life, HB-series lens mods tested. Full verdict for 2026."':
        'description="GoPro Hero 13 Black Testbericht: Neue magnetische Halterung, verbesserte Akkulaufzeit, HB-Objektiv-Mods getestet. Vollständiges Urteil für 2026."',
    'GoPro Hero 13 Black Review': 'GoPro Hero 13 Black Testbericht',
    'Action Camera · $399': 'Action-Kamera · 399 €',
}

SONY_A6700 = {
    'title="Sony A6700 Review 2026: Best APS-C for Creators?"':
        'title="Sony A6700 Testbericht 2026: Beste APS-C für Creator?"',
    'description="Sony A6700 review: 26MP APS-C, AI autofocus, 4K 120p tested. Is this the new king of APS-C? Full specs & verdict."':
        'description="Sony A6700 Testbericht: 26MP APS-C, KI-Autofokus, 4K 120p getestet. Ist dies der neue König von APS-C? Vollständige Spezifikationen."',
    'Sony A6700 Review': 'Sony A6700 Testbericht',
    'APS-C Mirrorless · $1,398': 'APS-C Spiegellos · 1.398 €',
}

PANASONIC_S5IIX = {
    'title="Panasonic Lumix S5IIX Review: Professional Hybrid Camera"':
        'title="Panasonic Lumix S5IIX Testbericht: Professionelle Hybrid-Kamera"',
    'description="In-depth review of the Panasonic Lumix S5IIX full-frame mirrorless camera featuring advanced video tools, impressive image quality, and professional hybrid capabilities."':
        'description="Ausführlicher Testbericht der Panasonic Lumix S5IIX Vollformat-Spiegelreflexkamera mit erweiterten Video-Tools, beeindruckender Bildqualität und professionellen Hybrid-Funktionen."',
    'Panasonic Lumix S5IIX Review': 'Panasonic Lumix S5IIX Testbericht',
    'Full-Frame Mirrorless · $2,099': 'Vollformat Spiegellos · 2.099 €',
}

SONY_ZV1_II = {
    'title="Sony ZV-1 II Review 2026: Best Compact Vlog Camera?"':
        'title="Sony ZV-1 II Testbericht 2026: Beste kompakte Vlog-Kamera?"',
    'description="Sony ZV-1 II review: Ultra-wide 18mm lens, flip screen, product showcase mode tested. Perfect pocket vlog cam? Full specs & verdict."':
        'description="Sony ZV-1 II Testbericht: Ultra-Weitwinkel 18mm Objektiv, Klappbildschirm, Produktpräsentationsmodus getestet. Perfekte Taschen-Vlog-Kamera?"',
    'Sony ZV-1 II Review': 'Sony ZV-1 II Testbericht',
    'Compact Vlog Camera · $899': 'Kompakte Vlog-Kamera · 899 €',
}

PANASONIC_G100D = {
    'title="Panasonic G100D Review 2026: Budget Vlog Camera"':
        'title="Panasonic G100D Testbericht 2026: Budget-Vlog-Kamera"',
    'description="Panasonic G100D review: Micro Four Thirds vlogging camera with tripod grip, flip screen tested. Best budget vlog cam? Full verdict."':
        'description="Panasonic G100D Testbericht: Micro Four Thirds Vlogging-Kamera mit Stativgriff, Klappbildschirm getestet. Beste Budget-Vlog-Kamera?"',
    'Panasonic G100D Review': 'Panasonic G100D Testbericht',
    'Micro Four Thirds · $599': 'Micro Four Thirds · 599 €',
}

OM_SYSTEM_OM5 = {
    'title="OM System OM-5 Review 2026: Compact Adventure Camera"':
        'title="OM System OM-5 Testbericht 2026: Kompakte Abenteuer-Kamera"',
    'description="OM System OM-5 review: Weather-sealed micro four thirds, 8.5EV IBIS, 50MP computational photography tested. Perfect for hiking?"':
        'description="OM System OM-5 Testbericht: Wetterfestes Micro Four Thirds, 8.5EV IBIS, 50MP Computational Photography getestet. Perfekt für Wanderungen?"',
    'OM System OM-5 Review': 'OM System OM-5 Testbericht',
    'Micro Four Thirds · $1,199': 'Micro Four Thirds · 1.199 €',
}

DJI_ACTION5 = {
    'title="DJI Osmo Action 5 Pro Review 2026: GoPro Killer?"':
        'title="DJI Osmo Action 5 Pro Testbericht 2026: GoPro-Killer?"',
    'description="DJI Osmo Action 5 Pro review: 1/1.3-inch sensor, 4-hour battery, dual touchscreens tested. Better than GoPro Hero 13? Full verdict."':
        'description="DJI Osmo Action 5 Pro Testbericht: 1/1.3-Zoll-Sensor, 4-Stunden-Akku, Dual-Touchscreens getestet. Besser als GoPro Hero 13?"',
    'DJI Osmo Action 5 Pro Review': 'DJI Osmo Action 5 Pro Testbericht',
    'Action Camera · $349': 'Action-Kamera · 349 €',
}

CANON_R6II = {
    'title="Canon R6 Mark II Review 2026: Hybrid Powerhouse"':
        'title="Canon R6 Mark II Testbericht 2026: Hybrid-Kraftpaket"',
    'description="Canon R6 Mark II review: 24MP full-frame, 40fps, 6K oversampled 4K tested. Best hybrid under $2,500? Full specs & verdict."':
        'description="Canon R6 Mark II Testbericht: 24MP Vollformat, 40fps, 6K-oversampled 4K getestet. Beste Hybrid unter 2.500 €?"',
    'Canon R6 Mark II Review': 'Canon R6 Mark II Testbericht',
    'Full-Frame Mirrorless · $2,499': 'Vollformat Spiegellos · 2.499 €',
}

SONY_FX3 = {
    'title="Sony FX3 Review 2026: Cinema Camera for Creators"':
        'title="Sony FX3 Testbericht 2026: Cinema-Kamera für Creator"',
    'description="Sony FX3 review: Full-frame cinema camera with 15+ stops dynamic range, 4K 120p 10-bit tested. Worth $3,898 for video pros?"':
        'description="Sony FX3 Testbericht: Vollformat-Cinema-Kamera mit 15+ Stops Dynamikumfang, 4K 120p 10-Bit getestet. Lohnen sich 3.898 € für Video-Profis?"',
    'Sony FX3 Review': 'Sony FX3 Testbericht',
    'Cinema Camera · $3,898': 'Cinema-Kamera · 3.898 €',
}

REVIEWS_MAP = {
    'insta360-x4-review.astro': INSTA360_X4,
    'gopro-hero-13-review.astro': GOPRO_HERO13,
    'sony-a6700-review.astro': SONY_A6700,
    'panasonic-s5iix-review.astro': PANASONIC_S5IIX,
    'sony-zv-1-ii-review.astro': SONY_ZV1_II,
    'panasonic-g100d-review.astro': PANASONIC_G100D,
    'om-system-om-5-review.astro': OM_SYSTEM_OM5,
    'dji-osmo-action-5-pro-review.astro': DJI_ACTION5,
    'canon-r6-ii-review.astro': CANON_R6II,
    'sony-fx3-review.astro': SONY_FX3,
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
    print("🇩🇪 German Translation v6 - New Review Pages\n")
    de_reviews_dir = BASE_DIR / 'src/pages/de/reviews'
    total = 0
    
    for filename, specific_trans in REVIEWS_MAP.items():
        file_path = de_reviews_dir / filename
        if not file_path.exists():
            print(f"⏭️  Skipping {filename} (not found)")
            continue
        
        # Apply common translations first
        count = apply_translations(file_path, COMMON_TRANS)
        # Apply page-specific translations
        count += apply_translations(file_path, specific_trans)
        
        if count:
            print(f"✅ {filename}: {count} translations applied")
        total += count
    
    print(f"\n{'='*60}")
    print(f"✨ Total: {total} translations applied across {len(REVIEWS_MAP)} files")
    print(f"\n📝 Next steps:")
    print(f"1. Run: python3 scripts/i18n/audit_german_v2.py")
    print(f"2. Manually review and refine translations")
    print(f"3. npm run build")

if __name__ == '__main__':
    main()
