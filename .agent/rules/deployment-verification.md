# Deployment & Verification Rules

## Purpose
Ensure every deployment is production-ready and maintains site quality.
Prevent broken links, performance regressions, and SEO issues.

---

## Pre-Deployment Checklist

### Code Quality
- [ ] All tests pass (if applicable)
- [ ] `npm run build` completes without errors
- [ ] No console errors in browser during local testing
- [ ] Git working directory is clean (no uncommitted changes)

### Performance
- [ ] Local Lighthouse score ≥ 90 (Performance)
- [ ] Core Web Vitals meet targets:
  - LCP < 2.5s
  - FCP < 1.8s
  - CLS < 0.1
  - TBT < 200ms

### Functionality
- [ ] All internal links work (no 404s)
- [ ] Language switcher works (EN ↔ DE)
- [ ] Mobile menu opens/closes correctly
- [ ] Images load on all tested pages
- [ ] Forms submit correctly (newsletter, etc.)

---

## Deployment Process

### GitHub Push
```bash
# 1. Verify build works locally
npm run build

# 2. Commit with semantic message
git add .
git commit -m "feat: add new camera review"

# 3. Push to trigger deployment
git push origin main
```

### Netlify Auto-Deploy
- Push to `main` branch triggers automatic deployment
- Check Netlify dashboard for build status
- Wait for "Published" status before testing

---

## Post-Deployment Verification

### Immediate Checks (within 5 minutes)
1. **Homepage loads**
   - Visit `https://cameraupick.com`
   - Check for any visual regressions
   - Verify header/footer display correctly

2. **Sample pages load**
   - Test 2-3 guide pages
   - Test 1-2 review pages
   - Test German homepage `/de/`

3. **Mobile responsiveness**
   - Resize browser to 375px width
   - Check header collapses to hamburger menu
   - Verify content is readable

### SEO Validation (within 1 hour)

#### Google Rich Results Test
- URL: https://search.google.com/test/rich-results
- Test pages:
  - Homepage
  - At least 2 guide pages
  - At least 1 review page
- Verify:
  - ✅ All structured data validates
  - ✅ `WebPage`, `Organization`, `BreadcrumbList` schemas present
  - ❌ No errors or warnings

#### Schema.org Validator
- URL: https://validator.schema.org/
- Paste page HTML source
- Ensure no schema errors

### Social Media Validation (within 1 hour)

#### Facebook Sharing Debugger
- URL: https://developers.facebook.com/tools/debug/
- Input: `https://cameraupick.com`
- Verify:
  - OG image displays (1200x630px)
  - Title and description appear correctly
  - No errors or warnings
- Click "Scrape Again" if old data cached

#### Twitter Card Validator
- URL: https://cards-dev.twitter.com/validator
- Input: `https://cameraupick.com`
- Verify:
  - Card type: `summary_large_image`
  - Image loads correctly
  - Title and description match

### Performance Validation (within 2 hours)

#### PageSpeed Insights
- URL: https://pagespeed.web.dev/
- Test: `https://cameraupick.com`
- Check both Mobile and Desktop
- Targets:
  - Mobile Performance: ≥ 85
  - Desktop Performance: ≥ 95
  - All Core Web Vitals in "Good" range

#### Lighthouse (Manual)
- Open production site in incognito Chrome
- Run Lighthouse audit (Mobile)
- Verify scores:
  - Performance: ≥ 90
  - Accessibility: ≥ 95
  - Best Practices: ≥ 95
  - SEO: 100

---

## Monitoring Rules

### Daily
- Check Netlify deploy logs for errors
- Review Google Analytics for traffic anomalies

### Weekly
- Run PageSpeed Insights on homepage
- Check Search Console for new issues:
  - Core Web Vitals report
  - Mobile usability issues
  - Index coverage errors

### Monthly
- Full site crawl with Screaming Frog (optional)
- Review top 10 landing pages in Analytics
- Update camera prices and deals

---

## Rollback Procedure

If deployment breaks the site:

1. **Identify the issue**
   - Check Netlify build logs
   - Review browser console errors
   - Test locally with `npm run build`

2. **Quick fix or rollback?**
   - Quick fix: Fix + push immediately
   - Major issue: Rollback to previous deploy

3. **Rollback in Netlify**
   - Go to: Deploys → Previous deploys
   - Click "Publish deploy" on last known good version
   - Investigate issue locally before re-deploying

---

## Common Deployment Issues

### Issue: Images Not Loading
**Symptoms**: Broken image placeholders
**Cause**: Incorrect asset paths (relative instead of absolute)
**Fix**: 
```astro
<!-- Change this -->
<img src="../assets/images/camera.jpg" />

<!-- To this -->
<img src="/assets/images/camera.jpg" />
```

### Issue: 404 on Internal Links
**Symptoms**: Links to guides/reviews return 404
**Cause**: `.html` extensions in URLs
**Fix**: Remove all `.html` from `href` attributes

### Issue: Fonts Not Loading
**Symptoms**: Text displays in fallback font
**Cause**: Google Fonts blocked or CORS issue
**Fix**: Verify preconnect tags in BaseLayout

### Issue: Slow Performance
**Symptoms**: Lighthouse score drops below 90
**Cause**: New blocking scripts or large images
**Fix**: 
- Run Lighthouse with network throttling
- Check for un-deferred scripts
- Optimize new images to WebP

---

## Analytics Verification

### Google Analytics
1. Visit homepage in incognito mode
2. Check real-time report in GA4
3. Verify pageview is recorded

### Check Events
- Newsletter subscription
- Quiz completion (if applicable)
- Affiliate link clicks (if tracked)

---

## Access & Credentials

### Required Access
- GitHub repository (for commits)
- Netlify dashboard (for deploy monitoring)
- Google Search Console (for SEO monitoring)
- Google Analytics (for traffic monitoring)

### Emergency Contacts
- Netlify support: https://answers.netlify.com/
- GitHub support: https://support.github.com/

---

## Deployment Frequency

### Recommended Schedule
- **Content updates**: As needed (reviews, guides)
- **Bug fixes**: Immediately
- **Feature additions**: Weekly sprints
- **Dependency updates**: Monthly

### Avoid Deploying
- During high-traffic hours (if known)
- Late Friday evenings (harder to monitor)
- During holidays or weekends (unless urgent)

---

## Success Criteria

A deployment is successful when:
- ✅ Netlify build succeeds
- ✅ Homepage loads without errors
- ✅ Lighthouse Performance ≥ 90
- ✅ Google Rich Results Test passes
- ✅ OG image displays in Facebook debugger
- ✅ No new Search Console errors (within 24h)
- ✅ Analytics tracking works

If all criteria met → Document in changelog
If any fail → Investigate and fix immediately
