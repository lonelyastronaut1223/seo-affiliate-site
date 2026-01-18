#!/usr/bin/env python3
"""
Script to analyze and improve image Alt text across the site
Checks for missing, generic, or non-descriptive Alt text
"""

import os
import re
from pathlib import Path
from collections import defaultdict

def extract_images_with_alt(html_content, filepath):
    """Extract all img tags and their alt text"""
    img_pattern = r'<img[^>]+>'
    images = []
    
    for match in re.finditer(img_pattern, html_content):
        img_tag = match.group(0)
        
        # Extract src
        src_match = re.search(r'src=["\'](.*?)["\']', img_tag)
        src = src_match.group(1) if src_match else 'unknown'
        
        # Extract alt
        alt_match = re.search(r'alt=["\'](.*?)["\']', img_tag)
        alt = alt_match.group(1) if alt_match else 'MISSING'
        
        images.append({
            'src': src,
            'alt': alt,
            'tag': img_tag,
            'file': filepath.name
        })
    
    return images

def categorize_alt_quality(alt_text):
    """Categorize Alt text quality"""
    if alt_text == 'MISSING' or alt_text == '':
        return 'missing'
    elif len(alt_text) < 10:
        return 'too_short'
    elif len(alt_text) > 125:
        return 'too_long'
    elif alt_text.lower() in ['image', 'photo', 'picture', 'img']:
        return 'generic'
    else:
        return 'good'

def analyze_site_images():
    """Analyze all images across the site"""
    print("🔍 Analyzing image Alt text across the site...\n")
    
    all_images = []
    issues = defaultdict(list)
    
    # Scan all HTML files
    for html_file in Path('.').rglob('*.html'):
        if '.git' in str(html_file) or '.venv' in str(html_file):
            continue
        
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        images = extract_images_with_alt(content, html_file)
        all_images.extend(images)
        
        for img in images:
            quality = categorize_alt_quality(img['alt'])
            if quality != 'good':
                issues[quality].append(img)
    
    # Print summary
    print(f"📊 Found {len(all_images)} images across the site\n")
    
    print("✅ Quality Summary:")
    good_count = len([img for img in all_images if categorize_alt_quality(img['alt']) == 'good'])
    print(f"  • Good Alt text: {good_count} ({good_count*100//len(all_images) if all_images else 0}%)")
    
    for category, imgs in issues.items():
        print(f"  • {category.replace('_', ' ').title()}: {len(imgs)}")
    
    # Detailed issues
    if issues:
        print("\n⚠️ Issues Found:\n")
        
        if 'missing' in issues:
            print(f"❌ Missing Alt Text ({len(issues['missing'])} images):")
            for img in issues['missing'][:5]:  # Show first 5
                print(f"  {img['file']}: {img['src']}")
            if len(issues['missing']) > 5:
                print(f"  ... and {len(issues['missing']) - 5} more")
            print()
        
        if 'too_short' in issues:
            print(f"⚠️  Too Short Alt Text ({len(issues['too_short'])} images):")
            for img in issues['too_short'][:5]:
                print(f"  {img['file']}: \"{img['alt']}\" → {img['src']}")
            if len(issues['too_short']) > 5:
                print(f"  ... and {len(issues['too_short']) - 5} more")
            print()
        
        if 'generic' in issues:
            print(f"⚠️  Generic Alt Text ({len(issues['generic'])} images):")
            for img in issues['generic'][:5]:
                print(f"  {img['file']}: \"{img['alt']}\"")
            if len(issues['generic']) > 5:
                print(f"  ... and {len(issues['generic']) - 5} more")
            print()
    
    print("\n💡 Recommendations:")
    print("  • Alt text should be 10-125 characters")
    print("  • Describe what's IN the image, not 'image of'")
    print("  • Include relevant keywords naturally")
    print("  • For decorative images, use alt=\"\"")
    
    return all_images, issues

if __name__ == "__main__":
    analyze_site_images()
