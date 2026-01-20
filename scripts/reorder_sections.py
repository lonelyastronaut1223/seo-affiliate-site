#!/usr/bin/env python3
"""
Reorder homepage sections to the new specified order.
"""

import re

def reorder_sections(html_path):
    """Reorder sections in index.html"""
    
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Define section boundaries using regex
    section_pattern = r'(<section class="section" id=".*?".*?</section>)'
    
    # Extract all sections
    sections_dict = {}
    
    # Find Guides (line ~456)
    guides_match = re.search(r'(<section class="section" id="guides">.*?</section>)', content, re.DOTALL)
    if guides_match:
        sections_dict['guides'] = guides_match.group(1)
    
    # Find Lenses (line ~556)
    lenses_match = re.search(r'(<!-- Lenses Section -->.*?<section class="section" id="lenses">.*?</section>)', content, re.DOTALL)
    if lenses_match:
        sections_dict['lenses'] = lenses_match.group(1)
    
    # Find Gear (line ~591)
    gear_match = re.search(r'(<!-- Gear Section -->.*?<section class="section" id="gear">.*?</section>)', content, re.DOTALL)
    if gear_match:
        sections_dict['gear'] = gear_match.group(1)
    
    # Find Deals (line ~626)
    deals_match = re.search(r'(<!-- Deals Section.*?<section class="section" id="deals">.*?</section>)', content, re.DOTALL)
    if deals_match:
        sections_dict['deals'] = deals_match.group(1)
    
    # Find Reviews (line ~666)
    reviews_match = re.search(r'(<section class="section" id="reviews">.*?</section>)', content, re.DOTALL)
    if reviews_match:
        sections_dict['reviews'] = reviews_match.group(1)
    
    # Find Compare (line ~770)
    compare_match = re.search(r'(<section class="section" id="compare">.*?</section>)', content, re.DOTALL)
    if compare_match:
        sections_dict['compare'] = compare_match.group(1)
    
    # Remove all sections first
    for section_name, section_content in sections_dict.items():
        content = content.replace(section_content, f'___PLACEHOLDER_{section_name.upper()}___')
    
    # Now replace in new order: Guides → Reviews → Deals → Compare → Lenses → Gear
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
    index_html = '/Users/taylor/Downloads/Project/SEO-Affiliate/seo-affiliate-site/index.html'
    reorder_sections(index_html)
