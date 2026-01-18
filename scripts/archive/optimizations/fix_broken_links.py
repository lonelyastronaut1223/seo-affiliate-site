#!/usr/bin/env python3
"""
Fix broken internal links found in the code audit
Addresses 49 broken link issues
"""

import re
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

def fix_broken_links():
    """Fix all broken internal links"""
    fixes = {
        # Fix 404 pages - absolute to relative paths
        '404.html': [
            ('/assets/css/style.min.css', 'assets/css/style.min.css'),
            ('/assets/images/favicon.png', 'assets/images/favicon.png'),
            ('/contact.html', 'contact.html'),
        ],
        'de/404.html': [
            ('/assets/css/style.min.css', '../assets/css/style.min.css'),
            ('/assets/images/favicon.png', '../assets/images/favicon.png'),
            ('/de/kontakt.html', 'kontakt.html'),
        ],
        
        # Fix German pages with self-referencing canonical issues
        'de/uber-uns.html': [
            ('de/uber-uns.html', 'uber-uns.html'),
        ],
        'de/angebote.html': [
            ('de/angebote.html', 'angebote.html'),
        ],
        'de/kontakt.html': [
            ('de/kontakt.html', 'kontakt.html'),
        ],
        'de/datenschutz.html': [
            ('de/datenschutz.html', 'datenschutz.html'),
        ],
        
        # Fix German review pages - point to German versions
        'de/bewertungen/nikon-z8-testbericht.html': [
            ('../de/bewertungen/nikon-z8-testbericht.html', 'nikon-z8-testbericht.html'),
            ('dji-osmo-pocket-3-review.html', 'dji-osmo-pocket-3-testbericht.html'),
            ('sony-a7c-ii-review.html', 'sony-a7c-ii-testbericht.html'),
            ('panasonic-s5-ii-review.html', 'panasonic-s5-ii-testbericht.html'),
        ],
        'de/bewertungen/sony-a7c-ii-testbericht.html': [
            ('../de/bewertungen/sony-a7c-ii-testbericht.html', 'sony-a7c-ii-testbericht.html'),
            ('sony-zv-e10-review.html', 'sony-zv-e10-testbericht.html'),
            ('nikon-z8-review.html', 'nikon-z8-testbericht.html'),
            ('panasonic-s5-ii-review.html', 'panasonic-s5-ii-testbericht.html'),
        ],
        'de/bewertungen/dji-osmo-pocket-3-testbericht.html': [
            ('../de/bewertungen/dji-osmo-pocket-3-testbericht.html', 'dji-osmo-pocket-3-testbericht.html'),
            ('canon-eos-r8-review.html', 'canon-eos-r8-testbericht.html'),
            ('sony-zv-e10-review.html', 'sony-zv-e10-testbericht.html'),
            ('sony-a7-iv-review.html', 'sony-a7-iv-testbericht.html'),
        ],
        'de/bewertungen/panasonic-s5-ii-testbericht.html': [
            ('../de/bewertungen/panasonic-s5-ii-testbericht.html', 'panasonic-s5-ii-testbericht.html'),
            ('sony-a7c-ii-review.html', 'sony-a7c-ii-testbericht.html'),
            ('fujifilm-x-t5-review.html', 'fujifilm-x-t5-testbericht.html'),
            ('sony-a7-iv-review.html', 'sony-a7-iv-testbericht.html'),
        ],
        'de/bewertungen/canon-eos-r8-testbericht.html': [
            ('../de/bewertungen/canon-eos-r8-testbericht.html', 'canon-eos-r8-testbericht.html'),
            ('sony-a7-iv-review.html', 'sony-a7-iv-testbericht.html'),
            ('sony-zv-e10-review.html', 'sony-zv-e10-testbericht.html'),
            ('panasonic-s5-ii-review.html', 'panasonic-s5-ii-testbericht.html'),
        ],
        'de/bewertungen/sony-zv-e10-testbericht.html': [
            ('../de/bewertungen/sony-zv-e10-testbericht.html', 'sony-zv-e10-testbericht.html'),
            ('dji-osmo-pocket-3-review.html', 'dji-osmo-pocket-3-testbericht.html'),
            ('panasonic-s5-ii-review.html', 'panasonic-s5-ii-testbericht.html'),
            ('sony-a7c-ii-review.html', 'sony-a7c-ii-testbericht.html'),
        ],
        'de/bewertungen/fujifilm-x-t5-testbericht.html': [
            ('../de/bewertungen/fujifilm-x-t5-testbericht.html', 'fujifilm-x-t5-testbericht.html'),
            ('sony-a7c-ii-review.html', 'sony-a7c-ii-testbericht.html'),
            ('dji-osmo-pocket-3-review.html', 'dji-osmo-pocket-3-testbericht.html'),
            ('canon-eos-r8-review.html', 'canon-eos-r8-testbericht.html'),
        ],
        'de/bewertungen/sony-a7-iv-testbericht.html': [
            ('../de/bewertungen/sony-a7-iv-testbericht.html', 'sony-a7-iv-testbericht.html'),
        ],
        
        # Fix German guide pages
        'de/ratgeber/beste-action-360-kamera.html': [
            ('../de/ratgeber/beste-action-360-kamera.html', 'beste-action-360-kamera.html'),
        ],
        'de/ratgeber/beste-vlog-kamera.html': [
            ('../de/ratgeber/beste-Vlog-kamera.html', 'beste-vlog-kamera.html'),
        ],
        'de/ratgeber/beste-hybrid-kamera.html': [
            ('../de/ratgeber/beste-hybrid-kamera.html', 'beste-hybrid-kamera.html'),
        ],
        'de/ratgeber/beste-vollformat-fuer-video.html': [
            ('../../guides/best-Vollformat-for-Video.html', '../ratgeber/beste-vollformat-fuer-video.html'),
        ],
        'de/ratgeber/beste-kamera-fuer-anfaenger-2026.html': [
            ('../de/ratgeber/beste-kamera-fuer-anfaenger-2026.html', 'beste-kamera-fuer-anfaenger-2026.html'),
        ],
        'de/ratgeber/beste-budget-kamera-unter-800.html': [
            ('../de/ratgeber/beste-Budget-kamera-unter-800.html', 'beste-budget-kamera-unter-800.html'),
        ],
        'de/ratgeber/beste-reisekamera.html': [
            ('../de/ratgeber/beste-reisekamera.html', 'beste-reisekamera.html'),
        ],
        
        # Fix German comparison pages
        'de/vergleiche/fujifilm-x-s20-vs-fujifilm-x-t5.html': [
            ('../de/vergleiche/fujifilm-x-s20-vs-fujifilm-x-t5.html', 'fujifilm-x-s20-vs-fujifilm-x-t5.html'),
        ],
        'de/vergleiche/sony-a7-v-vs-canon-r6-iii.html': [
            ('../de/vergleiche/sony-a7-v-vs-canon-r6-iii.html', 'sony-a7-v-vs-canon-r6-iii.html'),
        ],
        'de/vergleiche/sony-zv-e10-vs-sony-a6700.html': [
            ('../de/vergleiche/sony-zv-e10-vs-sony-a6700.html', 'sony-zv-e10-vs-sony-a6700.html'),
        ],
    }
    
    total_fixes = 0
    
    for file_path, replacements in fixes.items():
        full_path = BASE_DIR / file_path
        
        if not full_path.exists():
            print(f"⚠️  File not found: {file_path}")
            continue
        
        content = full_path.read_text(encoding='utf-8')
        original_content = content
        file_fixes = 0
        
        for old, new in replacements:
            if old in content:
                content = content.replace(old, new)
                file_fixes += 1
        
        if content != original_content:
            full_path.write_text(content, encoding='utf-8')
            total_fixes += file_fixes
            print(f"✅ {file_path}: {file_fixes} fixes")
        else:
            print(f"⏭️  {file_path}: no changes needed")
    
    return total_fixes

def main():
    print("🔧 Fixing broken internal links...\n")
    total = fix_broken_links()
    print(f"\n✅ Total fixes applied: {total}")
    print("\nRun 'python3 scripts/audit_code.py' to verify fixes")

if __name__ == '__main__':
    main()
