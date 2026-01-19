#!/usr/bin/env python3
"""
German Translation Fix - Version 4
Fixing remaining content in budget and hybrid guides
"""

from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent

# Budget Guide Translations
BUDGET_TRANSLATIONS = {
    # Hero section
    "to take professionell Fotos. These Kameras offer 90% of":
        ", um professionelle Fotos zu machen. Diese Kameras bieten 90% der",
    
    # Canon R100 section
    "💰 Cheapest Option": "💰 Günstigste Option",
    "identical to those from a 1.000 € body. Ideally suited for students who strictly want to learn\n              photography.":
        "identisch mit denen eines 1.000-€-Gehäuses. Ideal geeignet für Studenten, die rein Fotografie lernen wollen.",
    "Fixed (Non-Touch)": "Fest (Kein Touchscreen)",
    "Eye Detection": "Augenerkennung",
    "Unglaublich image quality for the price": "Unglaubliche Bildqualität für den Preis",
    "Kompakt and lightweight": "Kompakt und leicht",
    "Includes an electronic Sucher (EVF)": "Inklusive elektronischem Sucher (EVF)",
    "Großartig Canon colors": "Großartige Canon-Farben",
    "Display is fixed and not a Touchscreen": "Display ist fest und kein Touchscreen",
    "4K Video has a heavy Crop & bad Autofokus": "4K-Video hat starken Crop und schlechten Autofokus",
    "Uses older, slower technology": "Verwendet ältere, langsamere Technik",
    
    # Sony ZV-E10 section  
    "You get 4K\n              Video, a fully":
        "Du bekommst 4K-Video, einen voll",
    "It tracks eyes and faces\n              reliably, making it the perfect Budget hybrid for YouTubers who also take Fotos.":
        "Er verfolgt Augen und Gesichter zuverlässig und macht sie zum perfekten Budget-Hybrid für YouTuber, die auch fotografieren.",
    "Access to erschwinglich Sigma/Tamron lenses": "Zugang zu erschwinglichen Sigma/Tamron-Objektiven",
    
    # Panasonic G100D section
    "📸 Tiny Hybrid": "📸 Winziger Hybrid",
    "It uses the smaller Micro Four Thirds sensor, which allows\n              the Kamera and lenses to be incredibly portable. It has a beautiful, bright electronic\n              Sucher—something the Sony ZV-E10 lacks.":
        "Sie nutzt den kleineren Micro-Four-Thirds-Sensor, wodurch Kamera und Objektive unglaublich tragbar sind. Sie hat einen wunderschönen, hellen elektronischen Sucher – etwas, das der Sony ZV-E10 fehlt.",
    "oft\n              overlooked option for Reise vlogging on a shoestring Budget.":
        "oft übersehene Option für Reise-Vlogging mit kleinem Budget.",
    
    # Budget tips section
    "Kaufen Used to Save 30%": "Gebraucht kaufen und 30% sparen",
    "Kameras are durable. Kaufening a used \"Like New\" body from reputable dealers like MPB or KEH is the\n            smartest\n            way to stretch your Budget.":
        "Kameras sind langlebig. Ein gebrauchtes \"Wie Neu\"-Gehäuse von seriösen Händlern wie MPB oder KEH zu kaufen ist der cleveste Weg, dein Budget zu strecken.",
    "Kit Objektiv is Fine": "Kit-Objektiv ist in Ordnung",
    "Don't stress about teuer lenses yet. The 18-50mm (or similar) Kit-Objektiv that comes with these Kameras is\n            perfect for learning the basics.":
        "Mach dir noch keinen Stress wegen teurer Objektive. Das 18-50mm (oder ähnliche) Kit-Objektiv, das mit diesen Kameras kommt, ist perfekt zum Erlernen der Grundlagen.",
}

