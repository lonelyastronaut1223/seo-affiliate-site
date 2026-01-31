---
description: Sync German homepage with English - complete structure and content parity
---

# Sync DE Homepage Workflow

Use this workflow to ensure the German homepage matches the English homepage in structure, layout, and content.

## When to Use
- After major EN homepage updates
- After adding new sections to EN homepage
- After changing EN homepage layout

---

## Workflow Steps

### Step 1: Backup Current DE Homepage
```bash
cp src/pages/de/index.astro src/pages/de/index.astro.backup
```

### Step 2: Copy EN Homepage to DE
// turbo
```bash
cp src/pages/index.astro src/pages/de/index.astro
```

### Step 3: Run Primary Translation Script
// turbo
```bash
python3 scripts/i18n/translate_de_index.py
```

This script:
- Fixes import path (`../` → `../../`)
- Translates all section titles
- Fixes all URL paths (`/reviews/` → `/de/reviews/`)
- Translates navigation and buttons

### Step 4: Run Description Translation Script  
// turbo
```bash
python3 scripts/i18n/translate_de_descriptions.py
```

This script:
- Translates review card descriptions
- Translates FAQ answers
- Translates alt text
- Fixes price format ($ → €)

### Step 5: Build Test
// turbo
```bash
npm run build 2>&1 | grep -i error
```

**Expected:** No errors

### Step 6: Translation Audit
// turbo
```bash
python3 scripts/i18n/audit_german_v2.py
```

**Expected:** 0 English content detected

### Step 7: Visual Verification
Open both pages in browser:
```bash
open http://localhost:4321/
open http://localhost:4321/de/
```

Verify:
- [ ] Same section order
- [ ] Rating displays visible on DE
- [ ] All review cards translated
- [ ] Prices in € format
- [ ] Links go to /de/ paths

### Step 8: Commit Changes
```bash
git add src/pages/de/index.astro
git commit -m "feat(i18n): Sync DE homepage with EN"
git push
```

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Build error on import | Check `../../layouts/` path |
| English content remains | Add to translation scripts |
| Section order different | Re-copy from EN |
| Links go to EN pages | Run translate_de_index.py again |

---

## Estimated Time
5-10 minutes
