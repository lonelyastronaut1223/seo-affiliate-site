#!/usr/bin/env python3
"""
Comprehensive German Translation Fix - Version 3
Addresses ALL remaining English content including:
- FAQ Schema questions
- Privacy Policy (datenschutz.html)
- Product descriptions
- Mixed content
"""

import re
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent

# ============================================================================
# FAQ SCHEMA TRANSLATIONS (for all review pages)
# ============================================================================
FAQ_TRANSLATIONS = {
    # Canon EOS R8
    '"Is the Canon EOS R8 worth buying in 2026?"': '"Lohnt sich der Kauf der Canon EOS R8 im Jahr 2026?"',
    '"Canon R8 vs R6 II vs R7: Which should I buy?"': '"Canon R8 vs R6 II vs R7: Welche sollte ich kaufen?"',
    '"Why is the R8 so much cheaper than the R6 II?"': '"Warum ist die R8 so viel günstiger als die R6 II?"',
    '"Is the lack of IBIS a deal-breaker?"': '"Ist das Fehlen von IBIS ein Deal-Breaker?"',
    '"How is the Rolling Shutter compared to Sony?"': '"Wie ist der Rolling Shutter im Vergleich zu Sony?"',
    '"Should I invest in RF lenses or use EF with an adapter?"': '"Sollte ich in RF-Objektive investieren oder EF mit Adapter nutzen?"',
    '"Is the R8 worth it over the older RP?"': '"Lohnt sich die R8 gegenüber der älteren RP?"',
    
    # DJI Osmo Pocket 3
    '"Is the Osmo Pocket 3 gut for Schwachlicht?"': '"Ist der Osmo Pocket 3 gut bei Schwachlicht?"',
    '"Can you use the Osmo Pocket 3 for professionell work?"': '"Kann man den Osmo Pocket 3 für professionelle Arbeit nutzen?"',
    '"What is the battery life?"': '"Wie lange hält der Akku?"',
    '"Is the DJI Pocket 3 waterproof?"': '"Ist der DJI Pocket 3 wasserdicht?"',
    
    # Fujifilm X-T5
    '"Is the Fujifilm X-T5 gut for beginners?"': '"Ist die Fujifilm X-T5 gut für Anfänger?"',
    '"Fujifilm X-T5 vs Sony A7 IV: Which should I buy?"': '"Fujifilm X-T5 vs Sony A7 IV: Welche sollte ich kaufen?"',
    '"Does it have in-body image stabilization?"': '"Hat sie eine Sensor-Bildstabilisierung?"',
    '"Is the autofocus as good as Sony?"': '"Ist der Autofokus so gut wie bei Sony?"',
    
    # Nikon Z8
    '"Nikon Z8 vs Z9: Which should I buy?"': '"Nikon Z8 vs Z9: Welche sollte ich kaufen?"',
    '"Is the Z8 overpriced?"': '"Ist die Z8 überteuert?"',
    '"Does the Z8 overheat in 8K mode?"': '"Überhitzt die Z8 im 8K-Modus?"',
    
    # Panasonic S5 II
    '"Is the Panasonic S5 II worth it in 2026?"': '"Lohnt sich die Panasonic S5 II im Jahr 2026?"',
    '"S5 II vs S5 IIX: What\'s the difference?"': '"S5 II vs S5 IIX: Was ist der Unterschied?"',
    '"How does the autofocus compare to Sony?"': '"Wie vergleicht sich der Autofokus mit Sony?"',
    '"Is it good for photography too?"': '"Ist sie auch gut für Fotografie?"',
    
    # Sony A7C II
    '"Is the single card slot a dealbreaker?"': '"Ist der einzelne Kartensteckplatz ein Deal-Breaker?"',
    '"Does it overheat?"': '"Überhitzt sie?"',
    '"A7C II vs A7 IV: Which is better?"': '"A7C II vs A7 IV: Welche ist besser?"',
    
    # Sony ZV-E10
    '"Is the Sony ZV-E10 gut for beginners?"': '"Ist die Sony ZV-E10 gut für Anfänger?"',
    '"ZV-E10 vs ZV-E10 II: Which should I choose?"': '"ZV-E10 vs ZV-E10 II: Welche sollte ich wählen?"',
    '"Can you take photos with it?"': '"Kann man damit auch fotografieren?"',
}

