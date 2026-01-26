---
description: Automatically sync and update affiliate links after changing src/config/affiliateLinks.js
---

# Update Affiliate Links Workflow

Use this workflow whenever `src/config/affiliateLinks.js` is modified to ensure all frontend assets and cache-busting versions are updated.

// turbo-all
## 1. Sync, Minify, and Update
Run the main update script which handles synchronization, minification, and cache-busting versioning in HTML files.

```bash
./scripts/update-links.sh
```

## 2. Verify Link Health
Run the affiliate link audit to ensure no broken or empty links were introduced.

```bash
python3 scripts/core/audit_affiliate_links.py
```

## 3. Deployment
The script above will prompt for a git commit and push. Always follow through to ensure changes are live.
