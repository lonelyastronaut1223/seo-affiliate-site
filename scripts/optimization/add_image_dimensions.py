#!/usr/bin/env python3
"""
Add width/height dimensions to images for CLS prevention
Target: Guides pages without explicit dimensions
"""

import re
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
GUIDES_DIR = BASE_DIR / 'src' / 'pages' / 'guides'
GUIDES_DE_DIR = BASE_DIR / 'src' / 'pages' / 'de' / 'ratgeber'

# Standard dimensions for common image types
DIMENSIONS = {
    # Hero images (16:9 ratio)
    'hero': ' width="1400" height="900"',
    
    # Product shots (square for most cameras)
    'product': ' width="800" height="800"',
    
    # Team avatar
    'avatar': ' width="64" height="64"',
}

def add_dimensions_to_file(filepath):
    """Add width/height to images missing them"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    updates = 0
    
    # Pattern 1: Hero images (eager loading, no dimensions)
    hero_pattern = r'(<img\s+src="[^"]+\.(webp|jpg|png)(?:\?v=[^"]+)?"\s+alt="[^"]+"\s+loading="eager")(?!\s+width=)(?!\s+fetchpriority)'
    
    def replace_hero(match):
        nonlocal updates
        img_tag = match.group(1)
        if 'width=' not in img_tag:
            updates += 1
            return img_tag + DIMENSIONS['hero']
        return img_tag
    
    content = re.sub(hero_pattern, replace_hero, content)
    
    # Pattern 2: Product images (lazy loading, no dimensions, not avatar)
    product_pattern = r'(<img\s+src="[^"]+/guides/[^"]+\.(webp|jpg|png)"\s+alt="[^"]+"\s+loading="lazy")(?!\s+width=)(?!>)'
    
    def replace_product(match):
        nonlocal updates
        img_tag = match.group(1)
        if 'team-avatar' not in img_tag and 'width=' not in img_tag:
            updates += 1
            return img_tag + DIMENSIONS['product']
        return img_tag
    
    content = re.sub(product_pattern, replace_product, content)
    
    # Pattern 3: Ensure closing >
    content = re.sub(r'(width="\d+"\s+height="\d+")(\s*[^>])', r'\1>\2', content)
    content = re.sub(r'(width="\d+"\s+height="\d+")$', r'\1>', content, flags=re.MULTILINE)
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return updates
    return 0

def main():
    total_files =0
    total_updates = 0
    
    print("🖼️  Adding image dimensions for CLS optimization...\n")
    
    # Process EN guides
    if GUIDES_DIR.exists():
        for file in GUIDES_DIR.glob('*.astro'):
            updates = add_dimensions_to_file(file)
            if updates > 0:
                print(f"✓ {file.name}: {updates} images updated")
                total_files += 1
                total_updates += updates
    
    # Process DE guides
    if GUIDES_DE_DIR.exists():
        for file in GUIDES_DE_DIR.glob('*.astro'):
            updates = add_dimensions_to_file(file)
            if updates > 0:
                print(f"✓ DE/{file.name}: {updates} images updated")
                total_files += 1
                total_updates += updates
    
    print(f"\n{'='*50}")
    print(f"✨ Updated {total_files} files")
    print(f"🎯 Added dimensions to {total_updates} images")
    print(f"\n💡 Core Web Vitals impact:")
    print(f"   - Prevents layout shift (CLS)")
    print(f"   - Faster perceived performance")
    print(f"   - Better mobile UX")

if __name__ == '__main__':
    main()
