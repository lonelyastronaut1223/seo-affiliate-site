#!/usr/bin/env python3
"""
Add Author Schema and E-E-A-T signals to all article pages.
Improves Google's trust signals and search rankings.
"""

import re
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent

# Author information for E-E-A-T
AUTHOR_SCHEMA = '''
  <!-- Author Schema for E-E-A-T -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Person",
    "name": "cameraupick Editorial Team",
    "url": "https://cameraupick.com/about.html",
    "jobTitle": "Camera Review Experts",
    "description": "Professional photographers and videographers with 10+ years of experience testing cameras, lenses, and accessories.",
    "sameAs": [
      "https://cameraupick.com"
    ],
    "knowsAbout": [
      "Mirrorless Cameras",
      "Full-Frame Photography",
      "Video Production",
      "Camera Lenses",
      "Photography Equipment"
    ]
  }
  </script>
'''

# Visible author box HTML (English)
AUTHOR_BOX_EN = '''
    <!-- Author Box -->
    <section class="section author-box" style="background: var(--bg-soft); border-radius: 12px; padding: 24px; margin-top: 32px;">
      <div style="display: flex; gap: 16px; align-items: flex-start;">
        <div style="width: 64px; height: 64px; background: var(--accent); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 28px;">📷</div>
        <div>
          <h4 style="margin: 0 0 8px 0;">Written by cameraupick Editorial Team</h4>
          <p style="margin: 0; color: var(--muted); font-size: 14px;">
            Our team of professional photographers and videographers has 10+ years of experience testing cameras. 
            We buy our own gear and provide honest, unbiased reviews.
          </p>
          <a href="../about.html" style="font-size: 14px; margin-top: 8px; display: inline-block;">Learn more about our testing process →</a>
        </div>
      </div>
    </section>
'''

# Visible author box HTML (German)
AUTHOR_BOX_DE = '''
    <!-- Author Box -->
    <section class="section author-box" style="background: var(--bg-soft); border-radius: 12px; padding: 24px; margin-top: 32px;">
      <div style="display: flex; gap: 16px; align-items: flex-start;">
        <div style="width: 64px; height: 64px; background: var(--accent); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 28px;">📷</div>
        <div>
          <h4 style="margin: 0 0 8px 0;">Geschrieben vom cameraupick Redaktionsteam</h4>
          <p style="margin: 0; color: var(--muted); font-size: 14px;">
            Unser Team aus professionellen Fotografen und Videografen hat über 10 Jahre Erfahrung im Testen von Kameras. 
            Wir kaufen unsere eigene Ausrüstung und bieten ehrliche, unvoreingenommene Tests.
          </p>
          <a href="../uber-uns.html" style="font-size: 14px; margin-top: 8px; display: inline-block;">Mehr über unseren Testprozess erfahren →</a>
        </div>
      </div>
    </section>
'''


def add_author_info(file_path: Path) -> bool:
    """Add author schema and author box to article pages."""
    print(f"Processing: {file_path.name}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if already has author schema
    if '"@type": "Person"' in content or 'author-box' in content:
        print(f"  - Already has author info")
        return False
    
    modified = False
    
    # Add author schema in head
    if '</head>' in content:
        content = content.replace('</head>', f'{AUTHOR_SCHEMA}</head>')
        modified = True
    
    # Add visible author box before </main>
    if '</main>' in content:
        # Strict check for HTML lang attribute
        if '<html lang="de"' in content:
            content = content.replace('</main>', f'{AUTHOR_BOX_DE}\n  </main>')
        else:
            content = content.replace('</main>', f'{AUTHOR_BOX_EN}\n  </main>')
        modified = True
    
    if modified:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✓ Added author schema and author box")
        return True
    
    return False


def main():
    """Process guide and review pages."""
    updated_count = 0
    
    # Process guides
    for guides_dir in [BASE_DIR / 'guides', BASE_DIR / 'de' / 'ratgeber']:
        if guides_dir.exists():
            for html_file in guides_dir.glob('*.html'):
                if add_author_info(html_file):
                    updated_count += 1
    
    # Process reviews  
    for reviews_dir in [BASE_DIR / 'reviews', BASE_DIR / 'de' / 'bewertungen']:
        if reviews_dir.exists():
            for html_file in reviews_dir.glob('*.html'):
                if add_author_info(html_file):
                    updated_count += 1
    
    # Process comparisons
    for compare_dir in [BASE_DIR / 'compare', BASE_DIR / 'de' / 'vergleiche']:
        if compare_dir.exists():
            for html_file in compare_dir.glob('*.html'):
                if add_author_info(html_file):
                    updated_count += 1
    
    print(f"\n{'='*60}")
    print(f"Author Info Added (E-E-A-T)")
    print(f"Updated: {updated_count} pages")
    print(f"{'='*60}")


if __name__ == '__main__':
    main()
