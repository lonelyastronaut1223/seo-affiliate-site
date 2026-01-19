#!/usr/bin/env python3
"""
German Translation Fix - Version 6 (Complete Review Pages)
Comprehensive translation of all remaining English content in review pages
"""

from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent

# ============================================================================
# DJI OSMO POCKET 3 REVIEW - COMPLETE TRANSLATION
# ============================================================================
DJI_COMPLETE = {
    # Hero Section
    "The ultimate vlogging tool. A 1-inch sensor, mechanical Stabilisierung, and a rotating":
        "Das ultimative Vlogging-Werkzeug. Ein 1-Zoll-Sensor, mechanische Stabilisierung und ein drehbarer",
    
    # Badge
    "🏆 Beste for Vlogging": "🏆 Beste für Vlogging",
    
    # Verdict paragraphs
    "The DJI Osmo Pocket 3 is a masterpiece of engineering. It puts a massive":
        "Der DJI Osmo Pocket 3 ist ein Meisterwerk der Ingenieurskunst. Er packt einen massiven",
    "in einen winzigen Gimbal-Griff.":
        "in einen winzigen Gimbal-Griff.",
    "The low-light performance blows action Kameras out of the water, and the mechanical Gimbal is far smoother":
        "Die Schwachlichtleistung stellt Action-Kameras in den Schatten, und der mechanische Gimbal ist viel flüssiger",
    "than electronic Stabilisierung. The snappy <strong>rotatable screen</strong> makes vertical social content":
        "als elektronische Stabilisierung. Der schnelle <strong>drehbare Bildschirm</strong> macht vertikale Social-Media-Inhalte",
    "effortless.": "mühelos.",
    
    # Pros
    "Massive 1-inch sensor = großartig Schwachlicht quality": "Massiver 1-Zoll-Sensor = großartige Schwachlicht-Qualität",
    "Mechanical Gimbal is smoother than GoPro HyperSmooth": "Mechanischer Gimbal ist flüssiger als GoPro HyperSmooth",
    "Schnellste startup: Flip screen, shoot in 2 seconds": "Schnellster Start: Bildschirm drehen, in 2 Sekunden filmen",
    "Face tracking is incredibly sticky": "Gesichtsverfolgung ist unglaublich hartnäckig",
    
    # Cons
    "Not rugged or waterproof (needs a case)": "Nicht robust oder wasserdicht (braucht ein Gehäuse)",
    "Built-in mic is gut, but external mic is better for wind": "Eingebautes Mikrofon ist gut, aber externes ist besser bei Wind",
    "Festobjektiv Blende means you need ND filters": "Feste Objektivblende bedeutet, du brauchst ND-Filter",
    
    # Performance sections
    "The jump to a 1-inch sensor is massive. Night Material that would be mush on a phone or GoPro looks clean":
        "Der Sprung auf einen 1-Zoll-Sensor ist massiv. Nachtaufnahmen, die auf einem Handy oder GoPro matschig wären, sehen hier sauber",
    "and professionell here. Skin tones are natural and pleasing straight out of Kamera.":
        "und professionell aus. Hauttöne sind natürlich und ansprechend direkt aus der Kamera.",
    "Vertical Workflows": "Vertikale Arbeitsabläufe",
    "The rotating screen isn't just a gimmick. It physically rotates the UI and changes aspect ratio, making it":
        "Der drehbare Bildschirm ist kein Gimmick. Er dreht die Benutzeroberfläche physisch und ändert das Seitenverhältnis, was ihn",
    "the fastest way to switch between YouTube (16:9) and TikTok (9:16) shooting.":
        "zum schnellsten Weg macht, zwischen YouTube (16:9) und TikTok (9:16) Aufnahmen zu wechseln.",
    "Pair it with the DJI Mic 2 (which connects wirelessly without a receiver!) and you have a pro-level":
        "Kombiniere ihn mit dem DJI Mic 2 (das sich kabellos ohne Empfänger verbindet!) und du hast ein Profi-",
    "interview setup that fits in a jacket pocket.":
        "Interview-Setup, das in eine Jackentasche passt.",
    
    # FAQ Questions
    "Is the Pocket 3 enough to replace my Vlog Kamera?": "Kann der Pocket 3 meine Vlog-Kamera ersetzen?",
    "For 80% of Vloggers, yes.": "Für 80% der Vlogger, ja.",
    "The Gimbal Stabilisierung is unbeatable, and the 1-inch sensor handles":
        "Die Gimbal-Stabilisierung ist unschlagbar, und der 1-Zoll-Sensor meistert",
    "Schwachlicht well. You lose some creative control (no interchangeable lenses, fixed Blende), but the":
        "Schwachlicht gut. Du verlierst etwas kreative Kontrolle (keine Wechselobjektive, feste Blende), aber die",
    "convenience and Material quality are unglaublich. Keep a backup Kamera for specialty shots.":
        "Bequemlichkeit und Materialqualität sind unglaublich. Behalte eine Backup-Kamera für Spezialaufnahmen.",
    "Does it work well in Schwachlicht?": "Funktioniert er gut bei Schwachlicht?",
    "Better than any action Kamera or phone, but not as gut as Vollformat Kameras. The 1-inch sensor performs":
        "Besser als jede Action-Kamera oder Handy, aber nicht so gut wie Vollformat-Kameras. Der 1-Zoll-Sensor performt",
    "well up to ISO 3200. You'll see noise in dim restaurants or nighttime Streets, but it's totally usable.":
        "gut bis ISO 3200. Du siehst Rauschen in dunklen Restaurants oder nächtlichen Straßen, aber es ist völlig nutzbar.",
    "The ActiveTrack works even in Schwachlicht, which is beeindruckend.":
        "Das ActiveTrack funktioniert sogar bei Schwachlicht, was beeindruckend ist.",
    "Can I use it for professionell work?": "Kann ich ihn für professionelle Arbeit nutzen?",
    "Many professionells use it as a B-Kamera for BTS (behind-the-scenes), quick social media content, or":
        "Viele Profis nutzen ihn als B-Kamera für BTS (Behind-the-Scenes), schnelle Social-Media-Inhalte oder",
    "Gimbal shots. The 10-Bit D-Log M gives you gut Farbkorrektur flexibility. It won't replace an A7 IV for":
        "Gimbal-Aufnahmen. Das 10-Bit D-Log M gibt dir gute Farbkorrektur-Flexibilität. Er ersetzt keine A7 IV für",
    "client work, but it's an ausgezeichnet secondary tool that fits in your pocket.":
        "Kundenarbeit, aber er ist ein ausgezeichnetes Zweittool, das in deine Tasche passt.",
    "What accessories are essential?": "Welches Zubehör ist unverzichtbar?",
    "Get the DJI Mic 2 for wireless audio—it integrates seamlessly. The Weitwinkel Objektiv attachment adds":
        "Hol dir das DJI Mic 2 für kabelloses Audio – es integriert sich nahtlos. Der Weitwinkel-Objektivaufsatz fügt",
    "creative options. A wrist strap is a must (the Pocket 3 is slippery). Nachteileider the waterproof case if":
        "kreative Optionen hinzu. Ein Handschlaufe ist ein Muss (der Pocket 3 ist rutschig). Ziehe das wasserdichte Gehäuse in Betracht, wenn",
    "you shoot near water. Skip the ND filters unless you shoot in bright sunshine often.":
        "du in Wassernähe filmst. Überspringe die ND-Filter, es sei denn, du filmst oft in hellem Sonnenschein.",
}