# ============================================================================
# FAQ ANSWER TRANSLATIONS
# ============================================================================
FAQ_ANSWER_TRANSLATIONS = {
    # Canon R8 answers
    "At 1.997 €, the S5 II offers unglaublich Preis-Leistungs-Verhältnis with klassenführender Video, finally reliable Autofokus, and the best IBIS on the market. It's the swiss army knife for hybrid shooters while remaining unter 2.000 €.":
        "Mit 1.997 € bietet die S5 II ein unglaubliches Preis-Leistungs-Verhältnis mit klassenführendem Video, endlich zuverlässigem Autofokus und der besten IBIS auf dem Markt. Sie ist das Schweizer Taschenmesser für Hybrid-Fotografen und bleibt unter 2.000 €.",
    
    "For Reise and hobbyists, no. For paid Hochzeits, maybe—bring a backup memory or an extra Kamera.":
        "Für Reisen und Hobbyisten: nein. Für bezahlte Hochzeitsaufträge vielleicht – nimm einen Backup-Speicher oder eine Extra-Kamera mit.",
}

# ============================================================================
# PRIVACY POLICY (datenschutz.html) TRANSLATIONS
# ============================================================================
PRIVACY_TRANSLATIONS = {
    "Your privacy matters. Here's how we collect, use, and protect your data.":
        "Ihre Privatsphäre ist uns wichtig. So erheben, nutzen und schützen wir Ihre Daten.",
    
    "Information We Collect": "Informationen, die wir erheben",
    "How We Use Your Information": "Wie wir Ihre Informationen nutzen",
    "Cookies and Tracking": "Cookies und Tracking",
    "Third-Party Services": "Dienste Dritter",
    "Your Rights": "Ihre Rechte",
    "Contact Us": "Kontaktieren Sie uns",
    "Changes to This Policy": "Änderungen dieser Richtlinie",
    
    "We collect minimal data to provide our services:":
        "Wir erheben nur minimale Daten, um unsere Dienste bereitzustellen:",
    "Analytics data (anonymized page views, device type)":
        "Analysedaten (anonymisierte Seitenaufrufe, Gerätetyp)",
    "Information you voluntarily provide (contact form submissions)":
        "Informationen, die Sie freiwillig bereitstellen (Kontaktformular-Eingaben)",
    "Affiliate link clicks (to track conversions)":
        "Affiliate-Link-Klicks (zur Conversion-Verfolgung)",
    
    "We use your information to:":
        "Wir nutzen Ihre Informationen, um:",
    "Improve our content and recommendations":
        "Unsere Inhalte und Empfehlungen zu verbessern",
    "Analyze site performance": "Die Website-Leistung zu analysieren",
    "Process affiliate commissions": "Affiliate-Provisionen zu verarbeiten",
    
    "We use cookies for:": "Wir nutzen Cookies für:",
    "Essential site functionality": "Wesentliche Website-Funktionalität",
    "Analytics (Google Analytics)": "Analysen (Google Analytics)",
    "Remembering your preferences": "Das Speichern Ihrer Präferenzen",
    
    "We partner with:": "Wir arbeiten zusammen mit:",
    "Amazon Associates (affiliate links)": "Amazon Associates (Affiliate-Links)",
    "Google Analytics (anonymous traffic analysis)":
        "Google Analytics (anonyme Verkehrsanalyse)",
    
    "You have the right to:": "Sie haben das Recht:",
    "Access your data": "Auf Ihre Daten zuzugreifen",
    "Request deletion": "Löschung zu beantragen",
    "Opt-out of analytics": "Analytics abzulehnen",
    
    "For privacy questions, contact us at:":
        "Bei Fragen zum Datenschutz kontaktieren Sie uns unter:",
    
    "We may update this policy periodically. Changes will be posted on this page.":
        "Wir können diese Richtlinie regelmäßig aktualisieren. Änderungen werden auf dieser Seite veröffentlicht.",
}

