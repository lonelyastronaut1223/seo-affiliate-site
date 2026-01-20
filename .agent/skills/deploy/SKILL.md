---
name: Deploy Static Site
description: Deploy the SEO affiliate site to GitHub Pages or other static hosting platforms
---

# Deploy Static Site Skill

This skill helps you deploy the static website to various hosting platforms.

## Prerequisites
- Git repository configured
- GitHub Pages enabled (for GitHub deployment)
- Or other static hosting credentials configured

## Usage

When you need to deploy the site, invoke this skill by saying:
- "Deploy the site to GitHub Pages"
- "Deploy to production"
- "Push changes and deploy"

## Deployment Options

### 1. GitHub Pages (Recommended)

The site is already configured for GitHub Pages deployment. Simply:

```bash
git add .
git commit -m "Your commit message"
git push origin main
```

GitHub Pages will automatically deploy from the `main` branch.

### 2. Netlify

Install Netlify CLI and deploy:

```bash
npm install -g netlify-cli
netlify deploy --prod
```

### 3. Vercel

Install Vercel CLI and deploy:

```bash
npm install -g vercel
vercel --prod
```

## Pre-Deployment Checklist

Before deploying, always:
- [ ] Run site health audit: `python3 scripts/core/audit_site_health.py`
- [ ] Check for broken links
- [ ] Verify affiliate links are working
- [ ] Test on multiple browsers
- [ ] Compress large images
- [ ] Update sitemap.xml

## Post-Deployment

After deployment:
- [ ] Verify site loads correctly
- [ ] Test affiliate link redirects
- [ ] Check mobile responsiveness
- [ ] Verify analytics tracking
- [ ] Monitor Core Web Vitals

## Rollback

If deployment fails:

```bash
git revert HEAD
git push origin main
```

## Monitoring

- **GitHub Actions**: Check deployment status at https://github.com/USER/REPO/actions
- **Analytics**: Monitor traffic at Google Analytics
- **Performance**: Check PageSpeed Insights
