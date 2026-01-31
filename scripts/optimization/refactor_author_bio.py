#!/usr/bin/env python3
"""
Batch refactor review pages to use AuthorBio component
"""
import re
from pathlib import Path

REVIEW_DIR = Path("src/pages/reviews")

# Pattern to match the import section
IMPORT_PATTERN = r'(---\s*\nimport BaseLayout[^\n]+\nimport ProductSchema[^\n]+)'
IMPORT_REPLACEMENT = r'\1\nimport AuthorBio from "../../components/AuthorBio.astro";'

# Pattern to match the author box inline styles
AUTHOR_BOX_PATTERN = r'<!-- AUTHOR BOX -->\s*<section class="section author-box">\s*<div style="display: flex; gap: 16px; align-items: flex-start;">\s*<img[^>]+team-avatar\.webp[^>]+>\s*<div>\s*<h4[^>]*>Written by cameraupick Editorial Team</h4>\s*<p[^>]*>.*?</p>\s*<a href="/about"[^>]*>Learn more about our testing process →</a>\s*</div>\s*</div>\s*</section>'

AUTHOR_BOX_REPLACEMENT = '''<!-- AUTHOR BOX -->
        <section class="section author-box">
            <AuthorBio />
        </section>'''

def refactor_review_file(file_path: Path):
    """Refactor a single review file"""
    content = file_path.read_text(encoding='utf-8')
    
    # Check if already has AuthorBio import
    if 'import AuthorBio' in content:
        print(f"✓ {file_path.name} already refactored")
        return False
    
    # Check if has author box to replace
    if 'Written by cameraupick Editorial Team' not in content:
        print(f"⊘ {file_path.name} doesn't have author box")
        return False
    
    # Add import
    content = re.sub(IMPORT_PATTERN, IMPORT_REPLACEMENT, content, count=1)
    
    # Replace author box
    content = re.sub(AUTHOR_BOX_PATTERN, AUTHOR_BOX_REPLACEMENT, content, flags=re.DOTALL)
    
    # Write back
    file_path.write_text(content, encoding='utf-8')
    print(f"✅ Refactored {file_path.name}")
    return True

def main():
    review_files = list(REVIEW_DIR.glob("*-review.astro"))
    print(f"Found {len(review_files)} review files\n")
    
    refactored = 0
    for file_path in sorted(review_files):
        if refactor_review_file(file_path):
            refactored += 1
    
    print(f"\n📊 Refactored {refactored}/{len(review_files)} files")

if __name__ == "__main__":
    main()
