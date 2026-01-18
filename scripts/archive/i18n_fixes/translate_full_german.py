#!/usr/bin/env python3
"""
Complete German Translation Script V2
Performs comprehensive sentence-level translation for all German pages.
"""

import re
from pathlib import Path
from typing import Dict, List, Tuple

BASE_DIR = Path(__file__).parent.parent.parent

# =============================================================================
# SENTENCE-LEVEL TRANSLATIONS (Longest first for safety)
# =============================================================================
SENTENCE_TRANSLATIONS: List[Tuple[str, str]] = [
    # ==========================================================================
    # NIKON Z8 TESTBERICHT
    # ==========================================================================
    # Hero
    ("The flagship killer. It takes everything großartig about the massive Z9 and shrinks it into a\n            bag-friendly body.",
     "Der Flaggschiff-Killer. Er bringt alles Großartige der massiven Z9 in ein handliches Format."),
    
    # Verdict
    ("The Nikon Z8 is essentially a \"baby Z9.\" It has no mechanical shutter because it doesn't need one—the\n              sensor readout is instantly fast.",
     "Die Nikon Z8 ist im Wesentlichen eine \"kleine Z9\". Sie hat keinen mechanischen Verschluss – der Sensor ist blitzschnell."),
    ("For pros who switch between high-res Hochzeit Porträts and 8K Video, this is the ultimate hybrid. It's\n              bigger than a Sony A7 IV but feels incredibly balanced with pro lenses.",
     "Für Profis, die zwischen hochauflösenden Hochzeitsporträts und 8K-Video wechseln, ist dies die ultimative Hybrid-Kamera. Sie ist größer als eine Sony A7 IV, fühlt sich aber mit Profi-Objektiven unglaublich ausgewogen an."),
    
    # Pros
    ("Zero Rolling Shutter (thanks to stacked sensor)", "Kein Rolling Shutter (dank Stacked-Sensor)"),
    ("Internal 12-bit RAW Video recording (N-RAW)", "Interne 12-Bit RAW-Videoaufnahme (N-RAW)"),
    ("Unglaublich 45.7MP still image quality", "Unglaubliche 45,7MP Standbildqualität"),
    ("Pre-Release Capture ensures you never miss a moment", "Vorab-Aufnahme stellt sicher, dass Sie keinen Moment verpassen"),
    
    # Cons
    ("Akku life is just average (smaller EN-EL15c)", "Akkulaufzeit nur durchschnittlich (kleinerer EN-EL15c)"),
    ("Can get warm during extended 8K recording", "Kann bei längerer 8K-Aufnahme warm werden"),
    ("Still heavy compared to Sony/Canon spiegellos", "Immer noch schwer im Vergleich zu Sony/Canon spiegellos"),
    
    # Performance Section
    ("Nikon has caught up. The 3D Tracking is sticky and zuverlässig for fast Sport and Wildlife. It recognizes\n            people, dogs, cats, birds, planes, trains, and automobiles instantly.",
     "Nikon hat aufgeholt. Das 3D-Tracking ist präzise und zuverlässig für schnellen Sport und Wildlife. Es erkennt Menschen, Hunde, Katzen, Vögel, Flugzeuge, Züge und Autos sofort."),
    ("This is one of the few Kameras that shoots 8K 60p N-RAW internally. The Material is malleable and stunning.\n            For most users, the 4K 120p is the sweet spot for buttery smooth Zeitlupe.",
     "Dies ist eine der wenigen Kameras, die intern 8K 60p N-RAW aufnimmt. Das Material ist flexibel und atemberaubend. Für die meisten Nutzer ist 4K 120p der Sweet Spot für butterweiche Zeitlupe."),
    ("This is a Kamera for working pros. The grip fits your whole hand, the buttons are backlit for night work,\n            and the screen tilts 4 ways (including vertical tilt) which Porträt shooters love.",
     "Dies ist eine Kamera für arbeitende Profis. Der Griff passt in die ganze Hand, die Tasten sind für Nachtarbeit beleuchtet, und der Bildschirm neigt sich in 4 Richtungen (inkl. vertikaler Neigung), was Porträtfotografen lieben."),
    
    # Affiliate/Partner disclaimer
    ("links, which keeps this site ad-free.", "Links nutzen, was diese Website werbefrei hält."),
    
    # FAQ Questions
    ("Is the Z8 worth the extra cost over the Z6 III?", "Lohnt sich der Aufpreis der Z8 gegenüber der Z6 III?"),
    ("How does the Z8 compare to the Sony A1?", "Wie schneidet die Z8 im Vergleich zur Sony A1 ab?"),
    ("What Z-mount lenses are essential for the Z8?", "Welche Z-Mount-Objektive sind für die Z8 unverzichtbar?"),
    ("Does the Z8 overheat during long recording sessions?", "Überhitzt die Z8 bei langen Aufnahmesessions?"),
    ("Can I use this for Wildlife photography?", "Kann ich diese für Wildlife-Fotografie nutzen?"),
    
    # FAQ Answers
    ("If you shoot professionell Sport, Wildlife, or events—yes. The Z8 has 45MP (vs 24MP), faster burst speeds, 8K Video, and dual CFexpress slots. The Z6 III is ausgezeichnet for most users, but the Z8's resolution and speed justify the price for demanding work.",
     "Wenn Sie professionell Sport, Wildlife oder Events fotografieren – ja. Die Z8 hat 45MP (vs 24MP), schnellere Serienbildgeschwindigkeit, 8K-Video und duale CFexpress-Slots. Die Z6 III ist ausgezeichnet für die meisten Nutzer, aber die Auflösung und Geschwindigkeit der Z8 rechtfertigen den Preis für anspruchsvolle Arbeit."),
    ("They're extremely close. The Z8 is 1500 € cheaper, has better Ergonomie, and superior Akkulaufzeit. The A1 has a slight edge in Autofokus refinement and Objektivauswahl. Both are class-leading hybrid Kameras—choose based on Objektiv Ökosystem. If you're already in Nikon glass, the Z8 is a no-brainer.",
     "Sie sind extrem nah beieinander. Die Z8 ist 1500 € günstiger, hat bessere Ergonomie und längere Akkulaufzeit. Die A1 hat einen leichten Vorteil bei Autofokus-Feinheit und Objektivauswahl. Beide sind klassenführende Hybrid-Kameras – wählen Sie nach Objektiv-Ökosystem. Wenn Sie bereits Nikon-Glas haben, ist die Z8 die klare Wahl."),
    ("Start with the 24-120mm f/4 S for versatility, or the 24-70mm f/2.8 S if you need f/2.8. For Sport/Wildlife, the 100-400mm f/4.5-5.6 VR S is phenomenal. The 50mm f/1.8 S is cheap and tack-sharp. Avoid adapted F-mount lenses—native Z glass unlocks the Kamera's full potential.",
     "Starten Sie mit dem 24-120mm f/4 S für Vielseitigkeit, oder dem 24-70mm f/2.8 S wenn Sie f/2.8 brauchen. Für Sport/Wildlife ist das 100-400mm f/4.5-5.6 VR S phänomenal. Das 50mm f/1.8 S ist günstig und messerscharf. Vermeiden Sie adaptierte F-Mount-Objektive – native Z-Optik erschließt das volle Potenzial der Kamera."),
    ("Nikon engineered ausgezeichnet heat dissipation. With the latest firmware, you can record 8K for 90+ Minuten continuously. In 4K60, Überhitzung is essentially a non-issue. The fanless design stays silent, making it perfect for interviews and quiet environments.",
     "Nikon hat exzellente Wärmeableitung konstruiert. Mit der neuesten Firmware können Sie 8K über 90 Minuten durchgehend aufnehmen. In 4K60 ist Überhitzung praktisch kein Thema. Das lüfterlose Design bleibt leise – perfekt für Interviews und ruhige Umgebungen."),
    ("The 20fps RAW burst, pre-release capture, and subject detection (birds, animals) are unglaublich. Pair it with the 180-600mm f/5.6-6.3 VR or the 400mm f/4.5 S for reach. File management is critical—invest in dual 256GB CFexpress cards minimum.",
     "Der 20fps RAW-Burst, die Vorab-Aufnahme und die Motiverkennung (Vögel, Tiere) sind unglaublich. Kombinieren Sie sie mit dem 180-600mm f/5.6-6.3 VR oder dem 400mm f/4.5 S für Reichweite. Datei-Management ist entscheidend – investieren Sie in mindestens zwei 256GB CFexpress-Karten."),
    
    # ==========================================================================
    # ACTION 360 KAMERA (from before)
    # ==========================================================================
    ("Shoot first, frame later. Modern 360 Kameras capture every angle at once, so you never miss a moment. Action\n            cams are tougher, sharper, and steadier than ever.",
     "Erst filmen, dann einrahmen. Moderne 360-Kameras erfassen jeden Winkel gleichzeitig – so verpasst du keinen Moment. Action-Kameras sind robuster, schärfer und stabiler als je zuvor."),
    ("The X4 solves the biggest problem with 360 Video: sharpness. With 8K resolution, when you reframe (Crop) into a standard 16:9 Video, it actually looks crisp and 4K-ish.",
     "Die X4 löst das größte Problem von 360-Videos: die Schärfe. Mit 8K-Auflösung sieht das Bild beim Zuschneiden auf 16:9 tatsächlich scharf und 4K-artig aus."),
    ("The \"Invisible Selfie Stick\" effect is pure magic. It automatically stitches out the stick, making it look like a drone is following you 3 feet away. It's the ultimate tool for solo Reiseers and motorcycle riders.",
     "Der \"unsichtbare Selfie-Stick\"-Effekt ist pure Magie. Der Stab wird automatisch herausgerechnet – es sieht aus, als würde eine Drohne dir in 1 Meter Entfernung folgen. Das ultimative Werkzeug für Solo-Reisende und Motorradfahrer."),
    ("For traditional POV (point of view) action—mountain biking, surfing, skiing—GoPro is still the king. The chassis is proven tough, and the mounting system (fingers) is universal.",
     "Für klassische POV-Action (Point of View) – Mountainbiken, Surfen, Skifahren – ist GoPro nach wie vor der König. Das Gehäuse ist bewährt robust, und das Befestigungssystem (Fingers) ist universell."),
    ("The 8:7 aspect ratio sensor is brilliant. It shoots a nearly square image, allowing you to Crop a vertical Video for Instagram and a horizontal Video for YouTube from the exact same file.",
     "Der Sensor im 8:7-Seitenverhältnis ist brillant. Er nimmt ein fast quadratisches Bild auf, sodass du aus derselben Datei ein vertikales Video für Instagram und ein horizontales für YouTube schneiden kannst."),
    ("While GoPro owns the daylight, DJI owns the night (and the water). The Action 5 Profi has a larger 1/1.3\" sensor that gathers way more light, making your evening Material look clean rather than muddy.",
     "Während GoPro den Tag beherrscht, gehört die Nacht (und das Wasser) DJI. Die Action 5 Pro hat einen größeren 1/1.3\"-Sensor, der viel mehr Licht einfängt – dein Abendmaterial sieht sauber aus statt matschig."),
    ("It's also waterproof down to 20 meters <em>without</em> a case (GoPro is only 10m). The magnetic mounting system is faster and less annoying than GoPro's screw mount.",
     "Sie ist außerdem bis 20 Meter wasserdicht <em>ohne</em> Gehäuse (GoPro nur 10m). Das Magnetbefestigungssystem ist schneller und praktischer als GoPros Schraubhalterung."),
    
    # Section Headers
    ("360 vs Action: Which one?", "360 vs Action: Welche passt zu dir?"),
    ("Get 360 If...", "Wähle 360, wenn..."),
    ("Get Action If...", "Wähle Action, wenn..."),
    ("You want unique angles (like the drone shot) or if you are terrible at framing your subject. It captures everything, so you can't miss.",
     "Du einzigartige Blickwinkel willst (wie den Drohnen-Shot) oder schlecht im Bildausschnitt bist. Sie erfasst alles – du kannst nichts verpassen."),
    ("You want the highest quality Video (4K/5.3K sharp) and simplicity. You just hit record and go, no editing or reframing required.",
     "Du die höchste Videoqualität (4K/5.3K scharf) und Einfachheit willst. Einfach aufnehmen und los – kein Nachbearbeiten oder Zuschneiden nötig."),
    
    # Action 360 Pros/Cons
    ("8K resolution makes reframed Material usable", "8K-Auflösung macht zugeschnittenes Material nutzbar"),
    ("Magic \"Third Person View\" (Drone Shot)", "Magische \"Third-Person-Ansicht\" (Drohnen-Shot)"),
    ("Unglaublich mobile app for easy editing", "Unglaubliche mobile App für einfaches Bearbeiten"),
    ("Removable Objektiv guards (finally!)", "Abnehmbare Objektivschutzkappen (endlich!)"),
    ("Physically larger/heavier than older models", "Physisch größer/schwerer als ältere Modelle"),
    ("Low light performance is still grainy", "Schwachlichtleistung ist immer noch körnig"),
    ("Requires a powerful phone/PC to edit 8K", "Benötigt ein leistungsstarkes Handy/PC für 8K-Bearbeitung"),
    ("Industry standard mounting Ökosystem", "Industriestandard-Befestigungssystem"),
    ("Square sensor allows vertical+horizontal Crop", "Quadratischer Sensor ermöglicht vertikalen+horizontalen Zuschnitt"),
    ("GPS telemetry overlays (speed, altitude)", "GPS-Telemetrie-Overlays (Geschwindigkeit, Höhe)"),
    ("Compatible with Max Objektiv Mod for ultra-wide field", "Kompatibel mit Max Lens Mod für ultraweites Sichtfeld"),
    ("Overheats if static (needs airflow)", "Überhitzt bei Stillstand (braucht Luftstrom)"),
    ("Touch screen can be finicky when wet", "Touchscreen reagiert bei Nässe unzuverlässig"),
    ("Akku life in cold isn't perfect", "Akkulaufzeit bei Kälte nicht optimal"),
    ("Beste low-light image quality in class", "Beste Schwachlicht-Bildqualität der Klasse"),
    ("Deeper waterproofing (20m)", "Tiefere Wasserdichtigkeit (20m)"),
    ("Magnetic mount is extremely convenient", "Magnethalterung ist extrem praktisch"),
    ("Color temperature sensor for accurate underwater color", "Farbtemperatursensor für akkurate Unterwasserfarben"),
    ("Stabilisierung crops in slightly more than GoPro", "Stabilisierung beschneidet etwas mehr als GoPro"),
    ("Smaller accessory Ökosystem", "Kleineres Zubehör-Ökosystem"),
    ("Auflösung tops out at 4K (GoPro does 5.3K)", "Auflösung maximal 4K (GoPro schafft 5.3K)"),
    
    # Badges
    ("The King of POV", "Der König des POV"),
    ("🏄‍♂️ The King of POV", "🏄‍♂️ Der König des POV"),
    
    # Spec Labels
    ("Protection", "Schutz"),
    ("Removable Guards", "Abnehmbare Schutzkappen"),
    ("AI App Driven", "KI-App-gesteuert"),
    ("135 Minutes", "135 Minuten"),
    ("4 Hours (Max)", "4 Stunden (Max)"),
    ("Magnetic Quick", "Magnetisch Schnell"),
    ("Max Objektiv Mod 2.0", "Max Lens Mod 2.0"),
    ("20m ( Deep)", "20m (tief)"),
    
    # Button text
    ("Check Preis on Amazon", "Preis auf Amazon prüfen"),
    ("Check Preis", "Preis prüfen"),
    
    # Meta/Schema
    ("Capture everything. The best action Kameras and 360 Kameras for Sport, Reise, and creative reframing from GoPro, Insta360, and DJI.",
     "Alles erfassen. Die besten Action- und 360-Kameras für Sport, Reisen und kreatives Reframing von GoPro, Insta360 und DJI."),
    ("Action/360 cams with großartig Stabilisierung, horizon lock, and easy reframing.",
     "Action-/360-Kameras mit großartiger Stabilisierung, Horizontsperre und einfachem Reframing."),
    ("Top-Empfehlungen for Adventure", "Top-Empfehlungen für Abenteuer"),
    ("Kamera Testbericht Experts", "Kamera-Testbericht-Experten"),
    ("Professionell Fotografs and Videographers with 10+ years of experience testing Kameras, lenses, and accessories.",
     "Professionelle Fotografen und Videografen mit über 10 Jahren Erfahrung im Testen von Kameras, Objektiven und Zubehör."),
    
    # Table headers
    ("Waterproof", "Wasserdicht"),
    ("Modelllllll", "Modell"),
    
    # Comparison pages
    ("Bottom line", "Fazit"),
    ("Who should buy each", "Wer sollte welche kaufen"),
    ("Shop X-T5", "X-T5 kaufen"),
    ("Shop X-S20", "X-S20 kaufen"),
    ("Beste deal", "Bestes Angebot"),
    ("This page may contain affiliate links. If you buy through them, we may earn a small commission at no extra",
     "Diese Seite kann Affiliate-Links enthalten. Wenn Sie über diese kaufen, erhalten wir möglicherweise eine kleine Provision ohne zusätzliche"),
    ("cost to you.", "Kosten für Sie."),
    ("Key Features", "Hauptmerkmale"),
]

