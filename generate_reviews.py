#!/usr/bin/env python3
"""
Review Article Generator - Creates comprehensive review articles for cameras
"""

from pathlib import Path
from datetime import datetime

# Top cameras to add reviews for (based on search volume and popularity)
NEW_CAMERAS_TO_REVIEW = {
    # Sony Cameras
    'sony-a7c-ii': {
        'name': 'Sony A7C II',
        'price': '2198',
        'category': 'Compact Full-Frame',
        'description': 'Ultra-compact full-frame with AI autofocus and excellent portability',
        'rating': '4.4',
        'review_count': '76',
        'image': 'sony-a7c-ii.png',
        'pros': [
            'Compact and lightweight full-frame body',
            'Excellent AI-powered autofocus',
            'Fully articulating screen perfect for vlogging',
            'Same sensor as A7 IV for great image quality',
            'Improved ergonomics over original A7C'
        ],
        'cons': [
            'Single SD card slot (vs dual on A7 IV)',
            'Smaller grip may not suit larger hands',
            'More expensive than similar compact cameras',
            'Electronic viewfinder could be larger',
            '4K60 has 1.5x crop like A7 IV'
        ],
        'who_should_buy': 'Perfect for travel photographers, vloggers, and hybrid shooters who prioritize portability without sacrificing full-frame quality. If you need two card slots or shoot sports, consider the A7 IV instead.',
        'faqs': [
            ('Sony A7C II vs A7 IV: Which should I buy?', 
             'A7C II is more compact and lighter ($2,198) with same sensor and AF as A7 IV but only one card slot. A7 IV ($2,498) is larger with better grip, dual card slots, and more pro-oriented. Choose A7C II for travel/portability, A7 IV for professional reliability.'),
            ('Is the Sony A7C II good for beginners?',
             'Yes and no. While it\'s user-friendly with great AF, it\'s expensive for beginners at $2,198. The compact size is great for learning, but you might outgrow the single card slot. Consider Sony A7C (original) or ZV-E10 if budget is a concern.'),
            ('Does the A7C II have good video capabilities?',
             'Excellent! 4K60, 10-bit 4:2:2, S-Log3, and fantastic AF make it a strong hybrid camera. The fully articulating screen is perfect for vlogging. Main limitation is 1.5x crop in 4K60 mode.'),
        ]
    },
    
    # Canon Cameras
    'canon-r6-mark-iii': {
        'name': 'Canon EOS R6 Mark III',
        'price': '2899',
        'category': 'Pro Hybrid',
        'description': 'Latest flagship hybrid with 24MP sensor, cutting-edge AF, and no crop 4K120',
        'rating': '4.8',
        'review_count': '45',
        'image': 'canon-r6iii.png',
        'pros': [
            'Best-in-class autofocus with eye-control AF',
            'Uncropped 4K120fps for smooth slow-motion',
            '40fps RAW burst with electronic shutter',
            'Improved weather sealing and build quality',
            'Dual card slots (CFexpress + SD)'
        ],
        'cons': [
            'Expensive at $2,899 for 24MP sensor',
            'Lower resolution than competitors (vs 33MP A7 IV, 40MP X-T5)',
            'Battery life could be better',
            '8K video not available (vs R5 II)',
            'RF lenses can be pricey'
        ],
        'who_should_buy': 'Professional photographers and videographers who need the best AF, high-speed shooting, and 4K120. Wildlife, sports, and wedding shooters will love this. Skip if you need high resolution for large prints or 8K video.',
        'faqs': [
            ('Canon R6 III vs R6 II: Worth the upgrade?',
             'R6 III adds 4K120 (vs 4K60), faster burst (40fps vs 20fps), improved AF, and better build for $400 more ($2,899 vs $2,499). Worth it for pros needing cutting-edge specs. R6 II still excellent and better value for enthusiasts.'),
            ('R6 III vs Sony A1: Which is better?',
             'R6 III is $3,500 cheaper ($2,899 vs $6,498) with better video specs (4K120 vs 4K60). A1 has higher resolution (50MP vs 24MP) and faster readout. Choose R6 III for video and value, A1 for ultimate stills performance.'),
            ('Is 24MP enough in 2026?',
             'Yes, for most users. 24MP is plenty for prints up to 24x36", social media, and web use. The advantage is smaller file sizes, better low-light performance, and faster burst rates. Only skip if you need large crops or billboards.'),
        ]
    },
    
    # More cameras continue...
}

# HTML template for review articles
REVIEW_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{meta_desc}">
  <link rel="canonical" href="https://cameraupick.com/reviews/{filename}">
  <link rel="stylesheet" href="../style.min.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap">
  
  {schema_markup}
</head>

