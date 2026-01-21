---
name: UI Design Best Practices
description: Comprehensive UI/UX design guidelines for creating polished, user-friendly interfaces based on proven design principles
---

# UI Design Best Practices Skill

This skill provides guidance for creating professional, user-friendly UI designs. All tips are based on real-world tested principles from Jim Raptis's UI Design Tips.

## Core Principles

### 1. Visual Hierarchy

**Always establish clear visual hierarchy to guide user attention:**

- Make your primary CTA (Call-to-Action) the most prominent element
- Use bold font-weight to emphasize important text
- Reduce opacity of secondary information
- Scale title sizes by a fixed ratio (e.g., x1.25)
- Arrange elements to the left for LTR users
- Group related elements together

**Header Design Formula:**
1. Strong font-weight for titles
2. Type scale system (1.25x ratio) - if title is 40px, subtitle is 32px
3. Lower contrast for subtitles
4. Proper line-height for body text (1.5-1.7)
5. Left alignment for readability

---

## 2. Layout & Spacing

### The Gutenberg Principle (Z-Pattern)
Users' eyes travel in a Z-shaped path from top-left to bottom-right. **Place your CTA at the end of this flow** to lead users to take action.

### Whitespace
- Prefer whitespace over dividers to separate sections
- Whitespace reduces cognitive load and makes UI cleaner
- Use dividers sparingly, only between major sections

### Border Radius Consistency
```
Outer Radius = 2 × Inner Radius
```
When using rounded cards with rounded images inside, maintain this ratio for visual harmony.

### Padding on Rounded Cards
Use **double the padding** on edges with non-round elements (text, icons) compared to edges with round elements.

### Align Uneven Elements
Set the same width for all elements in a row. Pick the width of the biggest element and apply it to all items.

### Paragraph Width
Limit line width to **500-700px** or use CSS `ch` units:
```css
max-width: 65ch; /* 65 characters per line */
```

---

## 3. Buttons & CTAs

### Always Have a CTA Above the Fold
Many visitors never scroll - offer conversion option immediately.

### Button Consistency
- Use a **single primary CTA** in your hero section
- Don't confuse users with multiple different button styles
- Keep button copy actionable and specific

### De-emphasize Dangerous Actions
- Make delete/dangerous buttons secondary (smaller, muted color, text-only style)
- Prioritize the safe/default action visually
- Use multiple traits: color, size, type, placement

### Link Buttons
- Use styled buttons instead of plain links when not in body text
- Make copy actionable and hint at the action

### Modal Button Copy
- Avoid generic "Yes" / "No" labels
- Use descriptive sentences: "Delete Project" / "Keep Project"

---

## 4. Forms & Inputs

### Self-Explanatory Inputs
1. Use placeholder text to **guide**, not just repeat labels
2. Use appropriate input types (number picker for quantities)
3. Add country codes, validation hints inline

### Pick the Correct Element
- Number picker (+/-) for small integers instead of text input
- Dropdowns for limited predefined options
- Radio buttons when options need to be visible

### Deletion Validation
**Never allow deletion without confirmation:**
- Use inline or popup confirmation dialogs
- Provide undo functionality when possible

---

## 5. Color & Branding

### Brand Color Usage
- Highlight **only the most important elements** with primary color
- Use tints & shades for secondary elements
- Over-usage of brand color is a common mistake

### Selected State
Change background color to clearly indicate selected items - simple and accessible.

### Distinguish Elements Visually
Use **multiple attributes** (color + icon) not just one:
- Helps maintain hierarchy
- Improves accessibility for color-blind users

---

## 6. Accessibility

### Icons Need Labels
Icons can be misinterpreted across cultures and experience levels:
- Add subtle text labels near icons
- Essential for mobile (no hover support)

### Tooltips on Mobile
Desktop tooltips don't work on mobile. Add a clickable help (?) icon that shows tooltip content on tap.

### Color Blind Considerations
- Never rely solely on color to convey information
- Combine color with icons, shapes, or text labels

### Transparent Avatar Fallback
For PNG avatars, add:
- Subtle border matching background color
- Background color fallback

---

## 7. Cards & Components

### Make Cards Look Clickable
- Add visible CTA buttons - don't rely on hover effects alone
- **Never leave clickability to user imagination**

### Highlight Best Pricing Option
Use multiple visual cues:
- Different color/accent
- Larger size
- Elevation (shadow)
- "Popular" or "Recommended" badge

### Empty States
- Provide **templates** instead of blank states
- Help users experience value quickly
- Boost product adoption

---

## 8. User Experience

### Users Hate Surprises
- Make button actions clear before clicking
- Add helper text explaining what will happen
- "No credit card required" / "Free 14-day trial"

### Inform Users Beforehand
- Clarify if clicking will charge money
- Explain multi-step processes
- Reduce anxiety about taking action

### Prompt Users to Scroll
Show a glimpse of the next section to:
- Signal more content exists
- Create curiosity to explore

### Display Keyboard Shortcuts
Place shortcut hints next to action buttons for power users.

---

## 9. Data Visualization

### Choose Chart Types Carefully
- Line charts: continuous data, trends over time
- Bar charts: discrete categories, limited x-axis options
- Don't use line charts for monthly totals (implies daily data)

---

## 10. Quick Reference Checklist

When designing any UI, verify:

- [ ] Primary CTA is the most prominent element
- [ ] Visual hierarchy guides eye flow
- [ ] Buttons use consistent styling
- [ ] Dangerous actions are de-emphasized
- [ ] Forms use appropriate input types
- [ ] Icons have labels (especially mobile)
- [ ] Selected states are visually clear
- [ ] Color is not the only differentiator
- [ ] Cards show clear clickability
- [ ] Line width limited for readability
- [ ] Whitespace used for separation
- [ ] Border-radius is consistent
- [ ] Empty states provide templates
- [ ] User knows what actions will do

---

## CSS Quick Reference

```css
/* Typography Scale (1.25 ratio) */
--text-xs: 0.64rem;   /* 10.24px */
--text-sm: 0.8rem;    /* 12.8px */
--text-base: 1rem;    /* 16px */
--text-lg: 1.25rem;   /* 20px */
--text-xl: 1.563rem;  /* 25px */
--text-2xl: 1.953rem; /* 31.25px */
--text-3xl: 2.441rem; /* 39px */
--text-4xl: 3.052rem; /* 48.83px */

/* Line Width for Readability */
max-width: 65ch;          /* ~65 characters */
max-width: clamp(500px, 60vw, 700px);

/* Secondary Text */
color: rgba(255, 255, 255, 0.6); /* 60% opacity for dark mode */
color: rgba(0, 0, 0, 0.6);       /* 60% opacity for light mode */

/* Consistent Border Radius */
--radius-inner: 8px;
--radius-outer: calc(var(--radius-inner) * 2);

/* Card Padding with Rounded Corners */
padding: 24px 32px; /* More horizontal for text edges */
```

---

## Source

Based on UI Design Tips by Jim Raptis: https://www.uidesign.tips/ui-tips
