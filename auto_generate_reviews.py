#!/usr/bin/env python3
"""
自动评测文章生成器
使用模板和数据自动生成完整的相机评测文章
"""

from pathlib import Path
from datetime import datetime
import json

# 完整的相机数据库
CAMERAS_DATABASE = {
    'sony-a7c-ii': {
        'name': 'Sony A7C II',
        'price': '2198',
        'category': 'Compact Full-Frame',
        'brand': 'Sony',
        'sensor': '33MP Full-Frame',
        'video': '4K60 (1.5x crop)',
        'af_points': '759 phase-detect',
        'burst_rate': '10fps',
        'weight': '515g',
        'rating': '4.4',
        'review_count': '76',
        'image': 'sony-a7c-ii.png',
        
        # 详细评测内容
        'description': 'Ultra-compact full-frame camera with AI autofocus and exceptional portability',
        'tagline': 'The perfect full-frame camera for travelers and vloggers who refuse to compromise on quality',
        
        'image_quality': '''The Sony A7C II inherits the excellent 33MP sensor from the A7 IV, delivering outstanding image quality in a remarkably compact body. Dynamic range is superb at 14+ stops, with clean files up to ISO 6400 and usable results even at ISO 12800. The sensor's back-illuminated design ensures excellent low-light performance, making this an ideal camera for travel photography where lighting conditions are unpredictable.

Color science is classic Sony, with accurate color reproduction out of camera and excellent flexibility in post-processing thanks to 14-bit RAW files. The camera handles high-contrast scenes beautifully, with shadows that lift cleanly and highlights that roll off smoothly. For landscape photographers, the resolution is more than adequate for large prints, while the file sizes remain manageable for extensive travel shoots.''',
        
        'autofocus': '''Sony's latest AI processing unit brings significant improvements to autofocus performance. Real-time tracking is exceptional, with the camera reliably detecting and following human subjects (including eyes), animals, birds, and vehicles. The 759 phase-detect points cover nearly the entire frame, ensuring sharp focus even with off-center compositions.

In practice, the AF rarely hunts, even in challenging low-light situations down to -4 EV. Face and eye detection work flawlessly for portraiture, while animal eye AF is a game-changer for pet photography. The only scenarios where the AF struggles slightly are with very fast erratic movement, but for most travel, street, and portrait work, it's near-perfect.''',
        
        'video': '''Video capabilities are strong, with 4K60 recording at 10-bit 4:2:2 internally. The main limitation is the 1.5x crop in 4K60 mode, which can be restrictive with wider lenses. However, 4K30 is uncropped and delivers beautiful results. S-Log3 provides excellent dynamic range for color grading, though the camera also offers pleasing Rec.709 profiles for those who prefer to shoot ready-to-use footage.

The fully articulating screen is perfect for vlogging, and the compact size makes the A7C II ideal for gimbal work. Overheating is well-controlled, with the camera lasting comfortably through 30-minute+ recording sessions in moderate temperatures. Active stabilization mode helps smooth out handheld footage, though it does add an additional crop.''',
        
        'build': '''Build quality is excellent despite the compact dimensions. The magnesium alloy body feels solid and features comprehensive weather sealing, making it suitable for adventure photography. The grip, while smaller than the A7 IV, is still comfortable for extended shooting sessions, though photographers with larger hands might prefer adding a battery grip.

The control layout is well thought out, with key settings easily accessible. The mode dial includes a dedicated video mode, and the customizable buttons allow for personalized workflows. The electronic viewfinder is bright and clear at 2.36M dots, though it's slightly smaller than flagship models. Battery life is impressive at approximately 530 shots per charge, or longer when using the EVF sparingly.''',
        
        'pros': [
            'Compact and lightweight full-frame body perfect for travel',
            'Excellent 33MP image quality with strong dynamic range',
            'Outstanding AI-powered autofocus with subject detection',
            'Fully articulating screen ideal for vlogging and creative angles',
            'Improved ergonomics over original A7C with better grip',
            'Comprehensive weather sealing for adventure photography',
            'Long battery life (530 shots rated)',
            'Same sensor performance as the more expensive A7 IV'
        ],
        
        'cons': [
            'Single SD card slot (vs dual on A7 IV)',
            'Smaller grip may not suit photographers with larger hands',
            'More expensive than compact APS-C alternatives',
            'Electronic viewfinder could be larger and higher resolution',
            '4K60 has 1.5x crop (no uncropped option)',
            'Limited native lens selection for compact setup',
            'No built-in flash (though most won\'t miss it)'
        ],
        
        'who_should_buy': '''Perfect for travel photographers, vloggers, and hybrid shooters who prioritize portability without sacrificing full-frame image quality. The A7C II excels for street photography, documentary work, and any scenario where a smaller camera allows for more discreet shooting. 

Ideal buyers are photographers upgrading from APS-C who want full-frame performance in a package that won't weigh them down on day-long shoots or international trips. Content creators will love the vlogging features and excellent AF.

Skip this camera if you need dual card slots for professional reliability, shoot fast-action sports extensively, or have larger hands that would be more comfortable with the A7 IV's grip. Also consider alternatives if budget is tight - the original A7C offers similar portability at lower cost.''',
        
        'faqs': [
            {
                'q': 'Sony A7C II vs A7 IV: Which should I buy?',
                'a': 'A7C II is more compact and lighter ($2,198) with the same sensor and AF as A7 IV but only one card slot. A7 IV ($2,498) is larger with better grip, dual card slots, and more pro-oriented controls. Choose A7C II for travel and portability, A7 IV for professional reliability and ergonomics. The $300 difference is worth it if you need two card slots or prefer a larger camera.'
            },
            {
                'q': 'Is the Sony A7C II good for beginners?',
                'a': 'Yes and no. While it\'s user-friendly with excellent AF and intuitive menus, it\'s expensive for beginners at $2,198. The compact size is great for learning and building confidence, but beginners might outgrow the single card slot quickly. Consider the original Sony A7C (now discounted) or the ZV-E10 if budget is a concern, then upgrade later.'
            },
            {
                'q': 'Does the A7C II have good video capabilities?',
                'a': 'Excellent for most users! 4K60, 10-bit 4:2:2, S-Log3, and fantastic AF make it a strong hybrid camera. The fully articulating screen is perfect for vlogging. Main limitation is 1.5x crop in 4K60 mode - if you need uncropped 4K60, look at the Canon R6 II or Panasonic S5 II. For 4K30 work, it\'s nearly perfect.'
            },
            {
                'q': 'What lenses work best with the A7C II for compact setup?',
                'a': 'For maximum portability: Sony 28-60mm kit lens (tiny!), Sony 24mm f/2.8 G, Sony 40mm f/2.5 G, Sony 50mm f/2.5 G, or Tamron 20-40mm f/2.8. These keep the system compact. Avoid large lenses like the 24-70 GM which negate the body\'s compact advantage.'
            },
            {
                'q': 'Is one SD card slot a deal-breaker?',
                'a': 'Depends on your needs. For professional wedding/event work, yes - you need backup redundancy. For travel, landscapes, portraits, and content creation, it\'s fine with reliable UHS-II cards. Use high-quality cards and backup regularly. If you must have dual slots, get the A7 IV for $300 more.'
            }
        ],
        
        'related_cameras': ['sony-a7-iv', 'canon-eos-r8', 'fujifilm-x-t5']
    },
    
    # 可以继续添加更多相机...
}

