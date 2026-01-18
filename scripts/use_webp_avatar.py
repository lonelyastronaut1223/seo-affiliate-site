#!/usr/bin/env python3
"""
Replace team-avatar.png with team-avatar.webp in all HTML files
"""

from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

def replace_avatar_references():
    print("🔄 Switching to WebP avatar...")
    count = 0
    
    for html_file in BASE_DIR.rglob('*.html'):
        if '.git' in str(html_file): continue
        
        content = html_file.read_text(encoding='utf-8')
        
        if 'team-avatar.png' in content:
            new_content = content.replace('team-avatar.png', 'team-avatar.webp')
            html_file.write_text(new_content, encoding='utf-8')
            print(f"✅ Updated {html_file.relative_to(BASE_DIR)}")
            count += 1
            
    print(f"\n✨ Updated avatar in {count} files")

if __name__ == '__main__':
    replace_avatar_references()
