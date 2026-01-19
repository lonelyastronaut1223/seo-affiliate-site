#!/usr/bin/env python3
"""
Complete German Translation Fix
Translates all remaining English content in DE/ratgeber/ pages
"""

from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent

# Comprehensive translations for Action-360 guide
ACTION_360_TRANSLATIONS = {
    # Insta360 X4 descriptions
    "With 8K resolution, when you reframe (Crop)\n              into a standard 16:9 Video, it actually looks crisp and 4K-ish.":
        "Mit 8K-Auflösung sieht das Material beim Zurechtschneiden auf 16:9 tatsächlich scharf und 4K-ähnlich aus.",
    
    "It automatically stitches out the stick, making it look\n              like a drone is following you 3 feet away. It's the ultimate tool for solo Reiseers and motorcycle\n              riders.":
        "Er entfernt den Stick automatisch aus dem Bild, sodass es aussieht, als würde eine Drohne dir in einem Meter Entfernung folgen. Das ultimative Werkzeug für Alleinreisende und Motorradfahrer.",
    
    # GoPro Hero 13 descriptions
    "For traditional POV (point of view) action—mountain biking, surfing, skiing—GoPro is still the king. The\n              chassis is proven tough, and the mounting system (fingers) is universal.":
        "Für klassische POV-Action (Point-of-View) – Mountainbiking, Surfen, Skifahren – ist GoPro nach wie vor der König. Das Gehäuse ist bewährt robust und das Befestigungssystem (Finger) ist universell.",
    
    "The 8:7 aspect ratio sensor is brilliant. It shoots a nearly square image, allowing you to Crop a vertical\n              Video for Instagram and a horizontal Video for YouTube from the exact same file.":
        "Der Sensor im 8:7-Format ist genial. Er nimmt ein nahezu quadratisches Bild auf, sodass du aus einer einzigen Datei ein vertikales Video für Instagram und ein horizontales Video für YouTube zuschneiden kannst.",
    
    # DJI Osmo Action 5 Profi descriptions
    "While GoPro owns the daylight, DJI owns the night (and the water). The Action 5 Profi has a larger 1/1.3\"\n              sensor that gathers way more light, making your evening Material look clean rather than muddy.":
        "Während GoPro bei Tageslicht dominiert, gehört DJI die Nacht (und das Wasser). Die Action 5 Profi hat einen größeren 1/1.3\"-Sensor, der viel mehr Licht einfängt und deine Abendaufnahmen klar statt matschig aussehen lässt.",
    
    "It's also waterproof down to 20 meters <em>without</em> a case (GoPro is only 10m). The magnetic mounting\n              system is faster and less annoying than GoPro's screw mount.":
        "Sie ist auch bis 20 Meter wasserdicht – <em>ohne</em> Gehäuse (GoPro nur 10m). Das Magnetbefestigungssystem ist schneller und weniger nervig als GoPros Schraubhalterung.",
    
    # 360 vs Action section
    "You want unique angles (like the drone shot) or if you are terrible at framing your subject. It captures\n            everything, so you can't miss.":
        "Du einzigartige Perspektiven willst (wie den Drohnen-Shot) oder wenn du schlecht darin bist, dein Motiv zu rahmen. Sie erfasst alles, du kannst also nichts verpassen.",
    
    "You want the highest quality Video (4K/5.3K sharp) and simplicity. You just hit record and go, no editing\n            or reframing required.":
        "Du die höchste Videoqualität willst (4K/5.3K scharf) und Einfachheit. Du drückst einfach auf Aufnahme und los geht's – kein Bearbeiten oder Zurechtschneiden nötig.",
}

# Translations for other guide pages
VLOG_KAMERA_TRANSLATIONS = {
    # Check if any English remains
    "Great vlogging gear should be invisible":
        "Großartige Vlogging-Ausrüstung sollte unsichtbar sein",
}

HYBRID_KAMERA_TRANSLATIONS = {
    "The holy grail of modern cameras:":
        "Der heilige Gral moderner Kameras:",
    "one body that excels at both stills and video":
        "ein Gehäuse, das bei Fotos und Video gleichermaßen glänzt",
}

BUDGET_KAMERA_TRANSLATIONS = {
    "Contrary to popular belief, you don't need":
        "Entgegen der landläufigen Meinung brauchst du keine",
}

REISE_KAMERA_TRANSLATIONS = {
    "The golden rule of travel photography:":
        "Die goldene Regel der Reisefotografie:",
    "the best camera is the one you actually carry":
        "Die beste Kamera ist die, die du tatsächlich dabei hast",
}

ANFAENGER_TRANSLATIONS = {
    "Your first \"real\" camera should spark joy":
        "Deine erste \"echte\" Kamera sollte Freude entfachen",
}

VOLLFORMAT_TRANSLATIONS = {
    "When every pixel counts":
        "Wenn jeder Pixel zählt",
}

def apply_translations(file_path: Path, translations: dict) -> int:
    """Apply translations to a file. Returns count of replacements."""
    if not file_path.exists():
        return 0
        
    content = file_path.read_text(encoding='utf-8')
    original_content = content
    count = 0
    
    for en, de in translations.items():
        if en in content:
            content = content.replace(en, de)
            count += 1
    
    if content != original_content:
        file_path.write_text(content, encoding='utf-8')
        print(f"✅ {file_path.name}: {count} translations applied")
        return count
    else:
        print(f"⏭️  {file_path.name}: no changes needed")
        return 0

def main():
    print("🇩🇪 Completing German Translations...\n")
    
    de_ratgeber = BASE_DIR / 'de' / 'ratgeber'
    total = 0
    
    # Action-360 guide
    total += apply_translations(
        de_ratgeber / 'beste-action-360-kamera.html',
        ACTION_360_TRANSLATIONS
    )
    
    # Vlog guide
    total += apply_translations(
        de_ratgeber / 'beste-vlog-kamera.html',
        VLOG_KAMERA_TRANSLATIONS
    )
    
    # Hybrid guide
    total += apply_translations(
        de_ratgeber / 'beste-hybrid-kamera.html',
        HYBRID_KAMERA_TRANSLATIONS
    )
    
    # Budget guide
    total += apply_translations(
        de_ratgeber / 'beste-budget-kamera-unter-800.html',
        BUDGET_KAMERA_TRANSLATIONS
    )
    
    # Travel guide
    total += apply_translations(
        de_ratgeber / 'beste-reisekamera.html',
        REISE_KAMERA_TRANSLATIONS
    )
    
    # Beginner guide
    total += apply_translations(
        de_ratgeber / 'beste-kamera-fuer-anfaenger-2026.html',
        ANFAENGER_TRANSLATIONS
    )
    
    # Full-frame for video guide
    total += apply_translations(
        de_ratgeber / 'beste-vollformat-fuer-video.html',
        VOLLFORMAT_TRANSLATIONS
    )
    
    print(f"\n✨ Total translations: {total}")

if __name__ == '__main__':
    main()
