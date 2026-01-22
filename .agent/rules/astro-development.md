# Astro Development Rules

## Purpose
Maintain consistent Astro development practices for this SEO affiliate site.
Ensure clean, maintainable code that leverages Astro's strengths.

---

## Project Structure

### Required Structure
```
src/
├── layouts/
│   └── BaseLayout.astro    # Single source of truth for site structure
├── components/
│   ├── Header.astro        # Site header (sticky nav)
│   └── Footer.astro        # Site footer
├── pages/
│   ├── index.astro         # Homepage
│   ├── guides/             # Buying guides
│   ├── reviews/            # Camera reviews
│   ├── lenses/             # Lens guides
│   ├── gear/               # Accessories
│   └── de/                 # German translations
public/
├── assets/                 # Static assets (CSS, JS, images)
└── og-image.png            # Social sharing image
```

---

## Routing & URLs

### Astro Clean URLs
1. **Never use `.html` extensions in links**
   ```astro
   <!-- ❌ Wrong -->
   <a href="/guides/best-camera.html">Guide</a>
   
   <!-- ✅ Correct -->
   <a href="/guides/best-camera">Guide</a>
   ```

2. **Always use absolute paths**
   ```astro
   <!-- ❌ Wrong (breaks from deep pages) -->
   <a href="./guides/best-camera">Guide</a>
   
   <!-- ✅ Correct -->
   <a href="/guides/best-camera">Guide</a>
   ```

3. **Asset paths must be absolute**
   ```astro
   <!-- ❌ Wrong -->
   <img src="../assets/images/camera.jpg" />
   
   <!-- ✅ Correct -->
   <img src="/assets/images/camera.jpg" />
   ```

---

## Component Guidelines

### BaseLayout.astro
- **Single source of truth** for site-wide structure
- Must include all meta tags, CSS, and scripts
- Props: `title`, `description`, `canonical`
- Never modify BaseLayout for page-specific needs

### Page Components
```astro
---
import BaseLayout from '../layouts/BaseLayout.astro';

const title = "Clear, descriptive title";
const description = "SEO-optimized description (150-160 chars)";
const canonical = "https://cameraupick.com/page-url";
---

<BaseLayout {title} {description} {canonical}>
  <main id="main" class="container">
    <!-- Page content -->
  </main>
</BaseLayout>
```

### Reusable Components
- Keep components small and focused
- Use TypeScript interfaces for props
- Document required vs optional props

---

## Scripts in Astro

### Script Directives
1. **`is:inline`**: Use for critical inline scripts
   - Service worker registration
   - Google Analytics (deferred)
   - Small utility functions

2. **`defer`**: Use for all other scripts
   ```astro
   <script is:inline src="/assets/js/menu.js" defer></script>
   ```

3. **Component scripts**: Avoid unless necessary
   - Astro components are server-rendered by default
   - Add client-side JS sparingly

---

## Styling Rules

### CSS Loading Order
```astro
<!-- In BaseLayout.astro <head> -->
<link rel="stylesheet" href="/assets/css/style.min.css" />
<link rel="stylesheet" href="/assets/css/footer-enhancements.min.css" />
<link rel="stylesheet" href="/assets/css/loaders.min.css" />
<link rel="stylesheet" href="/assets/css/mega-menu.min.css" />
```

### CSS Best Practices
- Use existing CSS files in `public/assets/css/`
- Avoid `<style>` tags in components (use external CSS)
- Exception: Critical above-fold CSS can be inlined
- Use CSS variables for theming

---

## SEO & Meta Tags

### Required on Every Page
```astro
---
const title = "Page Title | cameraupick";
const description = "SEO meta description";
const canonical = "https://cameraupick.com/path";
---

<BaseLayout {title} {description} {canonical}>
  <!-- Content -->
</BaseLayout>
```

### Structured Data (JSON-LD)
- BaseLayout includes `WebPage` and `Organization` schema
- Add page-specific schema in page frontmatter if needed
- Use Schema.org validator to verify

---

## Internationalization (i18n)

### German Pages
- All German pages go in `src/pages/de/`
- URL structure: `/de/path` mirrors English `/path`
- Use absolute paths in language switcher:
  ```astro
  <a href="/">EN</a>
  <a href="/de/">DE</a>
  ```

### Translation Rules
- Refer to `.agent/rules/en-de-seo-rules.md`
- Never translate word-for-word
- Adapt keywords for German search behavior
- Keep structure parallel between EN and DE

---

## Build & Development

### Local Development
```bash
npm run dev          # Start dev server (localhost:4321)
npm run build        # Build for production
npm run preview      # Preview production build
```

### Build Requirements
- Build must complete without errors
- All pages must render correctly
- No broken internal links
- Check dist/ output before deploying

### Git Workflow
```bash
# Before committing
npm run build        # Ensure build works
git add .
git commit -m "type: description"
git push
```

---

## Performance Considerations

### Server-Side Rendering (SSR)
- Astro is static by default (good for performance)
- Avoid client-side hydration unless necessary
- Heavy JS features should be deferred

### Image Optimization
```astro
<!-- Use native <picture> for responsive images -->
<picture>
  <source srcset="/assets/images/hero.webp" type="image/webp">
  <img src="/assets/images/hero.jpg" 
       alt="Descriptive alt text"
       width="1200" 
       height="800"
       loading="lazy" />
</picture>
```

---

## Common Pitfalls

### ❌ Don't
- Use relative paths for assets or links
- Include `.html` in URLs
- Modify public/ files during build (use src/ instead)
- Add client-side JS unless absolutely necessary
- Create duplicate BaseLayout variations

### ✅ Do
- Use absolute paths everywhere
- Leverage Astro's static rendering
- Keep components simple and reusable
- Test build output before deploying
- Follow existing project structure

---

## Debugging

### Common Issues
1. **Images not loading**: Check paths are absolute (`/assets/...`)
2. **Styles not applying**: Verify CSS load order in BaseLayout
3. **Links 404**: Remove `.html` extensions, use absolute paths
4. **Build fails**: Check for syntax errors in frontmatter

### Useful Commands
```bash
# Clear Astro cache
rm -rf .astro

# Inspect build output
ls -la dist/

# Test specific page
open http://localhost:4321/guides/best-camera
```

---

## Code Quality

### TypeScript Integration
```astro
---
interface Props {
  title: string;
  description: string;
  canonical?: string;  // Optional
}

const { title, description, canonical } = Astro.props;
---
```

### Comments & Documentation
- Document complex logic in frontmatter
- Explain non-obvious prop requirements
- Add TODO comments for future improvements

---

## Migration Notes

This project was migrated from static HTML to Astro.
Key considerations:
- Original HTML files preserved in root (legacy)
- All active pages now in `src/pages/`
- Asset paths converted to absolute
- Clean URLs enforced throughout