# ============================================================================
# PANASONIC S5 II REVIEW - COMPLETE TRANSLATION
# ============================================================================
PANASONIC_COMPLETE = {
    # Hero Section
    "The Kamera that fixed Panasonic's biggest flaw. Finally with zuverlässig Autofokus, plus":
        "Die Kamera, die Panasonics größtes Manko behoben hat. Endlich mit zuverlässigem Autofokus, plus",
    
    # Badge
    "🎬 Beste for Filmmakers": "🎬 Beste für Filmemacher",
    
    # Verdict
    "For years, Panasonic Kameras had amazing Video specs but terrible Autofokus. The S5 II changed everything":
        "Jahrelang hatten Panasonic-Kameras tolle Video-Specs, aber schrecklichen Autofokus. Die S5 II hat alles verändert",
    "by adding **Phasen-AF**.":
        "durch Hinzufügen von **Phasen-AF**.",
    "It combines this new customized AF with the best In-Body Image Stabilisierung (IBIS) in the business. You":
        "Sie kombiniert diesen neuen angepassten AF mit der besten In-Body-Bildstabilisierung (IBIS) der Branche. Du",
    "can walk and talk without a Gimbal, and shoot 6K Video that looks like a cinema Kamera. For solo":
        "kannst gehen und sprechen ohne Gimbal und 6K-Video drehen, das wie eine Kinokamera aussieht. Für Solo-",
    "Filmemachers, this is the one to beat.":
        "Filmemacher ist dies die zu schlagende Kamera.",
    
    # Pros
    "Finally! Zuverlässig Phase Detect Autofokus": "Endlich! Zuverlässiger Phasenerkennungs-Autofokus",
    "Beste-in-class Stabilisierung (Active I.S.)": "Klassenbeste Stabilisierung (Active I.S.)",
    "6K Open Gate allows flexible reframing": "6K Open Gate erlaubt flexibles Umrahmen",
    "Built-in cooling fan = no Überhitzung": "Eingebauter Lüfter = keine Überhitzung",
    
    # Cons
    "L-mount Objektivauswahl is smaller than Sony's": "L-Mount-Objektivauswahl ist kleiner als Sonys",
    "Akku life drains fast in high-res modes": "Akkulaufzeit entleert sich schnell in hochauflösenden Modi",
    "Slightly heavier than the competition": "Etwas schwerer als die Konkurrenz",
    
    # Performance sections
    'The "pulsing" background of older DFD focus is gone. The S5 II tracks subjects smoothly and reliably. It\'s':
        'Das "Pulsieren" im Hintergrund des älteren DFD-Fokus ist weg. Die S5 II verfolgt Motive flüssig und zuverlässig. Sie ist',
    "not *quite* as predictive as Sony for Sport, but for 99% of Video work, it's perfect.":
        "nicht *ganz* so vorausschauend wie Sony für Sport, aber für 99% der Videoarbeit ist sie perfekt.",
    "Most Kameras shoot 16:9. The S5 II shoots 3:2 \"Open Gate,\" using the whole sensor height. This lets you":
        "Die meisten Kameras filmen in 16:9. Die S5 II filmt in 3:2 \"Open Gate\" und nutzt die volle Sensorhöhe. Das lässt dich",
    "Crop a vertical (9:16) short AND a horizontal (16:9) Video from the same clip.":
        "ein vertikales (9:16) Short UND ein horizontales (16:9) Video aus demselben Clip zuschneiden.",
    'Panasonic\'s "Active I.S." is black magic. It smooths out walking tremors so well that you can often leave':
        'Panasonics "Active I.S." ist schwarze Magie. Es glättet Gehzittern so gut, dass du oft',
    "the Gimbal at home, making your setup lighter and faster.":
        "den Gimbal zu Hause lassen kannst, was dein Setup leichter und schneller macht.",
    
    # Lens recommendations
    "Lumix S 20-60mm f/3.5-5.6 — weird range, but amazing for wide vlogging.":
        "Lumix S 20-60mm f/3.5-5.6 — seltsamer Bereich, aber großartig für weites Vlogging.",
    "Lumix S 50mm f/1.8 — erschwinglich, light, and sharp.":
        "Lumix S 50mm f/1.8 — erschwinglich, leicht und scharf.",
    "Sigma 24-70mm f/2.8 DG DN Art (L-Halterung) — the workhorse Objektiv.":
        "Sigma 24-70mm f/2.8 DG DN Art (L-Mount) — das Arbeitstier-Objektiv.",
    
    # FAQ Questions
    "What changed from S5 to S5 II?": "Was hat sich von S5 zu S5 II geändert?",
    "The biggest upgrade is phase-detect Autofokus—the original S5 had slow contrast-detect AF. The S5 II also":
        "Das größte Upgrade ist der Phasenerkennungs-Autofokus – die originale S5 hatte langsamen Kontrast-AF. Die S5 II bietet auch",
    "adds USB-C recording, improved IBIS (8 Blenden), and better heat management. It's a completely different":
        "USB-C-Aufnahme, verbesserte IBIS (8 Blenden) und besseres Wärmemanagement. Es ist eine komplett andere",
    "Kamera in terms of usability.": "Kamera in puncto Bedienbarkeit.",
    "Is L-mount a problem for Objektivauswahl?": "Ist L-Mount ein Problem für die Objektivauswahl?",
    "Not anymore. Sigma, Leica, and Panasonic all make L-mount lenses. You have access to erschwinglich Sigma":
        "Nicht mehr. Sigma, Leica und Panasonic stellen alle L-Mount-Objektive her. Du hast Zugang zu erschwinglichen Sigma",
    "Art lenses and high-end Leica glass. Third-party options from TTArtisan and Viltrox expand choices":
        "Art-Objektiven und High-End Leica-Glas. Drittanbieter-Optionen von TTArtisan und Viltrox erweitern die Auswahl",
    "further. L-mount is smaller than Sony E or Canon RF, but growing steadily.":
        "weiter. L-Mount ist kleiner als Sony E oder Canon RF, wächst aber stetig.",
    "How's the low-light performance vs Sony A7 IV?": "Wie ist die Schwachlichtleistung im Vergleich zur Sony A7 IV?",
    "Slightly better. The S5 II maxes at ISO 204,800 (vs 102,400 on A7 IV) and produces cleaner files at hohe":
        "Etwas besser. Die S5 II erreicht maximal ISO 204.800 (vs 102.400 bei A7 IV) und produziert sauberere Dateien bei hohen",
    "ISOs. The dual native ISO design (ISO 640 and 4000) means noise is minimal at common Video ISOs. For":
        "ISOs. Das duale native ISO-Design (ISO 640 und 4000) bedeutet minimales Rauschen bei üblichen Video-ISOs. Für",
    "nighttime event shooting, the S5 II has an edge.": "nächtliche Event-Aufnahmen hat die S5 II einen Vorteil.",
    "Can the S5 II replace my cinema Kamera?": "Kann die S5 II meine Kinokamera ersetzen?",
    "For many creators, yes. Unlimited 6K recording, 10-Bit 4:2:2 internal, and V-Log make it a legitimate":
        "Für viele Creator, ja. Unbegrenzte 6K-Aufnahme, 10-Bit 4:2:2 intern und V-Log machen sie zu einer legitimen",
    "cinema tool. It lacks built-in ND filters and XLR inputs (requires DMW-XLR1 adapter), but the image":
        "Kino-Werkzeug. Ihr fehlen eingebaute ND-Filter und XLR-Eingänge (erfordert DMW-XLR1-Adapter), aber die Bild-",
    "quality rivals Kameras 3-4x the price. Pair it with a Ninja V for ProRes recording.":
        "qualität rivalisiert mit Kameras, die 3-4x so viel kosten. Kombiniere sie mit einem Ninja V für ProRes-Aufnahme.",
}

