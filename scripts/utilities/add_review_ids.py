import os

# Mapping filename to the ID needed by links.js
reviews_map = {
    'reviews/sony-a7-iv-review.html': 'sony-a7iv',
    'reviews/fujifilm-x-t5-review.html': 'fuji-x-t5',
    'reviews/canon-eos-r8-review.html': 'canon-r8',
    'reviews/sony-zv-e10-review.html': 'sony-zv-e10',
    'reviews/nikon-z8-review.html': 'nikon-z8',
    'reviews/panasonic-s5-ii-review.html': 'panasonic-s5ii',
    'reviews/dji-osmo-pocket-3-review.html': 'dji-pocket-3'
}

count = 0

for filepath, product_id in reviews_map.items():
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Target the main product review card wrapper
    target = '<div class="product-review-card">'
    replacement = f'<div class="product-review-card" id="{product_id}">'
    
    if f'id="{product_id}"' in content:
        print(f"Skipping {filepath} (ID {product_id} already present)")
        continue
        
    if target in content:
        new_content = content.replace(target, replacement, 1) # Replace only the first occurrence
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath} with id='{product_id}'")
        count += 1
    else:
        print(f"Warning: Could not find product-review-card in {filepath}")

print(f"Total review pages updated: {count}")
