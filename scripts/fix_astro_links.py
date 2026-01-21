#!/usr/bin/env python3
"""
Fix internal links in Astro files to use clean URLs (without .html suffix).
Also fixes relative CSS/JS paths to use absolute /assets/ paths.
"""

import os
import re
from pathlib import Path

PAGES_DIR = Path("/Users/taylor/Downloads/Project/SEO-Affiliate/seo-affiliate-site/src/pages")

def fix_links_in_file(file_path: Path) -> tuple[int, int]:
    """Fix links in a single Astro file. Returns (links_fixed, css_fixed)."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        links_fixed = 0
        css_fixed = 0
        
        # 1. Fix internal .html links to clean URLs
        # Pattern: href="something.html" -> href="/something/"
        # But NOT for anchor links or external URLs
        
        def fix_href(match):
            nonlocal links_fixed
            full_match = match.group(0)
            href_value = match.group(1)
            
            # Skip external links, anchors, javascript, mailto
            if any(href_value.startswith(x) for x in ['http', '#', 'javascript:', 'mailto:', 'tel:']):
                return full_match
            
            # Skip if already clean URL (ends with /)
            if href_value.endswith('/'):
                return full_match
            
            # Skip non-html files
            if not href_value.endswith('.html'):
                return full_match
            
            # Convert to clean URL
            # Remove .html suffix
            clean_path = href_value[:-5]  # Remove ".html"
            
            # Ensure it starts with /
            if not clean_path.startswith('/'):
                # Make it absolute based on current page depth
                clean_path = '/' + clean_path
            
            # Add trailing slash
            if not clean_path.endswith('/'):
                clean_path = clean_path + '/'
            
            links_fixed += 1
            return f'href="{clean_path}"'
        
        content = re.sub(r'href="([^"]*)"', fix_href, content)
        
        # 2. Fix relative CSS/JS paths to absolute
        # Pattern: ../assets/... or ../../assets/... -> /assets/...
        def fix_asset_path(match):
            nonlocal css_fixed
            attr = match.group(1)  # href or src
            path = match.group(2)
            
            # Skip if already absolute
            if path.startswith('/') or path.startswith('http'):
                return match.group(0)
            
            # Fix relative paths to assets
            if 'assets/' in path:
                # Extract the part starting from assets/
                asset_idx = path.find('assets/')
                clean_path = '/' + path[asset_idx:]
                css_fixed += 1
                return f'{attr}="{clean_path}"'
            
            return match.group(0)
        
        content = re.sub(r'(href|src)="([^"]*assets[^"]*)"', fix_asset_path, content)
        
        # 3. Fix German page links that use relative paths
        # Pattern: ../bewertungen/xxx.html -> /de/bewertungen/xxx/
        def fix_german_links(match):
            nonlocal links_fixed
            href = match.group(1)
            
            # Already fixed or external
            if href.startswith('/') or href.startswith('http'):
                return match.group(0)
            
            # Count ../ to determine depth
            depth = href.count('../')
            clean_href = href.replace('../', '')
            
            # Remove .html
            if clean_href.endswith('.html'):
                clean_href = clean_href[:-5]
            
            # Add trailing slash
            if not clean_href.endswith('/'):
                clean_href += '/'
            
            # Determine if this is a DE page linking to another DE page
            if 'de/' in str(file_path):
                # If linking within DE section
                if not clean_href.startswith('de/'):
                    clean_href = '/de/' + clean_href
                else:
                    clean_href = '/' + clean_href
            else:
                clean_href = '/' + clean_href
            
            links_fixed += 1
            return f'href="{clean_href}"'
        
        content = re.sub(r'href="(\.\./[^"]*)"', fix_german_links, content)
        
        # Only write if changed
        if content != original:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
        
        return links_fixed, css_fixed
        
    except Exception as e:
        print(f"  ✗ Error: {file_path.name}: {e}")
        return 0, 0

def main():
    print("🔗 Fixing Internal Links for Astro")
    print("=" * 50)
    
    astro_files = list(PAGES_DIR.rglob("*.astro"))
    print(f"Found {len(astro_files)} Astro files\n")
    
    total_links = 0
    total_css = 0
    files_modified = 0
    
    for file_path in astro_files:
        links, css = fix_links_in_file(file_path)
        if links > 0 or css > 0:
            print(f"  ✓ {file_path.name}: {links} links, {css} assets")
            files_modified += 1
        total_links += links
        total_css += css
    
    print("\n" + "=" * 50)
    print(f"✅ Fixed {total_links} internal links")
    print(f"✅ Fixed {total_css} asset paths")
    print(f"📁 Modified {files_modified} files")

if __name__ == "__main__":
    main()
