#!/usr/bin/env python3
"""
Add Anime.js library and animations script to all HTML pages.
"""

import re
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent

# Scripts to add before </body>
ANIME_SCRIPTS = '''
  <!-- Anime.js Animation Library -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/animejs/3.2.2/anime.min.js" defer></script>
  <script src="{assets_path}assets/js/animations.js" defer></script>
'''


def add_anime_to_page(file_path: Path) -> bool:
    """Add anime.js scripts to a page."""
    print(f"Processing: {file_path.name}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if already has anime.js
    if 'animejs' in content or 'animations.js' in content:
        print(f"  - Already has anime.js")
        return False
    
    # Determine assets path based on file location
    rel_path = file_path.relative_to(BASE_DIR)
    depth = len(rel_path.parts) - 1  # -1 for the file itself
    assets_path = '../' * depth
    
    scripts = ANIME_SCRIPTS.format(assets_path=assets_path)
    
    # Insert before </body>
    if '</body>' in content:
        content = content.replace('</body>', f'{scripts}</body>')
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"  ✓ Added anime.js scripts")
        return True
    
    return False


def main():
    """Process all HTML pages."""
    updated_count = 0
    
    # Process all HTML files
    for html_file in BASE_DIR.rglob('*.html'):
        if '.git' in str(html_file) or 'includes' in str(html_file):
            continue
        if add_anime_to_page(html_file):
            updated_count += 1
    
    print(f"\n{'='*60}")
    print(f"Anime.js Added")
    print(f"Updated: {updated_count} pages")
    print(f"{'='*60}")


if __name__ == '__main__':
    main()
