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

### 2. Create Targeted Translations (if needed)
If issues are found, add translations to the appropriate script:

| Issue Type | Script |
|------------|--------|
| FAQ Schema | `complete_german_v3.py` |
| Product descriptions | `complete_german_v4.py` |
| Review pages | `complete_german_v5.py` |

### 3. Apply Translations
// turbo
```bash
python3 scripts/i18n/complete_german_v3.py
python3 scripts/i18n/complete_german_v4.py
python3 scripts/i18n/complete_german_v5.py
```

### 4. Re-Audit to Verify
// turbo
```bash
python3 scripts/i18n/audit_german_v2.py
```
Repeat steps 2-4 until issues are minimized.

### 5. Deploy Changes
```bash
git add de/ scripts/i18n/
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

## Estimated Time
- Initial run: 5-10 minutes
- Maintenance run: 2-3 minutes
