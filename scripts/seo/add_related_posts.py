#!/usr/bin/env python3
"""
Add Related Posts section to all guide and review pages for better internal linking.
"""

import re
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent

# Related posts configuration - organized by page type
RELATED_POSTS = {
    # German Guides
    "beste-hybrid-kamera.html": [
        ("Beste Vlog-Kamera", "beste-vlog-kamera.html"),
        ("Beste Vollformat für Video", "beste-vollformat-fuer-video.html"),
        ("Beste Reisekamera", "beste-reisekamera.html"),
    ],
    "beste-vlog-kamera.html": [
        ("Beste Hybrid-Kamera", "beste-hybrid-kamera.html"),
        ("Beste Kamera für Einsteiger", "beste-kamera-fuer-anfaenger-2026.html"),
        ("Sony ZV-E10 Testbericht", "../bewertungen/sony-zv-e10-testbericht.html"),
    ],
    "beste-reisekamera.html": [
        ("Beste Hybrid-Kamera", "beste-hybrid-kamera.html"),
        ("Beste Action- & 360-Kamera", "beste-action-360-kamera.html"),
        ("DJI Osmo Pocket 3 Testbericht", "../bewertungen/dji-osmo-pocket-3-testbericht.html"),
    ],
    "beste-kamera-fuer-anfaenger-2026.html": [
        ("Beste Budget-Kamera unter 800€", "beste-budget-kamera-unter-800.html"),
        ("Beste Vlog-Kamera", "beste-vlog-kamera.html"),
        ("Canon EOS R8 Testbericht", "../bewertungen/canon-eos-r8-testbericht.html"),
    ],
    "beste-budget-kamera-unter-800.html": [
        ("Beste Kamera für Einsteiger", "beste-kamera-fuer-anfaenger-2026.html"),
        ("Beste Vlog-Kamera", "beste-vlog-kamera.html"),
        ("Sony ZV-E10 Testbericht", "../bewertungen/sony-zv-e10-testbericht.html"),
    ],
    "beste-vollformat-fuer-video.html": [
        ("Beste Hybrid-Kamera", "beste-hybrid-kamera.html"),
        ("Sony A7 IV Testbericht", "../bewertungen/sony-a7-iv-testbericht.html"),
        ("Panasonic S5 II Testbericht", "../bewertungen/panasonic-s5-ii-testbericht.html"),
    ],
    "beste-action-360-kamera.html": [
        ("Beste Reisekamera", "beste-reisekamera.html"),
        ("Beste Vlog-Kamera", "beste-vlog-kamera.html"),
        ("DJI Osmo Pocket 3 Testbericht", "../bewertungen/dji-osmo-pocket-3-testbericht.html"),
    ],
    
    # English Guides  
    "best-hybrid-camera.html": [
        ("Best Vlog Camera", "best-vlog-camera.html"),
        ("Best Full-Frame for Video", "best-full-frame-for-video.html"),
        ("Best Travel Camera", "best-travel-camera.html"),
    ],
    "best-vlog-camera.html": [
        ("Best Hybrid Camera", "best-hybrid-camera.html"),
        ("Best Camera for Beginners", "best-camera-for-beginners-2026.html"),
        ("Sony ZV-E10 Review", "../reviews/sony-zv-e10-review.html"),
    ],
}

RELATED_POSTS_HTML_DE = '''
    <!-- Related Posts -->
    <section class="section related-posts">
      <h2>Das könnte Sie auch interessieren</h2>
      <div class="grid">
{links}
      </div>
    </section>
'''

RELATED_POSTS_HTML_EN = '''
    <!-- Related Posts -->
    <section class="section related-posts">
      <h2>You might also like</h2>
      <div class="grid">
{links}
      </div>
    </section>
'''

RELATED_LINK_TEMPLATE = '''        <article class="card card-plain">
          <h3><a href="{url}">{title}</a></h3>
        </article>'''


def add_related_posts(file_path: Path) -> bool:
    """Add related posts section to a page."""
    filename = file_path.name
    
    if filename not in RELATED_POSTS:
        return False
    
    print(f"Processing: {filename}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if already has related posts
    if 'related-posts' in content:
        print(f"  - Already has related posts")
        return False
    
    # Generate links HTML
    links = []
    for title, url in RELATED_POSTS[filename]:
        links.append(RELATED_LINK_TEMPLATE.format(title=title, url=url))
    links_html = "\n".join(links)
    
    # Determine language
    if 'lang="de"' in content:
        section_html = RELATED_POSTS_HTML_DE.format(links=links_html)
    else:
        section_html = RELATED_POSTS_HTML_EN.format(links=links_html)
    
    # Insert before </main>
    if '</main>' in content:
        content = content.replace('</main>', f'{section_html}\n  </main>')
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"  ✓ Added related posts section")
        return True
    
    return False


def main():
    """Process all pages."""
    updated_count = 0
    
    # Process guide pages
    for guide_dir in [BASE_DIR / 'guides', BASE_DIR / 'de' / 'ratgeber']:
        if guide_dir.exists():
            for html_file in guide_dir.glob('*.html'):
                if add_related_posts(html_file):
                    updated_count += 1
    
    print(f"\n{'='*60}")
    print(f"Related Posts Added")
    print(f"Updated: {updated_count} pages")
    print(f"{'='*60}")


if __name__ == '__main__':
    main()