# ============================================================================
# PRODUCT DESCRIPTION TRANSLATIONS
# ============================================================================
PRODUCT_TRANSLATIONS = {
    # Budget guide - Sony ZV-E10
    "Even with a successor out, the original ZV-E10 remains the king of Preis-Leistungs-Verhältnis.":
        "Auch mit einem Nachfolger bleibt die originale ZV-E10 die Königin des Preis-Leistungs-Verhältnisses.",
    "You get 4K Video, a fully schwenkbaren Bildschirm, Kopfhörerbuchse und Mikrofoneingang":
        "Du bekommst 4K-Video, einen voll schwenkbaren Bildschirm, Kopfhörerbuchse und Mikrofoneingang",
    "The Autofokus is still miles ahead of competitors in this price bracket.":
        "Der Autofokus ist immer noch Meilen voraus gegenüber der Konkurrenz in dieser Preisklasse.",
    "It tracks eyes and faces reliably, making it the perfect Budget hybrid for YouTubers who also take Fotos.":
        "Er verfolgt Augen und Gesichter zuverlässig und macht sie zum perfekten Budget-Hybrid für YouTuber, die auch fotografieren.",
    
    "The G100D is a tiny Kamera with a big heart.":
        "Die G100D ist eine winzige Kamera mit großem Herzen.",
    "It uses the smaller Micro Four Thirds sensor, which allows the Kamera and lenses to be incredibly portable.":
        "Sie nutzt den kleineren Micro-Four-Thirds-Sensor, wodurch Kamera und Objektive unglaublich tragbar sind.",
    "It has a beautiful, bright electronic Sucher—something the Sony ZV-E10 lacks.":
        "Sie hat einen wunderschönen, hellen elektronischen Sucher – etwas, das der Sony ZV-E10 fehlt.",
    "Sie bietet Nokia OZO Audio-Tracking, das den Ton auf den Sprechenden fokussiert.":
        "Sie bietet Nokia OZO Audio-Tracking, das den Ton auf den Sprechenden fokussiert.",
    "Es ist ein fantastisch, oft overlooked option for Reise vlogging on a shoestring Budget.":
        "Es ist eine fantastische, oft übersehene Option für Reise-Vlogging mit kleinem Budget.",
        
    # Budget guide pros/cons
    "Access to erschwinglichen Sigma/Tamron lenses": "Zugang zu erschwinglichen Sigma/Tamron-Objektiven",
    "Fully flip-out screen for selfies/vlogging": "Voll ausklappbarer Bildschirm für Selfies/Vlogging",
    "Zuverlässig face/eye Autofokus": "Zuverlässiger Gesichts-/Augen-Autofokus",
    "Headphone and Mic ports included": "Kopfhörer- und Mikrofon-Anschlüsse inklusive",
    "No Sucher (screen only)": "Kein Sucher (nur Bildschirm)",
    "Rolling shutter (jello effect) in 4K": "Rolling Shutter (Jello-Effekt) bei 4K",
    "Menus are the older, confusing style": "Menüs im älteren, verwirrenden Stil",
    "Ausgezeichnet Sucher for bright days": "Ausgezeichneter Sucher für helle Tage",
    "Huge selection of cheap used lenses": "Große Auswahl günstiger Gebraucht-Objektive",
    "Erweiterte Audio-Funktionen eingebaut": "Erweiterte Audio-Funktionen eingebaut",
    "USB-C charging (updated model)": "USB-C-Laden (aktualisiertes Modell)",
    "Heavy Crop in 4K Video": "Starker Crop bei 4K-Video",
    "Autofokus pulses (hunting) in Video": "Autofokus pulsiert (sucht) bei Video",
    "Smaller sensor than APS-C rivals": "Kleinerer Sensor als APS-C-Rivalen",
    
    # Fujifilm X-T5 review
    "The return to photography roots. High-resolution 40MP APS-C sensor with classic dials and ausgezeichnet photo quality.":
        "Die Rückkehr zu den Fotografie-Wurzeln. Hochauflösender 40MP APS-C-Sensor mit klassischen Einstellrädern und ausgezeichneter Bildqualität.",
    "The Fujifilm X-T5 is a love letter to Fotografs.":
        "Die Fujifilm X-T5 ist ein Liebesbrief an Fotografen.",
    "It ditches the \"hybrid\" Klappbildschirm of the X-T4 for a Fotograf-friendly 3-way tilt screen and packs a massive 40MP sensor.":
        "Sie verzichtet auf den \"hybriden\" Klappbildschirm der X-T4 zugunsten eines fotografenfreundlichen 3-Wege-Neigungsbildschirms und packt einen massiven 40MP-Sensor ein.",
    "With dedicated dials for Verschlusszeit, ISO, and Belichtung compensation, it's a joy to use.":
        "Mit dedizierten Einstellrädern für Verschlusszeit, ISO und Belichtungskorrektur ist sie eine Freude zu benutzen.",
    "While the Autofokus isn't quite at Sony's level for Sport, the Filmsimulations make your JPEGs look like finished art straight out of Kamera.":
        "Während der Autofokus nicht ganz auf Sonys Niveau für Sport ist, lassen die Filmsimulationen deine JPEGs wie fertige Kunst direkt aus der Kamera aussehen.",
    
    # Hybrid guide
    "from the  same clip  without losing quality. Außerdem hat sie den besten IBIS auf dem Markt.":
        "aus demselben Clip ohne Qualitätsverlust. Außerdem hat sie die beste IBIS auf dem Markt.",
    "The R6 Mark II schießt atemberaubende 40 Bilder pro Sekunde for action, and 6K Raw Video for cinematic projects.":
        "Die R6 Mark II schießt atemberaubende 40 Bilder pro Sekunde für Action und 6K-Raw-Video für cinematische Projekte.",
        
    # Deals page
    "Why trust our deals?": "Warum unseren Deals vertrauen?",
    "have tested and verified": "haben getestet und verifiziert",
    
    # Various mixed content fixes
    "the image quality for 20% of the price": "die Bildqualität für 20% des Preises",
    "identical to those from a 1.000 € body. Ideally suited for students and hobbyists.":
        "identisch mit denen eines 1.000-€-Gehäuses. Ideal geeignet für Studenten und Hobbyisten.",
    "entry-point for creators": "Einstiegspunkt für Creator",
    
    # Related posts section
    "Panasonic S5 II Testbericht": "Panasonic S5 II Testbericht",
    "The Kamera that fixed Panasonic's biggest flaw. Finally with zuverlässig Autofokus, plus klassenführender Stabilisierung und Video-Funktionen.":
        "Die Kamera, die Panasonics größtes Manko behoben hat. Endlich mit zuverlässigem Autofokus, plus klassenführender Stabilisierung und Video-Funktionen.",
    "DJI Osmo Pocket 3 Testbericht": "DJI Osmo Pocket 3 Testbericht",
    "The ultimate vlogging tool. A 1-inch sensor, mechanical Stabilisierung, and a rotating screen that fits in your pocket.":
        "Das ultimative Vlogging-Werkzeug. Ein 1-Zoll-Sensor, mechanische Stabilisierung und ein drehbarer Bildschirm, der in deine Tasche passt.",
    "Fujifilm X-S20 vs X-T5": "Fujifilm X-S20 vs X-T5",
    "Same lenses, different priorities: Video tools vs classic photo handling.":
        "Gleiche Objektive, unterschiedliche Prioritäten: Video-Werkzeuge vs klassische Foto-Handhabung.",
}

