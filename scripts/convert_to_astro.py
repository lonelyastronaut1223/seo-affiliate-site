#!/usr/bin/env python3
"""
Automated HTML to Astro Conversion Script
Converts all HTML files in src/pages to use BaseLayout.astro
"""

import os
import re
from pathlib import Path

PAGES_DIR = Path("/Users/taylor/Downloads/Project/SEO-Affiliate/seo-affiliate-site/src/pages")

def extract_title(html: str) -> str:
    """Extract title from HTML."""
    match = re.search(r'<title>(.*?)</title>', html, re.IGNORECASE | re.DOTALL)
    return match.group(1).strip() if match else "Camera Reviews"

def extract_description(html: str) -> str:
    """Extract meta description from HTML."""
    match = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', html, re.IGNORECASE)
    if not match:
        match = re.search(r'<meta\s+content=["\'](.*?)["\']\s+name=["\']description["\']', html, re.IGNORECASE)
    return match.group(1).strip() if match else "Camera reviews and buying guides."

def extract_main_content(html: str) -> str:
    """Extract content between <main> tags, or between </header> and <footer>."""
    # Try to find <main>...</main>
    match = re.search(r'<main[^>]*>(.*?)</main>', html, re.IGNORECASE | re.DOTALL)
    if match:
        return match.group(1).strip()
    
    # Fallback: Find content between header and footer
    match = re.search(r'</header>\s*(.*?)\s*<footer', html, re.IGNORECASE | re.DOTALL)
    if match:
        return match.group(1).strip()
    
    # Last fallback: Find body content
    match = re.search(r'<body[^>]*>(.*?)</body>', html, re.IGNORECASE | re.DOTALL)
    if match:
        content = match.group(1)
        # Remove header and footer if present
        content = re.sub(r'<header[^>]*>.*?</header>', '', content, flags=re.IGNORECASE | re.DOTALL)
        content = re.sub(r'<footer[^>]*>.*?</footer>', '', content, flags=re.IGNORECASE | re.DOTALL)
        return content.strip()
    
    return ""

def calculate_layout_path(file_path: Path) -> str:
    """Calculate the relative path to BaseLayout from the file location."""
    relative = file_path.relative_to(PAGES_DIR)
    depth = len(relative.parts) - 1  # Subtract 1 for the filename itself
    if depth == 0:
        return "../layouts/BaseLayout.astro"
    else:
        return "../" * depth + "../layouts/BaseLayout.astro"

def convert_html_to_astro(html_path: Path) -> bool:
    """Convert a single HTML file to Astro format."""
    try:
        with open(html_path, 'r', encoding='utf-8') as f:
            html = f.read()
        
        title = extract_title(html)
        description = extract_description(html)
        content = extract_main_content(html)
        layout_path = calculate_layout_path(html_path)
        
        if not content:
            print(f"  ⚠ No content extracted: {html_path.name}")
            return False
        
        # Build Astro file
        astro_content = f'''---
import BaseLayout from '{layout_path}';
---

<BaseLayout title="{title}" description="{description}">
{content}
</BaseLayout>
'''
        
        # Write .astro file
        astro_path = html_path.with_suffix('.astro')
        with open(astro_path, 'w', encoding='utf-8') as f:
            f.write(astro_content)
        
        # Remove original HTML file
        os.remove(html_path)
        
        print(f"  ✓ Converted: {html_path.name} → {astro_path.name}")
        return True
        
    except Exception as e:
        print(f"  ✗ Error converting {html_path.name}: {e}")
        return False

def main():
    print("🔄 Starting HTML to Astro Conversion")
    print("=" * 50)
    
    # Find all HTML files
    html_files = list(PAGES_DIR.rglob("*.html"))
    print(f"Found {len(html_files)} HTML files to convert\n")
    
    success = 0
    failed = 0
    
    for html_path in html_files:
        if convert_html_to_astro(html_path):
            success += 1
        else:
            failed += 1
    
    print("\n" + "=" * 50)
    print(f"✅ Converted: {success}")
    print(f"❌ Failed: {failed}")
    print(f"📊 Total: {len(html_files)}")

if __name__ == "__main__":
    main()
