#!/usr/bin/env python3
"""
Final performance optimizations:
1. Register Service Worker on all pages
2. Add font-display: swap to font loading
"""

import re
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent

SW_REGISTRATION = '''
  <!-- Service Worker Registration -->
  <script>
    if ('serviceWorker' in navigator) {
      window.addEventListener('load', () => {
        navigator.serviceWorker.register('/sw.js')
          .then(reg => console.log('SW registered'))
          .catch(err => console.log('SW registration failed'));
      });
    }
  </script>'''


def add_sw_registration(file_path: Path) -> bool:
    """Add Service Worker registration to a page."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if already registered
    if 'serviceWorker' in content:
        return False
    
    # Add before </body>
    if '</body>' in content:
        content = content.replace('</body>', f'{SW_REGISTRATION}\n</body>')
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    
    return False


def add_font_display_swap(file_path: Path) -> bool:
    """Add font-display=swap to Google Fonts loading."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    
    # Check if font URL exists without display=swap
    if 'fonts.googleapis.com' in content and 'display=swap' not in content:
        content = re.sub(
            r'(fonts\.googleapis\.com/css2\?family=[^"]+)(?!.*display=swap)',
            r'\1&display=swap',
            content
        )
        modified = True
    
    if modified:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    
    return False


def main():
    """Main execution."""
    sw_count = 0
    font_count = 0
    
    # Find all HTML files
    html_files = list(BASE_DIR.glob('*.html')) + \
                 list(BASE_DIR.glob('**/*.html'))
    
    # Filter out .git and .venv
    html_files = [f for f in html_files if '.git' not in str(f) and '.venv' not in str(f)]
    
    for file_path in html_files:
        print(f"Processing: {file_path.relative_to(BASE_DIR)}")
        
        if add_sw_registration(file_path):
            print(f"  ✓ Added SW registration")
            sw_count += 1
        
        if add_font_display_swap(file_path):
            print(f"  ✓ Added font-display: swap")
            font_count += 1
    
    print(f"\n{'='*60}")
    print(f"Performance Optimization Complete")
    print(f"SW Registration added: {sw_count} pages")
    print(f"Font display optimized: {font_count} pages")
    print(f"{'='*60}")


if __name__ == '__main__':
    main()