# =============================================================================
# WORD-LEVEL TRANSLATIONS (fallback)
# =============================================================================
WORD_TRANSLATIONS: Dict[str, str] = {
    # Headings
    "Key Features": "Hauptmerkmale",
    "Features": "Merkmale",
    "Specifications": "Spezifikationen",
    "Overview": "Überblick",
    "Summary": "Zusammenfassung",
    "The Bottom Line": "Das Fazit",
    "Bottom Line": "Fazit",
    "Who Should Buy": "Wer sollte kaufen",
    "Who Should": "Wer sollte",
    "Final Verdict": "Endgültiges Urteil",
    
    # Buttons
    "Check Price": "Preis prüfen",
    "Buy Now": "Jetzt kaufen",
    "Buy": "Kaufen",
    "View on Amazon": "Auf Amazon ansehen",
    
    # Labels
    "Reviews": "Testberichte",
    "Guides": "Ratgeber",
    "Battery": "Akku",
    "Resolution": "Auflösung",
    "Lens": "Objektiv",
    "Mount": "Halterung",
    "Reframing": "Zuschneiden",
    "Ecosystem": "Ökosystem",
    "Weight": "Gewicht",
    "Camera": "Kamera",
    "Pros": "Vorteile",
    "Cons": "Nachteile",
    "Autofocus": "Autofokus",
    "Review": "Testbericht",
    "Guide": "Ratgeber",
    
    # Time units
    "minutes": "Minuten",
    "Hours": "Stunden",
    "Deep": "tief",
    "Quick": "Schnell",
}


def translate_file(file_path: Path) -> bool:
    """Apply comprehensive translations to a single file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # 1. Apply sentence translations (longest first)
    for en, de in SENTENCE_TRANSLATIONS:
        content = content.replace(en, de)
    
    # 2. Apply word translations with word boundaries for short words
    for en, de in WORD_TRANSLATIONS.items():
        # For short words, use regex to avoid matching in class names, URLs, etc.
        if len(en) <= 6:
            # Only replace if it looks like visible text (after > or before <)
            content = re.sub(r'(?<=>)' + re.escape(en) + r'(?=<)', de, content)
            content = re.sub(r'(?<=>)\s*' + re.escape(en) + r'\s*(?=</)', de, content)
        else:
            content = content.replace(en, de)
    
    if content != original:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False


def main():
    de_dir = BASE_DIR / 'de'
    
    print("Applying comprehensive German translations...")
    
    updated = 0
    for html_file in de_dir.rglob('*.html'):
        if translate_file(html_file):
            print(f"  ✓ {html_file.name}")
            updated += 1
    
    print(f"\nUpdated {updated} files.")


if __name__ == '__main__':
    main()
