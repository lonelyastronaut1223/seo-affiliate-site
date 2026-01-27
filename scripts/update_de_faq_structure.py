#!/usr/bin/env python3
"""
Update DE review pages with unified FAQ structure.
Same logic as EN version, adapted for German pages.
"""

import re
import os

REVIEWS_DIR = "src/pages/de/reviews"

# All DE review files
DE_FILES = [
    "canon-eos-r8-review.astro",
    "canon-r5-ii-review.astro",
    "dji-osmo-pocket-3-review.astro",
    "fujifilm-x-s20-review.astro",
    "fujifilm-x-t5-review.astro",
    "nikon-z6-iii-review.astro",
    "nikon-z8-review.astro",
    "om-system-om-1-ii-review.astro",
    "panasonic-s5-ii-review.astro",
    "sony-a7-iv-review.astro",
    "sony-a7-v-review.astro",
    "sony-a7c-ii-review.astro",
    "sony-zv-e10-review.astro",
]

# Camera names for German FAQ titles
CAMERA_NAMES = {
    "canon-eos-r8-review.astro": "Canon EOS R8",
    "canon-r5-ii-review.astro": "Canon R5 Mark II",
    "dji-osmo-pocket-3-review.astro": "DJI Osmo Pocket 3",
    "fujifilm-x-s20-review.astro": "Fujifilm X-S20",
    "fujifilm-x-t5-review.astro": "Fujifilm X-T5",
    "nikon-z6-iii-review.astro": "Nikon Z6 III",
    "nikon-z8-review.astro": "Nikon Z8",
    "om-system-om-1-ii-review.astro": "OM System OM-1 II",
    "panasonic-s5-ii-review.astro": "Panasonic S5 II",
    "sony-a7-iv-review.astro": "Sony A7 IV",
    "sony-a7-v-review.astro": "Sony A7 V",
    "sony-a7c-ii-review.astro": "Sony A7C II",
    "sony-zv-e10-review.astro": "Sony ZV-E10",
}

# Pattern to match old FAQ structure
OLD_FAQ_PATTERN = re.compile(
    r'<h3>\s*<button class="faq-toggle" aria-expanded="false">\s*'
    r'<span class="faq-icon"></span>\s*'
    r'(.+?)\s*</button>\s*</h3>',
    re.DOTALL
)

def convert_faq_item(match):
    """Convert old FAQ structure to new format."""
    question = match.group(1).strip()
    return f'''<h3 class="faq-question">
              {question}
              <span class="faq-toggle">+</span>
            </h3>'''

def update_file(filepath):
    """Update a single DE review file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    filename = os.path.basename(filepath)
    camera_name = CAMERA_NAMES.get(filename, "Kamera")
    
    # Update section header (German: "Häufig gestellte Fragen" or "FAQ")
    content = re.sub(
        r'<section class="section">\s*<h2>(?:Häufig gestellte Fragen|FAQ|Frequently Asked Questions)</h2>',
        f'<section class="section faq-section">\n        <h2 class="section-title">{camera_name} FAQ</h2>',
        content
    )
    
    # Update FAQ items
    content = OLD_FAQ_PATTERN.sub(convert_faq_item, content)
    
    # Add max-height style to faq-answer if missing
    content = re.sub(
        r'<div class="faq-answer">(?!\s*style)',
        '<div class="faq-answer" style="max-height: 0; overflow: hidden;">',
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
    for filename in DE_FILES:
        filepath = os.path.join(REVIEWS_DIR, filename)
        if os.path.exists(filepath):
            if update_file(filepath):
                updated_count += 1
        else:
            print(f"✗ Not found: {filename}")
    
    print(f"\n✓ Updated {updated_count}/{len(DE_FILES)} DE files")

if __name__ == "__main__":
    main()
