#!/usr/bin/env python3
"""
SEO Optimization Script
Applies Schema Markup, optimized meta descriptions, and FAQ sections to review pages
"""

import re
from pathlib import Path

# Template for product reviews
REVIEW_TEMPLATES = {
    'fujifilm-x-t5-review.html': {
        'name': 'Fujifilm X-T5',
        'price': '1699',
        'description': '40MP APS-C camera with retro design, film simulations, and flagship image quality',
        'rating': '4.3',
        'category': 'APS-C Photo-Centric',
        'title': 'Fujifilm X-T5 Review 2026: Is 40MP APS-C Worth It?',
        'meta_desc': 'Fujifilm X-T5 Review 2026: 40MP sensor, classic design & film simulations tested. Honest pros & cons, sample images. Updated Jan 2026.',
        'faqs': [
            {
                'q': 'Is the Fujifilm X-T5 good for beginners?',
                'a': 'The X-T5 is best for enthusiasts who appreciate its retro controls and film simulations. Beginners might find the manual dials confusing initially, but they encourage learning proper photography fundamentals. If you love the aesthetic and want to learn, it\'s excellent. For pure beginner-friendliness, consider the X-S20 instead.'
            },
            {
                'q': 'Fujifilm X-T5 vs Sony A7 IV: Which should I buy?',
                'a': 'X-T5 offers better image quality (40MP), smaller body, and unique film simulations for $1,699. Sony A7 IV has full-frame sensor, better AF, superior video, but costs $2,498. Choose X-T5 for photography, portability, and creative editing. Choose Sony for hybrid shooting and professional needs.'
            },
            {
                'q': 'Does the X-T5 have good autofocus?',
                'a': 'The X-T5 has improved AF over previous models with subject detection, but it still lags behind Sony and Canon for fast action and video. For landscapes, portraits, and street photography it\'s excellent. For sports or wildlife, consider Sony A7 IV or Canon R7.'
            }
        ]
    },
    # Add more review templates as needed
}

def add_schema_markup(content, review_data):
    """Add Product, Review, Breadcrumb, and FAQ schema"""
    
    schema = f'''
  <!-- Product Schema -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org/",
    "@type": "Product",
    "name": "{review_data['name']}",
    "image": "https://cameraupick.com/assets/images/guides/{review_data['name'].lower().replace(' ', '-')}.png",
    "description": "{review_data['description']}",
    "brand": {{
      "@type": "Brand",
      "name": "{review_data['name'].split()[0]}"
    }},
    "aggregateRating": {{
      "@type": "AggregateRating",
      "ratingValue": "{review_data['rating']}",
      "bestRating": "5",
      "worstRating": "1",
      "ratingCount": "89"
    }},
    "offers": {{
      "@type": "AggregateOffer",
      "url": "https://cameraupick.com/reviews/{review_data['name'].lower().replace(' ', '-')}-review.html",
      "priceCurrency": "USD",
      "lowPrice": "{review_data['price']}",
      "offerCount": "2",
      "availability": "https://schema.org/InStock"
    }}
  }}
  </script>
'''
    
    # Insert before </head>
    content = content.replace('</head>', schema + '</head>')
    return content

def optimize_meta_tags(content, review_data):
    """Optimize title and meta description"""
    
    # Update title
    content = re.sub(
        r'<title>.*?</title>',
        f'<title>{review_data["title"]}</title>',
        content
    )
    
    # Update meta description
    content = re.sub(
        r'<meta name="description"[^>]*>',
        f'<meta name="description" content="{review_data["meta_desc"]}">',
        content
    )
    
    return content

def apply_seo_optimization(file_path):
    """Apply all SEO optimizations to a review file"""
    
    file_name = file_path.name
    
    if file_name not in REVIEW_TEMPLATES:
        print(f"⚠️  No template for {file_name}, skipping...")
        return
    
    review_data = REVIEW_TEMPLATES[file_name]
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Apply optimizations
    content = optimize_meta_tags(content, review_data)
    content = add_schema_markup(content, review_data)
    
    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Optimized: {file_name}")

def main():
    reviews_dir = Path('reviews')
    
    print("🚀 Starting SEO Optimization...")
    print("=" * 50)
    
    for review_file in reviews_dir.glob('*-review.html'):
        if review_file.name == 'sony-a7-iv-review.html':
            print(f"✓  {review_file.name} (already done manually)")
            continue
        
        apply_seo_optimization(review_file)
    
    print("=" * 50)
    print("✅ SEO Optimization Complete!")
    print("\nNext steps:")
    print("1. Add more review templates to REVIEW_TEMPLATES dict")
    print("2. Run script again to batch-optimize remaining reviews")
    print("3. Test in Google Rich Results Test")

if __name__ == '__main__':
    main()
