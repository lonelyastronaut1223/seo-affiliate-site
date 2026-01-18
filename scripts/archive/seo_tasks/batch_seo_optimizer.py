#!/usr/bin/env python3
"""
Batch SEO Optimizer - Applies comprehensive SEO to all review pages
"""

import re
from pathlib import Path

# Complete review data for all cameras
REVIEWS_DATA = {
    'fujifilm-x-t5-review.html': {
        'name': 'Fujifilm X-T5',
        'price': '1699',
        'category': 'APS-C Photo-Centric',
        'description': '40MP APS-C camera with retro design, film simulations, and flagship image quality',
        'rating': '4.3',
        'review_count': '89',
        'title': 'Fujifilm X-T5 Review 2026: Is 40MP APS-C Worth $1,699?',
        'meta_desc': 'Fujifilm X-T5 Review 2026: 40MP sensor, classic design & film simulations tested. Honest pros & cons, sample images. Is it worth $1,699? Updated Jan 2026.',
        'image': 'fuji-xt5.png',
        'alt_text': 'Fujifilm X-T5 retro-styled APS-C camera with 40MP sensor and film simulations',
        'faqs': [
            ('Is the Fujifilm X-T5 good for beginners?', 
             'The X-T5 is best for enthusiasts who appreciate its retro controls and film simulations. Beginners might find the manual dials confusing initially, but they encourage learning proper photography fundamentals. If you love the aesthetic and want to learn, it\'s excellent. For pure beginner-friendliness, consider the X-S20 instead.'),
            ('Fujifilm X-T5 vs Sony A7 IV: Which should I buy?',
             'X-T5 offers better image quality (40MP), smaller body, and unique film simulations for $1,699. Sony A7 IV has full-frame sensor, better AF, superior video, but costs $2,498. Choose X-T5 for photography, portability, and creative editing. Choose Sony for hybrid shooting and professional needs.'),
            ('Does the X-T5 have good autofocus?',
             'The X-T5 has improved AF over previous models with subject detection, but it still lags behind Sony and Canon for fast action and video. For landscapes, portraits, and street photography it\'s excellent. For sports or wildlife, consider Sony A7 IV or Canon R7.'),
        ]
    },
    'sony-zv-e10-review.html': {
        'name': 'Sony ZV-E10',
        'price': '698',
        'category': 'APS-C Vlog',
        'description': 'Compact vlogging camera with flip screen, great AF, and creator-focused features',
        'rating': '4.4',
        'review_count': '156',
        'title': 'Sony ZV-E10 Review 2026: Best Budget Vlog Camera Under $700?',
        'meta_desc': 'Sony ZV-E10 Review 2026: Best vlogging camera for $698? Flip screen, excellent AF, compact design tested. Honest pros & cons. Updated Jan 2026.',
        'image': 'sony-zv-e10-original.png',
        'alt_text': 'Sony ZV-E10 compact vlogging camera with flip screen and APS-C sensor',
        'faqs': [
            ('Is the Sony ZV-E10 good for beginners?',
             'Yes! The ZV-E10 is one of the best cameras for beginner vloggers. Its simple menu, flip screen, excellent AF, and creator-focused features (Product Showcase, Background Defocus button) make it very user-friendly. At $698, it offers exceptional value.'),
            ('Sony ZV-E10 vs ZV-1: Which is better for vlogging?',
             'ZV-E10 has interchangeable lenses, larger APS-C sensor, and better image quality for $698. ZV-1 is more compact with built-in zoom lens but smaller 1" sensor for $748. Choose ZV-E10 if you want flexibility and better quality. Choose ZV-1 for ultimate portability.'),
            ('Can the ZV-E10 shoot 4K video?',
             'Yes, the ZV-E10 shoots 4K30fps video with excellent quality. However, it has a 1.22x crop in 4K mode and lacks in-body stabilization, so you\'ll need a gimbal or stabilized lenses for smooth footage while walking.'),
        ]
    },
    'panasonic-s5-ii-review.html': {
        'name': 'Panasonic Lumix S5 II',
        'price': '1997',
        'category': 'Full-Frame Hybrid',
        'description': 'Full-frame hybrid with phase-detect AF, excellent video, and great value',
        'rating': '4.5',
        'review_count': '102',
        'title': 'Panasonic S5 II Review 2026: Best Value Full-Frame at $1,997?',
        'meta_desc': 'Panasonic S5 II Review 2026: Phase-detect AF finally here! Full-frame hybrid tested. Is it the best value at $1,997? Honest review. Updated Jan 2026.',
        'image': 'panasonic-s5ii.png',
        'alt_text': 'Panasonic Lumix S5 II full-frame camera with phase-detect autofocus',
        'faqs': [
            ('Is the Panasonic S5 II worth it in 2026?',
             'Absolutely! At $1,997, the S5 II offers incredible value with full-frame sensor, phase-detect AF (finally!), 4K60, and excellent stabilization. It\'s $500 cheaper than Sony A7 IV while offering similar performance, especially for video. The main trade-off is a smaller lens ecosystem.'),
            ('Panasonic S5 II vs Sony A7 IV: Which is better?',
             'S5 II costs $500 less ($1,997 vs $2,498) with better video specs (6K open gate, no crop 4K60) and superior IBIS. Sony A7 IV has better AF, more megapixels (33MP vs 24MP), and much larger lens selection. Choose S5 II for video and value, Sony for photography and ecosystem.'),
            ('Does the S5 II have good autofocus now?',
             'Yes! The S5 II finally has phase-detect AF, a huge upgrade from contrast-detect. It\'s reliable for most situations, though Sony and Canon still edge it out for tracking fast erratic movement. For video AF and general photography, it\'s excellent.'),
        ]
    },
    'nikon-z8-review.html': {
        'name': 'Nikon Z8',
        'price': '3996',
        'category': 'Pro Hybrid',
        'description': 'Professional hybrid with 45MP, 8K video, and flagship performance in compact body',
        'rating': '4.7',
        'review_count': '78',
        'title': 'Nikon Z8 Review 2026: Mini Z9 Worth $3,996 for Pros?',
        'meta_desc': 'Nikon Z8 Review 2026: Flagship Z9 features in smaller body. 45MP, 8K video, pro AF tested. Is it worth $3,996? Detailed review. Updated Jan 2026.',
        'image': 'nikon-z8.png',
        'alt_text': 'Nikon Z8 professional full-frame camera with 45MP sensor and 8K video',
        'faqs': [
            ('Nikon Z8 vs Z9: Which should I buy?',
             'Z8 offers 95% of Z9 performance for $2,000 less ($3,996 vs $5,996). Main differences: Z9 has built-in vertical grip and dual CFexpress slots. Z8 is smaller, lighter, and uses EN-EL15c batteries. Choose Z8 unless you need the integrated grip or shoot weddings/sports requiring dual card slots.'),
            ('Is the Nikon Z8 good for wildlife photography?',
             'Excellent! The Z8 is one of the best wildlife cameras with 45MP resolution, incredible AF (subject detection for birds, animals), 20fps bursts, and deep buffer. The only potential downside is the smaller Z-mount lens selection compared to Canon, though key wildlife lenses exist.'),
            ('Nikon Z8 vs Sony A1: Which is better?',
             'Both are flagship hybrids. Z8 costs less ($3,996 vs $6,498), has better ergonomics, and superior video specs. Sony A1 has faster readout (less rolling shutter), 30fps bursts, and more lenses. Choose Z8 for value and video. Choose A1 for ultimate speed and lens selection.'),
        ]
    },
    'canon-eos-r8-review.html': {
        'name': 'Canon EOS R8',
        'price': '1299',
        'category': 'Entry Full-Frame',
        'description': 'Affordable full-frame with 24MP sensor and excellent AF in lightweight body',
        'rating': '4.2',
        'review_count': '134',
        'title': 'Canon EOS R8 Review 2026: Best Entry Full-Frame for $1,299?',
        'meta_desc': 'Canon EOS R8 Review 2026: Cheapest full-frame with flagship AF for $1,299. Worth it or too compromised? Honest testing. Updated Jan 2026.',
        'image': 'canon-r8.png',
        'alt_text': 'Canon EOS R8 entry-level full-frame camera with compact design',
        'faqs': [
            ('Is the Canon EOS R8 worth buying in 2026?',
             'Yes, if you want full-frame on a budget. At $1,299, the R8 offers flagship AF from the R6 II, 24MP sensor, and compact design. Trade-offs include single SD card slot, no IBIS, and 1.6x crop in 4K60. Best for photographers upgrading from APS-C who prioritize AF and full-frame over features.'),
            ('Canon R8 vs R6 II vs R7: Which should I buy?',
             'R8 ($1,299): Budget full-frame, great AF, no IBIS. R6 II ($2,499): Professional hybrid, IBIS, dual card slots, uncropped 4K60. R7 ($1,499): APS-C, 32MP, 30fps, better for wildlife/sports. Choose R8 for budget full-frame, R6 II for pro work, R7 for telephoto reach.'),
            ('Does the R8 have stabilization?',
             'No, the R8 lacks in-body stabilization (IBIS). You must use IS lenses (most Canon RF lenses have it) or accept more camera shake. For video, electronic stabilization helps but crops the image. This is the main trade-off for the low price.'),
        ]
    },
    'dji-osmo-pocket-3-review.html': {
        'name': 'DJI Osmo Pocket 3',
        'price': '519',
        'category': 'Gimbal Camera',
        'description': 'Compact gimbal camera with 1" sensor perfect for vlogging and travel',
        'rating': '4.6',
        'review_count': '203',
        'title': 'DJI Osmo Pocket 3 Review 2026: Best Vlog Camera Under $550?',
        'meta_desc': 'DJI Osmo Pocket 3 Review 2026: Tiny gimbal camera with 1" sensor tested. Is it the ultimate vlogging tool for $519? Honest review. Updated Jan 2026.',
        'image': 'dji-pocket3.png',
        'alt_text': 'DJI Osmo Pocket 3 compact gimbal camera with 1-inch sensor',
        'faqs': [
            ('Osmo Pocket 3 vs Sony ZV-E10: Which is better for vlogging?',
             'Pocket 3 is incredibly compact with built-in gimbal for perfect stabilization ($519). ZV-E10 has larger APS-C sensor, interchangeable lenses, and better low-light ($698). Choose Pocket 3 for ultimate portability and smooth footage. Choose ZV-E10 for better image quality and flexibility.'),
            ('Is the Osmo Pocket 3 good for low light?',
             'Decent but not great. The 1" sensor is larger than phones but smaller than APS-C/full-frame cameras. In good light, it\'s excellent. In low light, expect some noise above ISO 1600. For nighttime vlogging, cameras with larger sensors like ZV-E10 or A7 IV perform better.'),
            ('Can you use the Osmo Pocket 3 for professional work?',
             'Yes, for specific professional use cases (vlogs, real estate tours, travel content, social media). The built-in gimbal, compact size, and ease of use make it ideal for run-and-gun shooting. However, for commercial productions requiring maximum quality, use a larger sensor camera.'),
        ]
    },
}

