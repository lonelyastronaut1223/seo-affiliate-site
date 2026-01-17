#!/usr/bin/env python3
"""
Script to enhance Article Schema in buying guide pages
Adds missing optional fields: image, author, headline
"""

import os
import re
from pathlib import Path

GUIDES_DIR = Path("guides")

# Guide data with image files
GUIDE_DATA = {
    "best-action-360-camera.html": {
        "headline": "Best Action & 360 Camera 2026: Top Picks for Adventure",
        "image": "action-cam.webp",
        "description": "Action/360 cams with great stabilization, horizon lock, and easy reframing."
    },
    "best-full-frame-for-video.html": {
        "headline": "Best Full-Frame Camera for Video 2026: Professional Picks",
        "image": "video-camera.webp",
        "description": "Full-frame hybrids with strong codecs, low rolling shutter, and good IBIS."
    },
    "best-hybrid-camera.html": {
        "headline": "Best Hybrid Camera 2026: Top Photo-Video All-Rounders",
        "image": "hybrid-camera.webp",
        "description": "Balanced photo-video bodies with 10-bit, dependable AF, and strong ecosystems."
    },
    "best-budget-camera-under-800.html": {
        "headline": "Best Budget Camera Under $800 (2026): Value Picks",
        "image": "budget-camera.webp",
        "description": "Value picks with reliable AF, decent battery, and affordable lens paths."
    },
    "best-travel-camera.html": {
        "headline": "Best Travel Camera 2026: Compact Favorites",
        "image": "travel-camera.webp",
        "description": "Carry-light kits that still deliver stabilized 4K and sharp travel photos."
    },
    "best-camera-for-beginners-2026.html": {
        "headline": "Best Camera for Beginners (2026): Simple, Powerful Picks",
        "image": "beginner-camera.webp",
        "description": "Safe, easy picks with fast AF, simple menus, solid battery, and room to grow."
    },
    "best-vlog-camera.html": {
        "headline": "Best Vlog Camera 2026: Top Picks for Content Creators",
        "image": "vlog-camera.webp",
        "description": "Fast AF, flip screens, gyro data or IBIS, and clean audio options."
    }
}

def enhance_article_schema(filepath, guide_data):
    """Add missing Article schema fields"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if Article schema exists
    if '"@type": "Article"' not in content:
        return False, "no Article schema found"
    
    # Find the Article schema block
    article_pattern = r'(<script type="application/ld\+json">.*?"@type": "Article".*?</script>)'
    match = re.search(article_pattern, content, re.DOTALL)
    
    if not match:
        return False, "could not parse Article schema"
    
    old_schema_block = match.group(1)
    
    # Check if already has these fields
    if '"image"' in old_schema_block and '"author"' in old_schema_block and '"headline"' in old_schema_block:
        return False, "already has complete schema"
    
    # Create enhanced schema
    enhanced_schema = f'''<script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "{guide_data['headline']}",
    "image": "https://cameraupick.com/assets/images/guides/{guide_data['image']}",
    "author": {{
      "@type": "Organization",
      "name": "cameraupick",
      "url": "https://cameraupick.com"
    }},
    "publisher": {{
      "@type": "Organization",
      "name": "cameraupick",
      "logo": {{
        "@type": "ImageObject",
        "url": "https://cameraupick.com/assets/images/favicon.png"
      }}
    }},
    "datePublished": "2026-01-15",
    "dateModified": "2026-01-17",
    "description": "{guide_data['description']}"
  }}
  </script>'''
    
    # Replace old schema with enhanced one
    content = content.replace(old_schema_block, enhanced_schema)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True, "enhanced"

def main():
    print("🔍 Enhancing Article Schema in buying guides...\n")
    
    enhanced_count = 0
    
    for filename, guide_data in GUIDE_DATA.items():
        filepath = GUIDES_DIR / filename
        
        if filepath.exists():
            success, message = enhance_article_schema(filepath, guide_data)
            
            if success:
                print(f"  ✅ {filename}")
                enhanced_count += 1
            else:
                print(f"  ℹ️  {filename}: {message}")
        else:
            print(f"  ⚠️  File not found: {filename}")
    
    print(f"\n✅ Complete! Enhanced {enhanced_count} buying guides")
    print("\n📊 Added fields:")
    print("  • headline - Article title")
    print("  • image - Featured image URL")
    print("  • author - Organization info")
    print("  • publisher - Brand info with logo")
    print("  • datePublished - Publication date")
    print("  • dateModified - Last update date")
    print("\n🌟 Benefits:")
    print("  • Rich snippets with images in search results")
    print("  • Author/publisher credibility signals")
    print("  • Better SEO authority")
    print("  • Improved click-through rates")

if __name__ == "__main__":
    main()
