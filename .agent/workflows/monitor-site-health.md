---
description: Comprehensive site health monitoring - run before ANY deployment or after major changes
---

# Site Health Monitoring Workflow

> **IMPORTANT**: This workflow MUST be run before ANY deployment to catch critical issues like broken affiliate links, 404 pages, or missing translations.

## Pre-Deployment Checklist

// turbo-all

### 1. Run Full Site Audit
```bash
cd /Users/taylor/Downloads/Project/SEO-Affiliate/seo-affiliate-site
python3 scripts/core/audit_site_health.py
```

### 2. Check Affiliate Links
```bash
python3 scripts/core/audit_affiliate_links.py
```

### 3. Check for 404s (Missing Pages)
```bash
python3 scripts/core/check_404s.py
```

### 4. Verify German Translations
```bash
python3 scripts/i18n/audit_german_v2.py
```

### 5. SEO Audit
```bash
python3 scripts/core/audit_seo.py
```

## Critical Checks (Manual)

### Affiliate Links
- [ ] Open homepage, click "Check Price" buttons - should go to Amazon
- [ ] Open a review page, click "Check Price" button - should go to Amazon
- [ ] Console should show "Links applied. Updated X comparisons/buttons."

### Page Accessibility
- [ ] Test all footer links (About, Contact, Privacy, Terms, Impressum)
- [ ] Test all navigation links
- [ ] Test German page equivalents

### Before Git Push
Always run:
```bash
git status
git diff --stat
```

Review changed files to ensure nothing critical was accidentally modified.

## Emergency Recovery

If affiliate links break:
```bash
# Check if links.min.js exists and is valid
cat assets/js/links.min.js | head -50

# Check git history for recent changes
git log --oneline -5 assets/js/links.min.js

# Restore from last known good version
git checkout HEAD~1 -- assets/js/links.min.js
```

## Reporting

After running audits, report any issues to the user immediately with:
- Number of issues found
- Severity (Critical/Warning/Info)
- Specific files affected
- Recommended fixes
