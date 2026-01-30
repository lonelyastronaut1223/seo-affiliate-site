---
description: Weekly price verification and deals update workflow
---

# Price Check & Deals Update Workflow

## 📅 Recommended Schedule
- **Weekly**: Every Monday morning
- **Special Events**: Black Friday, Prime Day, Holiday season - daily

---

## Step 1: Check Current Deals Status

// turbo
```bash
cat src/config/deals.config.js | head -50
```

Review active deals and expiration dates.

---

## Step 2: Verify Amazon Prices

For each product in deals, verify current price:

1. Open `src/config/affiliateLinks.js`
2. Check each deal's Amazon link is still valid
3. Note any price changes (up or down)

// turbo
```bash
grep -A5 "expiresAt" src/config/deals.config.js
```

---

## Step 3: Update Expired Deals

If a deal has expired or price returned to normal:

1. Remove from `deals.config.js`
2. Or update with new pricing info

```javascript
// Example: Update deal
{
  id: 'sony-zv-e10-deal',
  dealPrice: 698,  // Update this
  expiresAt: '2026-02-15',  // Update expiration
}
```

---

## Step 4: Add New Deals

When a new sale is discovered:

1. Add to `src/config/deals.config.js`:

```javascript
{
  id: 'new-product-deal',
  name: 'Product Name',
  originalPrice: 999,
  dealPrice: 799,
  savingsPercent: 20,
  expiresAt: '2026-MM-DD',
  isHot: true,
  category: 'camera',
  amazonUrl: 'https://amzn.to/xxx',
  description: 'Brief description of why this is a good deal'
}
```

---

## Step 5: Build and Verify

// turbo
```bash
npm run build 2>&1 | grep -E "(error|page|✓)" | tail -5
```

---

## Step 6: Commit Changes

```bash
git add src/config/deals.config.js src/pages/deals.astro src/pages/de/angebote.astro
git commit -m "chore: Weekly deals update - [DATE]

- Updated: [list updated deals]
- Added: [list new deals]
- Removed: [list expired deals]"
git push origin main
```

---

## 🔗 Quick Reference

**Amazon Price Check:**
- Open each deal's Amazon link
- Check "Other Sellers" for best price
- Note any Lightning Deals or Coupons

**Deals Categories:**
- `camera` - Camera bodies
- `lens` - Lenses
- `accessory` - SD cards, bags, tripods

**Deal Tags:**
- `isHot: true` - Featured deal (🔥 Hot Deal badge)
- `isLowest: true` - Historically lowest price
- `isNew: true` - Just added this week

---

## ⚠️ Important Notes

1. Never add deals for products we haven't reviewed
2. Verify savings claims are accurate
3. Update `lastUpdated` in deals.config.js after changes
4. DE deals should mirror EN deals with EUR prices
