#!/usr/bin/env python3
"""
German Translation Automation Script (No Dependencies)
Translates English HTML pages to German with proper localization
"""

import os
import re
from pathlib import Path

# Comprehensive translation dictionary
TRANSLATIONS = {
    # Navigation & headers
    ">Reviews<": ">Testberichte<",
    ">Guides<": ">Ratgeber<",
    ">Compare<": ">Vergleiche<",
    ">Deals<": ">Angebote<",
    ">Home<": ">Startseite<",
    ">About<": ">Über uns<",
    ">Contact<": ">Kontakt<",
    ">Privacy<": ">Datenschutz<",
    
    # Common UI elements  
    ">Read Review<": ">Zum Testbericht<",
    ">Quick Take<": ">Kurz-Test<",
    " Review<": " Testbericht<",
    ">Buy Now<": ">Jetzt kaufen<",
    ">Check Price on Amazon": ">Preis bei Amazon prüfen",
    ">Skip to content<": ">Zum Inhalt springen<",
    
    # Product-related terms
    " Kit<": " Set<",
    ">Body<": ">Gehäuse<",
    "Full-frame": "Vollformat",
    "🏆 Best All-Rounder": "🏆 Bester Allrounder",
    ">The Verdict<": ">Das Urteil<",
    ">What We Like<": ">Was uns gefällt<",
    ">The Downsides<": ">Die Nachteile<",
    
    # Content sections
    ">Detailed Performance<": ">Detaillierte Leistung<",
    ">Image Quality<": ">Bildqualität<",
    ">Handling & Build<": ">Handhabung & Verarbeitung<",
    ">Video Performance<": ">Video-Leistung<",
    ">Ideal Lenses<": ">Ideale Objektive<",
    ">Affiliate Disclosure<": ">Partner-Hinweis<",
    ">Frequently Asked Questions<": ">Häufig gestellte Fragen<",
    ">Related Reviews<": ">Verwandte Testberichte<",
    
    # Specs table headers
    ">Imaging<": ">Bildgebung<",
    ">Sensor<": ">Sensor<",
    ">Processor<": ">Prozessor<",
    ">Stabilization<": ">Stabilisierung<",
    " stops)": " Blenden)",
    ">Video<": ">Video<",
    ">Max Resolution<": ">Max. Auflösung<",
    ">Internal Rec<": ">Interne Aufnahme<",
    ">Profiles<": ">Profile<",
    ">Body & Connectivity<": ">Gehäuse & Konnektivität<",
    ">Viewfinder<": ">Sucher<",
    ">Screen<": ">Bildschirm<",
    ">Card Slots<": ">Karten-Slots<",
    ">Weight<": ">Gewicht<",
    "with battery": "mit Akku",
}

# URL mapping for internal links
URL_MAPPINGS = {
    'href="../reviews/': 'href="../bewertungen/',
    'href="reviews/': 'href="bewertungen/',
    'href="../guides/': 'href="../ratgeber/',
    'href="guides/': 'href="ratgeber/',
    'href="../compare/': 'href="../vergleiche/',
    'href="compare/': 'href="vergleiche/',
    'href="../deals.html"': 'href="../angebote.html"',
    'href="deals.html"': 'href="angebote.html"',
    'href="../about.html"': 'href="../uber-uns.html"',
    'href="about.html"': 'href="uber-uns.html"',
    'href="../contact.html"': 'href="../kontakt.html"',
    'href="contact.html"': 'href="kontakt.html"',
    'href="../privacy.html"': 'href="../datenschutz.html"',
    'href="privacy.html"': 'href="datenschutz.html"',
    'href="../"': 'href="../de/"',
    'href="../#reviews"': 'href="../de/#testberichte"',
    'href="../#guides"': 'href="../de/#ratgeber"',
    'href="../#deals"': 'href="../de/#angebote"',
    '/reviews/': '/de/bewertungen/',
    '/guides/': '/de/ratgeber/',
    '/compare/': '/de/vergleiche/',
}

