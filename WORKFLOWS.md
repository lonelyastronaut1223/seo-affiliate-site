# Standard Operating Workflows

This project uses defined workflows to ensure quality and consistency. You can execute these workflows using the agent instructions or manually following the steps.

## 🚀 Key Workflows

### 1. [Publish New Guide](.agent/workflows/publish_new_guide.md)
**Command:** `/publish_new_guide`
> Use when adding a new review or buying guide. Covers creation, translation, and verification.

### 2. [Run Maintenance](.agent/workflows/run_maintenance.md)
**Command:** `/run_maintenance`
> **Weekly Task.** Runs code audits, SEO checks, and updates the sitemap. Use this to keep the site healthy.

### 3. [Optimize Assets](.agent/workflows/optimize_assets.md)
**Command:** `/optimize_assets`
> Use after adding new images. Compressess JPEGs and generates WebP formats.

## 🛠️ Helper Scripts
Refer to `scripts/README.md` for detailed documentation on individual internal tools located in `scripts/core`, `scripts/i18n`, and `scripts/optimization`.
