---
description: Comprehensive post-update verification - code compliance, live site, DE sync, optimization
---

# Post-Update Verification Workflow

Run this workflow after completing any code changes to ensure quality and consistency.

## Quick Command
```bash
// turbo-all
./scripts/post_update_verify.sh
```

---

## Step 1: Global Code Compliance Check
// turbo
```bash
python3 scripts/core/audit_code.py
```
**Expected:** < 50 issues, no new critical issues

---

## Step 2: SEO Health Verification
// turbo
```bash
python3 scripts/core/audit_seo.py
```
**Expected:** > 95% overall score

---

## Step 3: Site Health & Links
// turbo
```bash
python3 scripts/core/audit_site_health.py
```
**Expected:** 0 critical issues, < 10 warnings

---

## Step 4: Affiliate Links Verification
// turbo
```bash
python3 scripts/core/audit_affiliate_links.py
```
**Expected:** 69+ active links, 0 empty links

---

## Step 5: German (DE) Page Sync Check
// turbo
```bash
python3 scripts/i18n/audit_german_v2.py
```
**Expected:** All DE pages have matching EN structure

**Manual Checks:**
- [ ] New EN pages have corresponding DE pages
- [ ] Meta tags are localized (not just copied)
- [ ] URLs use German slugs (ratgeber, bewertungen, etc.)

---

## Step 6: Code Optimization Check
// turbo
```bash
# Check large images
find assets/images -type f -size +500k -exec ls -lh {} \; | wc -l

# Check unminified files
find assets/js -name "*.js" ! -name "*.min.js" -size +5k
find assets/css -name "*.css" ! -name "*.min.css" -size +5k
```
**Expected:** 0 large images not in WebP, all JS/CSS minified

---

## Step 7: Live Site Verification
After deploying, verify:

1. **Homepage loads** - https://cameraupick.com
2. **Sticky header works** - Header stays fixed on scroll
3. **Search works** - Type "Sony", see results
4. **Affiliate links work** - Click "Check Price" → Amazon
5. **Navigation works** - Mega menu opens on hover
6. **Mobile responsive** - Test on mobile viewport
7. **DE site works** - https://cameraupick.com/de/

---

## Step 8: Deploy to Production
// turbo
```bash
git add -A && git status
```

Then manually review and commit:
```bash
git commit -m "Your commit message"
git push origin main
```

---

## Automated Script

Create this script at `scripts/post_update_verify.sh`:

```bash
#!/bin/bash
set -e

echo "🔍 POST-UPDATE VERIFICATION"
echo "================================"

echo "\n📊 1. Code Compliance..."
python3 scripts/core/audit_code.py | tail -20

echo "\n📈 2. SEO Health..."
python3 scripts/core/audit_seo.py | tail -15

echo "\n🏥 3. Site Health..."
python3 scripts/core/audit_site_health.py | tail -15

echo "\n💰 4. Affiliate Links..."
python3 scripts/core/audit_affiliate_links.py | tail -10

echo "\n🌐 5. German Sync..."
python3 scripts/i18n/audit_german_v2.py 2>/dev/null | tail -10 || echo "Skipped - no audit script"

echo "\n⚡ 6. Optimization Check..."
large_images=$(find assets/images -type f -size +500k 2>/dev/null | wc -l)
echo "   Large images (>500KB): $large_images"

echo "\n================================"
echo "✅ VERIFICATION COMPLETE"
echo "Review any issues above before deploying."
```

---

## Checklist Summary

Before every deployment:

- [ ] **Code Compliance:** < 50 issues
- [ ] **SEO Score:** > 95%
- [ ] **Site Health:** 0 critical
- [ ] **Affiliate Links:** All active
- [ ] **DE Sync:** All pages match
- [ ] **Optimization:** Images compressed, code minified
- [ ] **Live Test:** Manual spot check

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Sticky header not working | Add `header-sticky` class to `<header>` |
| Search not working | Check `mega-menu.min.js` is loaded |
| Affiliate links broken | Run `python3 scripts/check_affiliate_ids.py` |
| DE page missing | Copy EN page, run i18n script |
| Large images | Run `/optimize_assets` workflow |
