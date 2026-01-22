#!/usr/bin/env python3
"""
Convert simple <img> tags in Reviews, Lenses, Gear sections to responsive <picture> elements
"""

import re

def convert_img_to_picture(content, start_marker, end_marker):
    """Convert img tags between markers to picture elements"""
    
    # Find the section
    start_pos = content.find(start_marker)
    if start_pos == -1:
        return content
    
    end_pos = content.find(end_marker, start_pos)
    if end_pos == -1:
        end_pos = len(content)
    
    section = content[start_pos:end_pos]
    
    # Pattern to match img tags with .webp src
    pattern = r'(\s*)<img\s+([^>]*?)src="([^"]+\.webp)"([^>]*?)>'
    
    def replace_with_picture(match):
        indent = match.group(1)
        before_attrs = match.group(2)
        src_webp = match.group(3)
        after_attrs = match.group(4)
        
        # Extract attrs
        loading = re.search(r'loading="([^"]+)"', before_attrs + after_attrs)
        decoding = re.search(r'decoding="([^"]+)"', before_attrs + after_attrs) 
        alt = re.search(r'alt="([^"]*)"', before_attrs + after_attrs)
        width = re.search(r'width="([^"]+)"', before_attrs + after_attrs)
        height = re.search(r'height="([^"]+)"', before_attrs + after_attrs)
        
        loading_val = loading.group(1) if loading else "lazy"
        decoding_val = decoding.group(1) if decoding else "async"
        alt_val = alt.group(1) if alt else ""
        width_val = width.group(1) if width else "1200"
        height_val = height.group(1) if height else "800"
        
        # Get base path
        base_path = src_webp.replace('.webp', '')
        
        # Create picture element
        picture = f'''{indent}<picture>
{indent}  <source
{indent}    srcset="{base_path}-sm.webp 600w, {src_webp} 1200w"
{indent}    sizes="(max-width: 768px) 100vw, 50vw"
{indent}    type="image/webp">
{indent}  <img
{indent}    loading="{loading_val}"
{indent}    decoding="{decoding_val}"
{indent}    src="{base_path}.jpg"
{indent}    srcset="{base_path}-sm.jpg 600w, {base_path}.jpg 1200w"
{indent}    sizes="(max-width: 768px) 100vw, 50vw"
{indent}    alt="{alt_val}"
{indent}    width="{width_val}"
{indent}    height="{height_val}">
{indent}</picture>'''
        
        return picture
    
    # Replace in section
    new_section = re.sub(pattern, replace_with_picture, section)
    
    # Replace in content
    new_content = content[:start_pos] + new_section + content[end_pos:]
    
    return new_content

# Read file
with open('src/pages/index.astro', 'r', encoding='utf-8') as f:
    content = f.read()

print("Converting images to responsive picture elements...")

# Convert Reviews section
content = convert_img_to_picture(content, '<h2>Latest Reviews</h2>', '<section')
print("✅ Reviews section converted")

# Convert Lenses section  
content = convert_img_to_picture(content, '<h2>Lens Guides</h2>', '<section')
print("✅ Lenses section converted")

# Convert Gear section
content = convert_img_to_picture(content, '<h2>Gear & Accessories</h2>', '<section')
print("✅ Gear section converted")

# Write back
with open('src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(content)

print("\n✅ All conversions complete!")
print("File updated: src/pages/index.astro")
