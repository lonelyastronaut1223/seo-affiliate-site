#!/usr/bin/env python3
"""
DIRECT FIX for German guide pages with extensive English content.
This script completely rewrites the hero and product sections with proper German.
"""

from pathlib import Path
import re

BASE_DIR = Path(__file__).parent.parent.parent
DE_DIR = BASE_DIR / 'de'

# ============================================================================
# COMPLETE TRANSLATIONS FOR BESTE-VLOG-KAMERA.HTML
# ============================================================================

VLOG_TRANSLATIONS = {
    # Hero
    "Großartig vlogging gear should be invisible. It needs to keep you in focus, keep the shaky Material smooth, and\n            sound großartig without a PhD in audio engineering.":
        "Großartige Vlogging-Ausrüstung sollte unsichtbar sein. Sie muss dich im Fokus halten, verwackelte Aufnahmen stabilisieren und großartig klingen – ohne einen Doktortitel in Audiotechnik.",
    
    # Table headers
    "Max Quality": "Max. Qualität",
    "Mechanical (Perfect)": "Mechanisch (Perfekt)",
    "Active Digital": "Aktiv Digital",
    "Gimbal Cam": "Gimbal-Kamera",
    "Action Cam": "Action-Kamera",
    
    # Badge
    "🏆 Beste for Most People": "🏆 Beste für die Meisten",
    "💎 Ultimate Quality": "💎 Ultimative Qualität",
    "🏄‍♂️ Action Vibes": "🏄‍♂️ Action-Feeling",
    
    # DJI Section
    "This isn't just a Kamera; it's a cheat code. Der mechanische Gimbal bedeutet, dass deine walking Material looks like\n              it was shot on a Hollywood dolly track. It has a massive 1-inch sensor, so it actually works in dim\n              restaurants or at night.":
        "Das ist nicht nur eine Kamera – es ist ein Cheat-Code. Der mechanische Gimbal bedeutet, dass deine Laufaufnahmen aussehen, als wären sie auf einer Hollywood-Dolly-Schiene gedreht. Mit dem großen 1-Zoll-Sensor funktioniert sie auch in dunklen Restaurants oder nachts.",
    
    "The wireless microphone (DJI Mic 2) connects directly to it instantly. Flip the screen, it turns on. Flip\n              it back, it turns off. It is the fastest workflow in existence.":
        "Das kabellose Mikrofon (DJI Mic 2) verbindet sich sofort direkt mit ihr. Klappe den Bildschirm auf, sie schaltet sich ein. Klappe ihn zurück, sie schaltet sich aus. Der schnellste Workflow, den es gibt.",
    
    # DJI Specs
    "Wireless Ready": "Funk-fähig",
    "3-Axis Mechanical": "3-Achsen Mechanisch",
    "Size": "Größe",
    "Candy Bar": "Smartphone-Größe",
    
    # DJI Pros/Cons
    "Unbeatable mechanical Stabilisierung": "Unschlagbare mechanische Stabilisierung",
    "Large 1-inch sensor is großartig in Schwachlicht": "Großer 1-Zoll-Sensor hervorragend bei Schwachlicht",
    "Unglaublich face tracking": "Unglaubliche Gesichtsverfolgung",
    "Ready to shoot in 2 seconds": "In 2 Sekunden aufnahmebereit",
    "Festobjektiv (20mm equivalent)": "Festbrennweite (20mm äquivalent)",
    "Not rugged/waterproof without a case": "Nicht robust/wasserdicht ohne Hülle",
    "Akku is built-in (not swappable)": "Akku ist eingebaut (nicht wechselbar)",
    
    # Sony ZV-E1 Section
    "If you want your vlogs to look like Netflix documentaries, you need Vollformat. The ZV-E1 uses the same\n              sensor as the cinema-line FX3 but costs half the price. The background blur (bokeh) is real and creamy.":
        "Wenn deine Vlogs wie Netflix-Dokumentationen aussehen sollen, brauchst du Vollformat. Die ZV-E1 nutzt den gleichen Sensor wie die Cinema-Line FX3, kostet aber nur die Hälfte. Die Hintergrundunschärfe (Bokeh) ist echt und cremig.",
    
    "Its AI \"Auto Framing\" feature can digitally Crop in to follow you around the room as if you have a\n              Kameraman. The best low-light performance of any consumer Kamera, period.":
        "Die KI-Funktion \"Auto Framing\" kann dich digital verfolgen, während du dich im Raum bewegst – als hättest du einen Kameramann. Die beste Schwachlichtleistung aller Consumer-Kameras, Punkt.",
    
    # Sony Specs
    "AI Merkmale": "KI-Funktionen",
    "Auto Framing": "Automatische Bildausrichtung",
    "Interchangeable": "Wechselbar",
    
    # Sony Pros/Cons
    "Insane low-light capability": "Wahnsinnige Schwachlichtfähigkeit",
    "Cinematic Vollformat look": "Filmreifer Vollformat-Look",
    "Advanced AI Stabilisierung and framing": "Fortschrittliche KI-Stabilisierung und Bildausrichtung",
    "Product Showcase mode (instant focus switch)": "Produkt-Präsentationsmodus (sofortiger Fokuswechsel)",
    "Expensive body and lenses": "Teures Gehäuse und Objektive",
    "Can overheat in 4K60 if not careful": "Kann bei 4K60 überhitzen, wenn nicht aufgepasst wird",
    "Single SD card slot": "Einzelner SD-Kartensteckplatz",
    
    # GoPro Section
    "Sometimes vlogging is dangerous. For surfing, skiing, or just bad weather, the Hero 13 is indestructible.\n              HyperSmooth 7.0 is like magic—it keeps the horizon level even if you spin the Kamera 360 degrees.":
        "Manchmal ist Vloggen gefährlich. Beim Surfen, Skifahren oder bei schlechtem Wetter ist die Hero 13 unzerstörbar. HyperSmooth 7.0 ist wie Magie – es hält den Horizont gerade, selbst wenn du die Kamera um 360 Grad drehst.",
    
    "The front screen helps you frame shots, and the new 10-Bit color options allow for serious Farbkorrektur\n              if you're a pro editor.":
        "Der Frontbildschirm hilft beim Bildaufbau, und die neuen 10-Bit-Farboptionen ermöglichen ernsthafte Farbkorrektur, wenn du ein Profi-Editor bist.",
    
    # GoPro Specs
    "Front + Back": "Vorne + Hinten",
    
    # GoPro Pros/Cons
    "Indestructible and waterproof": "Unzerstörbar und wasserdicht",
    "Widest field of view (großartig for POV)": "Weitestes Sichtfeld (großartig für POV)",
    "Horizon Lock is a game changer": "Horizontsperre ist ein Game-Changer",
    "Small enough to mount anywhere": "Klein genug zum Montieren überall",
    "Low light performance works, but is noisy": "Schwachlichtleistung funktioniert, aber ist verrauscht",
    "Audio needs wind protection (Media Mod recommended)": "Audio braucht Windschutz (Media Mod empfohlen)",
    "Fixed focus (can't do blurry backgrounds)": "Festfokus (keine unscharfen Hintergründe möglich)",
    
    # Essentials Section
    "Vlogging Essentials 101": "Vlogging-Grundlagen 101",
    "Audio > Video": "Audio > Video",
    "People will watch blurry 720p Video if the story is gut, but they will click away instantly if the audio\n            is scratchy. Invest in a mic.":
        "Leute schauen unscharfes 720p-Video, wenn die Geschichte gut ist, aber sie klicken sofort weg bei kratzigem Audio. Investiere in ein Mikrofon.",
    "Lighting": "Beleuchtung",
    "A 50 € ring light or simply facing a window makes a bigger difference than upgrading from a 500 € Kamera to a\n            2000 € Kamera.":
        "Ein 50 € Ringlicht oder einfach dem Fenster zugewandt sein macht einen größeren Unterschied als ein Upgrade von einer 500 € Kamera auf eine 2000 € Kamera.",
}

