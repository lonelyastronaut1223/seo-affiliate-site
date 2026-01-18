# Internationalization (i18n) System

Multi-language translation infrastructure for the camera review website.

## Supported Languages

| Code | Language | Status |
|------|----------|--------|
| de | Deutsch (German) | ✅ Complete |
| es | Español (Spanish) | 📝 Placeholder |
| it | Italiano (Italian) | 📝 Placeholder |
| fr | Français (French) | 📝 Placeholder |

## Directory Structure

```
scripts/i18n/
├── translate.py          # Main translation engine
├── complete_german.py    # Full German content translator
├── deep_translate.py     # Dictionary-based translator
└── locales/
    ├── de.json           # German translations (complete)
    ├── es.json           # Spanish translations (placeholder)
    ├── it.json           # Italian translations (placeholder)
    └── fr.json           # French translations (placeholder)
```

## Usage

### Translate Pages
```bash
# Translate all pages to German
python scripts/i18n/complete_german.py

# Use the translation engine (with locale file)
python scripts/i18n/translate.py --lang de
```

### Adding a New Language

1. **Create locale file**: Copy `de.json` as template, translate all values
   ```bash
   cp scripts/i18n/locales/de.json scripts/i18n/locales/[lang].json
   ```

2. **Create language directory**: 
   ```bash
   mkdir -p [lang]/ratgeber [lang]/bewertungen [lang]/vergleiche
   ```

3. **Update translation engine**: Add language config to `translate.py`

4. **Run translation**:
   ```bash
   python scripts/i18n/translate.py --lang [lang]
   ```

## Locale File Structure

```json
{
  "meta": {
    "language": "de",
    "name": "Deutsch",
    "locale": "de_DE"
  },
  "navigation": { ... },
  "buttons": { ... },
  "headings": { ... },
  "table_headers": { ... },
  "badges": { ... },
  "camera_terms": { ... },
  "video_terms": { ... }
}
```

## Notes

- Manual translation provides best quality for product descriptions
- Locale files handle UI elements, buttons, labels
- For full content translation, extend `complete_german.py` with page-specific content
