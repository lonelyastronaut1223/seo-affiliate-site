#!/usr/bin/env python3
"""
FINAL comprehensive German translation fix.
Fixes ALL remaining English content on German pages.
"""

from pathlib import Path
import re

BASE_DIR = Path(__file__).parent.parent.parent
DE_DIR = BASE_DIR / 'de'

# ============================================================================
# COMPREHENSIVE TRANSLATION MAPPINGS
# ============================================================================

# Hero section translations for guide pages
HERO_TRANSLATIONS = {
    # beste-vlog-kamera.html
    "Großartig vlogging gear should be invisible. It needs to keep you in focus, keep the shaky Material smooth, and sound großartig without a PhD in audio engineering.":
        "Großartige Vlogging-Ausrüstung sollte unsichtbar sein. Sie muss dich im Fokus halten, verwackelte Aufnahmen stabilisieren und großartig klingen – ohne einen Doktortitel in Audiotechnik.",
    
    "Great vlogging gear should be invisible":
        "Großartige Vlogging-Ausrüstung sollte unsichtbar sein",
    
    # beste-reisekamera.html
    "The golden rule of Reise photography: the best Kamera is the one you actually carry. We picked Kameras that pack pro image quality into bodies small enough for a jacket pocket.":
        "Die goldene Regel der Reisefotografie: Die beste Kamera ist die, die du tatsächlich dabei hast. Wir haben Kameras ausgewählt, die Profi-Bildqualität in Gehäuse packen, die klein genug für die Jackentasche sind.",
    
    # beste-budget-kamera-unter-800.html  
    "Best Budget Camera Under 800 € (2026)":
        "Beste Budget-Kamera unter 800 € (2026)",
    
    "Contrary to popular belief, you don't need 3.000 € to take professionell Fotos. These cameras offer 90% of the image quality for 20% of the price.":
        "Entgegen der landläufigen Meinung brauchst du keine 3.000 €, um professionelle Fotos zu machen. Diese Kameras bieten 90% der Bildqualität für 20% des Preises.",
    
    # beste-action-360-kamera.html
    "The X4 solves the biggest problem with 360 Video: sharpness.":
        "Die X4 löst das größte Problem bei 360-Video: die Schärfe.",
    
    'The "Invisible Selfie Stick" effect is pure magic':
        'Der "Unsichtbare Selfie-Stick" Effekt ist pure Magie',
    
    "It automatically stitches out the stick, making it look like a drone is following you 3 feet away.":
        "Er blendet den Stick automatisch aus, sodass es aussieht, als würde eine Drohne dir in 1 Meter Abstand folgen.",
    
    "It's the ultimate tool for solo Reisers and motorcycle riders.":
        "Das ultimative Werkzeug für Solo-Reisende und Motorradfahrer.",
    
    # Individual phrases that may appear
    "This isn't just a camera; it's a cheat code.":
        "Das ist nicht nur eine Kamera – es ist ein Cheat-Code.",
    
    "The mechanical Gimbal means your":
        "Der mechanische Gimbal bedeutet, dass deine",
}

# Badge/Label translations
BADGE_TRANSLATIONS = {
    "BEST FOR TRAVEL": "BESTE FÜR REISEN",
    "BEST FOR MOST PEOPLE": "BESTE FÜR DIE MEISTEN",
    "BESTE FOR TRAVEL": "BESTE FÜR REISEN",
    "BESTE 360 KAMERA": "BESTE 360-KAMERA",
    "BUDGET": "BUDGET",  # This is international
    "POCKET": "KOMPAKT",
    "FOTO-FIRST": "FOTO-FOKUSSIERT",
    "Creator-First": "Creator-Fokussiert",
    "All-Rounder": "Allrounder",
    "Street / City": "Straße / Stadt",
    "Landscape / Hike": "Landschaft / Wandern",
    "POV Video": "POV-Video",
    "Schwachlicht": "Schwachlicht",  # Already German
    "360 / Creative": "360 / Kreativ",
    "✨ Best for Travel": "✨ Beste für Reisen",
    "✨ BEST FOR TRAVEL": "✨ BESTE FÜR REISEN",
}

# Product text translations
PRODUCT_TRANSLATIONS = {
    # Common phrases in product cards
    "This isn't just a camera; it's a cheat code. The mechanical Gimbal means your":
        "Das ist nicht nur eine Kamera – es ist ein Cheat-Code. Der mechanische Gimbal bedeutet, dass deine",
    
    "The Sony A7C II is a marvel of engineering, squeezing the powerful A7 IV into a body barely larger than an APS-C camera. It's the dream camera for travel photographers who demand full-frame quality without the bulk.":
        "Die Sony A7C II ist ein technisches Wunderwerk – sie packt die Power der A7 IV in ein Gehäuse, das kaum größer als eine APS-C-Kamera ist. Die Traumkamera für Reisefotografen, die Vollformat-Qualität ohne Volumen wollen.",
    
    "With Sony's latest AI autofocus chip, it tracks subjects with uncanny accuracy. For vloggers and hybrid shooters, the 10-bit video and flip screen are perfect, though the single card slot limits its professional \"wedding day\" appeal.":
        "Mit Sonys neuestem KI-Autofokus-Chip verfolgt sie Motive mit verblüffender Präzision. Für Vlogger und Hybrid-Fotografen sind 10-Bit-Video und Klappbildschirm perfekt, obwohl der einzelne Kartensteckplatz die professionelle \"Hochzeitstag\"-Eignung einschränkt.",
    
    # Table headers
    "MODELLL": "MODELL",
    "MODELLLLLLL": "MODELL",
    "MAX QUALITY": "MAX QUALITÄT",
    "WATERPROOF": "WASSERDICHT",
    "Check Preis on Amazon": "Preis auf Amazon prüfen",
    "Check Preis on Amazon →": "Preis auf Amazon prüfen →",
    
    # Spec labels that might be English
    "PROTECTION": "SCHUTZ",
    "REFRAMING": "UMRAHMUNG",
    "AKKU": "AKKU",  # Already German
    "AUFLÖSUNG": "AUFLÖSUNG",  # Already German
    
    # Common phrases
    "Exchangeable Objektiv": "Wechselobjektiv",
    "Fixed Objektiv": "Festobjektiv",
}