# ============================================================================
# TRANSLATIONS FOR BESTE-BUDGET-KAMERA.HTML
# ============================================================================

BUDGET_TRANSLATIONS = {
    # Title and Hero
    "Best Budget Camera Under 800 € (2026)": "Beste Budget-Kamera unter 800 € (2026)",
    "Contrary to popular belief, you don't need 3.000 € to take professionell Fotos. These cameras offer 90% of the image quality for 20% of the price.":
        "Entgegen der landläufigen Meinung brauchst du keine 3.000 €, um professionelle Fotos zu machen. Diese Kameras bieten 90% der Bildqualität für 20% des Preises.",
    
    # Table headers
    "MODELLL": "MODELL",
    "AUFLÖSUNG": "AUFLÖSUNG",
    "OBJEKTIVANSCHLUSS": "OBJEKTIVANSCHLUSS",
    "DSLR Style": "DSLR-Stil",
    "Compact": "Kompakt",
    
    # Phrases in content
    "This is currently the cheapest spiegellos Kamera on the market that includes a Sucher. It strips away":
        "Das ist derzeit die günstigste spiegellose Kamera auf dem Markt mit Sucher. Sie verzichtet auf",
    
    "It uses the same 24MP sensor found in much more teuer Canon Kameras, meaning your Fotos will look":
        "Sie nutzt den gleichen 24MP-Sensor wie in viel teureren Canon-Kameras, was bedeutet, dass deine Fotos",
}

