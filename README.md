# 📷 CameraUpick - SEO-Optimized Camera Affiliate Website

> A high-performance, bilingual (EN/DE) affiliate website for camera reviews, guides, and comparisons. Built with Astro for optimal SEO and Core Web Vitals.

[![Performance](https://img.shields.io/badge/Lighthouse-92%2F100-green)](https://pagespeed.web.dev/)
[![Accessibility](https://img.shields.io/badge/Accessibility-97%2F100-brightgreen)](https://pagespeed.web.dev/)
[![SEO](https://img.shields.io/badge/SEO-100%2F100-brightgreen)](https://pagespeed.web.dev/)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com/lonelyastronaut1223/seo-affiliate-site)

---

## 🎯 Project Overview

**CameraUpick** is a professionally optimized affiliate website focused on camera equipment reviews, buying guides, and comparisons. The site serves both English and German audiences with perfectly synchronized content.

### Key Features

- 🌍 **Bilingual Content**: Full EN/DE support with synchronized pages
- ⚡ **Lightning Fast**: 92/100 Performance score, <2.9s LCP
- 📱 **Mobile-First**: Responsive design with optimized images for all devices
- 🔍 **SEO Optimized**: 100/100 SEO score, semantic HTML, proper meta tags
- ♿ **Accessible**: 97/100 Accessibility score, WCAG AA compliant
- 🎨 **Modern UI**: Clean, professional design with smooth animations
- 📊 **Comprehensive Content**: 
  - 13+ Product Reviews
  - 7+ Buying Guides
  - 4+ Comparisons
  - 3+ Lens Guides
  - 3+ Gear Guides

---

## 📊 Performance Metrics

### Latest Lighthouse Scores (Netlify)

```
Performance:      92/100  (+29 from initial 63)
Accessibility:    97/100  (+2 from initial 95)
Best Practices:   92/100  (stable)
SEO:             100/100  (perfect)
PWA:             100/100  (installable)
```

### Core Web Vitals

| Metric | Score | Status | Target |
|--------|-------|--------|--------|
| **First Contentful Paint (FCP)** | 1.6s | 🟢 Good | <1.8s |
| **Largest Contentful Paint (LCP)** | 2.9s | 🟠 Needs Improvement | <2.5s |
| **Total Blocking Time (TBT)** | 120ms | 🟢 Good | <300ms |
| **Cumulative Layout Shift (CLS)** | 0.026 | 🟢 Good | <0.1 |
| **Speed Index** | 2.3s | 🟢 Good | <3.4s |
| **Time to Interactive (TTI)** | 3.8s | 🟠 Needs Improvement | <3.8s |

### Recent Performance Improvements

**Total Optimizations**: Performance improved by **46%** (63 → 92)

1. ✅ **CSS Optimization** (+29 points)
   - Removed CSS `!important` declarations causing 3.14s render delay
   - TBT reduced from 990ms to 120ms (-88%)
   
2. ✅ **Image Optimization** (~+3-5 points expected)
   - Created 18 responsive image variants (sm/md/lg)
   - Reduced image payload by 1MB (-40%)
   - Mobile images now 60-70% smaller
   
3. ✅ **Layout Stability** 
   - CLS improved from 0.101 to 0.026 (-74%)
   - Reverted async CSS to prevent FOUC

4. ✅ **Accessibility Enhancement**
   - Skip link contrast: 21:1 ratio (WCAG AAA)
   - Language switcher contrast: improved to white (#fff)

---

## 🛠️ Tech Stack

### Core Technologies

- **Framework**: [Astro 5.3.0](https://astro.build/) - Static Site Generator
- **Language**: JavaScript/TypeScript, HTML5, CSS3
- **Styling**: Vanilla CSS with CSS Variables
- **Images**: WebP format with responsive srcset
- **SEO**: Built-in sitemap, meta tags, structured data
- **Deployment**: GitHub Pages / Netlify
- **Version Control**: Git & GitHub

### Key Dependencies

```json
{
  "astro": "^5.3.0",
  "@astrojs/sitemap": "^4.0.3",
  "sharp": "^0.33.5" // Image optimization
}
```

### Development Tools

- **Python**: Image optimization scripts (PIL/Pillow)
- **Node.js**: Build tools and package management
- **Workflows**: Automated deployment via GitHub Actions

---

## 📁 Project Structure

```
seo-affiliate-site/
├── public/
│   ├── assets/
│   │   ├── css/
│   │   │   ├── bundle.min.css          # Main styles (51KB)
│   │   │   └── review-page.css         # Review page styles
│   │   ├── js/
│   │   │   ├── links.min.js            # Affiliate links (54 products)
│   │   │   ├── mega-menu.min.js        # Navigation
│   │   │   ├── animations.min.js       # Scroll animations
│   │   │   └── script.min.js           # Core functionality
│   │   └── images/
│   │       ├── guides/                 # Guide hero images (responsive)
│   │       ├── products/               # Product images
│   │       └── reviews/                # Review page images
│   ├── robots.txt
│   └── favicon.ico
├── src/
│   ├── components/
│   │   ├── Header.astro                # Global header with nav
│   │   ├── Footer.astro                # Global footer
│   │   ├── LanguageSwitcher.astro      # EN/DE switcher
│   │   ├── AuthorBio.astro             # Reusable author component
│   │   └── ResponsiveImage.astro       # Image component
│   ├── layouts/
│   │   └── BaseLayout.astro            # Base layout with SEO meta
│   ├── pages/
│   │   ├── index.astro                 # Homepage (EN)
│   │   ├── guides/                     # Buying guides (EN)
│   │   ├── reviews/                    # Product reviews (EN)
│   │   ├── compare/                    # Comparisons (EN)
│   │   ├── lenses/                     # Lens guides (EN)
│   │   ├── gear/                       # Gear guides (EN)
│   │   ├── deals.astro                 # Deals page
│   │   ├── about.astro                 # About page
│   │   ├── contact.astro               # Contact page
│   │   └── de/                         # German version of all above
│   ├── config/
│   │   ├── affiliateLinks.js           # All affiliate URLs (54 products)
│   │   └── deals.config.js             # Deals configuration
│   └── styles/
│       └── review-page.css
├── scripts/
│   ├── core/
│   │   └── sync_links.js               # Sync affiliate links to JS
│   └── optimization/
│       ├── optimize_images.py          # Image optimization script
│       └── add_image_dimensions.py     # Add width/height attributes
├── .agent/
│   ├── skills/                         # AI coding skills
│   └── workflows/                      # Maintenance workflows
├── astro.config.mjs                    # Astro configuration
├── package.json                        # Dependencies & scripts
├── netlify.toml                        # Netlify deployment config
└── README.md                           # This file
```

---

## 🚀 Getting Started

### Prerequisites

- **Node.js**: v18.0.0 or higher
- **npm**: v9.0.0 or higher
- **Python**: v3.8+ (for image optimization)
- **Git**: For version control

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/lonelyastronaut1223/seo-affiliate-site.git
   cd seo-affiliate-site
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Install Python dependencies (optional, for image optimization)**
   ```bash
   pip install Pillow
   ```

### Development

**Start development server**
```bash
npm run dev
```
- Opens at `http://localhost:4321`
- Hot reload enabled
- Astro DevTools available

**Build for production**
```bash
npm run build
```
- Outputs to `dist/` directory
- Minifies CSS/JS
- Optimizes images
- Generates sitemap

**Preview production build**
```bash
npm run preview
```
- Serves production build locally
- Test before deployment

### Custom Scripts

**Sync affiliate links**
```bash
node scripts/core/sync_links.js
```
- Reads `src/config/affiliateLinks.js`
- Generates `public/assets/js/links.js` and `links.min.js`
- Run after updating affiliate URLs

**Optimize images**
```bash
python3 scripts/optimization/optimize_images.py
```
- Creates responsive variants (sm/md/lg)
- Optimizes quality (80-85%)
- Saves to `public/assets/images/guides/`

---

## 📝 Content Management

### Adding a New Product Review

1. **Create review page**
   ```bash
   # English version
   src/pages/reviews/your-camera-review.astro
   
   # German version
   src/pages/de/reviews/your-camera-review.astro
   ```

2. **Add affiliate link** in `src/config/affiliateLinks.js`:
   ```javascript
   'your-camera': {
       name: 'Your Camera Name',
       price: 1399,
       currency: 'USD',
       url: 'https://amzn.to/yourlink',
   }
   ```

3. **Sync affiliate links**
   ```bash
   node scripts/core/sync_links.js
   ```

4. **Update language switcher** in `src/components/LanguageSwitcher.astro`:
   ```javascript
   '/reviews/your-camera-review': '/de/reviews/your-camera-review'
   ```

5. **Add product image** to `public/assets/images/products/your-camera.webp`

### Updating Affiliate Links

1. Edit `src/config/affiliateLinks.js`
2. Run `node scripts/core/sync_links.js`
3. Build and deploy

### Creating a New Guide

1. Create guide pages (EN + DE)
2. Add hero image with responsive variants
3. Update navigation in `Header.astro`
4. Update sitemap (auto-generated on build)
5. Add to language switcher

---

## 🎨 Styling Guidelines

### CSS Architecture

- **Variables**: Colors, spacing, typography in `:root`
- **Mobile-First**: Base styles for mobile, then media queries
- **BEM-ish**: Component-scoped class names
- **No Frameworks**: Vanilla CSS for maximum performance

### Adding Styles

**For global styles**, edit `public/assets/css/bundle.min.css`:
```css
/* Don't use !important - causes render delays */
.your-class {
    property: value;
}
```

**For page-specific styles**, use scoped CSS in `.astro` files:
```astro
<style>
  .page-specific {
    /* Styles here */
  }
</style>
```

### Performance Best Practices

- ✅ Avoid `!important` (causes 3s+ render delay!)
- ✅ Use CSS variables for consistency
- ✅ Minimize specificity
- ✅ Keep selectors short
- ✅ Async load non-critical CSS

---

## 🖼️ Image Optimization

### Image Strategy

**Format**: WebP (25-35% smaller than JPEG)

**Responsive Variants**:
- `image-sm.webp`: 600px width, quality 80 (mobile)
- `image-md.webp`: 900px width, quality 80 (tablet)
- `image-lg.webp`: 1200px width, quality 85 (desktop)

### Creating Responsive Images

**Automated with Python**:
```bash
python3 scripts/optimization/optimize_images.py
```

**Manual with PIL**:
```python
from PIL import Image

img = Image.open('original.webp')
img = img.resize((600, 400), Image.LANCZOS)
img.save('optimized.webp', 'WEBP', quality=80, method=6)
```

### Using Responsive Images

```astro
<picture>
  <source
    srcset="/assets/images/guides/hero-sm.webp 600w, 
            /assets/images/guides/hero-md.webp 900w,
            /assets/images/guides/hero-lg.webp 1200w"
    sizes="(max-width: 768px) 100vw, 1200px"
    type="image/webp">
  <img 
    src="/assets/images/guides/hero-lg.webp" 
    alt="Description"
    loading="eager"
    decoding="async"
    width="1200"
    height="800">
</picture>
```

---

## 🌐 Internationalization (i18n)

### Language Support

- **English (EN)**: Default language
- **German (DE)**: Under `/de/` path

### Translation Workflow

1. **Write English content** first
2. **Translate to German** (not literal - SEO-optimized)
3. **Maintain URL mapping** in `LanguageSwitcher.astro`
4. **Sync content structure** (same sections, different wording)

### SEO Localization Rules

See `.agent/memory/en-de-seo-rules.md` for detailed guidelines:
- Adapt keywords to German search behavior
- Use natural German phrasing
- Avoid Anglicisms unless common
- Follow German consumer preferences

---

## 🔍 SEO Optimization

### Current SEO Score: 100/100

**Implemented**:
- ✅ Semantic HTML structure
- ✅ Proper heading hierarchy (H1 → H6)
- ✅ Meta descriptions (155 chars)
- ✅ Title tags optimized
- ✅ Alt text on all images
- ✅ Sitemap.xml auto-generated
- ✅ Robots.txt configured
- ✅ Canonical URLs
- ✅ hreflang tags for DE/EN
- ✅ Internal linking
- ✅ Mobile-friendly viewport
- ✅ Fast load times (<3s)

### SEO Checklist for New Pages

- [ ] Unique, descriptive title (50-60 chars)
- [ ] Meta description (150-160 chars)
- [ ] One H1 tag (contains primary keyword)
- [ ] Logical H2-H6 hierarchy
- [ ] Alt text on all images
- [ ] Internal links to related content
- [ ] Canonical URL set
- [ ] Mobile-responsive
- [ ] Page speed <3s LCP

---

## 🚢 Deployment

### GitHub Pages

**Automatic deployment** via GitHub Actions on push to `main`:

1. Commits pushed to `main` branch
2. GitHub Actions runs build
3. Deploys to `gh-pages` branch
4. Live at `https://lonelyastronaut1223.github.io/seo-affiliate-site/`

### Netlify (Alternative)

**Configuration** in `netlify.toml`:
```toml
[build]
  command = "npm run build"
  publish = "dist"

[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200
```

**Deploy**:
1. Connect GitHub repo to Netlify
2. Auto-deploys on push
3. Live at custom domain or `*.netlify.app`

### Manual Deployment

```bash
# Build
npm run build

# Deploy dist/ to your hosting
# (FTP, rsync, cloud storage, etc.)
```

---

## 🔧 Maintenance

### Regular Tasks

**Weekly**:
- [ ] Check for broken links
- [ ] Update affiliate link prices
- [ ] Monitor PageSpeed scores

**Monthly**:
- [ ] Run full site audit (`/monitor-site-health`)
- [ ] Update dependencies (`npm update`)
- [ ] Optimize new images (`optimize_images.py`)
- [ ] Review and update content

**Quarterly**:
- [ ] Update product reviews
- [ ] Refresh buying guides
- [ ] Add new camera releases
- [ ] SEO keyword research

### Useful Workflows

Available in `.agent/workflows/`:

- `/run_maintenance` - Full audit, SEO check, sitemap
- `/check-deals-prices` - Verify affiliate link prices
- `/monitor-site-health` - Comprehensive site health check
- `/optimize_assets` - Batch optimize images
- `/publish_new_guide` - Create new camera guide
- `/update_affiliate_links` - Sync affiliate links

---

## 📈 Analytics & Monitoring

### Performance Monitoring

**Tools**:
- [PageSpeed Insights](https://pagespeed.web.dev/)
- [Lighthouse](https://developer.chrome.com/docs/lighthouse/)
- [WebPageTest](https://www.webpagetest.org/)

**Metrics to Track**:
- Performance score
- LCP (Largest Contentful Paint)
- FID/INP (Interaction latency)
- CLS (Cumulative Layout Shift)
- Total Blocking Time

### SEO Monitoring

**Tools**:
- Google Search Console
- Google Analytics
- Ahrefs / SEMrush

**Metrics to Track**:
- Organic traffic
- Keyword rankings
- Click-through rates
- Bounce rate
- Conversion rate (affiliate clicks)

---

## 🐛 Troubleshooting

### Common Issues

**Issue**: Images not loading
- **Solution**: Run `npm run build` to copy images to `dist/`

**Issue**: Affiliate links not working
- **Solution**: Run `node scripts/core/sync_links.js`

**Issue**: Performance score dropped
- **Solution**: Check for new `!important` in CSS, run image optimization

**Issue**: CLS increased
- **Solution**: Add explicit `width` and `height` to images

**Issue**: Build fails
- **Solution**: Check `astro.config.mjs` and dependency versions

### Performance Regression

If Performance score drops:

1. **Check CSS**: Look for new `!important` declarations
2. **Check Images**: Verify responsive srcset is working
3. **Check JS**: Look for render-blocking scripts
4. **Run Lighthouse**: Identify specific issues
5. **Review Recent Changes**: `git log` and revert if needed

---

## 📚 Documentation

### Key Resources

- **Astro Docs**: https://docs.astro.build/
- **Lighthouse Guide**: https://web.dev/lighthouse/
- **WebP Guide**: https://developers.google.com/speed/webp
- **SEO Guide**: https://developers.google.com/search/docs

### Project-Specific Docs

- `.agent/memory/user_global.md` - Global project rules
- `.agent/memory/en-de-seo-rules.md` - Translation guidelines
- `.agent/memory/seo-content-rules.md` - Content creation rules
- `.agent/workflows/` - Maintenance workflows

---

## 🎯 Roadmap

### Completed ✅

- [x] Initial site setup with Astro
- [x] Bilingual EN/DE content
- [x] 13+ product reviews
- [x] 7+ buying guides
- [x] Affiliate link system
- [x] Responsive image optimization
- [x] Performance optimization (63 → 92)
- [x] Accessibility improvements (95 → 97)
- [x] CSS render delay fix (-2.6s)
- [x] Image payload reduction (-1MB)

### In Progress 🔄

- [ ] Remaining guide pages responsive images (6 pages)
- [ ] Product images lazy loading
- [ ] Further LCP optimization (<2.5s target)

### Future Plans 🚀

- [ ] Dark mode support
- [ ] PWA offline functionality
- [ ] AVIF image format (10-20% smaller)
- [ ] Video reviews integration
- [ ] User comments system
- [ ] Newsletter subscription
- [ ] Advanced filtering for comparisons
- [ ] AI-powered camera recommendations

---

## 📊 Changelog

### v1.3.0 - 2026-01-31
**Performance Optimization Release** (+3-5 points expected)

- ✅ Created 18 responsive image variants (sm/md/lg)
- ✅ Removed 2 unused large images (748KB)
- ✅ Updated 3 guide pages with responsive srcset
- ✅ Total image savings: 1,010KB (-40%)
- ✅ Mobile data reduction: -60-70%
- 🎯 Expected: Performance 92 → 95-97

### v1.2.0 - 2026-01-31
**CSS Performance Fix** (+29 points)

- 🔥 **Critical Fix**: Removed CSS `!important` declarations
- ✅ Element render delay: 3,140ms → 0ms (-100%)
- ✅ Total Blocking Time: 990ms → 120ms (-88%)
- ✅ Performance: 63 → 92 (+29 points, +46%)
- ✅ CLS: 0.101 → 0.026 (-74%)

### v1.1.0 - 2026-01-23
**Accessibility & Links Update**

- ✅ Improved skip-link contrast (WCAG AAA 21:1)
- ✅ Enhanced language switcher contrast
- ✅ Synced affiliate links (49 → 54 products)
- ✅ Fixed sony-zv-1-ii affiliate link

### v1.0.0 - 2026-01-22
**Initial Release**

- ✅ Full EN/DE bilingual site
- ✅ 13 product reviews
- ✅ 7 buying guides
- ✅ 4 comparisons
- ✅ SEO optimization (100/100)
- ✅ Mobile responsive
- ✅ Performance baseline (81/100)

---

## 🤝 Contributing

### Development Guidelines

1. **Follow existing patterns**
2. **Test on multiple devices**
3. **Run Lighthouse before committing**
4. **Update documentation**
5. **Follow SEO best practices**

### Code Style

- **JavaScript**: ESLint standard
- **CSS**: BEM-ish naming
- **Astro**: Component-based
- **Commits**: Conventional commits (feat:, fix:, perf:)

### Performance Rules

- ❌ Never use CSS `!important`
- ✅ Always use responsive images
- ✅ Lazy load below-fold images
- ✅ Minimize JavaScript
- ✅ Test Performance impact

---

## 📧 Contact & Support

**Project Maintainer**: Taylor  
**GitHub**: [@lonelyastronaut1223](https://github.com/lonelyastronaut1223)  
**Repository**: [seo-affiliate-site](https://github.com/lonelyastronaut1223/seo-affiliate-site)

---

## 📄 License

This project is private and proprietary. All rights reserved.

---

## 🙏 Acknowledgments

- **Astro Team** - Amazing SSG framework
- **Google Lighthouse** - Performance insights
- **WebP Team** - Superior image format
- **Netlify** - Excellent hosting platform

---

<div align="center">

**Built with ❤️ using Astro**

[⬆ Back to Top](#-cameraupick---seo-optimized-camera-affiliate-website)

</div>