#!/usr/bin/env python3
"""
Complete translation of review card descriptions in DE index.astro
"""

import re
from pathlib import Path

def translate_review_descriptions():
    file_path = Path("src/pages/de/index.astro")
    content = file_path.read_text(encoding="utf-8")
    
    # Review card descriptions - translate each one
    translations = [
        # Nikon Z6 III
        ("Versatile full-frame hybrid with 24MP partially stacked sensor, 6K\n            video, and Nikon's best autofocus yet. Exceptional IBIS and video\n            features.",
         "Vielseitige Vollformat-Hybrid mit 24MP teilweise gestapeltem Sensor, 6K\n            Video und Nikons bestem Autofokus. Herausragender IBIS und Video-Funktionen."),
        
        # Canon R5 Mark II
        ("Professional flagship with 45MP sensor, 8K 60p RAW, and\n            revolutionary Eye Control AF. Canon's most capable hybrid camera to\n            date.",
         "Profi-Flaggschiff mit 45MP-Sensor, 8K 60p RAW und\n            revolutionärer Eye Control AF. Canons leistungsfähigste Hybrid-Kamera."),
        
        # Fujifilm X-S20
        ("Best APS-C hybrid value with 26MP X-Trans sensor, 6.2K video, IBIS,\n            and legendary Film Simulations. Perfect for content Creator.",
         "Bestes APS-C-Hybrid Preis-Leistungs-Verhältnis mit 26MP X-Trans-Sensor, 6.2K-Video, IBIS\n            und legendären Filmsimulationen. Perfekt für Content Creator."),
        
        # Sony ZV-E10 II
        ("Best beginner camera with A6700-level AF, 4K60, and NP-FZ100 battery.\n            Perfect for creators who want to grow.",
         "Beste Einsteigerkamera mit A6700-Niveau AF, 4K60 und NP-FZ100-Akku.\n            Perfekt für Creator, die wachsen wollen."),
        
        # Canon EOS R50
        ("Easiest-to-use mirrorless with Creative Assist, EVF, and Canon's \n            beautiful color science. Perfect for beginners.",
         "Einfachste spiegellose Kamera mit Creative Assist, EVF und Canons\n            schöner Farbwissenschaft. Perfekt für Anfänger."),
        
        # Fujifilm X-T50
        ("40MP sensor with Film Simulation dial for instant looks. The camera \n            that makes photography feel artistic again.",
         "40MP-Sensor mit Filmsimulations-Wählrad für sofortige Looks. Die Kamera,\n            die Fotografie wieder künstlerisch macht."),
        
        # OM System OM-1 Mark II
        ("Compact pro MFT with 120fps burst, IP53 weather sealing, and\n            computational photography. Ultimate adventure camera for\n            portability.",
         "Kompakte Profi-MFT mit 120fps Serienaufnahme, IP53-Wetterschutz und\n            Computational Photography. Ultimative Abenteuer-Kamera für maximale\n            Portabilität."),
        
        # Sony A7C II
        ("Ultra-compact full-frame with AI autofocus. Perfect for travel; same\n            sensor as A7 IV in smaller body. Single card slot but excellent\n            portability.",
         "Ultra-kompakte Vollformat mit KI-Autofokus. Perfekt für Reisen; gleicher\n            Sensor wie A7 IV in kleinerem Gehäuse. Ein Kartensteckplatz, aber exzellente\n            Portabilität."),
        
        # Sony A7 IV  
        ("Hybrid favorite with strong AF and color; menus need learning.\n            10-bit, solid thermals, great lens options; rolling shutter still to\n            mind.",
         "Hybrid-Favorit mit starkem AF und Farben; Menüs brauchen Einarbeitung.\n            10-Bit, solide Thermik, tolle Objektivauswahl; Rolling Shutter beachten."),
        
        # Fujifilm X-T5
        ("40MP detail, film sims, classic dials. Best for photo-first\n            shooters; video good but rolling shutter in HQ needs care.",
         "40MP-Details, Filmsimulationen, klassische Einstellräder. Ideal für Foto-first\n            Shooter; Video gut, aber Rolling Shutter in HQ beachten."),
        
        # Canon EOS R8
        ("Lightweight full-frame with top AF and Canon color. Perfect FF\n            starter; add batteries and avoid fast pans for rolling shutter.",
         "Leichtes Vollformat mit Top-AF und Canon-Farben. Perfekter FF-Einstieg;\n            extra Akkus einpacken und schnelle Schwenks meiden wegen Rolling Shutter."),
        
        # Sony ZV-E10
        ("Best entry vlog cam with flip screen, tally light, mic jack; lacks\n            4K60 but unbeatable for budget creators.",
         "Beste Einsteiger-Vlogkamera mit Klappbildschirm, Tally-Licht, Mikrofonanschluss;\n            kein 4K60, aber unschlagbar für Budget-Creator."),
        
        # Nikon Z8
        ("Pro-level stills/video, 8K options, strong AF. Great for serious\n            hybrid shooters wanting pro ergonomics in a smaller body.",
         "Profi-Niveau Fotos/Video, 8K-Optionen, starker AF. Ideal für ernsthafte\n            Hybrid-Shooter mit Profi-Ergonomie im kompakteren Gehäuse."),
        
        # Panasonic S5 II
        ("PDAF fixes AF, strong IBIS, 6K open-gate, great value for\n            video-first creators.",
         "PDAF löst AF-Probleme, starker IBIS, 6K Open-Gate, tolles Preis-Leistungs-\n            Verhältnis für Video-first Creator."),
        
        # DJI Osmo Pocket 3
        ("1-inch gimbal cam, great stabilization, improved skin tones. Perfect\n            for travel walk-and-talk.",
         "1-Zoll-Gimbal-Kamera, tolle Stabilisierung, verbesserte Hauttöne. Perfekt\n            für Travel Walk-and-Talk."),
    ]
    
    for en_text, de_text in translations:
        content = content.replace(en_text, de_text)
    
    # Also fix prices from $ to €
    content = content.replace("$2,499", "2.499 €")
    content = content.replace("$4,299", "4.299 €")
    content = content.replace("$1,299", "1.299 €")
    content = content.replace("$898", "898 €")
    content = content.replace("$679", "679 €")
    content = content.replace("$1,399", "1.399 €")
    content = content.replace("$2,199", "2.199 €")
    
    # Fix remaining English in meta sections - reviews count
    content = content.replace("(76 reviews)", "(76 Bewertungen)")
    content = content.replace("(142 reviews)", "(142 Bewertungen)")
    content = content.replace("(89 reviews)", "(89 Bewertungen)")
    
    # Fix meta categories
    content = content.replace(">Beginner ·", ">Einsteiger ·")
    content = content.replace(">Lifestyle ·", ">Lifestyle ·")
    content = content.replace(">Pro MFT ·", ">Profi MFT ·")
    
    # FAQ answers - translate them too
    faq_translations = [
        # Best camera for beginners
        ("For beginners, we recommend the Sony ZV-E10 or Canon EOS R8. These\n              cameras feature fast autofocus, simple menus, good battery life,\n              and lens options that you can grow with. The Sony ZV-E10 is\n              particularly good for budget vloggers ($698), while the Canon R8\n              is an excellent value full-frame entry ($1,499).",
         "Für Anfänger empfehlen wir die Sony ZV-E10 oder Canon EOS R8. Diese\n              Kameras bieten schnellen Autofokus, einfache Menüs, gute Akkulaufzeit\n              und Objektivoptionen zum Mitwachsen. Die Sony ZV-E10 ist besonders\n              gut für Budget-Vlogger (698 €), während die Canon R8 ein exzellenter\n              Vollformat-Einstieg ist (1.499 €)."),
        
        # Full-frame needed
        ("Not necessarily. APS-C cameras (like the Fujifilm X-T5 or Sony\n              A6700) offer an excellent balance of image quality, low-light\n              performance, and price. Full-frame cameras excel in extreme low\n              light and shallow depth of field, but APS-C cameras are lighter,\n              cheaper, and have smaller lenses. Unless you shoot professional\n              weddings or need extreme low-light performance, APS-C is perfectly\n              adequate.",
         "Nicht unbedingt. APS-C-Kameras (wie die Fujifilm X-T5 oder Sony\n              A6700) bieten eine ausgezeichnete Balance aus Bildqualität, Low-Light-\n              Leistung und Preis. Vollformat-Kameras glänzen bei extremem Low-Light\n              und flacher Schärfentiefe, aber APS-C-Kameras sind leichter, günstiger\n              und haben kleinere Objektive. Außer für professionelle Hochzeiten oder\n              extreme Low-Light-Anforderungen ist APS-C völlig ausreichend."),
        
        # First lens
        ("Start with a kit lens or a 24-70mm f/4 zoom. This gives you\n              flexibility to explore your photographic style. Once you know what\n              you shoot most, you can invest in dedicated lenses: wide-angle for\n              travel (16-35mm), bright prime for portraits (50mm f/1.8), or\n              telephoto for wildlife (70-200mm). Don't buy expensive f/1.4\n              primes right away—learn to use light first.",
         "Starte mit einem Kit-Objektiv oder einem 24-70mm f/4 Zoom. Das gibt dir\n              Flexibilität, deinen fotografischen Stil zu entdecken. Sobald du weißt,\n              was du am meisten fotografierst, kannst du in spezielle Objektive investieren:\n              Weitwinkel für Reisen (16-35mm), lichtstarke Festbrennweite für Porträts\n              (50mm f/1.8) oder Tele für Wildlife (70-200mm). Kaufe nicht sofort teure\n              f/1.4-Festbrennweiten — lerne zuerst mit Licht umzugehen."),
        
        # Mirrorless vs DSLR
        ("Mirrorless cameras use an electronic viewfinder instead of an\n              optical one, making them smaller, lighter, and offering better\n              video features and real-time preview. All major manufacturers\n              (Canon, Sony, Nikon, Fujifilm) have transitioned to mirrorless\n              systems. New lens releases, better autofocus, and video features\n              are all concentrated on mirrorless. Unless you have a large DSLR\n              lens collection, buy mirrorless.",
         "Spiegellose Kameras verwenden einen elektronischen Sucher statt eines\n              optischen, was sie kleiner, leichter macht und bessere Video-Funktionen\n              sowie Echtzeit-Vorschau bietet. Alle großen Hersteller (Canon, Sony,\n              Nikon, Fujifilm) sind auf spiegellose Systeme umgestiegen. Neue Objektive,\n              besserer Autofokus und Video-Features konzentrieren sich auf spiegellos.\n              Außer du hast eine große DSLR-Objektivsammlung, kaufe spiegellos."),
        
        # Video specs
        ("Look for a camera with 4K 30fps (minimum), 10-bit internal\n              recording (for color grading), a flip screen, good in-body image\n              stabilization (IBIS) or lens stabilization, and clean HDMI output.\n              For serious vlogging, prioritize fast autofocus (Sony / Canon),\n              overheating management, and at least 60 minutes of recording\n              limits. Hybrid cameras like the Sony A7C II or Panasonic S5 II\n              strike a good balance between video and stills.",
         "Achte auf eine Kamera mit 4K 30fps (Minimum), 10-Bit interner\n              Aufnahme (für Farbkorrektur), Klappbildschirm, guter Bildstabilisierung\n              (IBIS) oder Objektiv-Stabilisierung und sauberem HDMI-Ausgang.\n              Für ernsthaftes Vlogging priorisiere schnellen Autofokus (Sony / Canon),\n              Überhitzungsmanagement und mindestens 60 Minuten Aufnahmelimit.\n              Hybrid-Kameras wie Sony A7C II oder Panasonic S5 II bieten eine gute\n              Balance zwischen Video und Fotos."),
        
        # $1000 budget
        ("For $1,000 you can get excellent entry-level kits. Sony ZV-E10 +\n              16-50mm ($798), Canon EOS M50 Mark II ($699), or Fujifilm X-S10 +\n              lens ($999) are all solid options. Prioritize reliable autofocus\n              and good lens ecosystems over chasing maximum megapixels or 8K\n              video. At this price point, body + lens + memory card + spare\n              battery should all fit within budget.",
         "Für 1.000 € bekommst du ausgezeichnete Einsteiger-Kits. Sony ZV-E10 +\n              16-50mm (798 €), Canon EOS M50 Mark II (699 €) oder Fujifilm X-S10 +\n              Objektiv (999 €) sind alle solide Optionen. Priorisiere zuverlässigen\n              Autofokus und gute Objektiv-Ökosysteme statt maximale Megapixel oder\n              8K-Video. Bei diesem Preis sollten Body + Objektiv + Speicherkarte +\n              Ersatz-Akku im Budget liegen."),
    ]
    
    for en_text, de_text in faq_translations:
        content = content.replace(en_text, de_text)
    
    # Alt text translations (important for accessibility/SEO)
    alt_translations = [
        ("alt=\"Nikon Z6 III full-frame hybrid camera\"", "alt=\"Nikon Z6 III Vollformat-Hybrid-Kamera\""),
        ("alt=\"Canon EOS R5 Mark II professional camera\"", "alt=\"Canon EOS R5 Mark II Profi-Kamera\""),
        ("alt=\"Fujifilm X-S20 compact hybrid camera\"", "alt=\"Fujifilm X-S20 kompakte Hybrid-Kamera\""),
        ("alt=\"Sony ZV-E10 II beginner camera\"", "alt=\"Sony ZV-E10 II Einsteigerkamera\""),
        ("alt=\"Canon EOS R50 beginner camera\"", "alt=\"Canon EOS R50 Einsteigerkamera\""),
        ("alt=\"Fujifilm X-T50 lifestyle camera\"", "alt=\"Fujifilm X-T50 Lifestyle-Kamera\""),
        ("alt=\"OM System OM-1 Mark II professional camera\"", "alt=\"OM System OM-1 Mark II Profi-Kamera\""),
        ("alt=\"Sony A7C II compact full-frame camera\"", "alt=\"Sony A7C II kompakte Vollformat-Kamera\""),
        ("alt=\"Sony A7 IV hybrid camera\"", "alt=\"Sony A7 IV Hybrid-Kamera\""),
        ("alt=\"Fujifilm X-T5 mirrorless camera\"", "alt=\"Fujifilm X-T5 spiegellose Kamera\""),
        ("alt=\"Canon EOS R8 full-frame camera\"", "alt=\"Canon EOS R8 Vollformat-Kamera\""),
        ("alt=\"Sony ZV-E10 vlog camera\"", "alt=\"Sony ZV-E10 Vlog-Kamera\""),
        ("alt=\"Nikon Z8 professional camera\"", "alt=\"Nikon Z8 Profi-Kamera\""),
        ("alt=\"Panasonic S5 II hybrid camera\"", "alt=\"Panasonic S5 II Hybrid-Kamera\""),
        ("alt=\"DJI Osmo Pocket 3 gimbal camera\"", "alt=\"DJI Osmo Pocket 3 Gimbal-Kamera\""),
        ("alt=\"Modern mirrorless camera buying guide hero image\"", "alt=\"Moderne spiegellose Kamera Kaufberatung Hero-Bild\""),
        ("alt=\"Beginner mirrorless camera kit\"", "alt=\"Einsteiger spiegellose Kamera Kit\""),
        ("alt=\"Compact travel camera used on the street\"", "alt=\"Kompakte Reisekamera für Straßenfotografie\""),
        ("alt=\"Vlog camera with microphone setup\"", "alt=\"Vlog-Kamera mit Mikrofon-Setup\""),
        ("alt=\"Affordable mirrorless camera on a wooden desk\"", "alt=\"Günstige spiegellose Kamera auf Holztisch\""),
        ("alt=\"Mirrorless camera body close up\"", "alt=\"Spiegellose Kamera Gehäuse Nahaufnahme\""),
        ("alt=\"Full frame camera video rig\"", "alt=\"Vollformat-Kamera Video-Rig\""),
        ("alt=\"Action camera mounted outdoors\"", "alt=\"Action-Kamera draußen montiert\""),
        ("alt=\"YouTube creator studio setup with camera and ring light\"", "alt=\"YouTube Creator Studio mit Kamera und Ringlicht\""),
        ("alt=\"Sony ZV-E10 deal\"", "alt=\"Sony ZV-E10 Angebot\""),
        ("alt=\"Panasonic S5 II deal\"", "alt=\"Panasonic S5 II Angebot\""),
        ("alt=\"Sony E-mount G Master lens\"", "alt=\"Sony E-Mount G Master Objektiv\""),
        ("alt=\"Canon RF lens with red ring\"", "alt=\"Canon RF Objektiv mit rotem Ring\""),
        ("alt=\"Silver Fujifilm X-mount lens\"", "alt=\"Silbernes Fujifilm X-Mount Objektiv\""),
        ("alt=\"Carbon fiber travel tripod\"", "alt=\"Carbon-Reisestativ\""),
        ("alt=\"Camera backpack and sling bag\"", "alt=\"Kamera-Rucksack und Sling-Bag\""),
        ("alt=\"High speed SD cards\"", "alt=\"Hochgeschwindigkeits-SD-Karten\""),
    ]
    
    for en_alt, de_alt in alt_translations:
        content = content.replace(en_alt, de_alt)
    
    file_path.write_text(content, encoding="utf-8")
    print(f"✅ Completed translation of review descriptions: {file_path}")

if __name__ == "__main__":
    translate_review_descriptions()
