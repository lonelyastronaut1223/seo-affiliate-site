# UI Consistency Rules

## ⚠️ CRITICAL PRINCIPLE — READ FIRST

> **设计一致性是绝对原则，不可违反。**

1. **禁止擅自修改界面设计** — 在没有用户明确批准的情况下，绝不修改任何现有的UI/UX设计、布局、颜色、间距或交互模式。
2. **新内容必须保持一致** — 创建新页面或新组件时，必须完全遵循现有页面的设计模式，不得引入任何视觉差异。
3. **复制而非创新** — 当不确定时，直接复制现有组件的结构和样式，而不是尝试创建新的设计。
4. **修改前必须确认** — 如果任何更改可能影响页面外观，必须先询问用户确认。

---

## Purpose
Ensure all new pages maintain visual and structural consistency with existing pages.

## Review Pages Rules

### Structure (MUST follow)
1. **Hero Section** - Title + subtitle with camera specs summary
2. **Verdict Box** - Rating, pros/cons, and "Best For" tags
3. **Specs Table** - Use existing `.specs-table` class
4. **Detailed Sections** - H2 headings with consistent padding
5. **Lens Recommendations** - Use `.product-review-card` style
6. **FAQ Section** - Use `<details>/<summary>` pattern
7. **Buy Button** - Use `.btn-buy` class with affiliate link

### Styling (MUST use)
- Colors: `#10b981` (green accent), `#f59e0b` (warning)
- Font: System font stack (no custom fonts)
- Spacing: `2rem` section padding
- Cards: `border-radius: 12px`, `box-shadow` on hover

### Template Reference
Copy structure from: `src/pages/reviews/sony-a7-v-review.astro`

---

## Comparison Pages Rules

### Structure
1. Side-by-side product cards
2. Comparison table with specs
3. Winner section for different use cases
4. Individual "Check Price" buttons

### Template Reference
Copy structure from: `src/pages/compare/fujifilm-x-s20-vs-fujifilm-x-t5.astro`

---

## Guide Pages Rules

### Structure
1. Hero with guide topic
2. "At a Glance" quick picks table
3. Individual product sections
4. Buying tips section

### Template Reference
Copy structure from: `src/pages/guides/best-cameras-for-beginners.astro`

---

## Code Rules

1. **Import layout**: `import BaseLayout from '../../layouts/BaseLayout.astro';`
2. **Use ProductSchema** for SEO
3. **Use getAffiliateLink()** for buy buttons
4. **No inline styles** - use existing CSS classes
5. **Responsive images** - use `<picture>` with WebP

---

## Checklist Before Publishing

- [ ] Hero section matches existing reviews
- [ ] Verdict box has rating + pros/cons
- [ ] Specs table uses standard format
- [ ] FAQ section included (3-5 questions)
- [ ] Buy button uses `getAffiliateLink()`
- [ ] ProductSchema component added
- [ ] Mobile responsive verified

