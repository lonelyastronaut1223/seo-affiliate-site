# Image & Asset Optimization Rules

## Purpose
Maintain fast page loads through optimized images and assets.
Every image must be web-optimized before adding to the project.

---

## Image Format Rules

### Primary Format: WebP
- **All new images** must be WebP format
- Quality setting: 80-85% (balances size vs quality)
- Provide JPEG fallback for older browsers

### Format Selection Guide
| Content Type | Primary | Fallback | Notes |
|--------------|---------|----------|-------|
| Photos (cameras, products) | WebP | JPEG | 80% quality |
| Screenshots | WebP | PNG | 85% quality |
| Logos, icons | SVG | PNG | Vector when possible |
| OG share image | PNG | - | Exact 1200x630px |

---

## Image Sizing Rules

### Hero Images (LCP Elements)
- **Desktop**: 1280px width, WebP format
- **Mobile**: 750px width, WebP format
- **Aspect ratio**: 16:9 or 21:9 (consistent)
- **File size**: < 150KB per image

### Card Thumbnails (Grid Layout)
- **Large**: 1200x800px (for 2-column grid)
- **Small**: 600x400px (mobile version)
- **Aspect ratio**: 3:2 (consistent)
- **File size**: < 80KB (large), < 30KB (small)

### Product Images (Reviews)
- **Main image**: 1200x800px
- **Comparison shots**: 800x600px
- **Detail shots**: 600x400px
- **Always**: White or neutral background

---

## Responsive Image Strategy

### Use `<picture>` for Art Direction
```html
<picture>
  <!-- WebP for modern browsers -->
  <source 
    srcset="/assets/images/hero-sm.webp 600w,
            /assets/images/hero.webp 1200w" 
    sizes="(max-width: 768px) 100vw, 50vw"
    type="image/webp">
  
  <!-- JPEG fallback -->
  <img 
    src="/assets/images/hero.jpg" 
    srcset="/assets/images/hero-sm.jpg 600w,
            /assets/images/hero.jpg 1200w"
    sizes="(max-width: 768px) 100vw, 50vw"
    alt="Descriptive alt text"
    width="1200" 
    height="800"
    loading="lazy">
</picture>
```

### Lazy Loading Rules
- **Hero/LCP image**: `loading="eager"` + `fetchpriority="high"`
- **Above-fold** (first 2-3 cards): `loading="eager"`
- **Below-fold**: `loading="lazy"`
- **Never lazy-load** images that affect LCP

---

## File Naming Convention

### Pattern
```
{category}-{descriptor}-{size}.{format}

Examples:
hero-camera-review-1280.webp
hero-camera-review-1280.jpg
card-sony-a7iv-1200.webp
card-sony-a7iv-600.webp
logo-brand.svg
og-share-image.png
```

### Rules
- All lowercase
- Hyphens (not underscores)
- Descriptive names (no `IMG_1234.jpg`)
- Include size for multiple versions
- Format extension matches actual format

---

## Directory Structure

```
public/assets/
├── images/
│   ├── guides/              # Buying guide images
│   │   ├── hero-*.webp
│   │   ├── card-*.webp
│   │   └── *.jpg           # JPEG fallbacks
│   ├── reviews/            # Camera review images
│   ├── lenses/             # Lens images
│   ├── gear/               # Accessory images
│   └── ui/                 # UI elements (icons, logos)
├── css/                    # Stylesheets
└── js/                     # JavaScript files
```

---

## Optimization Tools

### Required Tools
1. **ImageMagick** (batch conversion)
   ```bash
   # Install
   brew install imagemagick
   
   # Convert to WebP (80% quality)
   magick input.jpg -quality 80 output.webp
   ```

2. **Squoosh** (manual optimization)
   - URL: https://squoosh.app/
   - Use for one-off images
   - Compare formats side-by-side

3. **cwebp** (command-line WebP encoder)
   ```bash
   # Install
   brew install webp
   
   # Convert with specific quality
   cwebp -q 80 input.jpg -o output.webp
   ```