# HTML模板
HTML_TEMPLATE = '''<!DOCTYPE html>
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
          <p class="hero-sub">{tagline}</p>
          <div class="meta review-price-badge">{category} · ${price}</div>
        </div>
        <div class="hero-media">
          <picture>
            <img src="../assets/images/guides/{image}" alt="{name} {alt_suffix}" loading="eager">
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
            <img src="../assets/images/guides/{image}" alt="{name}" loading="lazy" class="product-image">
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

        <div class="specs-grid">
          <div class="spec-item">
            <span class="spec-label">Sensor</span>
            <span class="spec-value">{sensor}</span>
          </div>
          <div class="spec-item">
            <span class="spec-label">Video</span>
            <span class="spec-value">{video}</span>
          </div>
          <div class="spec-item">
            <span class="spec-label">Autofocus</span>
            <span class="spec-value">{af_points}</span>
          </div>
          <div class="spec-item">
            <span class="spec-label">Burst Rate</span>
            <span class="spec-value">{burst_rate}</span>
          </div>
          <div class="spec-item">
            <span class="spec-label">Weight</span>
            <span class="spec-value">{weight}</span>
          </div>
        </div>
      </div>
    </section>

    <section class="section">
      <h2>Detailed Performance</h2>
      
      <article>
        <h3>Image Quality & Sensor Performance</h3>
        {image_quality_html}
      </article>

      <article>
        <h3>Autofocus & Tracking</h3>
        {autofocus_html}
      </article>

      <article>
        <h3>Video Capabilities</h3>
        {video_html}
      </article>

      <article>
        <h3>Build & Ergonomics</h3>
        {build_html}
      </article>
    </section>

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

    <section class="section">
      <h2>Who Should Buy the {name}?</h2>
      {who_should_buy_html}
      <div class="cta-box">
        <a href="#" class="btn-primary affiliate-link" data-product="{slug}">Check Latest Price on Amazon →</a>
      </div>
    </section>

    <section class="section">
      <h2>Frequently Asked Questions</h2>
      
      <div class="faq-container">
{faq_html}
      </div>
    </section>

    <section class="section">
      <h2>Related Camera Reviews</h2>
      <div class="grid">
{related_html}
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

</html>'''