def apply_all_translations(file_path: Path) -> int:
    """Apply all translation dictionaries to a file"""
    if not file_path.exists():
        return 0
    
    content = file_path.read_text(encoding='utf-8')
    original = content
    count = 0
    
    # Apply FAQ translations
    for en, de in FAQ_TRANSLATIONS.items():
        if en in content:
            content = content.replace(en, de)
            count += 1
    
    # Apply FAQ answer translations
    for en, de in FAQ_ANSWER_TRANSLATIONS.items():
        if en in content:
            content = content.replace(en, de)
            count += 1
    
    # Apply privacy translations
    for en, de in PRIVACY_TRANSLATIONS.items():
        if en in content:
            content = content.replace(en, de)
            count += 1
    
    # Apply product translations
    for en, de in PRODUCT_TRANSLATIONS.items():
        if en in content:
            content = content.replace(en, de)
            count += 1
    
    if content != original:
        file_path.write_text(content, encoding='utf-8')
        return count
    return 0

def main():
    """Process all German files"""
    print("🇩🇪 Comprehensive German Translation Fix v3\n")
    
    de_dir = BASE_DIR / 'de'
    total = 0
    files_fixed = 0
    
    # Process all HTML files
    for html_file in de_dir.rglob('*.html'):
        count = apply_all_translations(html_file)
        if count > 0:
            rel_path = html_file.relative_to(BASE_DIR)
            print(f"✅ {rel_path}: {count} translations")
            total += count
            files_fixed += 1
        else:
            rel_path = html_file.relative_to(BASE_DIR)
            print(f"⏭️  {rel_path}: no changes")
    
    print(f"\n{'='*60}")
    print(f"✨ Total: {total} translations in {files_fixed} files")
    print(f"{'='*60}")
    
    return total

if __name__ == '__main__':
    main()
