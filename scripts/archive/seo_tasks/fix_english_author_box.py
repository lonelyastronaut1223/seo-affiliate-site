#!/usr/bin/env python3
"""
Fix the German Author Box leak in English pages.
The issue was caused by add_author.py matching 'lang="de"' in hreflang tags.
This script reverts the German text to English for pages that are NOT in the /de/ folder.
"""

from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent

# Wrong German Text (to look for)
GERMAN_TITLE = "Geschrieben vom cameraupick Redaktionsteam"
GERMAN_DESC_START = "Unser Team aus professionellen Fotografen"
GERMAN_LINK_TEXT = "Mehr über unseren Testprozess erfahren →"
GERMAN_LINK_HREF = "uber-uns.html"

# Correct English Text (to replace with)
ENGLISH_TITLE = "Written by cameraupick Editorial Team"
ENGLISH_DESC = """Our team of professional photographers and videographers has 10+ years of experience testing cameras. 
            We buy our own gear and provide honest, unbiased reviews."""
ENGLISH_LINK_TEXT = "Learn more about our testing process →"
ENGLISH_LINK_HREF = "about.html"

def fix_page(file_path: Path) -> bool:
    """Revert German author info to English if found in English page."""
    
    # Skip German pages
    if '/de/' in str(file_path):
        return False
        
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    
    # Check if we have the German title in an English file
    if GERMAN_TITLE in content:
        # Replace Title
        content = content.replace(GERMAN_TITLE, ENGLISH_TITLE)
        
        # Replace Description (using a regex or string match might be tricky due to whitespace)
        # Let's try to replace the paragraph body.
        # Since whitespace might vary, let's identify the block.
        
        # We'll just generic string replace the segments we know are unique
        content = content.replace(
            "Unser Team aus professionellen Fotografen und Videografen hat über 10 Jahre Erfahrung im Testen von Kameras. \n            Wir kaufen unsere eigene Ausrüstung und bieten ehrliche, unvoreingenommene Tests.",
            ENGLISH_DESC
        )
        
        # Also try the one without newline just in case
        content = content.replace(
            "Unser Team aus professionellen Fotografen und Videografen hat über 10 Jahre Erfahrung im Testen von Kameras. Wir kaufen unsere eigene Ausrüstung und bieten ehrliche, unvoreingenommene Tests.",
            ENGLISH_DESC
        )
        
        # Replace Link Text
        content = content.replace(GERMAN_LINK_TEXT, ENGLISH_LINK_TEXT)
        
        # Replace Link Href (handle relative paths carefully)
        # The German link usually ends with uber-uns.html
        # We need to be careful not to break other links, but inside the author box context it should be fine.
        # But wait, looking at the code, it's just `href="../uber-uns.html"` or similar.
        # Let's target the full tag if possible, or just the href part if it's unique enough.
        # Actually in the snippet it was: 
        # <a href="../uber-uns.html" ...>Mehr über...</a>
        
        content = content.replace('href="../uber-uns.html"', 'href="../about.html"')
        content = content.replace('href="uber-uns.html"', 'href="about.html"')
        
        modified = True
        
    if modified:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✓ Fixed German leak in {file_path.name}")
        return True
        
    return False

def main():
    print("Scanning for German content leaks in English pages...")
    fixed_count = 0
    
    # Scan all HTML files
    for html_file in BASE_DIR.rglob('*.html'):
        # Skip .git and /de/ directory
        if '.git' in str(html_file) or '/de/' in str(html_file):
            continue
            
        if fix_page(html_file):
            fixed_count += 1
            
    print(f"\n{'='*60}")
    print(f"Repair Complete")
    print(f"Fixed: {fixed_count} pages")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()
