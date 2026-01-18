---
description: End-to-end process for creating and publishing a new camera guide
---

# New Content Publishing Workflow

Follow this process when creating a new review or guide page.

## Phase 1: Creation (English)

1. **Create HTML File**: 
   - Duplicate an existing template (e.g., `guides/template.html` if exists, or a similar guide).
   - Naming convention: `guides/best-[topic]-camera.html` or `reviews/[camera-model]-review.html`.

2. **Draft Content**:
   - Write content in English.
   - ensure clean HTML structure (H1, H2, p, ul/li).
   - **Critical**: usage of `class="pros"` and `class="cons"` for lists.

3. **Add Images**:
   - Place images in `assets/images/guides/` or `assets/images/reviews/`.
   - Run optimization:
     ```bash
     python3 scripts/optimization/optimize_images.py
     ```

## Phase 2: Auditing (English)

4. **Verify SEO & Code**:
   - Run the audit tool on your specific file (or verify via global audit):
     ```bash
     python3 scripts/core/audit_seo.py
     ```
   - Check for: Title length, Meta description, Layout shifts (specify dimensions for images).

## Phase 3: Localization (German)

5. **Create German Version**:
   - Copy English file to `de/ratgeber/` or `de/bewertungen/`.
   - Rename file to German URL slug (e.g., `best-travel-camera.html` -> `beste-reisekamera.html`).

6. **Translate Content**:
   - Use the helper script to translate (or use AI assistant):
     ```bash
     python3 scripts/i18n/translate.py --source [english_file_path] --target [german_file_path]
     ```
   - *Note: Manual review is strictly required after machine translation.*

7. **Fix Cross-Links**:
   - Ensure the German page links to other `/de/` pages.
   - Update the "Language Switcher" link in the header:
     - English page -> links to German version.
     - German page -> links to English version.

## Phase 4: Finalization

8. **Update System Files**:
   - Regenerate Sitemap:
     ```bash
     python3 scripts/core/generate_sitemap.py
     ```

9. **Final Audit**:
   - Run the full project audit to ensure no broken links were introduced:
     ```bash
     python3 scripts/core/audit_code.py
     ```

10. **Deploy**:
    - Commit and push changes.
