#!/usr/bin/env python3
"""
Script to verify all affiliate link IDs match between HTML files and links.js
"""

import re
import json
from pathlib import Path

# Read links.js to get all product IDs
links_js = Path("/Users/taylor/Downloads/Project/SEO-Affiliate/seo-affiliate-site/assets/js/links.js")
content = links_js.read_text()

# Extract all product IDs from affiliateLinks object
product_ids = set()
for match in re.finditer(r'"([^"]+)":\s*"https?://[^"]*"', content):
    product_ids.add(match.group(1))

print(f"Found {len(product_ids)} product IDs in links.js")
print("\n=== Product IDs in links.js ===")
for pid in sorted(product_ids):
    print(f"  - {pid}")

# Find all HTML files with id="..." attributes
html_files = list(Path("/Users/taylor/Downloads/Project/SEO-Affiliate/seo-affiliate-site").rglob("*.html"))

print(f"\n=== Checking {len(html_files)} HTML files ===\n")

missing_ids = []
for htmlfile in html_files:
    try:
        html_content = htmlfile.read_text()
        
        # Find all id="product-xxx" in product-review-card divs
        for match in re.finditer(r'<div[^>]*class="product-review-card"[^>]*id="([^"]+)"', html_content):
            review_id = match.group(1)
            if review_id not in product_ids:
                missing_ids.append((htmlfile.relative_to(Path("/Users/taylor/Downloads/Project/SEO-Affiliate/seo-affiliate-site")), review_id))
                
        # Find all buttons with data-product but no matching ID
        for match in re.finditer(r'data-product="([^"]+)"', html_content):
            data_product = match.group(1)
            if data_product not in product_ids:
                print(f"⚠️  {htmlfile.name}: data-product='{data_product}' NOT IN links.js")
                
    except Exception as e:
        print(f"Error reading {htmlfile}: {e}")

if missing_ids:
    print("\n=== ❌ Missing IDs in links.js ===")
    for filepath, missing_id in missing_ids:
        print(f"  {filepath}: id='{missing_id}' NOT IN links.js")
else:
    print("\n✅ All review card IDs are present in links.js")

print("\n=== Summary ===")
print(f"Total product IDs in links.js: {len(product_ids)}")
print(f"Missing IDs: {len(missing_ids)}")