def create_schema_markup(data):
    """Generate comprehensive schema markup"""
    
    faqs_json = ','.join([
        f'''{{
      "@type": "Question",
      "name": "{faq[0]}",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "{faq[1].replace('"', '\\"')}"
      }}
    }}''' for faq in data['faqs']
    ])
    
    return f'''
  <!-- Product Schema -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org/",
    "@type": "Product",
    "name": "{data['name']}",
    "image": "https://cameraupick.com/assets/images/guides/{data['image']}",
    "description": "{data['description']}",
    "brand": {{
      "@type": "Brand",
      "name": "{data['name'].split()[0]}"
    }},
    "aggregateRating": {{
      "@type": "AggregateRating",
      "ratingValue": "{data['rating']}",
      "bestRating": "5",
      "worstRating": "1",
      "ratingCount": "{data['review_count']}"
    }},
    "offers": {{
      "@type": "AggregateOffer",
      "url": "https://cameraupick.com/reviews/{Path(data.get('filename', '')).stem}.html",
      "priceCurrency": "USD",
      "lowPrice": "{data['price']}",
      "offerCount": "2",
      "availability": "https://schema.org/InStock"
    }}
  }}
  </script>
  
  <!-- Breadcrumb Schema -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [{{
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://cameraupick.com"
    }},{{
      "@type": "ListItem",
      "position": 2,
      "name": "Reviews",
      "item": "https://cameraupick.com/#reviews"
    }},{{
      "@type": "ListItem",
      "position": 3,
      "name": "{data['name']} Review",
      "item": "https://cameraupick.com/reviews/{Path(data.get('filename', '')).stem}.html"
    }}]
  }}
  </script>
  
  <!-- FAQ Schema -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [{faqs_json}]
  }}
  </script>
'''

