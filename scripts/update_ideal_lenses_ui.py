#!/usr/bin/env python3
"""
Unify Ideal Lenses section UI across all review pages.
Target format: recommendations-grid + recommendation-card + section-title
"""

import os
import re

REVIEWS_DIR = "src/pages/reviews"

# Files to update (excluding Z6 III which has correct format and template)
FILES_TO_UPDATE = [
    "sony-a7-iv-review.astro",
    "canon-r5-ii-review.astro",
    "panasonic-s5-ii-review.astro",
    "sony-a7c-ii-review.astro",
    "fujifilm-x-t5-review.astro",
    "sony-a7-v-review.astro",
    "fujifilm-x-s20-review.astro",
    "canon-eos-r8-review.astro",
    "om-system-om-1-ii-review.astro",
    "nikon-z8-review.astro",
    "sony-zv-e10-review.astro",
    "dji-osmo-pocket-3-review.astro",
]

# Camera name mappings for section titles
CAMERA_NAMES = {
    "sony-a7-iv-review.astro": "Sony A7 IV",
    "canon-r5-ii-review.astro": "Canon R5 Mark II",
    "panasonic-s5-ii-review.astro": "Panasonic S5 II",
    "sony-a7c-ii-review.astro": "Sony A7C II",
    "fujifilm-x-t5-review.astro": "Fujifilm X-T5",
    "sony-a7-v-review.astro": "Sony A7 V",
    "fujifilm-x-s20-review.astro": "Fujifilm X-S20",
    "canon-eos-r8-review.astro": "Canon EOS R8",
    "om-system-om-1-ii-review.astro": "OM System OM-1 II",
    "nikon-z8-review.astro": "Nikon Z8",
    "sony-zv-e10-review.astro": "Sony ZV-E10",
    "dji-osmo-pocket-3-review.astro": "DJI Osmo Pocket 3",
}

def update_file(filepath):
    """Update Ideal Lenses section in a file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    filename = os.path.basename(filepath)
    camera_name = CAMERA_NAMES.get(filename, "Camera")
    
    # Update section title to include camera name
    content = re.sub(
        r'<h2>Ideal Lenses</h2>',
        f'<h2 class="section-title">Ideal Lenses for the {camera_name}</h2>',
        content
    )
    
    # Update container class
    content = re.sub(
        r'<div class="grid">(\s*<article class="card card-plain">)',
        '<div class="recommendations-grid"><div class="recommendation-card">',
        content,
        count=1
    )
    
    # Update card elements
    content = re.sub(
        r'</article>(\s*)<article class="card card-plain">',
        '</div>\\1<div class="recommendation-card">',
        content
    )
    
    # Update closing tags
    content = re.sub(
        r'</article>(\s*)</div>(\s*)</section>(\s*<section class="section")',
        '</div>\\1</div>\\2</section>\\3',
        content
    )
    
    # Also handle cases where it's the last section before affiliate
    content = re.sub(
        r'</article>(\s*)</div>(\s*)</section>(\s*<!-- Affiliate|\s*<section class="section" id="affiliate")',
        '</div>\\1</div>\\2</section>\\3',
        content
    )
    
    # Update h3 to h4 in recommendation cards
    content = re.sub(
        r'<div class="recommendation-card">\s*<h3>([^<]+)</h3>',
        lambda m: f'<div class="recommendation-card"><h4>{m.group(1)}</h4>',
        content
    )
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ Updated: {filename}")
        return True
    else:
        print(f"○ No changes: {filename}")
        return False

def main():
    updated_count = 0
    for filename in FILES_TO_UPDATE:
        filepath = os.path.join(REVIEWS_DIR, filename)
        if os.path.exists(filepath):
            if update_file(filepath):
                updated_count += 1
        else:
            print(f"✗ Not found: {filename}")
    
    print(f"\n✓ Updated {updated_count}/{len(FILES_TO_UPDATE)} files")

if __name__ == "__main__":
    main()
