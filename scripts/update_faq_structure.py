#!/usr/bin/env python3
"""
Batch update review pages with unified FAQ structure.
Converts button-based FAQ to h3.faq-question + span.faq-toggle format.
"""

import re
import os

REVIEWS_DIR = "src/pages/reviews"

# Files that need updating (have button-based FAQ)
FILES_TO_UPDATE = [
    "nikon-z8-review.astro",
    "panasonic-s5-ii-review.astro", 
    "fujifilm-x-t5-review.astro",
    "canon-eos-r8-review.astro",
    "dji-osmo-pocket-3-review.astro",
    "sony-a7-v-review.astro",
    "sony-a7c-ii-review.astro",
    "sony-zv-e10-review.astro",
    "om-system-om-1-ii-review.astro",
]

# Pattern to match old FAQ structure
OLD_FAQ_PATTERN = re.compile(
    r'<h3>\s*<button class="faq-toggle" aria-expanded="false">\s*'
    r'<span class="faq-icon"></span>\s*'
    r'(.+?)\s*</button>\s*</h3>',
    re.DOTALL
)

# Pattern for section title
OLD_SECTION_PATTERN = re.compile(
    r'<section class="section">\s*<h2>Frequently Asked Questions</h2>',
    re.DOTALL
)

def get_camera_name(filename):
    """Extract camera name from filename for FAQ title."""
    name = filename.replace("-review.astro", "").replace("-", " ").title()
    # Fix common abbreviations
    name = name.replace("Dji", "DJI")
    name = name.replace("Om System Om 1 Ii", "OM System OM-1 II")
    name = name.replace("Zv E10", "ZV-E10")
    name = name.replace("A7 V", "A7 V")
    name = name.replace("A7C Ii", "A7C II")
    name = name.replace("S5 Ii", "S5 II")
    name = name.replace("X T5", "X-T5")
    name = name.replace("R5 Ii", "R5 II")
    name = name.replace("Eos R8", "EOS R8")
    name = name.replace("Z8", "Z8")
    return name

def convert_faq_item(match):
    """Convert old FAQ structure to new format."""
    question = match.group(1).strip()
    return f'''<h3 class="faq-question">
              {question}
              <span class="faq-toggle">+</span>
            </h3>'''

def update_file(filepath):
    """Update a single review file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Get camera name for section title
    filename = os.path.basename(filepath)
    camera_name = get_camera_name(filename)
    
    # Update section header
    content = re.sub(
        r'<section class="section">\s*<h2>Frequently Asked Questions</h2>',
        f'<section class="section faq-section">\n        <h2 class="section-title">{camera_name} FAQ</h2>',
        content
    )
    
    # Update FAQ items
    content = OLD_FAQ_PATTERN.sub(convert_faq_item, content)
    
    # Add max-height style to faq-answer if missing
    content = re.sub(
        r'<div class="faq-answer">',
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
