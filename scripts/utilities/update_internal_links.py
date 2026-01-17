import os
import random
import re
from pathlib import Path

# Config
REVIEWS_DIR = Path('reviews')
NUM_LINKS = 3

# Define available reviews manually to ensure quality titles and images
# This matches the structure in check_related_links.py + new additions if any
REVIEWS_DATA = {
    'canon-eos-r8-review.html': {
        'title': 'Canon EOS R8 Review',
        'image': '../assets/images/guides/canon-eos-r8.png',
        'alt': 'Canon EOS R8'
    },
    'dji-osmo-pocket-3-review.html': {
        'title': 'DJI Osmo Pocket 3 Review',
        'image': '../assets/images/guides/dji-osmo-pocket-3.png',
        'alt': 'DJI Osmo Pocket 3'
    },
    'fujifilm-x-t5-review.html': {
        'title': 'Fujifilm X-T5 Review',
        'image': '../assets/images/guides/fujifilm-x-t5.png',
        'alt': 'Fujifilm X-T5'
    },
    'nikon-z8-review.html': {
        'title': 'Nikon Z8 Review',
        'image': '../assets/images/guides/nikon-z8.png',
        'alt': 'Nikon Z8'
    },
    'panasonic-s5-ii-review.html': {
        'title': 'Panasonic S5 II Review',
        'image': '../assets/images/guides/panasonic-s5ii.png',
        'alt': 'Panasonic S5 II'
    },
    'sony-a7-iv-review.html': {
        'title': 'Sony A7 IV Review',
        'image': '../assets/images/guides/sony-a7iv.png',
        'alt': 'Sony A7 IV'
    },
    'sony-zv-e10-review.html': {
        'title': 'Sony ZV-E10 Review',
        'image': '../assets/images/guides/sony-zv-e10-original.png',
        'alt': 'Sony ZV-E10'
    },
    'sony-a7c-ii-review.html': {
        'title': 'Sony A7C II Review',
        'image': '../assets/images/guides/sony-a7c-ii.png',
        'alt': 'Sony A7C II'
    }
}

def generate_related_html(current_filename):
    """Generates the HTML for the Related Reviews section."""
    
    # Get all available files excluding current
    candidates = [f for f in REVIEWS_DATA.keys() if f != current_filename]
    
    # Select random unique links
    selected = random.sample(candidates, min(len(candidates), NUM_LINKS))
    
    html = '    <section class="section">\n'
    html += '      <h2>Related Reviews</h2>\n'
    html += '      <div class="grid">\n'
    
    for filename in selected:
        data = REVIEWS_DATA[filename]
        # Use webp if possible (we assume optimization task ran), but let's stick to existing mix or use picture tag?
        # For simplicity and robust linking, let's use the path defined in data, but maybe upgrade to picture tag later.
        # Since we just optimized images, we should ideally use webp.
        # Let's check if we should auto-upgrade to webp here.
        # The previous task converted images to webp.
        
        # Simple img tag construction
        html += '        <article class="card">\n'
        html += f'          <div class="card-thumb"><img src="{data["image"]}" alt="{data["alt"]}" loading="lazy"></div>\n'
        html += f'          <h3><a href="{filename}">{data["title"]}</a></h3>\n'
        html += '        </article>\n'
        
    html += '      </div>\n'
    html += '    </section>\n'
    return html

def process_file(filepath):
    filename = filepath.name
    if filename not in REVIEWS_DATA:
        print(f"Skipping {filename} (not in data list)")
        return

    print(f"Processing {filename}...")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # defined pattern to find existing Related Reviews section
    # It might look like <section class="section"> <h2>Related Reviews</h2> ... </section>
    # We will use a regex to find it and replace it, or append if not found.
    
    # Regex to capture the section. 
    # Warning: HTML parsing with regex is fragile, but for this structured template it's likely fine.
    # We assume standard formatting: 2-space indentation.
    
    pattern = re.compile(r'<section class="section">\s*<h2>Related Reviews</h2>[\s\S]*?</section>', re.MULTILINE)
    
    new_section = generate_related_html(filename)
    
    if pattern.search(content):
        print(f"  - Updating existing section.")
        new_content = pattern.sub(new_section.strip(), content) # .strip() to avoid adding too many newlines
    else:
        print(f"  - Injecting new section.")
        # Inject before </main>
        if '</main>' in content:
            new_content = content.replace('</main>', f'\n{new_section}\n  </main>')
        else:
            print(f"  ! ERROR: Could not find </main> tag.")
            return

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("  - Saved.")
    else:
        print("  - No changes needed.")

def main():
    if not REVIEWS_DIR.exists():
        print(f"Directory {REVIEWS_DIR} not found.")
        return

    for html_file in REVIEWS_DIR.glob('*.html'):
        process_file(html_file)

if __name__ == "__main__":
    main()
