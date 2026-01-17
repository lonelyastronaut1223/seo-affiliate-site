#!/usr/bin/env python3
"""
Add language switchers to all pages for better SEO internal linking.
This helps Google discover and index the German pages faster.
"""

import re
from pathlib import Path
from typing import Dict, Tuple

# URL mappings between English and German pages
URL_MAPPINGS = {
    # Reviews
    'reviews/sony-a7-iv-review.html': 'de/bewertungen/sony-a7-iv-testbericht.html',
    'reviews/sony-a7c-ii-review.html': 'de/bewertungen/sony-a7c-ii-testbericht.html',
    'reviews/sony-zv-e10-review.html': 'de/bewertungen/sony-zv-e10-testbericht.html',
    'reviews/panasonic-s5-ii-review.html': 'de/bewertungen/panasonic-s5-ii-testbericht.html',
    'reviews/fujifilm-x-t5-review.html': 'de/bewertungen/fujifilm-x-t5-testbericht.html',
    'reviews/canon-eos-r8-review.html': 'de/bewertungen/canon-eos-r8-testbericht.html',
    'reviews/nikon-z8-review.html': 'de/bewertungen/nikon-z8-testbericht.html',
    'reviews/dji-osmo-pocket-3-review.html': 'de/bewertungen/dji-osmo-pocket-3-testbericht.html',
    
    # Guides
    'guides/best-vlog-camera.html': 'de/ratgeber/beste-vlog-kamera.html',
    'guides/best-hybrid-camera.html': 'de/ratgeber/beste-hybrid-kamera.html',
    'guides/best-camera-for-beginners-2026.html': 'de/ratgeber/beste-kamera-fuer-anfaenger-2026.html',
    'guides/best-travel-camera.html': 'de/ratgeber/beste-reisekamera.html',
    'guides/best-full-frame-for-video.html': 'de/ratgeber/beste-vollformat-fuer-video.html',
    'guides/best-budget-camera-under-800.html': 'de/ratgeber/beste-budget-kamera-unter-800.html',
    'guides/best-action-360-camera.html': 'de/ratgeber/beste-action-360-kamera.html',
    
    # Comparisons
    'compare/sony-a7-iv-vs-canon-r6-ii.html': 'de/vergleiche/sony-a7-iv-vs-canon-r6-ii.html',
    'compare/sony-a7-v-vs-canon-r6-iii.html': 'de/vergleiche/sony-a7-v-vs-canon-r6-iii.html',
    'compare/sony-zv-e10-vs-sony-a6700.html': 'de/vergleiche/sony-zv-e10-vs-sony-a6700.html',
    'compare/fujifilm-x-s20-vs-fujifilm-x-t5.html': 'de/vergleiche/fujifilm-x-s20-vs-fujifilm-x-t5.html',
    
    # Info pages
    'about.html': 'de/uber-uns.html',
    'contact.html': 'de/kontakt.html',
    'privacy.html': 'de/datenschutz.html',
    'deals.html': 'de/angebote.html',
}

def get_relative_path(from_path: str, to_path: str) -> str:
    """Calculate relative path from one file to another."""
    from_parts = from_path.split('/')
    to_parts = to_path.split('/')
    
    # Remove filename
    from_dir = from_parts[:-1]
    
    # Calculate how many levels up
    levels_up = len(from_dir)
    
    # Build relative path
    if levels_up == 0:
        return to_path
    else:
        return '../' * levels_up + to_path

def create_language_switcher(english_path: str, german_path: str, is_german: bool) -> str:
    """Create language switcher HTML."""
    if is_german:
        # Calculate relative path from German to English
        en_link = get_relative_path(german_path, english_path)
        de_link = './'
        
        return f'<a href="{en_link}" hreflang="en">EN</a> · <a href="{de_link}" hreflang="de" aria-current="page">DE</a>'
    else:
        # Calculate relative path from English to German  
        en_link = './'
        de_link = get_relative_path(english_path, german_path)
        
        return f'<a href="{en_link}" hreflang="en" aria-current="page">EN</a> · <a href="{de_link}" hreflang="de">DE</a>'

def add_language_switcher_to_file(file_path: Path, english_relative: str, german_relative: str) -> bool:
    """Add language switcher to a single file."""
    print(f"Processing: {file_path}")
    
    # Read file
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if language switcher already exists
    if 'hreflang="en"' in content and 'hreflang="de"' in content:
        # Check if it's in the nav (not just in <head>)
        if '<nav' in content and 'hreflang="en">EN</a>' in content:
            print(f"  ✓ Language switcher already exists")
            return False
    
    # Determine if this is a German page
    is_german = str(file_path).startswith(str(Path('de')))
    
    # Create switcher
    switcher = create_language_switcher(english_relative, german_relative, is_german)
    
    # Find navigation and add switcher
    # Pattern 1: Look for <nav aria-label="...">
    nav_pattern = r'(<nav[^>]*>)(.*?)(</nav>)'
    
    def add_to_nav(match):
        opening = match.group(1)
        content = match.group(2)
        closing = match.group(3)
        
        # Check if already has language links
        if 'hreflang=' in content:
            return match.group(0)  # Already has it
        
        # Add before closing tag
        return f'{opening}{content}\n        {switcher}{closing}'
    
    # Try to add to existing nav
    new_content = re.sub(nav_pattern, add_to_nav, content, count=1, flags=re.DOTALL)
    
    if new_content != content:
        # Write back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"  ✓ Added language switcher")
        return True
    else:
        print(f"  ⚠ Could not add switcher (no suitable nav found)")
        return False

def main():
    """Main execution."""
    base_dir = Path(__file__).parent.parent.parent
    
    updated_count = 0
    failed_count = 0
    
    # Process each English-German page pair
    for english_path, german_path in URL_MAPPINGS.items():
        english_file = base_dir / english_path
        german_file = base_dir / german_path
        
        # Update English page
        if english_file.exists():
            if add_language_switcher_to_file(english_file, english_path, german_path):
                updated_count += 1
        else:
            print(f"⚠ Not found: {english_file}")
            failed_count += 1
        
        # Update German page
        if german_file.exists():
            if add_language_switcher_to_file(german_file, english_path, german_path):
                updated_count += 1
        else:
            print(f"⚠ Not found: {german_file}")
            failed_count += 1
    
    print(f"\n{'='*60}")
    print(f"Language switcher update complete")
    print(f"Updated: {updated_count} pages")
    print(f"Failed: {failed_count} pages")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()
