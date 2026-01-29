#!/usr/bin/env python3
"""
Proper HTML to Astro Conversion - Preserves ALL content exactly
Extracts content between </header> and <footer> and wraps with BaseLayout
"""

import os
import re
from pathlib import Path

PROJECT_ROOT = Path("/Users/taylor/Downloads/Project/SEO-Affiliate/seo-affiliate-site")
PAGES_DIR = PROJECT_ROOT / "src" / "pages"

def extract_title(html: str) -> str:
    """Extract title from HTML."""
    match = re.search(r'<title>(.*?)</title>', html, re.IGNORECASE | re.DOTALL)
    return match.group(1).strip() if match else "cameraupick"

def extract_description(html: str) -> str:
    """Extract meta description from HTML."""
    match = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', html, re.IGNORECASE)
    if not match:
        match = re.search(r'<meta\s+content=["\'](.*?)["\']\s+name=["\']description["\']', html, re.IGNORECASE)
    return match.group(1).strip() if match else "Camera reviews and buying guides."

def extract_body_content(html: str) -> str:
    """Extract everything from </header> to <footer, preserving hero section."""
    # Find content after </header> and before <footer
    match = re.search(r'</header>\s*(.*?)\s*<footer', html, re.IGNORECASE | re.DOTALL)
    if match:
        return match.group(1).strip()
    
    # Fallback: extract main content
    match = re.search(r'<main[^>]*>(.*?)</main>', html, re.IGNORECASE | re.DOTALL)
    if match:
        return f"<main>{match.group(1)}</main>"
    
    return ""

def calculate_layout_path(file_path: Path) -> str:
    """Calculate the relative path to BaseLayout from the file location."""
    relative = file_path.relative_to(PAGES_DIR)
    depth = len(relative.parts) - 1
    if depth == 0:
        return "../layouts/BaseLayout.astro"
    else:
        return "../" * depth + "../layouts/BaseLayout.astro"

def escape_for_astro(content: str) -> str:
    """Escape content that might conflict with Astro/JSX syntax."""
    # Replace { and } with their HTML entities inside content (but not in attributes)
    # This is a simple approach - may need refinement for complex cases
    return content

def convert_html_to_astro(html_path: Path, output_path: Path) -> bool:
    """Convert a single HTML file to Astro format."""
    try:
        with open(html_path, 'r', encoding='utf-8') as f:
            html = f.read()
        
        title = extract_title(html)
        description = extract_description(html)
        content = extract_body_content(html)
        layout_path = calculate_layout_path(output_path)
        
        if not content:
            print(f"  ⚠ No content extracted: {html_path.name}")
            return False
        
        # Escape special characters for Astro
        title_escaped = title.replace('"', '\\"')
        description_escaped = description.replace('"', '\\"')
        
        # Build Astro file
        astro_content = f'''---
import BaseLayout from '{layout_path}';
---

<BaseLayout title="{title_escaped}" description="{description_escaped}">
{content}
</BaseLayout>
'''
        
        # Ensure output directory exists
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Write .astro file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(astro_content)
        
        print(f"  ✓ {html_path.name} → {output_path.name}")
        return True
        
    except Exception as e:
        print(f"  ✗ Error: {html_path.name}: {e}")
        return False

def main():
    print("🔄 Converting HTML to Astro (Exact Replica)")
    print("=" * 50)
    
    # Find all HTML files in root and subdirectories
    html_dirs = [
        (PROJECT_ROOT, PAGES_DIR),  # Root HTML files
        (PROJECT_ROOT / "guides", PAGES_DIR / "guides"),
        (PROJECT_ROOT / "reviews", PAGES_DIR / "reviews"),
        (PROJECT_ROOT / "lenses", PAGES_DIR / "lenses"),
        (PROJECT_ROOT / "gear", PAGES_DIR / "gear"),
        (PROJECT_ROOT / "compare", PAGES_DIR / "compare"),
        (PROJECT_ROOT / "de", PAGES_DIR / "de"),
    ]
    
    success = 0
    failed = 0
    
    for src_dir, dest_dir in html_dirs:
        if not src_dir.exists():
            continue
            
        # Get HTML files in this directory (not recursive for subdirs)
        if src_dir == PROJECT_ROOT:
            html_files = [f for f in src_dir.glob("*.html") if f.name != "404.html"]
        else:
            html_files = list(src_dir.rglob("*.html"))
        
        for html_path in html_files:
            # Calculate relative path for nested files
            if src_dir == PROJECT_ROOT:
                rel_path = html_path.name
            else:
                rel_path = html_path.relative_to(src_dir)
            
            output_path = dest_dir / str(rel_path).replace('.html', '.astro')
            
            if convert_html_to_astro(html_path, output_path):
                success += 1
            else:
                failed += 1
    
    print("\n" + "=" * 50)
    print(f"✅ Converted: {success}")
    print(f"❌ Failed: {failed}")

if __name__ == "__main__":
    main()
