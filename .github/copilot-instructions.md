<!-- Copilot / AI agent instructions for this repo -->
# Copilot instructions — SEO_Affiliate_Automatic_Content_Site

Purpose: give AI coding agents the minimal, actionable knowledge to be productive editing this static SEO affiliate site.

- **Big picture**: This is a small, static multi-page site (HTML + CSS) focused on product reviews, buying guides, and comparisons. Content lives as individual HTML files organized by topic (examples: `guides/`, `reviews/`, `compare/`). There is an English root and a German localized folder at `de/`.

- **Key files & structure**:
  - `index.html`: site shell and example page layout (navigation, hero, sections for guides/reviews/compare).
  - `de/index.html`: German localized variant. Use this pattern for language folders.
  - `style.css`: global styles used across pages. Common classes to reuse: `site-header`, `container`, `hero`, `badge`, `grid`, `card`, `site-footer`.
  - Content directories referenced from `index.html`: `guides/`, `reviews/`, `compare/` (add new files there as slugged HTML pages).

- **Why things are organized this way**: the site is optimized for SEO and predictable URLs — each guide/review/comparison is a standalone HTML file with a clear slug. Language variants are separate directories (not inlined). Keep URLs stable when editing.

- **Content & SEO conventions (discoverable from files)**:
  - Each page should include a descriptive `<title>` and a `<meta name="description">` tuned for search intent.
  - Filenames use lowercase hyphen-separated slugs, e.g. `best-camera-for-beginners.html` or `sony-a7-iv-review.html`.
  - Preserve the `hreflang` alternate links in `index.html` (and update when adding locales): they point to canonical site URLs and must use the site domain placeholder.
  - Affiliate links are inserted inline in content (placeholders currently in `de/index.html` comments). Do not auto-insert live affiliate IDs unless instructed — use a placeholder and ask for credentials.

- **Local preview / developer workflow**:
  - README suggests `npm install` and `npm run dev` but there is no `package.json` in the repo. DO NOT assume a build pipeline exists.
  - Recommended quick preview commands (safe to run locally):

    - `npx serve .` (simple static server)
    - or `python3 -m http.server 3000` from the repo root and open `http://localhost:3000`.

  - If adding automation, prefer a minimal `package.json` with a `dev` script that runs a static server; document it in `README.md`.

- **Editing patterns to follow (concrete examples)**:
  - To add a new buying guide: create `guides/<slug>.html`, include `<meta name="description">`, a clear `<h1>`, and keep the page structure consistent with `index.html`'s `card` examples.
  - To add a localized page: duplicate the English file into `de/` and translate text; update `de/index.html` navigation and ensure `hreflang` links in the root `index.html` remain accurate.
  - Keep class names and small inline script for dynamic year (`document.getElementById("year").textContent = new Date().getFullYear();`).

- **Stylistic & safety rules for AI edits**:
  - Preserve existing HTML structure and classes where possible — CSS targets those names.
  - Do not add third-party tracking or affiliate IDs without explicit instruction from the repo owner.
  - When changing URLs or slugs, update every internal link (search for `./guides/`, `./reviews/`, `./compare/`) and the `hreflang` links.

- **Integration points / external considerations**:
  - `index.html` contains `link rel="alternate" hreflang` entries pointing to `https://YOURDOMAIN.com/` — replace with the production domain only at deploy time.
  - There is no backend; all dynamic behavior should be minimal and client-side.

- **What to ask the maintainer when unclear**:
  - Do you want automated build tooling (`package.json`), and if so which dev server or bundler?
  - Where should live affiliate IDs and analytics be stored (environment/config file or injected at deploy)?

If anything above is unclear or you want me to include build scripts or a starter `package.json`, say so and I will update this file accordingly.
