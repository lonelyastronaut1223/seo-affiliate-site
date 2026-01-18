#!/usr/bin/env python3
"""
Script to add Review schema to camera review pages
Adds detailed Review structured data for better SEO
"""

import os
import re
from pathlib import Path

REVIEWS_DIR = Path("reviews")

# Review schema template
REVIEW_SCHEMA_TEMPLATE = '''
  <!-- Review Schema -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org/",
    "@type": "Review",
    "itemReviewed": {{
      "@type": "Product",
      "name": "{product_name}",
      "image": "https://cameraupick.com/assets/images/guides/{image_filename}",
      "brand": {{
        "@type": "Brand",
        "name": "{brand}"
      }}
    }},
    "reviewRating": {{
      "@type": "Rating",
      "ratingValue": "{rating}",
      "bestRating": "5",
      "worstRating": "1"
    }},
    "author": {{
      "@type": "Organization",
      "name": "cameraupick"
    }},
    "reviewBody": "{review_summary}",
    "datePublished": "2026-01-15"
  }}
  </script>
'''

# Camera data for reviews
CAMERA_DATA = {
    "sony-a7-iv-review.html": {
        "product_name": "Sony A7 IV",
        "brand": "Sony",
        "rating": "4.7",
        "image_filename": "sony-a7iv.png",
        "review_summary": "The Sony A7 IV is the ultimate hybrid camera, balancing 33MP stills, 4K60p video, and industry-leading autofocus in a professional body."
    },
    "sony-a7c-ii-review.html": {
        "product_name": "Sony A7C II",
        "brand": "Sony",
        "rating": "4.5",
        "image_filename": "sony-a7c-ii.webp",
        "review_summary": "Compact full-frame powerhouse with AI autofocus and excellent video features, perfect for travel photographers."
    },
    "sony-zv-e10-review.html": {
        "product_name": "Sony ZV-E10",
        "brand": "Sony",
        "rating": "4.6",
        "image_filename": "sony-zv-e10.webp",
        "review_summary": "The best budget vlogging camera with flip screen, product showcase mode, and exceptional autofocus."
    },
    "canon-eos-r8-review.html": {
        "product_name": "Canon EOS R8",
        "brand": "Canon",
        "rating": "4.4",
        "image_filename": "canon-r8.webp",
        "review_summary": "Affordable full-frame camera with excellent image quality and RF lens compatibility."
    },
    "fujifilm-x-t5-review.html": {
        "product_name": "Fujifilm X-T5",
        "brand": "Fujifilm",
        "rating": "4.8",
        "image_filename": "fujifilm-xt5.webp",
        "review_summary": "40MP APS-C camera with stunning image quality, film simulations, and retro design."
    },
    "nikon-z8-review.html": {
        "product_name": "Nikon Z8",
        "brand": "Nikon",
        "rating": "4.9",
        "image_filename": "nikon-z8.webp",
        "review_summary": "Professional-grade hybrid camera with 8K video, blazing fast autofocus, and robust build quality."
    },
    "panasonic-s5-ii-review.html": {
        "product_name": "Panasonic Lumix S5 II",
        "brand": "Panasonic",
        "rating": "4.7",
        "image_filename": "panasonic-s5ii.webp",
        "review_summary": "Best value full-frame hybrid with phase-detect AF, superb video specs, and excellent stabilization."
    },
    "dji-osmo-pocket-3-review.html": {
        "product_name": "DJI Osmo Pocket 3",
        "brand": "DJI",
        "rating": "4.8",
        "image_filename": "dji-pocket3.webp",
        "review_summary": "Revolutionary gimbal camera with 1-inch sensor, perfect for ultra-portable professional vlogging."
    }
}

def add_review_schema_to_file(filepath, camera_data):
    """Add Review schema to review HTML file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if Review schema already exists
    if '"@type": "Review"' in content:
        print(f"  ✓ Review schema already exists in {filepath.name}")
        return False
    
    # Generate the schema
    schema = REVIEW_SCHEMA_TEMPLATE.format(**camera_data)
    
    # Insert after Product schema (before </head>)
    if '</head>' in content:
        content = content.replace('</head>', f'{schema}\n</head>')
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"  ✅ Added Review schema to {filepath.name}")
        return True
    else:
        print(f"  ⚠️ Could not find </head> in {filepath.name}")
        return False

def main():
    print("🔍 Adding Review Schema to camera review pages...\n")
    
    added_count = 0
    
    for filename, camera_data in CAMERA_DATA.items():
        filepath = REVIEWS_DIR / filename
        
        if filepath.exists():
            if add_review_schema_to_file(filepath, camera_data):
                added_count += 1
        else:
            print(f"  ⚠️ File not found: {filename}")
    
    print(f"\n✅ Complete! Added Review schema to {added_count} files")
    print("\n📊 Benefits:")
    print("  • Rich snippets in search results")
    print("  • Star ratings displayed in Google")
    print("  • Improved click-through rates")
    print("  • Better SEO authority")

if __name__ == "__main__":
    main()
