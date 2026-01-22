#!/usr/bin/env python3
"""
Script to unify page layout to narrow card style.
Moves hero section inside the container for all Astro pages.
"""

import os
import re

def fix_layout(content):
    """
    Convert structure from:
        <section class="hero">...</section>
        <main class="container"> or <main id="main" class="container">
    
    To:
        <main id="main" class="container">
        <section class="hero">...</section>
    """
    
    # Pattern to find hero section followed by main container
    # This handles the case where hero is OUTSIDE the main container
    pattern = r'(<section\s+class="hero"[^>]*>.*?</section>)\s*\n\s*(<main[^>]*class="container"[^>]*>)'
    
    def replacement(match):
        hero_section = match.group(1)
        main_tag = match.group(2)
        # Put main tag first, then hero inside
        return f'{main_tag}\n    {hero_section}'
    
    # Apply the fix
    fixed = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    return fixed


def process_file(filepath):
    """Process a single Astro file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if this file has the pattern we need to fix
    # Hero OUTSIDE container pattern
    if re.search(r'<section\s+class="hero".*?</section>\s*\n\s*<main[^>]*class="container"', content, re.DOTALL):
        fixed = fix_layout(content)
        if fixed != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(fixed)
            return True
    return False


def main():
    pages_dir = '/Users/taylor/Downloads/Project/SEO-Affiliate/seo-affiliate-site/src/pages'
    
    modified_count = 0
    
    for root, dirs, files in os.walk(pages_dir):
        for filename in files:
            if filename.endswith('.astro'):
                filepath = os.path.join(root, filename)
                if process_file(filepath):
                    print(f"✓ Fixed: {filepath}")
                    modified_count += 1
    
    print(f"\n✅ Modified {modified_count} files")


if __name__ == '__main__':
    main()
