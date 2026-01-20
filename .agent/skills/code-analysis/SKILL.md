---
name: Code Analysis
description: Analyze code quality, identify technical debt, and suggest improvements
---

# Code Analysis Skill

This skill provides code analysis capabilities to maintain high code quality standards.

## Prerequisites
- Python 3.x for audit scripts
- Git for code history analysis

## Usage

Invoke this skill by saying:
- "Analyze code quality"
- "Find code issues"
- "Suggest code improvements"
- "Review technical debt"

## Analysis Categories

### 1. Static Code Analysis

**HTML Analysis**:
```bash
# Find inline styles
grep -r 'style="' *.html | wc -l

# Find missing alt attributes
grep -r '<img' *.html | grep -v 'alt=' | wc -l

# Find external links without rel attributes
grep -r 'href="http' *.html | grep -v 'rel=' | wc -l
```

**CSS Analysis**:
```bash
# Find large CSS files
find assets/css -name "*.css" -size +50k -exec ls -lh {} \;

# Find unminified CSS
find assets/css -name "*.css" ! -name "*.min.css" -size +10k
```

**JavaScript Analysis**:
```bash
# Find unminified JS
find assets/js -name "*.js" ! -name "*.min.js"

# Check for console.log (debugging statements)
grep -r 'console\.log' assets/js/
```

### 2. Performance Analysis

**Image Optimization**:
```bash
# Find large images (>500KB)
find assets/images -type f \( -name "*.jpg" -o -name "*.png" -o -name "*.webp" \) -size +500k -exec ls -lh {} \; | sort -k5 -hr

# Check WebP coverage
total_images=$(find assets/images -name "*.jpg" | wc -l)
webp_images=$(find assets/images -name "*.webp" | wc -l)
echo "WebP coverage: $webp_images / $total_images"
```

**Bundle Size Analysis**:
```bash
# Total CSS size
du -sh assets/css/

# Total JS size
du -sh assets/js/

# Total images size
du -sh assets/images/
```

### 3. Code Complexity

**File Size Analysis**:
```bash
# Find largest HTML files
find . -name "*.html" -exec wc -l {} \; | sort -nr | head -10

# Find files with most inline styles
for file in *.html; do 
  count=$(grep -o 'style="' "$file" | wc -l)
  echo "$count $file"
done | sort -nr | head -10
```

**Duplicate Code Detection**:
```bash
# Find repeated CSS rules
cat assets/css/*.css | grep -E '^\s*\.[a-z-]+\s*\{' | sort | uniq -d

# Find similar HTML structures
# (Manual review recommended)
```

### 4. Dependency Analysis

**Check for unused files**:
```bash
# Find unreferenced images
for img in assets/images/**/*; do
  if ! grep -r "$(basename $img)" *.html de/*.html > /dev/null; then
    echo "Unused: $img"
  fi
done
```

**External dependencies**:
```bash
# List all external scripts
grep -rh '<script.*src="http' *.html | sed 's/.*src="\([^"]*\)".*/\1/' | sort -u

# List all external stylesheets
grep -rh '<link.*href="http' *.html | sed 's/.*href="\([^"]*\)".*/\1/' | sort -u
```

### 5. Code Quality Metrics

Run comprehensive audit:
```bash
python3 scripts/core/audit_code.py
```

**Generates report on**:
- Large images count and sizes
- Inline styles per file
- Missing alt text
- Unminified CSS/JS
- Accessibility issues

### 6. Git History Analysis

**Code churn** (files changed frequently):
```bash
git log --pretty=format: --name-only | grep -v '^$' | sort | uniq -c | sort -rn | head -20
```

**Recent activity**:
```bash
# Files changed in last 10 commits
git log --name-status -10 --oneline
```

**Contributors**:
```bash
git shortlog -sn
```

## Improvement Recommendations

Based on analysis results, the skill will suggest:

### High Priority
- Compress images >500KB
- Remove inline styles (use CSS classes)
- Add missing alt text
- Minify CSS/JS files

### Medium Priority
- Reduce CSS file size
- Consolidate duplicate styles
- Remove unused code
- Optimize font loading

### Low Priority
- Add code comments
- Improve naming conventions
- Extract repeated patterns into components

## Automated Fixes

Some issues can be auto-fixed:

**Image compression**:
```bash
bash scripts/optimization/compress_images.sh
```

**Remove inline styles** (manual conversion to CSS classes recommended)

**Format code**:
```bash
# Install prettier
npm install -g prettier

# Format HTML
prettier --write "**/*.html"
```

## Quality Gates

Before merging code, ensure:
- [ ] No critical issues in audit_code.py
- [ ] No images >500KB
- [ ] Inline styles < 5 per file
- [ ] All images have alt text
- [ ] CSS/JS are minified

## Reporting

Generate a code quality report:

```bash
python3 scripts/core/audit_code.py > code_quality_report.txt
cat code_quality_report.txt
```

The report includes:
- Total issues count
- Breakdown by category
- Prioritized recommendations
- Affected file locations
