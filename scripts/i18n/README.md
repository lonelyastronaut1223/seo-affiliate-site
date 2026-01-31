# i18n Translation Scripts

Tools for maintaining English-German translation parity for the SEO affiliate site.

## Quick Start

```bash
# Check translation status
python3 scripts/i18n/audit_german_v2.py

# Sync DE homepage with EN
python3 scripts/i18n/translate_de_index.py
python3 scripts/i18n/translate_de_descriptions.py
```

---

## Available Scripts

| Script | Purpose | When to Use |
|--------|---------|-------------|
| `audit_german_v2.py` | Scan DE pages for English content | Before every deployment |
| `translate_de_index.py` | Translate homepage structure | After EN homepage update |
| `translate_de_descriptions.py` | Translate descriptions, FAQ, alt text | After EN homepage update |
| `complete_german_v3.py` | Fix FAQ Schema translations | When FAQ audit fails |
| `complete_german_v4.py` | Fix product descriptions | When product audit fails |
| `complete_german_v5.py` | Fix review page content | When review audit fails |
| `complete_german_v6.py` | Batch translate review pages | For new review pages |
| `fix_de_review_imports.py` | Fix import paths in DE reviews | After bulk page creation |
| `translate.py` | General translation utilities | As base for other scripts |

---

## Workflow

### 1. Homepage Sync
```bash
cp src/pages/index.astro src/pages/de/index.astro
python3 scripts/i18n/translate_de_index.py
python3 scripts/i18n/translate_de_descriptions.py
```

### 2. Review Page Translation
```bash
python3 scripts/i18n/complete_german_v6.py
```

### 3. Audit & Verify
```bash
python3 scripts/i18n/audit_german_v2.py
npm run build 2>&1 | grep -i error
```

---

## Adding New Translations

### To translate_de_index.py:
Add new string replacements to the `translations` list:
```python
content = content.replace('English Text', 'German Text')
```

### To translate_de_descriptions.py:
Add to the `translations` list for review descriptions:
```python
translations = [
    ("English description text", "German description text"),
    # Add more...
]
```

---

## False Positives

These English terms are acceptable in German pages:
- Technical: APS-C, IBIS, PDAF, EVF, OLED, CMOS
- Brands: Sony, Canon, Nikon, GoPro
- Loan words: Video, Vlog, Streaming, Podcast

---

## Related Resources

- [i18n Skill](.agent/skills/i18n/SKILL.md)
- [DE Page Checklist](.agent/rules/de-page-checklist.md)
- [EN-DE SEO Rules](.agent/rules/en-de-seo-rules.md)
- [Multilingual Parity Workflow](.agent/workflows/maintain_multilingual_parity.md)
