#!/usr/bin/env python3
"""
自动评测文章生成器
Based on the User's Preferred Design (Fujifilm X-T5 style)
Features:
- "The Verdict" text section
- Rich Specs Table (Imaging, Video, Body)
- "What We Like" / "The Downsides" Pros/Cons
- Detailed Performance Cards
- Ideal Lenses Grid
"""

from pathlib import Path
import json

# 完整的相机数据库
CAMERAS_DATABASE = {
    'sony-a7c-ii': {
        'name': 'Sony A7C II',
        'price': '2198',
        'category': 'Compact Full-Frame',
        'badge': '✨ Best for Travel',
        'brand': 'Sony',
        # Specs
        'sensor': '33MP Full-Frame BSI CMOS',
        'processor': 'BIONZ XR + AI Unit',
        'ibis': '5-Axis (7.0 stops)',
        'video_res': '4K 60p (S35) / 4K 30p (FF)',
        'internal_rec': '10-bit 4:2:2',
        'profiles': 'S-Log3, S-Cinetone, LUTs',
        'evf': '2.36M-dot OLED (0.7x)',
        'screen': '3.0" Vari-angle Touch',
        'card_slots': '1x SD UHS-II',
        'weight': '515g (with battery)',
        
        'rating': '4.5',
        'review_count': '76',
        'image': 'sony-a7c-ii.png',
        
        'verdict_p1': 'The Sony A7C II is a marvel of engineering, squeezing the powerful A7 IV into a body barely larger than an APS-C camera. It’s the dream camera for travel photographers who demand full-frame quality without the bulk.',
        'verdict_p2': 'With Sony’s latest AI autofocus chip, it tracks subjects with uncanny accuracy. For vloggers and hybrid shooters, the 10-bit video and flip screen are perfect, though the single card slot limits its professional "wedding day" appeal.',
        
        'image_quality': 'The 33MP sensor provides a sweet spot for resolution and file size. Dynamic range is excellent, recovering shadows cleanly. High ISO performance is solid up to 6400.',
        'handling': 'The grip is improved over the original A7C but still small for large lenses. The new front dial makes manual exposure much easier. It feels dense and premium.',
        'video_perf': '4K60p is sharp but incurs a 1.5x crop. The Active Stabilization mode works wonders for walking shots, effectively removing the need for a gimbal for casual b-roll.',
        
        'pros': [
            'Tiny body with uncompromising full-frame sensor',
            'Best-in-class AI Autofocus tracking',
            'Excellent 10-bit 4:2:2 video quality',
            'Vari-angle screen great for content creation'
        ],
        'cons': [
            'Single SD card slot risk for pros',
            '1.5x crop in 4K60 mode',
            'Small, lower-resolution viewfinder',
            'No joystick for AF point selection'
        ],
        
        'lenses': [
            {'name': 'Sony 20-70mm f/4 G', 'desc': 'The perfect modern travel zoom with extra width.'},
            {'name': 'Sony 40mm f/2.5 G', 'desc': 'Tiny prime that matches the body size perfectly.'},
            {'name': 'Tamron 28-75mm f/2.8 G2', 'desc': 'Bright, light, and sharp standard zoom.'}
        ],
        
        'faqs': [
            {'q': 'Is the single card slot a dealbreaker?', 'a': 'For travel and hobbyists, no. For paid weddings, maybe.'},
            {'q': 'Does it overheat?', 'a': 'Better than the A7C, but compact bodies do get warm in 4K60.'}
        ],
        'related_cameras': ['sony-a7-iv', 'canon-eos-r8', 'fujifilm-x-t5']
    },
    'sony-a7-iv': {
        'name': 'Sony A7 IV',
        'price': '2498',
        'category': 'Full-frame Hybrid',
        'badge': '🏆 Best All-Rounder',
        'brand': 'Sony',
        # Specs
        'sensor': '33MP Full-Frame BSI CMOS',
        'processor': 'BIONZ XR',
        'ibis': '5-Axis (5.5 stops)',
        'video_res': '4K 60p (S35) / 4K 30p (FF)',
        'internal_rec': '10-bit 4:2:2',
        'profiles': 'S-Log3, S-Cinetone',
        'evf': '3.69M-dot OLED (0.78x)',
        'screen': '3.0" Vari-angle Touch',
        'card_slots': '2x (1x CFexpress A/SD, 1x SD)',
        'weight': '658g (with battery)',
        
        'rating': '4.7',
        'review_count': '128',
        'image': 'sony-a7iv.png',
        
        'verdict_p1': 'The Sony A7 IV defines the modern standard for hybrid mirrorless cameras. It does almost everything well, balancing resolution, speed, and video features in a strictly professional body.',
        'verdict_p2': 'Unlike the A7C II, this offers the redundancy of dual card slots and a significantly better EVF and grip. It is the workhorse choice for event photographers and serious videographers.',
        
        'image_quality': '33MP offers plenty of crop potential. Colors are accurate and the RAW files are incredibly pliable. It is a significant step up from the 24MP of the A7 III.',
        'handling': 'The deep grip is comfortable for all-day shooting with heavy lenses. The full-size HDMI port is a huge plus for video work compared to flimsy micro-HDMI ports.',
        'video_perf': 'Focus breathing compensation with Sony lenses is a game changer. Rolling shutter is noticeable in 4K24p full-frame, but the S35 4K60p image is stunningly detailed.',
        
        'pros': [
            'Dual card slots for professional peace of mind',
            'Full-size HDMI port',
            'Excellent ergonomics and deep grip',
            'Huge lens selection'
        ],
        'cons': [
            '4K60 has a 1.5x crop',
            'Rolling shutter in full-frame video',
            'Screen resolution is merely average',
            'Burst rate drops with highest quality RAWs'
        ],
        
        'lenses': [
            {'name': 'Sony 24-70mm f/2.8 GM II', 'desc': 'Ultimate pro zoom, surprisingly light.'},
            {'name': 'Sony 85mm f/1.8', 'desc': 'Affordable, sharp, fast portrait lens.'},
            {'name': 'Sigma 24-70mm f/2.8 DG DN', 'desc': 'Great value alternative to the GM.'}
        ],
        
        'faqs': [
            {'q': 'A7 IV or A7C II?', 'a': 'A7 IV for pros (dual slots, grip). A7C II for travel.'},
            {'q': 'Is it good for sports?', 'a': '10fps is okay, but stacking sensor cameras like A9/A1 are better.'}
        ],
        'related_cameras': ['sony-a7c-ii', 'canon-eos-r6-ii', 'panasonic-s5-ii']
    }
}

HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{name} Review 2026: Details, Specs & Verdict</title>
  <meta name="description" content="{name} Review 2026: Detailed testing of image quality, autofocus, and video. Is it worth ${price}?">
  <link rel="canonical" href="https://cameraupick.com/reviews/{filename}">
  <link rel="stylesheet" href="../style.min.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap">
  
{schema_markup}
</head>

<body>
  <div class="reading-progress">
    <div class="progress-bar"></div>
  </div>

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
          <p class="hero-sub">{verdict_p1}</p>
          <div class="meta review-price-badge">{category} · ${price}</div>
        </div>
        <div class="hero-media">
          <picture>
            <img src="../assets/images/guides/{image}" alt="{name}" loading="eager">
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
            <span class="badge-best">{badge}</span>
            <picture>
              <img src="../assets/images/guides/{image}" alt="{name} Product Shot">
            </picture>
          </div>
          <div class="product-info">
            <h2 class="product-title">The Verdict</h2>
            <p>{verdict_p1}</p>
            <p>{verdict_p2}</p>

            <!-- Rich Specs Table -->
            <table class="specs-table">
              <tr>
                <th colspan="2" class="specs-group-header">Imaging</th>
              </tr>
              <tr>
                <th>Sensor</th>
                <td>{sensor}</td>
              </tr>
              <tr>
                <th>Processor</th>
                <td>{processor}</td>
              </tr>
              <tr>
                <th>Stabilization</th>
                <td>{ibis}</td>
              </tr>

              <tr>
                <th colspan="2" class="specs-group-header">Video</th>
              </tr>
              <tr>
                <th>Max Resolution</th>
                <td>{video_res}</td>
              </tr>
              <tr>
                <th>Internal Rec</th>
                <td>{internal_rec}</td>
              </tr>
              <tr>
                <th>Profiles</th>
                <td>{profiles}</td>
              </tr>

              <tr>
                <th colspan="2" class="specs-group-header">Body & Connectivity</th>
              </tr>
              <tr>
                <th>Viewfinder</th>
                <td>{evf}</td>
              </tr>
              <tr>
                <th>Screen</th>
                <td>{screen}</td>
              </tr>
              <tr>
                <th>Card Slots</th>
                <td>{card_slots}</td>
              </tr>
              <tr>
                <th>Weight</th>
                <td>{weight}</td>
              </tr>
            </table>

            <a href="#" class="btn-buy" rel="sponsored noopener noreferrer" target="_blank" data-product="{slug}">
              Check Price on Amazon &rarr;
            </a>
          </div>
        </div>

        <div class="pros-cons">
          <div class="pros">
            <h4>What We Like</h4>
            <ul>
{pros_html}
            </ul>
          </div>
          <div class="cons">
            <h4>The Downsides</h4>
            <ul>
{cons_html}
            </ul>
          </div>
        </div>
      </div>
    </section>

    <section class="section">
      <h2>Detailed Performance</h2>
      <div class="grid">
        <article class="card card-plain">
          <h3>Image Quality</h3>
          <p>{image_quality}</p>
        </article>
        <article class="card card-plain">
          <h3>Handling & Build</h3>
          <p>{handling}</p>
        </article>
        <article class="card card-plain">
          <h3>Video Performance</h3>
          <p>{video_perf}</p>
        </article>
      </div>
    </section>

    <section class="section">
      <h2>Ideal Lenses</h2>
      <div class="grid">
{lenses_html}
      </div>
    </section>

    <section class="section" id="affiliate">
      <h2>Affiliate Disclosure</h2>
      <p class="section-sub">
        We buy our own gear or rent it. No manufacturers paid for this review. We earn a commission if you use our
        links, which keeps this site ad-free.
      </p>
    </section>
    
    <section class="section">
      <h2>Frequently Asked Questions</h2>
      <div class="faq-container">
{faq_html}
      </div>
    </section>
    
    <section class="section">
      <h2>Related Reviews</h2>
      <div class="grid">
        <article class="card">
           <div class="card-thumb"><img src="../assets/images/guides/fujifilm-x-t5.png" alt="X-T5"></div>
           <h3><a href="fujifilm-x-t5-review.html">Fujifilm X-T5 Review</a></h3>
        </article>
         <article class="card">
           <div class="card-thumb"><img src="../assets/images/guides/canon-eos-r8.png" alt="R8"></div>
           <h3><a href="canon-eos-r8-review.html">Canon R8 Review</a></h3>
        </article>
      </div>
    </section>

  </main>

  <footer class="site-footer">
    <div class="footer-content">
      <div class="footer-links">
        <a href="../">Home</a>
        <a href="../#reviews">Reviews</a>
        <a href="../#guides">Guides</a>
        <a href="../#deals">Deals</a>
      </div>
       <div class="social-links">
        <a href="https://youtube.com/@cameraupick" target="_blank" rel="noopener" aria-label="YouTube">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>
        </a>
        <a href="https://twitter.com/cameraupick" target="_blank" rel="noopener" aria-label="Twitter">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>
        </a>
        <a href="https://instagram.com/cameraupick" target="_blank" rel="noopener" aria-label="Instagram">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
        </a>
      </div>
      <p class="footer-copy">© <span id="year"></span> cameraupick</p>
    </div>
  </footer>

  <button id="toTop" class="to-top">↑</button>

  <script src="../links.js"></script>
  <script src="../script.js"></script>
