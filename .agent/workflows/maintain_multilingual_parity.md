---
description: Workflow to ensure English and German (and future) pages are perfectly synchronized in structure and content.
---

# Multi-Language Parity Workflow

**Golden Rule**: The English (EN) version is the **Source of Truth**. Always modify the English page first, then propagate changes to other languages.

## 1. Content Updates (Text Changes)

If you are updating text, prices, or recommendations:

1.  **Edit English Page**: Make changes to `*.html` (e.g., `reviews/sony-a7-iv-review.html`).
2.  **Identify Target Page**: Find the corresponding German page (e.g., `de/bewertungen/sony-a7-iv-testbericht.html`).
3.  **Translate & Update**:
    *   **Manual**: For small edits, manually translate and update the specific section in the DE page.
    *   **Automated**: For large rewrites, use `scripts/i18n/translate.py`.
        ```bash
        python3 scripts/i18n/translate.py --lang de --page [filename_keyword]
        ```

## 2. Structural Updates (New Sections/Layouts)

If you are changing the HTML structure (adding a new section, changing div classes, adding schema):

1.  **Implement in English**: Perfect the structure in the EN file.
2.  **Copy to German**:
    *   Copy the *new HTML block* from the English file.
    *   Paste it into the corresponding location in the German file.
    *   **Translate Content**: Replace English text within the new block with German text, keeping HTML tags intact.

## 3. Global Assets (CSS/JS)

*   **Styles**: Edit `assets/css/index.css` (or `style.min.css`). Changes apply globally to all languages immediately.
*   **Scripts**:
    *   **Shared Logic**: Edit `assets/js/animations.js` or `links.js`. Applies to all.
    *   **Locale-specific**: If logic depends on language (like the Quiz), update BOTH `assets/js/script.js` (EN) and `assets/js/script-de.js` (DE).

## 4. Verification Checklist

Before marking a task as complete:

- [ ] **Dual Check**: Open both EN and DE versions of the page.
- [ ] **Visual Parity**: Ensure layout, spacing, and images are identical.
- [ ] **Functional Parity**: key features (quiz, buttons, sliders) work on both.
- [ ] **Link Parity**: Check that internal links on DE pages point to DE destinations (e.g., `../bewertungen/` not `../reviews/`).

## 5. Automated Checks (Optional)

Run the parity checker script (if available) to identify missing pages or schema mismatches.