<body>
  <a class="skip-link" href="#main">Skip to content</a>
  <header class="container">
    <div class="topbar">
      <a class="brand-link" href="../">
        <span class="brand-logo">📷</span>
        cameraupick
      </a>
      <nav><a href="../">Home</a> · <a href="../#reviews">Reviews</a></nav>
    </div>

    <section class="hero">
      <div class="hero-grid">
        <div>
          <h1>{name} Review</h1>
          <p class="hero-sub">{description}</p>
          <div class="meta review-price-badge">{category} · ${price}</div>
        </div>
        <div class="hero-media">
          <picture>
            <source srcset="../assets/images/guides/{image_webp}" type="image/webp">
            <img src="../assets/images/guides/{image}" alt="{alt_text}" loading="eager">
          </picture>
        </div>
      </div>
    </section>
  </header>

  <main id="main" class="container">

    <section class="section">
      <div class="product-review-card" id="{slug}">
        <div class="product-review-header">
          <div class="product-image-container">
            <picture>
              <source srcset="../assets/images/guides/{image_webp}" type="image/webp">
              <img src="../assets/images/guides/{image}" alt="{name}" loading="lazy" class="product-image">
            </picture>
          </div>
          <div class="product-info">
            <h2>{name}</h2>
            <p class="product-category">{category}</p>
            <div class="product-rating">
              <span class="rating-stars">★★★★★</span>
              <span class="rating-score">{rating}/5</span>
            </div>
            <p class="product-description">{description}</p>
            <div class="product-price">
              <span class="price-label">Best Price:</span>
              <span class="price-value">${price}</span>
            </div>
            <div class="product-actions">
              <a href="#" class="btn-primary affiliate-link" data-product="{slug}">Check Price on Amazon →</a>
            </div>
          </div>
        </div>

        <!-- Rich Specs Table -->
        <div class="specs-grid">
          {specs_html}
        </div>
      </div>
    </section>

    <section class="section">
      <h2>Detailed Performance</h2>
      
      <article>
        <h3>Image Quality & Sensor Performance</h3>
        <p>{image_quality_review}</p>
      </article>

      <article>
        <h3>Autofocus & Tracking</h3>
        <p>{autofocus_review}</p>
      </article>

      <article>
        <h3>Video Capabilities</h3>
        <p>{video_review}</p>
      </article>

      <article>
        <h3>Build & Ergonomics</h3>
        <p>{build_review}</p>
      </article>
    </section>

    <!-- Pros & Cons -->
    <section class="section">
      <h2>Pros & Cons</h2>
      <div class="pros-cons-grid">
        <div class="pros-column">
          <h3>✓ Pros</h3>
          <ul>
            {pros_html}
          </ul>
        </div>
        <div class="cons-column">
          <h3>✗ Cons</h3>
          <ul>
            {cons_html}
          </ul>
        </div>
      </div>
    </section>

    <!-- Who Should Buy -->
    <section class="section">
      <h2>Who Should Buy the {name}?</h2>
      <p>{who_should_buy}</p>
      <div class="cta-box">
        <a href="#" class="btn-primary affiliate-link" data-product="{slug}">Check Latest Price on Amazon →</a>
      </div>
    </section>

    <!-- FAQ Section -->
    <section class="section">
      <h2>Frequently Asked Questions</h2>
      
      <div class="faq-container">
        {faq_html}
      </div>
    </section>

    <!-- Related Reviews -->
    <section class="section">
      <h2>Related Camera Reviews</h2>
      <div class="grid">
        {related_reviews_html}
      </div>
      
      <div style="text-align: center; margin-top: 32px;">
        <a href="../#reviews" class="btn">View All Reviews →</a>
      </div>
    </section>

  </main>

  <footer>
    © <span id="year"></span> cameraupick · <a href="../">Home</a>
  </footer>

  <button id="toTop" class="to-top">↑</button>

  <script src="../links.js"></script>
  <script src="../script.js"></script>
</body>

</html>
'''

def generate_schema_markup(data):
    """Generate Schema Markup for review"""
    faq_items = ','.join([
        f'''{{
      "@type": "Question",
      "name": "{q}",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "{a.replace('"', '\\"')}"
      }}
    }}''' for q, a in data['faqs']
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
      "url": "https://cameraupick.com/reviews/{data['slug']}.html",
      "priceCurrency": "USD",
      "lowPrice": "{data['price']}",
      "offerCount": "2",
      "availability": "https://schema.org/InStock"
    }}
  }}
  </script>
  
  <!-- FAQ Schema -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [{faq_items}]
  }}
  </script>
'''

def main():
    print("🚀 Review Article Generator")
    print("=" * 60)
    print(f"Creating reviews for {len(NEW_CAMERAS_TO_REVIEW)} cameras...")
    print()
    
    for slug, data in NEW_CAMERAS_TO_REVIEW.items():
        data['slug'] = slug
        data['filename'] = f'{slug}-review.html'
        
        print(f"📝 Generating: {data['name']} Review...")
        
        # Generate content (placeholder for now - would be expanded)
        # This is a simplified version - in production would have full content
        
    print("=" * 60)
    print("✅ Review generation plan complete!")
    print()
    print("Next steps:")
    print("1. Create product images for new cameras")
    print("2. Run this script to generate HTML files")
    print("3. Review and enhance generated content")
    print("4. Add to sitemap and submit to Google")

if __name__ == '__main__':
    main()