# Hybrid Guide Translations
HYBRID_TRANSLATIONS = {
    # Hero section
    "These hybrid workhorses deliver 33MP+ high-resolution Fotos for clients and\n            10-Bit 4K Video for YouTube, all in a single body.":
        "Diese Hybrid-Arbeitstiere liefern 33MP+ hochauflösende Fotos für Kunden und 10-Bit 4K Video für YouTube, alles in einem einzigen Gehäuse.",
    
    # Sony A7 IV section
    "With a 33MP sensor, it offers significantly more cropping\n              room for Fotos than its 24MP rivals.":
        "Mit einem 33MP-Sensor bietet sie deutlich mehr Zuschneidespielraum für Fotos als ihre 24MP-Rivalen.",
    "It has a huge Ökosystem of Objektive von Drittanbietern from Sigma, Tamron, and Samyang, making it the most\n              erschwinglich system to build long-term.":
        "Sie hat ein riesiges Ökosystem an Drittanbieter-Objektiven von Sigma, Tamron und Samyang, was sie zum erschwinglichsten System für den langfristigen Aufbau macht.",
    
    # Panasonic S5II section
    "The S5II uses Phasen-AF (PDAF), making it zuverlässig for solo\n              shooters.":
        "Die S5II nutzt Phasen-AF (PDAF), was sie zuverlässig für Solo-Filmer macht.",
    "Why does that matter? It allows you to Crop a vertical 9:16 (TikTok) and a horizontal 16:9 (YouTube) Video\n              from the <em>same clip</em> without losing quality.":
        "Warum ist das wichtig? Es erlaubt dir, ein vertikales 9:16 (TikTok) und ein horizontales 16:9 (YouTube) Video aus dem <em>selben Clip</em> ohne Qualitätsverlust zuzuschneiden.",
    
    # Canon R6 II section
    "The R6 Mark II schießt atemberaubende 40 Bilder pro Sekunde elektronisch. It's a monster for\n              Sport and Wildlife. For Video, it's the only Kamera in this price range that shoots 4K 60p using the\n              <em>full width</em> of the sensor (no Crop).":
        "Die R6 Mark II schießt atemberaubende 40 Bilder pro Sekunde elektronisch. Sie ist ein Monster für Sport und Wildlife. Für Video ist sie die einzige Kamera in dieser Preisklasse, die 4K 60p mit der <em>vollen Breite</em> des Sensors aufnimmt (kein Crop).",
    "It's a pure joy to use if\n              you prioritize speed and usability.":
        "Es ist eine pure Freude, sie zu benutzen, wenn du Geschwindigkeit und Bedienbarkeit priorisierst.",
    
    # Buying tips
    "If you choose Sony, you get cheap Objektive von Drittanbietern. If you choose Canon, you get teuer but brilliant\n            proprietary lenses. Choose the system, not just the body.":
        "Wenn du Sony wählst, bekommst du günstige Drittanbieter-Objektive. Wenn du Canon wählst, bekommst du teure, aber brillante hauseigene Objektive. Wähle das System, nicht nur das Gehäuse.",
    "24MP is plenty for 4K Video and social media. Only pay extra for the Sony A7 IV's 33MP if you Crop heavily\n            or print huge billboards.":
        "24MP reichen für 4K-Video und Social Media völlig aus. Zahle nur den Aufpreis für die 33MP der Sony A7 IV, wenn du stark zuschneidest oder riesige Plakate druckst.",
}

# Comparison Page Translations
COMPARISON_TRANSLATIONS = {
    "Beste for": "Beste für",
    "you're okay with a tilt screen": "du mit einem Neigungsbildschirm okay bist",
    "Solid for long takes": "Solide für lange Aufnahmen",
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
    print("🇩🇪 German Translation Fix v4\n")
    de_dir = BASE_DIR / 'de'
    total = 0
    
    # Budget guide
    c = apply_all(de_dir / 'ratgeber' / 'beste-budget-kamera-unter-800.html', BUDGET_TRANSLATIONS)
    if c: print(f"✅ beste-budget-kamera-unter-800.html: {c} translations")
    total += c
    
    # Hybrid guide
    c = apply_all(de_dir / 'ratgeber' / 'beste-hybrid-kamera.html', HYBRID_TRANSLATIONS)
    if c: print(f"✅ beste-hybrid-kamera.html: {c} translations")
    total += c
    
    # Comparison pages
    for comp_file in (de_dir / 'vergleiche').glob('*.html'):
        c = apply_all(comp_file, COMPARISON_TRANSLATIONS)
        if c: print(f"✅ {comp_file.name}: {c} translations")
        total += c
    
    print(f"\n{'='*50}")
    print(f"✨ Total: {total} translations applied")

if __name__ == '__main__':
    main()
