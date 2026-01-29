#!/usr/bin/env python3
"""
Fix incorrect FAQ structure in review pages.
Convert wrong: h3.faq-question + span.faq-toggle with "+"
To correct: button.faq-toggle + span.faq-icon (matching X-T5 pattern)
"""

import re
import os

# Files with incorrect structure
FILES_TO_FIX = [
    "src/pages/reviews/_review-template.astro",
    "src/pages/reviews/nikon-z6-iii-review.astro",
    "src/pages/de/reviews/canon-r5-ii-review.astro",
    "src/pages/de/reviews/fujifilm-x-s20-review.astro",
    "src/pages/de/reviews/nikon-z6-iii-review.astro",
    "src/pages/de/reviews/om-system-om-1-ii-review.astro",
    "src/pages/de/reviews/sony-a7-v-review.astro",
]

# Pattern to match wrong FAQ structure
WRONG_FAQ_PATTERN = re.compile(
    r'<h3 class="faq-question">\s*([^<]+)\s*<span class="faq-toggle">\+</span>\s*</h3>',
    re.DOTALL
)

def convert_faq_item(match):
    """Convert wrong FAQ structure to correct format."""
    question = match.group(1).strip()
    return f'''<h3>
            <button class="faq-toggle" aria-expanded="false">
              <span class="faq-icon"></span>
              {question}
            </button>
          </h3>'''

def fix_file(filepath):
    """Fix FAQ structure in a single file."""
    if not os.path.exists(filepath):
        print(f"✗ Not found: {filepath}")
        return False
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Fix FAQ structure
    content = WRONG_FAQ_PATTERN.sub(convert_faq_item, content)
    
    # Also fix section titles if they have non-standard format
    content = re.sub(
        r'<section class="section faq-section">\s*<h2 class="section-title">([^<]+)</h2>',
        r'<section class="section">\n      <h2>\1</h2>',
        content
    )
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ Fixed: {filepath}")
        return True
    else:
        print(f"○ No changes needed: {filepath}")
        return False

def main():
    fixed_count = 0
    for filepath in FILES_TO_FIX:
        if fix_file(filepath):
            fixed_count += 1
    
    print(f"\n✓ Fixed {fixed_count}/{len(FILES_TO_FIX)} files")

if __name__ == "__main__":
    main()
