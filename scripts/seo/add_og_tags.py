#!/usr/bin/env python3
"""
Batch add missing Open Graph and Twitter Card meta tags to HTML pages.
"""

from pathlib import Path
import re

BASE_DIR = Path(__file__).parent.parent.parent

# Pages to fix (from audit results)
PAGES_TO_FIX = [
    # Reviews
    'reviews/sony-zv-e10-review.html',
    'reviews/canon-eos-r8-review.html',
    'reviews/sony-a7-iv-review.html',
    'reviews/sony-a7c-ii-review.html',
    'reviews/dji-osmo-pocket-3-review.html',
    'reviews/nikon-z8-review.html',
    'reviews/fujifilm-x-t5-review.html',
    'reviews/panasonic-s5-ii-review.html',
    # Guides
    'guides/best-full-frame-for-video.html',
    'guides/best-hybrid-camera.html',
    'guides/best-camera-for-beginners-2026.html',
    'guides/best-travel-camera.html',
    'guides/best-action-360-camera.html',
    'guides/best-budget-camera-under-800.html',
    'guides/best-vlog-camera.html',
    # Compare
    'compare/fujifilm-x-s20-vs-fujifilm-x-t5.html',
    'compare/sony-a7-v-vs-canon-r6-iii.html',
    'compare/sony-zv-e10-vs-sony-a6700.html',
]

def extract_page_info(content: str, file_path: Path) -> dict:
    """Extract title and description from existing meta tags."""
    # Get title
    title_match = re.search(r'<title[^>]*>(.+?)</title>', content, re.DOTALL)
    title = title_match.group(1).strip() if title_match else file_path.stem.replace('-', ' ').title()
    
    # Get description
    desc_match = re.search(r'<meta\s+name=["\']description["\']\s+content=["\']([^"\']+)["\']', content, re.I)
    description = desc_match.group(1).strip() if desc_match else f"Expert review and guide for {file_path.stem}"
    
    # Generate image path
    slug = file_path.stem
    if 'review' in str(file_path):
        # Extract camera name from slug
        camera = slug.replace('-review', '')
        image = f"https://cameraupick.com/assets/images/guides/{camera}.png"
    elif 'guide' in str(file_path) or 'best' in slug:
        image = f"https://cameraupick.com/assets/images/guides/{slug}.png"
    else:
        image = "https://cameraupick.com/assets/images/og-default.png"
    
    # Generate URL
    url = f"https://cameraupick.com/{file_path}"
    
    return {
        'title': title,
        'description': description[:160],  # Truncate to safe length
        'image': image,
        'url': url
    }

def generate_og_tags(info: dict) -> str:
    """Generate OG and Twitter meta tags."""
    return f'''  <!-- Open Graph / Twitter -->
  <meta property="og:type" content="article">
  <meta property="og:site_name" content="CameraUpick">
  <meta property="og:title" content="{info['title']}">
  <meta property="og:description" content="{info['description']}">
  <meta property="og:url" content="{info['url']}">
  <meta property="og:image" content="{info['image']}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{info['title']}">
  <meta name="twitter:description" content="{info['description']}">
  <meta name="twitter:image" content="{info['image']}">
'''

def add_og_tags(file_path: Path) -> bool:
    """Add OG tags to a file if missing."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if already has OG tags
    if 'og:title' in content:
        print(f"  ⏭️  {file_path.name} - already has OG tags")
        return False
    
    # Extract page info
    info = extract_page_info(content, file_path)
    og_tags = generate_og_tags(info)
    
    # Insert after <meta charset> and viewport
    # Look for a good insertion point
    insert_patterns = [
        r'(<meta\s+name=["\']viewport["\'][^>]*>)',
        r'(<meta\s+charset=[^>]*>)',
        r'(<head[^>]*>)'
    ]
    
    for pattern in insert_patterns:
        match = re.search(pattern, content, re.I)
        if match:
            insert_pos = match.end()
            new_content = content[:insert_pos] + '\n' + og_tags + content[insert_pos:]
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"  ✅ {file_path.name} - added OG tags")
            return True
    
    print(f"  ❌ {file_path.name} - couldn't find insertion point")
    return False

def main():
    print("Adding Open Graph tags to pages...\n")
    
    fixed = 0
    for page in PAGES_TO_FIX:
        file_path = BASE_DIR / page
        if file_path.exists():
            if add_og_tags(file_path):
                fixed += 1
        else:
            print(f"  ⚠️  {page} - file not found")
    
    print(f"\n✅ Fixed {fixed} files")

if __name__ == '__main__':
    main()
