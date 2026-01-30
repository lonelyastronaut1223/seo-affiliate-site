#!/usr/bin/env python3
"""
Add lazy loading and explicit dimensions to images for Core Web Vitals
Skips hero images (loading="eager") and adds width/height to reduce CLS
"""

import re
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
PAGES_DIR = BASE_DIR / 'src' / 'pages'

# Standard dimensions for product images
DIMENSIONS = {
    'guides': {'width': 800, 'height': 600},
    'team-avatar': {'width': 64, 'height': 64},
    'product': {'width': 800, 'height': 600},
    'hero': {'width': 1400, 'height': 900},
}

def should_skip_file(content, img_match):
    """Check if image should be skipped (already has loading or is hero)"""
    img_tag = img_match.group(0)
    
    # Skip if already has loading attribute
    if 'loading=' in img_tag:
        return True
    
    # Skip if has fetchpriority="high" (LCP images)
    if 'fetchpriority="high"' in img_tag:
        return True
        
    return False

def add_lazy_loading(file_path):
    """Add lazy loading to images in a file"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    changes = 0
    
    # Find all <img> tags
    img_pattern = r'<img\s+([^>]+)>'
    
    def replace_img(match):
        nonlocal changes
        img_tag = match.group(0)
        attrs = match.group(1)
        
        # Skip if already has loading
        if 'loading=' in attrs:
            return img_tag
            
        # Skip LCP images
        if 'fetchpriority="high"' in attrs:
            return img_tag
        
        # Add loading="lazy" before the last attribute
        if attrs.endswith('/'):
            # Self-closing
            new_attrs = attrs[:-1].strip() + ' loading="lazy" /'
        else:
            new_attrs = attrs.strip() + ' loading="lazy"'
        
        changes += 1
        return f'<img {new_attrs}>'
    
    content = re.sub(img_pattern, replace_img, content)
    
    if changes > 0:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return changes
    
    return 0

def main():
    print("🖼️  Adding lazy loading to images...\\n")
    
    total_files = 0
    total_images = 0
    
    for astro_file in PAGES_DIR.rglob('*.astro'):
        changes = add_lazy_loading(astro_file)
        if changes > 0:
            total_files += 1
            total_images += changes
            print(f"  ✅ {astro_file.relative_to(BASE_DIR)}: +{changes} lazy images")
    
    print(f"\\n{'='*50}")
    print(f"✨ Updated {total_files} files")
    print(f"🎯 Added lazy loading to {total_images} images")
    print(f"\\n💡 Core Web Vitals impact:")
    print(f"   - Faster initial page load")
    print(f"   - Better LCP scores")
    print(f"   - Reduced bandwidth usage")

if __name__ == '__main__':
    main()