def generate_schema_markup(camera):
    """生成Schema Markup"""
    faq_items = ',\n'.join([
        f'''    {{
      "@type": "Question",
      "name": "{faq['q']}",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "{faq['a'].replace('"', '\\"')}"
      }}
    }}''' for faq in camera['faqs']
    ])
    
    return f'''  <!-- Product Schema -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org/",
    "@type": "Product",
    "name": "{camera['name']}",
    "image": "https://cameraupick.com/assets/images/guides/{camera['image']}",
    "description": "{camera['description']}",
    "brand": {{
      "@type": "Brand",
      "name": "{camera['brand']}"
    }},
    "aggregateRating": {{
      "@type": "AggregateRating",
      "ratingValue": "{camera['rating']}",
      "bestRating": "5",
      "worstRating": "1",
      "ratingCount": "{camera['review_count']}"
    }},
    "offers": {{
      "@type": "AggregateOffer",
      "url": "https://cameraupick.com/reviews/{camera['slug']}.html",
      "priceCurrency": "USD",
      "lowPrice": "{camera['price']}",
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
      "name": "{camera['name']} Review",
      "item": "https://cameraupick.com/reviews/{camera['slug']}.html"
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

def format_paragraphs(text):
    """将长文本分成段落"""
    paragraphs = text.strip().split('\n\n')
    return '\n        '.join([f'<p>{p.strip()}</p>' for p in paragraphs if p.strip()])

def generate_review_html(slug, camera_data):
    """生成完整的评测HTML"""
    camera = camera_data.copy()
    camera['slug'] = slug
    camera['filename'] = f'{slug}-review.html'
    
    # 生成各部分HTML
    camera['title'] = f"{camera['name']} Review 2026: Worth ${camera['price']}? Honest Pros & Cons"
    camera['meta_desc'] = f"{camera['name']} Review 2026: {camera['description']} Detailed testing, pros & cons. Updated Jan 2026."
    camera['alt_suffix'] = camera['category'].lower() + ' camera'
    
    camera['schema_markup'] = generate_schema_markup(camera)
    
    # 格式化内容部分
    camera['image_quality_html'] = format_paragraphs(camera['image_quality'])
    camera['autofocus_html'] = format_paragraphs(camera['autofocus'])
    camera['video_html'] = format_paragraphs(camera['video'])
    camera['build_html'] = format_paragraphs(camera['build'])
    camera['who_should_buy_html'] = format_paragraphs(camera['who_should_buy'])
    
    # 生成优缺点列表
    camera['pros_html'] = '\n'.join([f'            <li>{pro}</li>' for pro in camera['pros']])
    camera['cons_html'] = '\n'.join([f'            <li>{con}</li>' for con in camera['cons']])
    
    # 生成FAQ
    faq_items = []
    for faq in camera['faqs']:
        faq_items.append(f'''        <div class="faq-item">
          <h3>{faq['q']}</h3>
          <p>{faq['a']}</p>
        </div>''')
    camera['faq_html'] = '\n'.join(faq_items)
    
    # 生成Related Reviews（简化版，需要实际数据）
    camera['related_html'] = '''        <article class="card">
          <div class="card-thumb">
            <img src="../assets/images/guides/sony-a7iv.png" alt="Sony A7 IV" loading="lazy">
          </div>
          <h3><a href="sony-a7-iv-review.html">Sony A7 IV Review</a></h3>
          <p>Same sensor, larger body with dual card slots.</p>
        </article>'''
    
    return HTML_TEMPLATE.format(**camera)

def main():
    print("🚀 自动评测文章生成器")
    print("=" * 60)
    
    output_dir = Path('reviews')
    output_dir.mkdir(exist_ok=True)
    
    generated_count = 0
    
    for slug, camera_data in CAMERAS_DATABASE.items():
        print(f"\n📝 生成评测: {camera_data['name']}")
        
        html_content = generate_review_html(slug, camera_data)
        
        output_file = output_dir / f'{slug}-review.html'
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"   ✓ 已保存: {output_file}")
        print(f"   - 字数: ~{len(html_content.split())} words")
        print(f"   - Schema: ✓ Product + FAQ + Breadcrumb")
        print(f"   - FAQ: {len(camera_data['faqs'])} questions")
        
        generated_count += 1
    
    print("\n" + "=" * 60)
    print(f"✅ 完成！生成了 {generated_count} 篇评测文章")
    print("\n下一步:")
    print("1. 检查生成的HTML文件")
    print("2. 运行 batch_seo_optimizer.py 进行SEO优化")
    print("3. 测试页面显示")
    print("4. 提交到Git并部署")

if __name__ == '__main__':
    main()
