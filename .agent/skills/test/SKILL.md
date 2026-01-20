---
name: Test Site Quality
description: Run comprehensive tests on the SEO affiliate site including SEO, performance, and accessibility
---

# Test Site Quality Skill

This skill provides a comprehensive testing framework for the SEO affiliate site.

## Prerequisites
- Python 3.x installed
- Site audit scripts in `scripts/core/`

## Usage

Invoke this skill by saying:
- "Run all tests"
- "Test site quality"
- "Check for issues"
- "Run SEO audit"

## Test Categories

### 1. SEO Audit

```bash
python3 scripts/core/audit_seo.py
```

Checks:
- Meta tags (title, description, og tags)
- Schema markup
- Headings hierarchy
- Image alt text
- Canonical URLs

**Expected Score**: > 95%

### 2. Site Health

```bash
python3 scripts/core/audit_site_health.py
```

Checks:
- Affiliate links functionality
- Essential pages exist
- JavaScript syntax
- Internal 404 links

**Expected**: 0 critical issues

### 3. Affiliate Links

```bash
python3 scripts/core/audit_affiliate_links.py
```

Checks:
- links.min.js exists and is valid
- All buttons have proper data-product attributes
- Active vs empty links count

**Expected**: 25+ active affiliate links

### 4. Code Quality

```bash
python3 scripts/core/audit_code.py
```

Checks:
- Large images (>500KB)
- Inline styles
- Unminified CSS/JS
- Missing meta tags

**Expected**: < 50 issues

### 5. German Translation (i18n)

```bash
python3 scripts/i18n/audit_german_v2.py
```

Checks:
- English content in German pages
- Translation completeness

**Expected**: 0 English words in DE pages

## Full Test Suite

Run all tests at once:

```bash
# Create a test runner script
cat > scripts/test_all.sh << 'EOF'
#!/bin/bash
echo "🧪 Running Full Test Suite..."
echo "================================"

echo "\n📊 1. SEO Audit"
python3 scripts/core/audit_seo.py

echo "\n🏥 2. Site Health"
python3 scripts/core/audit_site_health.py

echo "\n💰 3. Affiliate Links"
python3 scripts/core/audit_affiliate_links.py

echo "\n📝 4. Code Quality"
python3 scripts/core/audit_code.py

echo "\n🌐 5. German Translation"
python3 scripts/i18n/audit_german_v2.py

echo "\n================================"
echo "✅ Test Suite Complete"
EOF

chmod +x scripts/test_all.sh
./scripts/test_all.sh
```

## Continuous Integration

For CI/CD pipelines, add this to `.github/workflows/test.yml`:

```yaml
name: Quality Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.x'
      - name: Run audits
        run: |
          python3 scripts/core/audit_site_health.py
          python3 scripts/core/audit_seo.py
```

## Performance Testing

Use Lighthouse CLI for performance scores:

```bash
npm install -g lighthouse
lighthouse https://cameraupick.com --view
```

**Target Scores**:
- Performance: > 90
- Accessibility: > 95
- Best Practices: > 95
- SEO: > 95

## Issue Resolution Priority

When tests fail, address in this order:
1. **Critical**: Broken affiliate links, 404 pages
2. **High**: SEO score < 90%, missing meta tags
3. **Medium**: Large images, inline styles
4. **Low**: Minor translation issues
