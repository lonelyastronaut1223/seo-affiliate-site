#!/usr/bin/env python3
"""
Add Last Updated dates and related posts to all pages for SEO freshness.
"""

import re
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).parent.parent.parent

# Current date for updates
CURRENT_DATE = "2026-01-18"
CURRENT_DATE_DE = "18. Januar 2026"
CURRENT_DATE_EN = "January 18, 2026"


def add_last_updated(file_path: Path) -> bool:
    """Add last updated meta tag and visible date to a page."""
    print(f"Processing: {file_path.name}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    
    # Check if already has last-modified meta
    if 'article:modified_time' not in content:
        # Add meta tag in head section
        meta_tag = f'  <meta property="article:modified_time" content="{CURRENT_DATE}T12:00:00+01:00">\n'
        
        # Insert before </head>
        if '</head>' in content:
            content = content.replace('</head>', f'{meta_tag}</head>')
            modified = True
            print(f"  ✓ Added modified_time meta")
    
    # Check if already has dateModified in schema
    if '"dateModified"' not in content and '"datePublished"' in content:
        # Already has datePublished, add dateModified after it
        content = re.sub(
            r'("datePublished"\s*:\s*"[^"]*")',
            f'\\1,\n    "dateModified": "{CURRENT_DATE}"',
            content
        )
        modified = True
        print(f"  ✓ Added dateModified to schema")
    
    if modified:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    else:
        print(f"  - Already has dates or not applicable")
        return False


def main():
    """Process all HTML pages."""
    updated_count = 0
    
    # Process all HTML files except includes
    for html_file in BASE_DIR.rglob('*.html'):
        if 'includes' in str(html_file) or '.git' in str(html_file):
            continue
        if add_last_updated(html_file):
            updated_count += 1
    
    print(f"\n{'='*60}")
    print(f"Last Updated Dates Added")
    print(f"Updated: {updated_count} pages")
    print(f"{'='*60}")


if __name__ == '__main__':
    main()
