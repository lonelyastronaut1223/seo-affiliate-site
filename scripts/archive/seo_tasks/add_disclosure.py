#!/usr/bin/env python3
"""
Add affiliate disclosure section to guide pages that are missing it.
"""

from pathlib import Path
import re

BASE_DIR = Path(__file__).parent.parent.parent

# Guide pages that need disclosure (from audit)
PAGES_TO_FIX = [
    'guides/best-full-frame-for-video.html',
    'guides/best-hybrid-camera.html',
    'guides/best-action-360-camera.html',
    'guides/best-budget-camera-under-800.html',
    'guides/best-vlog-camera.html',
]

DISCLOSURE_EN = '''
    <section class="section" id="affiliate">
      <h2>Partner Note</h2>
      <p class="section-sub">
        We buy or rent our own equipment. No manufacturer paid for this guide. We earn a commission when you use our
        affiliate links, which keeps this site ad-free.
      </p>
    </section>
'''

def add_disclosure(file_path: Path) -> bool:
    """Add disclosure section if missing."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if already has disclosure
    if 'affiliate' in content.lower() and ('commission' in content.lower() or 'provision' in content.lower()):
        print(f"  ⏭️  {file_path.name} - already has disclosure")
        return False
    
    # Find a good insertion point (before </main> or before footer)
    insert_patterns = [
        (r'(</main>)', 0),  # Before </main>
        (r'(<footer)', 0),  # Before footer
        (r'(<!-- Author Box -->)', 0),  # Before author box
    ]
    
    for pattern, group in insert_patterns:
        match = re.search(pattern, content, re.I)
        if match:
            insert_pos = match.start()
            new_content = content[:insert_pos] + DISCLOSURE_EN + '\n  ' + content[insert_pos:]
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"  ✅ {file_path.name} - added disclosure")
            return True
    
    print(f"  ❌ {file_path.name} - couldn't find insertion point")
    return False

def main():
    print("Adding affiliate disclosure to guide pages...\n")
    
    fixed = 0
    for page in PAGES_TO_FIX:
        file_path = BASE_DIR / page
        if file_path.exists():
            if add_disclosure(file_path):
                fixed += 1
        else:
            print(f"  ⚠️  {page} - file not found")
    
    print(f"\n✅ Fixed {fixed} files")

if __name__ == '__main__':
    main()
