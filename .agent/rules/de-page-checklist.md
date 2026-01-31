---
trigger: always_on
---

# DE Page Creation Checklist

## Purpose
Ensure every German (DE) page is properly created with correct paths, translations, and SEO optimization.

---

## Before Creating a DE Page

### Prerequisites
- [ ] EN version exists and is finalized
- [ ] Content is reviewed and approved
- [ ] Translation priority determined

---

## File Creation Checklist

### 1. File Location
```
✅ Correct: src/pages/de/reviews/camera-review.astro
❌ Wrong:   src/pages/reviews/de/camera-review.astro
```

### 2. Import Paths (CRITICAL)
DE pages require **one extra `../`** compared to EN:

| Page Location | Import Path |
|--------------|-------------|
| `src/pages/*.astro` | `../layouts/` |
| `src/pages/de/*.astro` | `../../layouts/` |
| `src/pages/reviews/*.astro` | `../../layouts/` |
| `src/pages/de/reviews/*.astro` | `../../../layouts/` ⚠️ |

### 3. URL Paths in Links
All internal links must have `/de/` prefix:
```astro
// ❌ Wrong (will link to EN)
href="/reviews/sony-a7-iv-review"

// ✅ Correct
href="/de/reviews/sony-a7-iv-review"
```

---

## Translation Checklist

### Must Translate
- [ ] `title` prop (SEO optimized, not literal)
- [ ] `description` prop (SEO optimized)
- [ ] All `<h1>`, `<h2>`, `<h3>` headings
- [ ] All paragraph content
- [ ] Button text
- [ ] Image `alt` attributes
- [ ] Schema.org `description` fields
- [ ] FAQ questions and answers
- [ ] Meta sections (category labels)

### Must Localize
- [ ] Currency: `$` → `€` (e.g., `$1,299` → `1.299 €`)
- [ ] Number format: `1,299` → `1.299`
- [ ] Date format: `January 31, 2026` → `31. Januar 2026`

### Keep in English
- Technical terms: APS-C, IBIS, PDAF, EVF, OLED, CMOS
- Brand names: Sony, Canon, Nikon, GoPro
- Loan words: Video, Vlog, Streaming, Podcast
- Camera model names: A7 IV, R6 III, X-T5

---

## URL Slug Mapping

| EN Slug | DE Slug |
|---------|---------|
| `/guides/` | `/ratgeber/` |
| `/reviews/` | `/reviews/` (keep same) |
| `/compare/` | `/vergleiche/` |
| `/lenses/` | `/objektive/` |
| `/gear/` | `/zubehoer/` |
| `/deals` | `/angebote` |
| `/about` | `/ueber-uns` |
| `/contact` | `/kontakt` |
| `/privacy` | `/datenschutz` |
| `/terms` | `/agb` |

---

## Verification Checklist

After creating a DE page:

```bash
// Run build test
npm run build 2>&1 | grep -i error

// Run translation audit
python3 scripts/i18n/audit_german_v2.py

// Check page loads
curl -I http://localhost:4321/de/path-to-page
```

### Manual Checks
- [ ] Page loads without errors
- [ ] No visible English text (except technical terms)
- [ ] All links work and go to correct DE pages
- [ ] Images have German alt text
- [ ] Currency displayed in €
- [ ] Language switcher works both ways

---

## Common Mistakes

### 1. Wrong Import Path (Build Error)
```
Could not resolve "../../layouts/BaseLayout.astro"
```
**Fix:** Add extra `../` for DE subdirectory

### 2. Links Go to EN Pages
**Fix:** Add `/de/` prefix to all hrefs

### 3. Partial Translation
**Fix:** Run `audit_german_v2.py` and fix detected content

### 4. Missing Alt Text Translation
**Fix:** Add translations to `translate_de_descriptions.py`

---

## Quick Commands

```bash
# Create DE page from EN
cp src/pages/reviews/new-review.astro src/pages/de/reviews/new-review.astro

# Fix import paths in all DE reviews
python3 scripts/i18n/fix_de_review_imports.py

# Full translation audit
python3 scripts/i18n/audit_german_v2.py

# Build test
npm run build 2>&1 | tail -20
```
