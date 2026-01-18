#!/usr/bin/env python3
"""
Replace the CSS-based author emoji with the professional image asset.
Targeting the specific <div> structure added by add_author.py.
"""

import re
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent

# The old HTML to replace
OLD_HTML_REGEX = r'<div style="width: 64px; height: 64px; background: var\(--accent\); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 28px;">📷</div>'

# The new HTML to insert
# Note: Using relative path from CSS/JS perspective or absolute path might be tricky.
# Since this is inserted into pages at different depths, we need to handle paths dynamically or use a root relative path if possible.
# However, the site structure is simple. Let's try to use a relative path logic or just hardcode root relative for simplicity if server supports it.
# Actually, add_author.py didn't handle depth for links either (it used ../about.html which assumes 1 level deep).
# Let's start with a generic replacement that assumes we are in a subfolder (most pages are reviews/guides).
# Better yet, let's use the same logic as add_anime_to_page to determine depth.

def update_author_image(file_path: Path) -> bool:
    """Update author avatar in a page."""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Determine assets path based on file location
    rel_path = file_path.relative_to(BASE_DIR)
    depth = len(rel_path.parts) - 1
    assets_prefix = '../' * depth
    
    # New HTML with correct path
    new_html = f'<img src="{assets_prefix}assets/images/team-avatar.png" alt="cameraupick Editorial Team" style="width: 64px; height: 64px; border-radius: 50%; object-fit: contain; background: white; border: 2px solid var(--accent); padding: 4px;">'

    # Perform replacement
    if re.search(OLD_HTML_REGEX, content):
        content = re.sub(OLD_HTML_REGEX, new_html, content)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"  ✓ Updated author avatar in {file_path.name}")
        return True
        
    return False


def main():
    """Process all HTML pages."""
    updated_count = 0
    
    # Process all HTML files
    for html_file in BASE_DIR.rglob('*.html'):
        if '.git' in str(html_file) or 'includes' in str(html_file):
            continue
        if update_author_image(html_file):
            updated_count += 1
    
    print(f"\n{'='*60}")
    print(f"Author Avatar Updated")
    print(f"Updated: {updated_count} pages")
    print(f"{'='*60}")


if __name__ == '__main__':
    main()
