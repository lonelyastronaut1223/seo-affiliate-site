# CameraPick — Camera Reviews & Buying Guides

CameraPick is a multilingual (English / German) camera review and buying guide website.
The goal of the site is to help users choose the right camera for photography and video through clear comparisons and practical recommendations.

The project is designed as a lightweight static website and optimized for SEO and affiliate marketing.

---

## Features

- 📷 **Independent Reviews**: Unbiased camera reviews and direct comparisons.
- 🧭 **Buying Guides**: Curated lists for Beginners, Travel, Vlogging, and Hybrid shooters.
- 🛍️ **Camera Finder**: Interactive quiz (3-step logic) to recommend the perfect camera based on Usage, Experience, and Budget.
- 🔥 **Daily Deals**: Dedicated page (`deals.html`) for curated price drops and discounts.
- 🌍 **Multilingual**: Full English and German (DE) localization, including dynamic quiz content.
- ⚡ **Performance**: Pure HTML/CSS/JS with optimized WebP images for fast loading.
- 🎨 **Modern Design**: Dark mode aesthetic with glassmorphism elements and responsive layouts.

---

## Project Structure

```text
/
├── index.html              # English homepage (includes Camera Finder)
├── deals.html              # Camera deals & discounts page
├── style.css               # Global styles (Dark mode, Variables, Utilities)
├── script.js               # Main logic (Quiz, UI interactions)
├── links.js                # Affiliate link mapping (centralized)
├── /de/                    # German localization
│   ├── index.html          # German homepage (1:1 feature parity)
│   └── script-de.js        # Localized quiz logic in German
├── /guides/                # Buying guide articles
├── /reviews/               # Individual camera reviews
├── /compare/               # Direct camera comparisons
└── /assets/                # Optimized images and icons
```

---

## Deployment

This is a **static website** — no build process required.
Simply deploy the root directory to:
- GitHub Pages
- Netlify (drag & drop)
- Vercel

---

## Monetization & Ethics

This site is reader-supported via affiliate links (marked with `rel="sponsored"`).
We only recommend gear based on performance and value, not commission rates.

---

## License

MIT License