# ============================================================================
# TRANSLATIONS FOR BESTE-REISEKAMERA.HTML
# ============================================================================

REISE_TRANSLATIONS = {
    "The golden rule of Reise photography: the best Kamera is the one you actually carry. We picked Kameras that pack pro image quality into bodies small enough for a jacket pocket.":
        "Die goldene Regel der Reisefotografie: Die beste Kamera ist die, die du tatsächlich dabei hast. Wir haben Kameras ausgewählt, die Profi-Bildqualität in Gehäuse packen, die klein genug für die Jackentasche sind.",
    
    "All-Rounder": "Allrounder",
    "Street / City": "Straße / Stadt",
    "Landscape / Hike": "Landschaft / Wandern",
    "Exchangeable Objektiv": "Wechselobjektiv",
    "Fixed Objektiv": "Festobjektiv",
}

# ============================================================================
# TRANSLATIONS FOR BESTE-ACTION-360-KAMERA.HTML
# ============================================================================

ACTION_TRANSLATIONS = {
    "✨ BESTE 360 KAMERA": "✨ BESTE 360-KAMERA",
    "POV Video": "POV-Video",
    "360 / Creative": "360 / Kreativ",
    "Schwachlicht": "Schwachlicht",
    "Check Preis on Amazon →": "Preis auf Amazon prüfen →",
    
    "The X4 solves the biggest problem with 360 Video: sharpness. With 8K resolution, when you reframe (Crop) into a standard 16:9 Video, it actually looks crisp and 4K-ish.":
        "Die X4 löst das größte Problem bei 360-Video: die Schärfe. Mit 8K-Auflösung sieht dein Video beim Umrahmen (Crop) auf Standard 16:9 tatsächlich scharf und 4K-mäßig aus.",
    
    'The "Invisible Selfie Stick" effect is pure magic. It automatically stitches out the stick, making it look like a drone is following you 3 feet away. It\'s the ultimate tool for solo Reisers and motorcycle riders.':
        'Der "Unsichtbare Selfie-Stick" Effekt ist pure Magie. Er blendet den Stick automatisch aus, sodass es aussieht, als würde eine Drohne dir in 1 Meter Abstand folgen. Das ultimative Werkzeug für Solo-Reisende und Motorradfahrer.',
    
    "PROTECTION": "SCHUTZ",
    "REFRAMING": "UMRAHMUNG",
    "Removable Guards": "Abnehmbare Schutzvorrichtungen",
    "AI App Driven": "KI-App-gesteuert",
}

def apply_translations(file_path: Path, translations: dict) -> int:
    """Apply translations to a file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    count = 0
    
    for en, de in translations.items():
        if en in content:
            content = content.replace(en, de)
            count += 1
    
    if content != original:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
    
    return count

def main():
    print("="*60)
    print("DIRECT GERMAN TRANSLATION FIX")
    print("="*60)
    
    # Fix beste-vlog-kamera.html
    vlog_file = DE_DIR / 'ratgeber' / 'beste-vlog-kamera.html'
    if vlog_file.exists():
        count = apply_translations(vlog_file, VLOG_TRANSLATIONS)
        print(f"✅ beste-vlog-kamera.html: {count} replacements")
    
    # Fix beste-budget-kamera-unter-800.html
    budget_file = DE_DIR / 'ratgeber' / 'beste-budget-kamera-unter-800.html'
    if budget_file.exists():
        count = apply_translations(budget_file, BUDGET_TRANSLATIONS)
        print(f"✅ beste-budget-kamera-unter-800.html: {count} replacements")
    
    # Fix beste-reisekamera.html
    reise_file = DE_DIR / 'ratgeber' / 'beste-reisekamera.html'
    if reise_file.exists():
        count = apply_translations(reise_file, REISE_TRANSLATIONS)
        print(f"✅ beste-reisekamera.html: {count} replacements")
    
    # Fix beste-action-360-kamera.html
    action_file = DE_DIR / 'ratgeber' / 'beste-action-360-kamera.html'
    if action_file.exists():
        count = apply_translations(action_file, ACTION_TRANSLATIONS)
        print(f"✅ beste-action-360-kamera.html: {count} replacements")
    
    print("\n" + "="*60)
    print("COMPLETE")
    print("="*60)

if __name__ == '__main__':
    main()