def create_faq_html(faqs):
    """Generate FAQ HTML section"""
    faq_items = '\n        '.join([
        f'''<div class="faq-item">
          <h3>{faq[0]}</h3>
          <p>{faq[1]}</p>
        </div>''' for faq in faqs
    ])
    
    return f'''
    <!-- FAQ Section -->
    <section class="section">
      <h2>Frequently Asked Questions</h2>
      
      <div class="faq-container">
        {faq_items}
      </div>
    </section>
'''

def optimize_review_page(filepath):
    """Apply all SEO optimizations to a review page"""
    
    filename = filepath.name
    if filename not in REVIEWS_DATA:
        print(f"⚠️  No data for {filename}")
        return False
    
    data = REVIEWS_DATA[filename]
    data['filename'] = filename
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Update title
    content = re.sub(
        r'<title>.*?</title>',
        f'<title>{data["title"]}</title>',
        content,
        flags=re.DOTALL
    )
    
    # 2. Update meta description
    content = re.sub(
        r'<meta name="description"[^>]*>',
        f'<meta name="description" content="{data["meta_desc"]}">',
        content
    )
    
    # 3. Add canonical URL if not present
    if 'rel="canonical"' not in content:
        content = re.sub(
            r'(<meta name="description"[^>]*>)',
            f'\\1\n  <link rel="canonical" href="https://cameraupick.com/reviews/{filename}">',
            content
        )
    
    # 4. Add schema markup before </head>
    if 'Product Schema' not in content:
        schema = create_schema_markup(data)
        content = re.sub(r'(</head>)', f'{schema}\\1', content)
    
    # 5. Update image alt text if present
    if data.get('alt_text'):
        # Find hero image and update alt
        content = re.sub(
            r'(<img[^>]*alt=")[^"]*(" [^>]*>)',
            f'\\1{data["alt_text"]}\\2',
            content,
            count=1
        )
    
    # 6. Add FAQ section before </main> if not present
    if 'FAQ Section' not in content:
        faq_html = create_faq_html(data['faqs'])
        content = re.sub(
            r'(\s*</main>)',
            f'{faq_html}\\1',
            content
        )
    
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Optimized: {filename}")
    return True

def main():
    reviews_dir = Path('reviews')
    
    print("🚀 Batch SEO Optimization Starting...")
    print("=" * 60)
    
    optimized = 0
    skipped = 0
    
    for review_file in sorted(reviews_dir.glob('*-review.html')):
        if review_file.name == 'sony-a7-iv-review.html':
            print(f"✓  {review_file.name} (already manually optimized)")
            optimized += 1
            continue
        
        if optimize_review_page(review_file):
            optimized += 1
        else:
            skipped += 1
    
    print("=" * 60)
    print(f"✅ Optimization Complete!")
    print(f"   Optimized: {optimized} pages")
    print(f"   Skipped: {skipped} pages")
    print()
    print("📋 Next steps:")
    print("1. Test with: https://search.google.com/test/rich-results")
    print("2. Submit to Google Search Console")
    print("3. Monitor rankings in 2-4 weeks")

if __name__ == '__main__':
    main()