### Workflow Script
Create `/scripts/optimize_images.sh`:
```bash
#!/bin/bash
# Optimize all JPEG/PNG in a directory to WebP

for img in "$1"/*.{jpg,jpeg,png}; do
  [ -f "$img" ] || continue
  filename="${img%.*}"
  cwebp -q 80 "$img" -o "$filename.webp"
  echo "Converted: $img → $filename.webp"
done
```

---

## Alt Text Rules

### SEO-Optimized Alt Text
- **Be descriptive**: Include camera model, context, use case
- **Keep concise**: 125 characters or less
- **Include keywords**: Naturally, not stuffed
- **Avoid redundancy**: Don't say "image of" or "picture of"

### Examples
```html
<!-- ❌ Bad -->
<img alt="camera" />
<img alt="Image of a camera on a table" />

<!-- ✅ Good -->
<img alt="Sony A7 IV full-frame mirrorless camera with 24-70mm lens" />
<img alt="Canon EOS R8 compact camera comparison size" />
<img alt="Best travel camera 2026 hero image" />
```

---

## Image Performance Metrics

### Target Metrics
- **LCP image**: < 150KB (WebP)
- **Card thumbnail**: < 80KB (large), < 30KB (small)
- **Total images per page**: < 2MB combined
- **Image CDN**: Use Netlify's CDN (automatic)

### Monitoring
- Check Lighthouse "Properly size images" audit
- Review network waterfall for slow images
- Use PageSpeed Insights image recommendations

---

## Special Cases

### OG Share Image
- **Exact size**: 1200x630px (Facebook/Twitter requirement)
- **Format**: PNG (better text rendering)
- **Location**: `/public/og-image.png`
- **Content**: Logo + tagline + clean background
- **File size**: < 300KB

### Favicons
- **Sizes**: 16x16, 32x32, 180x180 (Apple)
- **Format**: PNG with transparency
- **Location**: `/public/assets/images/favicon.png`
- **manifest.json**: Include icon references

### Logo
- **Primary**: SVG (scalable, crisp)
- **Fallback**: PNG with transparency
- **Sizes**: Multiple (logo-sm.svg, logo.svg)

---

## CSS & JavaScript Assets

### CSS Rules
1. **Minify all CSS**: Use `.min.css` extension
2. **Combine when possible**: Reduce HTTP requests
3. **Critical CSS**: Inline if < 3KB
4. **File size target**: < 50KB per CSS file

### JavaScript Rules
1. **Minify all JS**: Use `.min.js` extension
2. **Defer non-critical**: Add `defer` attribute
3. **Avoid large libraries**: No jQuery, lodash, etc.
4. **File size target**: < 30KB per JS file (after minification)

### Version Control
```html
<!-- Add cache-busting version parameter -->
<link rel="stylesheet" href="/assets/css/style.min.css?v=20260122">
<script src="/assets/js/script.min.js?v=20260122"></script>
```

---

## Asset Delivery

### CDN Strategy
- Netlify Edge CDN (automatic)
- Cloudflare (if needed for extra caching)
- No need for external image CDN (Netlify handles it)

### Caching Headers
Netlify automatically sets:
- Images: `Cache-Control: public, max-age=31536000` (1 year)
- CSS/JS: `Cache-Control: public, max-age=31536000`
- HTML: `Cache-Control: public, max-age=0, must-revalidate`

---

## Quality Assurance

### Before Adding New Image
- [ ] Optimized to WebP (+ JPEG fallback)
- [ ] Properly sized for use case
- [ ] File size meets targets
- [ ] Descriptive filename
- [ ] Alt text written
- [ ] Tested on retina displays

### Image Audit (Monthly)
- Run Lighthouse "Optimize images" audit
- Check for oversized images (> target size)
- Review unused images (remove from project)
- Update old JPEG-only images to WebP

---

## Anti-Patterns

### ❌ Never
- Upload unoptimized images from camera/phone
- Use images larger than display size
- Serve JPEG when WebP is available
- Forget width/height attributes (causes CLS)
- Use background images for content images
- Hotlink images from other sites

### ✅ Always
- Optimize before committing to repo
- Use `<picture>` for responsive images
- Specify explicit dimensions
- Provide WebP + fallback
- Test image loading on slow networks
- Compress with 80-85% quality (visual quality is preserved)