# ============================================================================
# OTHER REVIEW PAGES - COMMON FIXES
# ============================================================================
COMMON_REVIEW_FIXES = {
    # Canon R8
    "✨ Beste for Photographers": "✨ Beste für Fotografen",
    "look like finished art straight out of Kamera": "sehen aus wie fertige Kunst direkt aus der Kamera",
    
    # Fujifilm X-T5
    "Beste Entry Vollformat for": "Beste Entry-Vollformat für",
    
    # Sony ZV-E10
    "But the original ZV-E10 is still ausgezeichnet and cheaper.": "Aber die originale ZV-E10 ist immer noch ausgezeichnet und günstiger.",
    "For a Brand neu budget, the original is perfect.": "Für ein brandneues Budget ist die originale perfekt.",
    
    # Common patterns
    "Worth 3.996 € for Vorteile?": "3.996 € wert für die Vorteile?",
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
    print("🇩🇪 German Translation Fix v6 (Complete Review Pages)\n")
    de_dir = BASE_DIR / 'de'
    total = 0
    
    # DJI Osmo Pocket 3
    c = apply_translations(de_dir / 'bewertungen' / 'dji-osmo-pocket-3-testbericht.html', DJI_COMPLETE)
    if c: print(f"✅ dji-osmo-pocket-3-testbericht.html: {c} translations")
    total += c
    
    # Panasonic S5 II
    c = apply_translations(de_dir / 'bewertungen' / 'panasonic-s5-ii-testbericht.html', PANASONIC_COMPLETE)
    if c: print(f"✅ panasonic-s5-ii-testbericht.html: {c} translations")
    total += c
    
    # Apply common fixes to all review pages
    for review_file in (de_dir / 'bewertungen').glob('*.html'):
        c = apply_translations(review_file, COMMON_REVIEW_FIXES)
        if c: print(f"✅ {review_file.name}: {c} common fixes")
        total += c
    
    print(f"\n{'='*50}")
    print(f"✨ Total: {total} translations applied")

if __name__ == '__main__':
    main()
