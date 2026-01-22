#!/usr/bin/env python3
"""
Convert simple img tags to responsive picture elements with srcset
For use with cameraupick SEO affiliate site mobile optimization
"""

import re
import sys
from pathlib import Path

def convert_simple_img_to_responsive(content):
    """
    Convert patterns like:
      <img src="/assets/images/guides/name.webp" alt="..." width="1200" height="800">
    
    To:
      <picture>
        <source srcset="/assets/images/guides/name-sm.webp 600w, /assets/images/guides/name.webp 1200w"
                sizes="(max-width: 768px) 100vw, 50vw" type="image/webp">
        <img loading="lazy" decoding="async" src="/assets/images/guides/name.jpg"
             srcset="/assets/images/guides/name-sm.jpg 600w, /assets/images/guides/name.jpg 1200w"
             sizes="(max-width: 768px) 100vw, 50vw" alt="..." width="1200" height="800">
      </picture>
    """
    
    # Pattern to match simple images (not already in picture tags)
    pattern = r'''(<img\s+                              # img tag
                     (?:loading="lazy"\s+)?              # optional loading
                     (?:decoding="async"\s+)?            # optional decoding
                     src="([^"]+\.webp)"                 # src attribute (webp)
                     (?:[^>]*?)                          # other attrs
                     alt="([^"]*)"                       # alt
                     (?:[^>]*?)                          # other attrs
                     width="(\d+)"\s+height="(\d+)"      # dimensions
                     [^>]*>)                             # end tag
                  '''
    
    def replace_img(match):
        full_tag = match.group(1)
        src_webp = match.group(2)
        alt_text = match.group(3)
        width = match.group(4)
        height = match.group(5)
        
        # Skip if already in a picture tag (simple heuristic)
        # This function should only be called on content without picture tags
        
        # Extract base path (remove .webp extension)
        base_path = src_webp.replace('.webp', '')
        
        # Create responsive picture element
        responsive_html = f'''<picture>
              <source 
                srcset="{base_path}-sm.webp 600w, 
                        {src_webp} 1200w" 
                sizes="(max-width: 768px) 100vw, 50vw"
                type="image/webp">
              <img 
                loading="lazy" 
                decoding="async" 
                src="{base_path}.jpg"
                srcset="{base_path}-sm.jpg 600w, 
                        {base_path}.jpg 1200w"
                sizes="(max-width: 768px) 100vw, 50vw"
                alt="{alt_text}" 
                width="{width}" 
                height="{height}">
            </picture>'''
        
        return responsive_html
    
    # Only convert images that are NOT already in picture tags
    # Split content by picture tags and process non-picture sections
    parts = re.split(r'(<picture>.*?</picture>)', content, flags=re.DOTALL)
    
    result = []
    for i, part in enumerate(parts):
        if i % 2 == 0:  # Not inside a picture tag
            part = re.sub(pattern, replace_img, part, flags=re.VERBOSE)
        result.append(part)
    
    return ''.join(result)

def main():
    if len(sys.argv) < 2:
        print("Usage: python convert_images_responsive.py <file>")
        sys.exit(1)
    
    file_path = Path(sys.argv[1])
    
    if not file_path.exists():
        print(f"❌ File not found: {file_path}")
        sys.exit(1)
    
    # Read file
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Convert images
    new_content = convert_simple_img_to_responsive(content)
    
    # Count changes
    changes = content.count('<img') - new_content.count('<img')
    
    if changes > 0:
        # Write back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"✅ Converted {changes} images to responsive pictures in {file_path.name}")
    else:
        print(f"⏭️  No changes needed in {file_path.name}")

if __name__ == "__main__":
    main()