# Fix paths by shifting depth +1
def fix_relative_paths(html_content, file_type):
    """Adjust relative paths for deeper German directory structure"""
    
    # 1. Fix asset paths (CSS, JS, Images)
    # Move ../assets to ../../assets (for reviews/guides)
    html_content = html_content.replace('href="../assets/', 'href="../../assets/')
    html_content = html_content.replace('src="../assets/', 'src="../../assets/')
    html_content = html_content.replace('srcset="../assets/', 'srcset="../../assets/')
    
    # Move assets/ to ../assets/ (for info pages moving from root to de/)
    html_content = html_content.replace('href="assets/', 'href="../assets/')
    html_content = html_content.replace('src="assets/', 'src="../assets/')
    html_content = html_content.replace('srcset="assets/', 'srcset="../assets/')
    
    # 2. Fix Home Link
    # If original was "../" (root), it becomes "../" (de/ root) from de/subdir/ directories
    # But for info pages (de/), it was "./" or "/" -> needs "../" to go to de/? 
    
    # Actually, simpler URL mappings usually handled this, but let's correct some specific issues
    # If we created href="../de/" in mapping, it might be wrong for deep files
    # Correcting common mis-mappings:
    html_content = html_content.replace('href="../de/"', 'href="../"') # Points to de/ index from subdirs
    
    # 3. Fix Broken Image Paths
    # The URL mapping /guides/ -> /de/ratgeber/ incorrectly renamed asset folders
    # We must revert them for images
    html_content = html_content.replace('assets/images/de/ratgeber/', 'assets/images/guides/')
    html_content = html_content.replace('assets/images/de/bewertungen/', 'assets/images/reviews/')
    html_content = html_content.replace('assets/images/de/vergleiche/', 'assets/images/compare/')
    
    return html_content

def convert_currency(text):
    """Convert USD to EUR with German formatting"""
    # Pattern: $1,299 -> 1.299 €
    text = re.sub(r'\$([0-9]{1,3}),([0-9]{3})', r'\1.\2 €', text)
    # Pattern: $599 -> 599 €
    text = re.sub(r'\$([0-9]+)', r'\1 €', text)
    # Pattern: -$100 -> 100 € Rabatt
    text = re.sub(r'-\$([0-9.,]+)', r'\1 € Rabatt', text)
    # Change priceCurrency in JSON
    text = text.replace('"priceCurrency": "USD"', '"priceCurrency": "EUR"')
    
    return text

def translate_text(html_content):
    """Apply translation dictionary to HTML content"""
    for english, german in TRANSLATIONS.items():
        html_content = html_content.replace(english, german)
    return html_content

def update_internal_links(html_content):
    """Update internal links to point to German pages"""
    for old_url, new_url in URL_MAPPINGS.items():
        html_content = html_content.replace(old_url, new_url)
    return html_content

def add_hreflang_tags(html_content, english_url, german_url):
    """Add hreflang tags for SEO"""
    # Find the canonical tag to insert hreflang after it
    canonical_pattern = r'(<link rel="canonical" href="[^"]+">)'
    
    hreflang_tags = f'\n  <link rel="alternate" hreflang="en" href="{english_url}">\n  <link rel="alternate" hreflang="de" href="{german_url}">\n  <link rel="alternate" hreflang="x-default" href="{english_url}">'
    
    html_content = re.sub(canonical_pattern, r'\1' + hreflang_tags, html_content)
    
    return html_content

