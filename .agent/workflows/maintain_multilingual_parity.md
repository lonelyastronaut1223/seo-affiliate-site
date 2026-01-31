---
description: Workflow to ensure English and German (and future) pages are perfectly synchronized in structure and content.
---

# Maintain Multilingual Parity Workflow

This workflow ensures all German pages are fully translated and synchronized with their English counterparts.

## When to Use
- After adding or modifying English content
- Before any major deployment
- Weekly maintenance check

## Workflow Steps

### 1. Audit German Pages for English Content
// turbo
```bash
python3 scripts/i18n/audit_german_v2.py
```
Check the output for remaining issues. Target is **0 issues**.

### 2. Homepage Sync (if needed)
If homepage was updated, use the dedicated workflow:
```bash
/sync-de-homepage
```

Or run manually:
// turbo
```bash
python3 scripts/i18n/translate_de_index.py
python3 scripts/i18n/translate_de_descriptions.py
```

### 3. Review Pages Translation
For review pages, use the batch translation script:
// turbo
```bash
python3 scripts/i18n/complete_german_v6.py
```

### 4. Additional Translation Scripts (if needed)
Run these for specific issue types:

| Issue Type | Script |
|------------|--------|
| FAQ Schema | `complete_german_v3.py` |
| Product descriptions | `complete_german_v4.py` |
| Review pages | `complete_german_v5.py` |
| Homepage | `translate_de_index.py` + `translate_de_descriptions.py` |
| Import paths | `fix_de_review_imports.py` |

### 5. Re-Audit to Verify
// turbo
```bash
python3 scripts/i18n/audit_german_v2.py
```
Repeat steps 2-5 until issues are minimized.

### 6. Build Test
// turbo
```bash
npm run build 2>&1 | grep -i error
```
**Expected:** No errors

### 7. Deploy Changes
```bash
git add src/pages/de/ scripts/i18n/
git commit -m "🇩🇪 i18n: Update German translations"
git push
```

## Automation Loop Pattern
The agent should follow this self-verifying pattern:
1. Run audit
2. Fix issues
3. Re-run audit
4. Continue until satisfied
5. Only then commit and deploy

## False Positives to Ignore
These English terms are acceptable in German pages:
- **Technical terms**: APS-C, IBIS, PDAF, EVF, OLED, CMOS
- **Brand names**: GoPro, Nokia OZO, HyperSmooth
- **Compound terms**: Run-and-Gun, Full-Frame Look
- **Loan words**: Video, Vlog, Podcast, Streaming

## Available Scripts Reference

| Script | Purpose |
|--------|---------|
| `audit_german_v2.py` | Main audit tool |
| `translate_de_index.py` | Homepage structure translation |
| `translate_de_descriptions.py` | Review descriptions, FAQ, alt text |
| `complete_german_v3.py` | FAQ Schema fixes |
| `complete_german_v4.py` | Product descriptions |
| `complete_german_v5.py` | Review page content |
| `complete_german_v6.py` | Batch review translation |
| `fix_de_review_imports.py` | Fix import paths |

## Estimated Time
- Initial run: 5-10 minutes
- Maintenance run: 2-3 minutes
