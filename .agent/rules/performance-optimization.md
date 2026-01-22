# Performance Optimization Rules

## Purpose
Maintain exceptional website performance for SEO and user experience.
All changes must preserve or improve Core Web Vitals scores.

---

## Core Web Vitals Targets

### Required Thresholds
- **LCP (Largest Contentful Paint)**: < 2.5s (Target: < 1.0s)
- **FCP (First Contentful Paint)**: < 1.8s (Target: < 0.8s)
- **TBT (Total Blocking Time)**: < 200ms (Target: 0ms)
- **CLS (Cumulative Layout Shift)**: < 0.1 (Target: 0)
- **INP (Interaction to Next Paint)**: < 200ms

### Lighthouse Score Targets
- Performance: ≥ 90
- Accessibility: ≥ 95
- Best Practices: ≥ 95
- SEO: 100

---

## Image Optimization Rules

1. **Always use WebP format** for modern browsers
   - Provide JPEG fallback in `<picture>` elements
   - Use `type="image/webp"` in source tags

2. **Specify dimensions** on all images
   - Width and height attributes prevent CLS
   - Match actual display size (no oversized images)

3. **Lazy loading strategy**
   - Hero/LCP image: `loading="eager"` + `fetchpriority="high"`
   - Above-fold images: `loading="eager"`
   - Below-fold images: `loading="lazy"`

4. **Responsive images**
   - Use `srcset` and `sizes` for multi-resolution support
   - Serve appropriate sizes for mobile/tablet/desktop

---

## Script Loading Rules

1. **Never block the main thread**
   - All non-critical scripts must have `defer` attribute
   - Use `async` only for truly independent scripts

2. **Defer heavy interactive features**
   ```javascript
   // Use requestIdleCallback for non-critical features
   if (window.requestIdleCallback) {
       requestIdleCallback(loadQuiz, { timeout: 1000 });
   } else {
       setTimeout(loadQuiz, 100);
   }
   ```

3. **Minimize inline scripts**
   - Only critical path code should be inline
   - Everything else goes to external .js files with defer

4. **Third-party scripts**
   - Google Analytics: deferred via requestIdleCallback
   - Other analytics: load after page interactive
   - Never load third-party CSS/fonts synchronously

---

## CSS Optimization Rules

1. **Critical CSS strategy**
   - Inline critical CSS if < 3KB
   - Otherwise preload with `<link rel="preload" as="style">`

2. **Font loading**
   - Always use `font-display: swap`
   - Preload font CSS, not font files directly
   - Use system fonts as fallback

3. **Avoid render-blocking CSS**
   - Split CSS by page/component when possible
   - Use media queries to defer non-critical CSS

---

## Resource Hints

### Always Include
```html
<!-- Fonts -->
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />

<!-- Analytics -->
<link rel="preconnect" href="https://www.googletagmanager.com" />
<link rel="dns-prefetch" href="https://www.googletagmanager.com" />

<!-- CDNs -->
<link rel="preconnect" href="https://cdnjs.cloudflare.com" />
```

### Preload Critical Resources
- LCP image (hero image)
- Primary stylesheet
- Web fonts (only if visible above fold)

---

## Mobile Performance Rules

1. **Mobile-first optimization**
   - Test on real devices, not just DevTools
   - Throttle network to "Slow 3G" during testing

2. **Reduce mobile payload**
   - Serve smaller images via `srcset`
   - Consider removing heavy animations on mobile

3. **Touch-friendly interactions**
   - Buttons ≥ 48x48px tap target
   - No hover-only interactions

---

## Testing Requirements

### Before Every Commit
- Run local dev server Lighthouse audit
- Check Network tab for unexpected resources
- Verify no console errors

### Before Deploy
- Run Lighthouse on production build
- Test on mobile device (real or emulator)
- Verify Core Web Vitals in PageSpeed Insights

### After Deploy
- Monitor Real User Metrics (RUM) via Search Console
- Check for new CLS issues in production
- Verify analytics is working

---

## Anti-Patterns to Avoid

❌ **Never do this:**
- Load heavy libraries (jQuery, etc.) unless absolutely necessary
- Use synchronous `<script>` tags for non-critical code
- Forget image dimensions (causes CLS)
- Load fonts without `font-display: swap`
- Use oversized images "just in case"
- Add tracking scripts without deferring
- Implement auto-playing videos above fold
- Use `setTimeout(fn, 0)` instead of `requestIdleCallback`

✅ **Always do this:**
- Preload LCP element
- Defer all non-critical JavaScript
- Use WebP + JPEG fallback
- Test on slow networks
- Minimize main thread work

---

## Monitoring

### Tools
- Google PageSpeed Insights (weekly)
- Lighthouse CI (on every deploy)
- Search Console Core Web Vitals report (monthly)
- WebPageTest (for detailed waterfall analysis)

### Key Metrics to Watch
- Field data (real users) vs Lab data
- 75th percentile scores (Google's threshold)
- Mobile vs Desktop performance gap