def translate_html_file(input_path, output_path, file_type='review'):
    """Main translation function"""
    print(f"Translating: {input_path.name} -> {output_path.name}")
    
    # Read the HTML file
    with open(input_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Change lang attribute
    html_content = html_content.replace('<html lang="en">', '<html lang="de">')
    
    # Apply currency conversion
    html_content = convert_currency(html_content)
    
    # Translate text content
    html_content = translate_text(html_content)
    
    # Update internal links
    html_content = update_internal_links(html_content)
    
    # Fix relative paths (CSS/Images)
    html_content = fix_relative_paths(html_content, file_type)
    
    # Update canonical URL and add hreflang
    if file_type == 'review':
        # Update canonical URL from /reviews/ to /de/bewertungen/
        html_content = re.sub(
            r'<link rel="canonical" href="https://cameraupick\.com/reviews/([^"]+)">',
            r'<link rel="canonical" href="https://cameraupick.com/de/bewertungen/\1">',
            html_content
        )
        # Extract URLs for hreflang
        match = re.search(r'href="https://cameraupick\.com/de/bewertungen/([^"]+)"', html_content)
        if match:
            filename = match.group(1)
            english_url = f"https://cameraupick.com/reviews/{filename.replace('testbericht', 'review')}"
            german_url = f"https://cameraupick.com/de/bewertungen/{filename}"
            html_content = add_hreflang_tags(html_content, english_url, german_url)
        
        # Fix Schema.org URLs
        html_content = html_content.replace('"https://cameraupick.com/reviews/', '"https://cameraupick.com/de/bewertungen/')
        html_content = html_content.replace('"https://cameraupick.com/#reviews"', '"https://cameraupick.com/de/#testberichte"')
        
    elif file_type == 'guide':
        html_content = re.sub(
            r'<link rel="canonical" href="https://cameraupick\.com/guides/([^"]+)">',
            r'<link rel="canonical" href="https://cameraupick.com/de/ratgeber/\1">',
            html_content
        )
        match = re.search(r'href="https://cameraupick\.com/de/ratgeber/([^"]+)"', html_content)
        if match:
            filename = match.group(1)
            # Map German filenames back to English
            english_filename = filename.replace('beste-', 'best-').replace('kamera', 'camera').replace('fuer-', 'for-').replace('anfaenger', 'beginners').replace('vollformat', 'full-frame').replace('reisekamera', 'travel-camera')
            english_url = f"https://cameraupick.com/guides/{english_filename}"
            german_url = f"https://cameraupick.com/de/ratgeber/{filename}"
            html_content = add_hreflang_tags(html_content, english_url, german_url)
        
        html_content = html_content.replace('"https://cameraupick.com/guides/', '"https://cameraupick.com/de/ratgeber/')
        html_content = html_content.replace('"https://cameraupick.com/#guides"', '"https://cameraupick.com/de/#ratgeber"')
        
    elif file_type == 'compare':
        html_content = re.sub(
            r'<link rel="canonical" href="https://cameraupick\.com/compare/([^"]+)">',
            r'<link rel="canonical" href="https://cameraupick.com/de/vergleiche/\1">',
            html_content
        )
        match = re.search(r'href="https://cameraupick\.com/de/vergleiche/([^"]+)"', html_content)
        if match:
            filename = match.group(1)
            english_url = f"https://cameraupick.com/compare/{filename}"
            german_url = f"https://cameraupick.com/de/vergleiche/{filename}"
            html_content = add_hreflang_tags(html_content, english_url, german_url)
        
        html_content = html_content.replace('"https://cameraupick.com/compare/', '"https://cameraupick.com/de/vergleiche/')
    
    elif file_type == 'info':
        # Handle special info pages
        page_mappings = {
            'uber-uns.html': ('about.html', 'about'),
            'kontakt.html': ('contact.html', 'contact'),
            'datenschutz.html': ('privacy.html', 'privacy'),
            'angebote.html': ('deals.html', 'deals'),
        }
        
        output_filename = output_path.name
        if output_filename in page_mappings:
            english_file, page_name = page_mappings[output_filename]
            english_url = f"https://cameraupick.com/{english_file}"
            german_url = f"https://cameraupick.com/de/{output_filename}"
            
            html_content = re.sub(
                r'<link rel="canonical" href="https://cameraupick\.com/[^"]+">',
                f'<link rel="canonical" href="{german_url}">',
                html_content
            )
            html_content = add_hreflang_tags(html_content, english_url, german_url)
    
    # Create output directory if needed
    os.makedirs(output_path.parent, exist_ok=True)
    
    # Write output
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✓ Created: {output_path}")
    return True

def main():
    """Main execution"""
    # Resolves to project root (since we are in scripts/i18n/)
    base_dir = Path(__file__).parent.parent.parent
    
    # Define translation tasks (prioritized order)
    # Manual high-priority files (Sony A7 IV, Beginner Guide, About, Contact) removed to prevent overwrite
    tasks = [
        # Reviews
        # ('reviews/sony-a7-iv-review.html', 'de/bewertungen/sony-a7-iv-testbericht.html', 'review'), # Manual
        ('reviews/sony-a7c-ii-review.html', 'de/bewertungen/sony-a7c-ii-testbericht.html', 'review'),
        ('reviews/sony-zv-e10-review.html', 'de/bewertungen/sony-zv-e10-testbericht.html', 'review'),
        ('reviews/panasonic-s5-ii-review.html', 'de/bewertungen/panasonic-s5-ii-testbericht.html', 'review'),
        ('reviews/fujifilm-x-t5-review.html', 'de/bewertungen/fujifilm-x-t5-testbericht.html', 'review'),
        ('reviews/canon-eos-r8-review.html', 'de/bewertungen/canon-eos-r8-testbericht.html', 'review'),
        ('reviews/nikon-z8-review.html', 'de/bewertungen/nikon-z8-testbericht.html', 'review'),
        ('reviews/dji-osmo-pocket-3-review.html', 'de/bewertungen/dji-osmo-pocket-3-testbericht.html', 'review'),
        
        # Guides
        ('guides/best-vlog-camera.html', 'de/ratgeber/beste-vlog-kamera.html', 'guide'),
        ('guides/best-hybrid-camera.html', 'de/ratgeber/beste-hybrid-kamera.html', 'guide'),
        # ('guides/best-camera-for-beginners-2026.html', 'de/ratgeber/beste-kamera-fuer-anfaenger-2026.html', 'guide'), # Manual
        ('guides/best-travel-camera.html', 'de/ratgeber/beste-reisekamera.html', 'guide'),
        ('guides/best-full-frame-for-video.html', 'de/ratgeber/beste-vollformat-fuer-video.html', 'guide'),
        ('guides/best-budget-camera-under-800.html', 'de/ratgeber/beste-budget-kamera-unter-800.html', 'guide'),
        ('guides/best-action-360-camera.html', 'de/ratgeber/beste-action-360-kamera.html', 'guide'),
        
        # Comparisons
        ('compare/sony-a7-iv-vs-canon-r6-ii.html', 'de/vergleiche/sony-a7-iv-vs-canon-r6-ii.html', 'compare'),
        ('compare/sony-a7-v-vs-canon-r6-iii.html', 'de/vergleiche/sony-a7-v-vs-canon-r6-iii.html', 'compare'),
        ('compare/sony-zv-e10-vs-sony-a6700.html', 'de/vergleiche/sony-zv-e10-vs-sony-a6700.html', 'compare'),
        ('compare/fujifilm-x-s20-vs-fujifilm-x-t5.html', 'de/vergleiche/fujifilm-x-s20-vs-fujifilm-x-t5.html', 'compare'),
        
        # Info pages
        # ('about.html', 'de/uber-uns.html', 'info'), # Manual
        # ('contact.html', 'de/kontakt.html', 'info'), # Manual
        ('privacy.html', 'de/datenschutz.html', 'info'),
        ('deals.html', 'de/angebote.html', 'info'),
    ]
    
    print("=" * 60)
    print("German Translation Automation (No External Dependencies)")
    print("=" * 60)
    
    success_count = 0
    fail_count = 0
    
    for input_file, output_file, file_type in tasks:
        input_path = base_dir / input_file
        output_path = base_dir / output_file
        
        if not input_path.exists():
            print(f"⚠ Skipping (not found): {input_file}")
            fail_count += 1
            continue
        
        try:
            translate_html_file(input_path, output_path, file_type)
            success_count += 1
        except Exception as e:
            print(f"✗ Error translating {input_file}: {e}")
            import traceback
            traceback.print_exc()
            fail_count += 1
    
    print("=" * 60)
    print(f"Translation complete: {success_count} successful, {fail_count} failed")
    print("=" * 60)

if __name__ == '__main__':
    main()