# Full sentence translations for review pages
REVIEW_TRANSLATIONS = {
    "The Sony A7C II is a marvel of engineering":
        "Die Sony A7C II ist ein technisches Wunderwerk",
    
    "Compact Vollformat": "Kompaktes Vollformat",
    "COMPACT VOLLFORMAT": "KOMPAKTES VOLLFORMAT",
    
    # FAQ and section headers
    "What's the main difference": "Was ist der Hauptunterschied",
    "Is the compact size a disadvantage": "Ist die kompakte Größe ein Nachteil",
    "How is the electronic": "Wie ist der elektronische",
    "Can I use this": "Kann ich diese",
    
    # Button text
    "Preis auf Amazon prüfen →": "Preis auf Amazon prüfen →",  # Keep as is
}

# Footer link fixes (the href attributes)
FOOTER_HREF_FIXES = {
    'href="/about': 'href="/de/uber-uns',
    'href="/contact': 'href="/de/kontakt', 
    'href="/privacy': 'href="/de/datenschutz',
    'href="/deals': 'href="/de/angebote',
}

def translate_file(file_path: Path) -> int:
    """Apply all translations to a file. Returns number of replacements made."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    replacements = 0
    
    # Apply hero translations
    for en, de in HERO_TRANSLATIONS.items():
        if en in content:
            content = content.replace(en, de)
            replacements += 1
    
    # Apply badge translations
    for en, de in BADGE_TRANSLATIONS.items():
        # Use regex to avoid replacing inside class names or URLs
        # Match when surrounded by > and < or quotes
        patterns = [
            (f'>{en}<', f'>{de}<'),
            (f'>{en} <', f'>{de} <'),
            (f'" {en}"', f'" {de}"'),
            (f"'{en}'", f"'{de}'"),
        ]
        for old, new in patterns:
            if old in content:
                content = content.replace(old, new)
                replacements += 1
    
    # Apply product translations
    for en, de in PRODUCT_TRANSLATIONS.items():
        if en in content:
            content = content.replace(en, de)
            replacements += 1
    
    # Apply review translations
    for en, de in REVIEW_TRANSLATIONS.items():
        if en in content:
            content = content.replace(en, de)
            replacements += 1
    
    # Fix footer hrefs
    for old, new in FOOTER_HREF_FIXES.items():
        if old in content:
            content = content.replace(old, new)
            replacements += 1
    
    # Write back if changed
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✅ {file_path.relative_to(BASE_DIR)} - {replacements} replacements")
        return replacements
    else:
        print(f"  ⏭️  {file_path.relative_to(BASE_DIR)} - no changes needed")
        return 0

def fix_broken_image(file_path: Path) -> bool:
    """Fix the broken Reisekamera image."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # The broken image is likely referencing a non-existent file
    # Fix common broken image patterns
    fixes = [
        ('src="../../assets/images/guides/Reise.jpg"', 'src="../../assets/images/guides/travel-camera.png"'),
        ('src="../assets/images/guides/Reise.jpg"', 'src="../assets/images/guides/travel-camera.png"'),
        ('assets/images/guides/Reise.jpg', 'assets/images/guides/travel-camera.png'),
    ]
    
    changed = False
    for old, new in fixes:
        if old in content:
            content = content.replace(old, new)
            changed = True
    
    if changed:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  🖼️  Fixed broken image in {file_path.name}")
        return True
    return False

def main():
    print("="*60)
    print("FINAL COMPREHENSIVE GERMAN TRANSLATION FIX")
    print("="*60)
    
    total_replacements = 0
    files_changed = 0
    
    print("\n📄 Processing German pages...\n")
    
    # Process all German HTML files
    for html_file in DE_DIR.rglob('*.html'):
        result = translate_file(html_file)
        if result > 0:
            total_replacements += result
            files_changed += 1
    
    # Also fix broken images
    print("\n🖼️  Checking for broken images...\n")
    for html_file in DE_DIR.rglob('*.html'):
        fix_broken_image(html_file)
    
    print("\n" + "="*60)
    print(f"✅ COMPLETE: {total_replacements} replacements in {files_changed} files")
    print("="*60)

if __name__ == '__main__':
    main()
