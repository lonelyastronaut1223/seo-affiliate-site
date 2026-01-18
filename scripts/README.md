# Project Scripts

This directory contains utility scripts for maintaining and optimizing the website.

## 📂 Directory Structure

### `core/` - Essential Maintenance Tools
Scripts that should be run regularly or are critical for site health.

- **`audit_code.py`**: Comprehensive audit of HTML, images, CSS, and JS quality.
  - Usage: `python3 scripts/core/audit_code.py`
  - Output: Logs to console and saves report to `scripts/core/audit_report.json`

- **`audit_seo.py`**: In-depth SEO analysis (meta tags, schema, affiliate links).
  - Usage: `python3 scripts/core/audit_seo.py [--verbose]`

- **`generate_sitemap.py`**: Updates the `sitemap.xml` based on current content.
  - Usage: `python3 scripts/core/generate_sitemap.py`

### `i18n/` - Internationalization
Tools for translating and managing multi-language content.

- **`translate.py`**: Helper for translating content files.
- **`locales/`**: Data files for translations.

### `optimization/` - Performance Tools
Scripts to fast-track performance improvements.

- **`optimize_images.py`**: Compresses JPEG and WebP images.
  - Usage: `python3 scripts/optimization/optimize_images.py`

### `archive/` - Old & One-off Scripts
Historical scripts kept for reference. Includes:
- `maintenance/`: Old maintenance tasks
- `i18n_fixes/`: One-off translation fixes
- `optimizations/`: Previous optimization runs (broken links, bulk edits)
- `seo_tasks/`: Specific SEO implementations (adding authors, dates, schemas)

## 🚀 Common Workflows

### 1. Daily/Weekly Health Check
```bash
python3 scripts/core/audit_code.py
```

### 2. After Adding New Content
```bash
# Update sitemap
python3 scripts/core/generate_sitemap.py

# Check SEO
python3 scripts/core/audit_seo.py
```

### 3. After Adding Images
```bash
# Optimize new images
python3 scripts/optimization/optimize_images.py
```
