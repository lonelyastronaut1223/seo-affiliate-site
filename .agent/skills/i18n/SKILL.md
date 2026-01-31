---
name: i18n Translation & Localization
description: German (DE) page creation, translation scripts, and EN/DE synchronization for SEO affiliate site
---

# i18n Translation & Localization Skill

This skill covers creating and maintaining German translations that are SEO-optimized and synchronized with English content.

## When to Use
- Creating new DE pages
- Syncing DE pages with EN updates
- Running translation audits
- Fixing translation issues

---

## Quick Start

### Check Current Translation Status
```bash
// turbo
python3 scripts/i18n/audit_german_v2.py
```
Target: **0 English content detected**

### Sync DE Homepage with EN
```bash
// turbo
cp src/pages/index.astro src/pages/de/index.astro
python3 scripts/i18n/translate_de_index.py
python3 scripts/i18n/translate_de_descriptions.py
```

---

## Available Scripts

| Script | Purpose |
|--------|---------|
| `audit_german_v2.py` | Scan DE pages for remaining English content |
| `translate_de_index.py` | Translate homepage structure and navigation |
| `translate_de_descriptions.py` | Translate review descriptions, FAQ, alt text |
| `complete_german_v3.py` | Fix FAQ Schema translations |
| `complete_german_v4.py` | Fix product description translations |
| `complete_german_v5.py` | Fix review page translations |
| `complete_german_v6.py` | Batch translate review pages |
| `fix_de_review_imports.py` | Fix import paths in DE subdirectory |

---

## DE Page Creation Workflow

### Step 1: Copy EN Page
```bash
cp src/pages/reviews/new-camera-review.astro src/pages/de/reviews/new-camera-review.astro
```

### Step 2: Fix Import Paths
DE pages are one level deeper, so imports need adjustment:
```astro
// EN (src/pages/reviews/)
import BaseLayout from "../../layouts/BaseLayout.astro";

// DE (src/pages/de/reviews/)
import BaseLayout from "../../../layouts/BaseLayout.astro";
```

### Step 3: Fix URL Paths
```astro
// EN links
href="/reviews/sony-a7c-ii-review"

// DE links (add /de/ prefix)
href="/de/reviews/sony-a7c-ii-review"
```

### Step 4: Translate Content
Must translate:
- `title` and `description` props
- All headings (h1, h2, h3)
- Paragraph content
- Alt text for images
- Price formatting ($ → €)

### Step 5: Run Audit
```bash
python3 scripts/i18n/audit_german_v2.py
```

---

## Translation Guidelines

### DO
- Localize for German users (not literal translation)
- Use € for currency
- Use metric measurements
- Adapt keywords for German search behavior
- Keep structure parallel between EN and DE

### DON'T
- Translate technical terms (APS-C, IBIS, PDAF, EVF)
- Translate brand names
- Use aggressive marketing language
- Promise results ("garantiert", "perfekt")

---

## Common Issues & Fixes

| Issue | Solution |
|-------|----------|
| Import path error | Add extra `../` for DE subdirectory |
| 404 on DE review | Check URL has `/de/` prefix |
| English content detected | Run appropriate translation script |
| Price still in $ | Update to € in translations |
| Alt text in English | Add to `translate_de_descriptions.py` |

---

## File Structure

```
src/pages/
├── index.astro              # EN homepage
├── reviews/
│   └── *.astro              # EN reviews
├── de/
│   ├── index.astro          # DE homepage (synced with EN)
│   └── reviews/
│       └── *.astro          # DE reviews (imports: ../../../)
```

---

## Related Resources
- [EN/DE SEO Rules](file://.agent/rules/en-de-seo-rules.md)
- [DE Page Checklist](file://.agent/rules/de-page-checklist.md)
- [Multilingual Parity Workflow](file://.agent/workflows/maintain_multilingual_parity.md)
