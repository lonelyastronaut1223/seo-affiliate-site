#!/usr/bin/env python3
"""
Properly reorder homepage sections in index.html.
Target order: guides → reviews → deals → compare → lenses → gear
"""

import re

def reorder_sections_properly(html_path):
    """Reorder sections in index.html properly"""
    
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find each section with its full content
    sections = {}
    
    # Pattern to match each section
    section_ids = ['guides', 'reviews', 'deals', 'compare', 'lenses', 'gear']
    
    for section_id in section_ids:
        # Match from <section class="section" id="xxx"> to </section>
        # Also capture any comment before it
        pattern = rf'(\s*(?:<!-- [^>]+ -->\s*)?<section class="section" id="{section_id}">.*?</section>)'
        match = re.search(pattern, content, re.DOTALL)
        if match:
            sections[section_id] = match.group(1)
            print(f"✓ Found section: {section_id}")
        else:
            print(f"✗ Could not find section: {section_id}")
    
    # Find the marker between quiz section and first content section
    quiz_end_pattern = r'(</section>\s*</section>\s*)'
    quiz_match = re.search(quiz_end_pattern, content[:2000], re.DOTALL)
    
    # Find where sections start (after camera-finder)
    sections_start_pattern = r'(</section>\s*\n\s*<section class="section" id="guides")'
    start_match = re.search(sections_start_pattern, content, re.DOTALL)
    
    if not start_match:
        print("Could not find section start pattern")
        return
    
    # Find where sections end (before affiliate section)
    sections_end_pattern = r'(</section>\s*\n\s*<section class="section highlight" id="affiliate")'
    end_match = re.search(sections_end_pattern, content, re.DOTALL)
    
    if not end_match:
        print("Could not find section end pattern")
        return
    
    # Get content before and after the sections to reorder
    start_pos = start_match.start() + len('</section>')
    end_pos = end_match.start() + len('</section>')
    
    content_before = content[:start_pos]
    content_after = content[end_pos:]
    
    # Build new sections in correct order
    target_order = ['guides', 'reviews', 'deals', 'compare', 'lenses', 'gear']
    
    new_sections_content = "\n"
    for section_id in target_order:
        if section_id in sections:
            new_sections_content += sections[section_id].strip() + "\n\n"
    
    # Combine
    new_content = content_before + "\n" + new_sections_content.strip() + "\n\n    "
    new_content += content_after.lstrip()
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"\n✅ Reordered sections to: {' → '.join(target_order)}")

if __name__ == '__main__':
    import sys
    html_path = sys.argv[1] if len(sys.argv) > 1 else '/Users/taylor/Downloads/Project/SEO-Affiliate/seo-affiliate-site/index.html'
    reorder_sections_properly(html_path)
