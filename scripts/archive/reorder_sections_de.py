#!/usr/bin/env python3
"""
Reorder German (DE) homepage sections to match EN.
"""

import re

def reorder_sections_de(html_path):
    """Reorder sections in de/index.html"""
    
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract all sections
    sections_dict = {}
    
    # Find Deals (Angebote) - should be at top currently
    deals_match = re.search(r'(<!-- Angebote Section.*?<section class="section" id="deals">.*?</section>)', content, re.DOTALL)
    if deals_match:
        sections_dict['deals'] = deals_match.group(1)
    
    # Find Guides (Kaufberatungen)
    guides_match = re.search(r'(<section class="section" id="guides">.*?</section>)', content, re.DOTALL)
    if guides_match:
        sections_dict['guides'] = guides_match.group(1)
    
    # Find Lenses (Objektive)
    lenses_match = re.search(r'(<!-- Objektive Section -->.*?<section class="section" id="objektive">.*?</section>)', content, re.DOTALL)
    if lenses_match:
        sections_dict['lenses'] = lenses_match.group(1)
    
    # Find Gear (Zubehör)
    gear_match = re.search(r'(<!-- Zubehör Section -->.*?<section class="section" id="zubehoer">.*?</section>)', content, re.DOTALL)
    if gear_match:
        sections_dict['gear'] = gear_match.group(1)
    
    # Find Reviews (Testberichte)
    reviews_match = re.search(r'(<section class="section" id="reviews">.*?</section>)', content, re.DOTALL)
    if reviews_match:
        sections_dict['reviews'] = reviews_match.group(1)
    
    # Find Compare (Vergleiche)
    compare_match = re.search(r'(<section class="section" id="compare">.*?</section>)', content, re.DOTALL)
    if compare_match:
        sections_dict['compare'] = compare_match.group(1)
    
    # Remove all sections first
    for section_name, section_content in sections_dict.items():
        content = content.replace(section_content, f'___PLACEHOLDER_{section_name.upper()}___')
    
    # New order to match EN: Guides → Reviews → Deals → Compare → Lenses → Gear
    new_order = ['guides', 'reviews', 'deals', 'compare', 'lenses', 'gear']
    
    for section_name in new_order:
        if section_name in sections_dict:
            content = content.replace(
                f'___PLACEHOLDER_{section_name.upper()}___',
                sections_dict[section_name]
            )
    
    # Write back
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✓ Reordered sections in {html_path}")
    print(f"  New order: {' → '.join(new_order)}")

if __name__ == '__main__':
    index_de = '/Users/taylor/Downloads/Project/SEO-Affiliate/seo-affiliate-site/de/index.html'
    reorder_sections_de(index_de)
