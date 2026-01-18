---
description: Batch optimization for images (JPEG/WebP) and other assets
---

# Asset Optimization Workflow

Run this workflow after adding new images to the `assets/images/` directory.

## 1. Optimize Images
Compress large JPEG images and generate efficient WebP versions for all valid images.
*Note: This script skips PNGs to avoid quality loss, refer to manual tools for PNG optimization if needed.*

```bash
python3 scripts/optimization/optimize_images.py
```

## 2. Verify Output
Check the output for:
- Size reduction percentages
- Any skipped files (usually meaning they are already optimized)

## 3. Update HTML References (Manual)
If you generated new WebP files for existing images, ensure your HTML uses them.
*Example Pattern:*
```html
<picture>
  <source srcset="../assets/images/example.webp" type="image/webp">
  <img src="../assets/images/example.jpg" alt="Example Description">
</picture>
```

## 4. Commit Changes
```bash
git add assets/images/
git commit -m "🖼️ Assets: Optimize images"
```