</body>
</html>'''

def generate_schema_markup(camera):
    faq_template = '''    {{
      "@type": "Question",
      "name": "{q}",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "{a}"
      }}
    }}'''
    
    faq_items_list = []
    for faq in camera['faqs']:
        safe_answer = faq['a'].replace('"', '\\"')
        faq_items_list.append(faq_template.format(q=faq['q'], a=safe_answer))
    
    faq_items = ',\n'.join(faq_items_list)
    
    schema_template = '''  <!-- Product Schema -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org/",
    "@type": "Product",
    "name": "{name}",
    "image": "https://cameraupick.com/assets/images/guides/{image}",
    "description": "{description}",
    "brand": {{
      "@type": "Brand",
      "name": "{brand}"
    }},
    "aggregateRating": {{
      "@type": "AggregateRating",
      "ratingValue": "{rating}",
      "bestRating": "5",
      "worstRating": "1",
      "ratingCount": "{review_count}"
    }},
    "offers": {{
      "@type": "AggregateOffer",
      "url": "https://cameraupick.com/reviews/{slug}.html",
      "priceCurrency": "USD",
      "lowPrice": "{price}",
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
      "name": "{name} Review",
      "item": "https://cameraupick.com/reviews/{slug}.html"
    }}]
  }}
  </script>
  
  <!-- FAQ Schema -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
{faq_items}
    ]
  }}
  </script>'''

    return schema_template.format(
        name=camera['name'],
        image=camera['image'],
        description=camera.get('verdict_p1', '')[:150] + '...', # shortened description
        brand=camera['brand'],
        rating=camera['rating'],
        review_count=camera['review_count'],
        slug=camera['slug'],
        price=camera['price'],
        faq_items=faq_items
    )

def generate_review_html(slug, camera_data):
    """生成完整的评测HTML"""
    camera = camera_data.copy()
    camera['slug'] = slug
    camera['filename'] = f'{slug}-review.html'
    
    camera['schema_markup'] = generate_schema_markup(camera)
    
    # Generate list HTML
    camera['pros_html'] = '\n'.join([f'              <li>{pro}</li>' for pro in camera['pros']])
    camera['cons_html'] = '\n'.join([f'              <li>{con}</li>' for con in camera['cons']])
    
    # Generate Lenses HTML
    lens_template = '''        <article class="card card-plain">
          <h3>{name}</h3>
          <p>{desc}</p>
        </article>'''
    camera['lenses_html'] = '\n'.join([lens_template.format(**lens) for lens in camera.get('lenses', [])])
    
    # Generate FAQ HTML
    faq_items = []
    for faq in camera['faqs']:
        faq_items.append(f'''        <div class="faq-item">
          <h3>{faq['q']}</h3>
          <p>{faq['a']}</p>
        </div>''')
    camera['faq_html'] = '\n'.join(faq_items)
    
    return HTML_TEMPLATE.format(**camera)

def main():
    print("🚀 Auto Review Generator (X-T5 Style)")
    print("=" * 60)
    
    output_dir = Path('reviews')
    output_dir.mkdir(exist_ok=True)
    
    for slug, camera_data in CAMERAS_DATABASE.items():
        print(f"\n📝 Generating: {camera_data['name']}")
        html_content = generate_review_html(slug, camera_data)
        output_file = output_dir / f'{slug}-review.html'
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        print(f"   ✓ Saved: {output_file}")
    
    print("\n✅ All reviews generated successfully!")

if __name__ == '__main__':
    main()
