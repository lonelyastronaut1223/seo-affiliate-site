---
description: Run comprehensive project maintenance (Audit, SEO, Sitemap)
---

# Routine Maintenance Workflow

Run this workflow weekly or after significant code changes to conduct a health check of the project.

## 1. Run Comprehensive Code Audit
Check for HTML errors, missing alt tags, large images, and basic code quality issues.

```bash
python3 scripts/core/audit_code.py
```

## 2. Run Deep SEO Audit
Check for meta tags completeness, affiliate link health, and schema markup validation.

```bash
python3 scripts/core/audit_seo.py
```

## 3. Update Sitemap
Ensure `sitemap.xml` reflects all current HTML files.

```bash
python3 scripts/core/generate_sitemap.py
```

## 4. Verify Results
- Review `scripts/core/audit_report.json` if issues were found.
- Check terminal output for any critical errors (❌).

## 5. Commit Updates (if any)
If the sitemap was updated or if you fixed issues:

```bash
git add sitemap.xml
git commit -m "🔧 Maintenance: Update sitemap and fix audit issues"
```
