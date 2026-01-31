#!/usr/bin/env python3
"""
Fix import paths for newly copied DE review files
"""

from pathlib import Path
import re

BASE_DIR = Path(__file__).parent.parent.parent
DE_REVIEWS = BASE_DIR / "src/pages/de/reviews"

# List of review files that need fixing (10 new ones)
NEW_REVIEWS = [
    "insta360-x4-review.astro",
    "gopro-hero-13-review.astro",
    "sony-a6700-review.astro",
    "panasonic-s5iix-review.astro",
    "sony-zv-1-ii-review.astro",
    "panasonic-g100d-review.astro",
    "om-system-om-5-review.astro",
    "dji-osmo-action-5-pro-review.astro",
    "canon-r6-ii-review.astro",
    "sony-fx3-review.astro"
]

def fix_imports(file_path):
    """Fix import paths in DE review file"""
    content = file_path.read_text(encoding="utf-8")
    original = content
    
    # Fix BaseLayout import
    content = re.sub(
        r'from "\.\./(.*?)/BaseLayout\.astro"',
        r'from "../../../layouts/BaseLayout.astro"',
        content
    )
    # Fix ProductSchema import
    content = re.sub(
        r'from "\.\./(.*?)/ProductSchema\.astro"',
        r'from "../../../components/ProductSchema.astro"',
        content
    )
    # Fix AuthorBio import
    content = re.sub(
        r'from "\.\./(.*?)/AuthorBio\.astro"',
        r'from "../../../components/AuthorBio.astro"',
        content
    )
    # Fix CSS import
    content = re.sub(
        r'import "\.\./(.*?)/review-page\.css"',
        r'import "../../../styles/review-page.css"',
        content
    )
    
    # Also fix missing styles import
    if 'review-page.css' not in content and 'class="review-' in content:
        # Add import after other imports
        content = re.sub(
            r'(import AuthorBio.*?;)',
            r'\1\nimport "../../../styles/review-page.css";',
            content
        )
    
    if content != original:
        file_path.write_text(content, encoding="utf-8")
        return True
    return False

def main():
    print("🔧 Fixing DE Review Import Paths\n")
    fixed = 0
    
    for filename in NEW_REVIEWS:
        file_path = DE_REVIEWS / filename
        if not file_path.exists():
            print(f"⚠️ {filename}: not found")
            continue
            
        if fix_imports(file_path):
            print(f"✅ {filename}: imports fixed")
            fixed += 1
        else:
            print(f"⏭️ {filename}: already correct")
    
    print(f"\n{'='*50}")
    print(f"✨ Fixed {fixed}/{len(NEW_REVIEWS)} files")
    print(f"{'='*50}\n")

if __name__ == "__main__":
    main()
