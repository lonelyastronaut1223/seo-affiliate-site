# Cameraupick — Camera Reviews, Comparisons & Buying Guides

<p align="center">
  <img src="public/assets/images/logo.webp" alt="Kameraupick Logo" width="120">
</p>

<p align="center">
  <strong>Independent camera reviews for photographers and creators.</strong><br>
  🇺🇸 English · 🇩🇪 Deutsch
</p>

<p align="center">
  <a href="https://cameraupick.com">Live Site</a> •
  <a href="#features">Features</a> •
  <a href="#tech-stack">Tech Stack</a> •
  <a href="#getting-started">Getting Started</a> •
  <a href="#project-structure">Project Structure</a>
</p>

---

## Features

| Feature | Description |
|---------|-------------|
| 📷 **In-Depth Reviews** | 8 camera reviews with detailed specs, pros/cons, and FAQ sections |
| ⚖️ **Side-by-Side Comparisons** | 4 camera comparison pages with specs tables and score grids |
| 📚 **Buying Guides** | 7 curated guides (Beginners, Travel, Vlog, Budget, Hybrid, Full-Frame Video, Action/360) |
| 🔍 **Camera Finder** | Interactive 3-step quiz to find the perfect camera |
| 🌍 **Bilingual** | Full English & German localization with proper SEO per language |
| 🎬 **Number Animations** | Dynamic counter animations for scores and spec values |
| 📱 **Mobile-First** | Responsive design optimized for all devices |
| ⚡ **Performance** | Static generation, optimized WebP images, minimal JS |

---

## Tech Stack

| Technology | Purpose |
|------------|---------|
| [Astro](https://astro.build) | Static site generator |
| HTML/CSS | Semantic markup & modern styling |
| Vanilla JS | Animations, quiz logic, UI interactions |
| [anime.js](https://animejs.com) | Number counter animations |

---

## Getting Started

### Prerequisites

- Node.js 18+
- npm or yarn

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/seo-affiliate-site.git
cd seo-affiliate-site

# Install dependencies
npm install

# Start development server
npm run dev

# Build for production
npm run build

# Preview production build  
npm run preview
```

The dev server runs at `http://localhost:4321`

---

## Project Structure

```text
seo-affiliate-site/
├── src/
│   ├── components/          # Reusable Astro components
│   │   ├── Header.astro     # Internationalized navigation
│   │   ├── Footer.astro     # Internationalized footer
│   │   └── LanguageSwitcher.astro
│   ├── layouts/
│   │   └── BaseLayout.astro # Main page layout
│   └── pages/
│       ├── index.astro      # English homepage
│       ├── reviews/         # 8 camera review pages
│       ├── compare/         # 4 comparison pages
│       ├── guides/          # 7 buying guide pages
│       ├── lenses/          # 3 lens guides + index
│       ├── gear/            # 3 accessory guides + index
│       └── de/              # German localization (mirror structure)
│           ├── bewertungen/ # German reviews
│           ├── vergleiche/  # German comparisons
│           ├── ratgeber/    # German guides
│           ├── objektive/   # German lens guides
│           └── zubehoer/    # German gear guides
├── public/
│   └── assets/
│       ├── css/             # Stylesheets
│       ├── js/              # JavaScript (animations, quiz)
│       └── images/          # Optimized WebP images
├── scripts/                 # Maintenance & utility scripts
└── .agent/                  # Agent workflows & skills
```

---

## Content Overview

### Reviews (8)
| Camera | Category |
|--------|----------|
| Sony A7C II | Compact Full-Frame |
| Sony A7 IV | Hybrid Full-Frame |
| Sony ZV-E10 | Budget Vlogging |
| Canon EOS R8 | Entry Full-Frame |
| Fujifilm X-T5 | APS-C Photo-Centric |
| Nikon Z8 | Professional Hybrid |
| Panasonic S5 II | Video-Focused |
| DJI Osmo Pocket 3 | Gimbal Camera |

### Comparisons (4)
- Sony A7 IV vs Canon R6 II
- Sony A7 V vs Canon R6 III
- Sony ZV-E10 vs Sony A6700
- Fujifilm X-S20 vs Fujifilm X-T5

### Guides (7)
- Best Camera for Beginners 2026
- Best Travel Camera
- Best Vlog Camera
- Best Budget Camera Under $800
- Best Hybrid Camera
- Best Full-Frame for Video
- Best Action & 360 Camera

---

## Internationalization

The site is fully localized for English and German:

| English Route | German Route |
|---------------|--------------|
| `/reviews/*` | `/de/bewertungen/*` |
| `/compare/*` | `/de/vergleiche/*` |
| `/guides/*` | `/de/ratgeber/*` |
| `/lenses/*` | `/de/objektive/*` |
| `/gear/*` | `/de/zubehoer/*` |

Header and Footer components automatically detect the current language and display appropriate content.

---

## Development Workflows

Standardized workflows are available in `.agent/workflows/`:

| Workflow | Description |
|----------|-------------|
| `/publish_new_guide` | Create, translate, and publish new content |
| `/run_maintenance` | Weekly health checks (SEO, sitemap, audit) |
| `/optimize_assets` | Image compression and optimization |
| `/maintain_multilingual_parity` | Ensure EN/DE content sync |
| `/post-update-verify` | Verification after updates |

---

## Deployment

### Production Build

```bash
npm run build
```

Output is in the `dist/` directory.

### Hosting Options

- **GitHub Pages** — Deploy via GitHub Actions
- **Netlify** — Drag & drop or git integration
- **Vercel** — Automatic Astro detection

### Netlify Configuration

A `netlify.toml` is included with:
- Clean URL redirects
- Proper MIME types
- Cache headers for assets

---

## Monetization & Ethics

This site is reader-supported through Amazon affiliate links.

- ✅ All affiliate links use `rel="sponsored noopener noreferrer"`
- ✅ Products recommended based on quality, not commission rates
- ✅ Clear disclosure on all pages
- ✅ No fake reviews or inflated claims

---

## Scripts

Utility scripts are in `scripts/`:

```bash
# Check broken links
python scripts/check_broken_links.py

# Validate affiliate IDs
python scripts/check_affiliate_ids.py

# Generate sitemap
python scripts/generate_sitemap.py

# Optimize images
python scripts/optimize_images.py
```

---

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## License

MIT License — see [LICENSE](LICENSE) for details.

---

<p align="center">
  Made with 📷 by the Kameraupick Team
</p>