#!/usr/bin/env python3
"""
Multi-Language Translation Engine for Camera Review Website

This script translates HTML pages from English to any supported language
using locale files. Designed for scalability to support DE, ES, IT, FR.

Usage:
    python translate.py --lang de           # Translate to German
    python translate.py --lang es           # Translate to Spanish (future)
    python translate.py --lang de --page guides/best-hybrid-camera.html
"""

import json
import re
import argparse
from pathlib import Path
from typing import Dict, List, Tuple
import shutil

# Base directories
SCRIPT_DIR = Path(__file__).parent
BASE_DIR = SCRIPT_DIR.parent.parent
LOCALES_DIR = SCRIPT_DIR / "locales"

# Language configuration
LANGUAGE_CONFIG = {
    "de": {
        "dir": "de",
        "guides_dir": "ratgeber",
        "reviews_dir": "bewertungen", 
        "compare_dir": "vergleiche",
        "currency": "€",
        "currency_position": "after"  # 100€ vs €100
    },
    "es": {
        "dir": "es",
        "guides_dir": "guias",
        "reviews_dir": "resenas",
        "compare_dir": "comparativas",
        "currency": "€",
        "currency_position": "before"
    },
    "it": {
        "dir": "it",
        "guides_dir": "guide",
        "reviews_dir": "recensioni",
        "compare_dir": "confronti",
        "currency": "€",
        "currency_position": "before"
    },
    "fr": {
        "dir": "fr",
        "guides_dir": "guides",
        "reviews_dir": "tests",
        "compare_dir": "comparatifs",
        "currency": "€",
        "currency_position": "before"
    }
}


def load_locale(lang: str) -> Dict:
    """Load locale file for given language."""
    locale_file = LOCALES_DIR / f"{lang}.json"
    if not locale_file.exists():
        raise FileNotFoundError(f"Locale file not found: {locale_file}")
    
    with open(locale_file, 'r', encoding='utf-8') as f:
        return json.load(f)


def flatten_locale(locale: Dict) -> Dict[str, str]:
    """Flatten nested locale dict into single-level dict."""
    flattened = {}
    for category, translations in locale.items():
        if category == "meta":
            continue
        if isinstance(translations, dict):
            flattened.update(translations)
    return flattened


def translate_content(content: str, translations: Dict[str, str]) -> str:
    """Apply translations to content."""
    result = content
    
    # Sort by length (longest first) to prevent partial replacements
    sorted_translations = sorted(
        translations.items(), 
        key=lambda x: len(x[0]), 
        reverse=True
    )
    
    for english, translated in sorted_translations:
        if english in result:
            result = result.replace(english, translated)
    
    return result


def update_html_lang(content: str, lang: str) -> str:
    """Update <html lang="..."> attribute."""
    return re.sub(
        r'<html lang="[^"]*"',
        f'<html lang="{lang}"',
        content
    )


def update_hreflang_tags(content: str, lang: str, page_path: str) -> str:
    """Update hreflang canonical tags."""
    config = LANGUAGE_CONFIG.get(lang, {})
    lang_dir = config.get('dir', lang)
    
    # Update canonical URL
    content = re.sub(
        r'<link rel="canonical" href="https://cameraupick.com/[^"]*"',
        f'<link rel="canonical" href="https://cameraupick.com/{lang_dir}/{page_path}"',
        content
    )
    
    return content


def translate_file(source_path: Path, target_path: Path, translations: Dict[str, str], lang: str) -> bool:
    """Translate a single file."""
    print(f"  Translating: {source_path.name} → {target_path.name}")
    
    with open(source_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Apply translations
    translated = translate_content(content, translations)
    
    # Update HTML lang attribute
    translated = update_html_lang(translated, lang)
    
    # Ensure target directory exists
    target_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Write translated file
    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(translated)
    
    return True


def get_page_mapping(lang: str) -> List[Tuple[str, str]]:
    """Get source → target file mapping for a language."""
    config = LANGUAGE_CONFIG[lang]
    
    mappings = []
    
    # Guide pages
    guide_files = [
        ("best-hybrid-camera.html", "beste-hybrid-kamera.html"),
        ("best-vlog-camera.html", "beste-vlog-kamera.html"),
        ("best-travel-camera.html", "beste-reisekamera.html"),
        ("best-camera-for-beginners-2026.html", "beste-kamera-fuer-anfaenger-2026.html"),
        ("best-budget-camera-under-800.html", "beste-budget-kamera-unter-800.html"),
        ("best-full-frame-for-video.html", "beste-vollformat-fuer-video.html"),
        ("best-action-360-camera.html", "beste-action-360-kamera.html"),
    ]
    
    for src, tgt in guide_files:
        mappings.append((
            f"guides/{src}",
            f"{config['dir']}/{config['guides_dir']}/{tgt}"
        ))
    
    # Review pages
    review_files = [
        "sony-a7-iv-review.html",
        "sony-a7c-ii-review.html",
        "sony-zv-e10-review.html",
        "fujifilm-x-t5-review.html",
        "canon-eos-r8-review.html",
        "nikon-z8-review.html",
        "panasonic-s5-ii-review.html",
        "dji-osmo-pocket-3-review.html",
    ]
    
    for src in review_files:
        tgt = src.replace("-review.html", "-testbericht.html")
        mappings.append((
            f"reviews/{src}",
            f"{config['dir']}/{config['reviews_dir']}/{tgt}"
        ))
    
    # Compare pages
    compare_files = [
        "sony-a7-iv-vs-canon-r6-ii.html",
        "sony-a7-v-vs-canon-r6-iii.html",
        "sony-zv-e10-vs-sony-a6700.html",
        "fujifilm-x-s20-vs-fujifilm-x-t5.html",
    ]
    
    for src in compare_files:
        mappings.append((
            f"compare/{src}",
            f"{config['dir']}/{config['compare_dir']}/{src}"
        ))
    
    # Info pages
    info_mapping = {
        "about.html": "uber-uns.html",
        "contact.html": "kontakt.html",
        "privacy.html": "datenschutz.html",
        "deals.html": "angebote.html",
        "404.html": "404.html",
        "index.html": "index.html",
    }
    
    for src, tgt in info_mapping.items():
        mappings.append((src, f"{config['dir']}/{tgt}"))
    
    return mappings


def main():
    parser = argparse.ArgumentParser(description="Multi-language translation engine")
    parser.add_argument("--lang", required=True, help="Target language (de, es, it, fr)")
    parser.add_argument("--page", help="Specific page to translate (optional)")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be done")
    
    args = parser.parse_args()
    
    if args.lang not in LANGUAGE_CONFIG:
        print(f"Error: Language '{args.lang}' not supported")
        print(f"Supported languages: {list(LANGUAGE_CONFIG.keys())}")
        return 1
    
    print(f"\n{'='*60}")
    print(f"Translation Engine - Target: {args.lang.upper()}")
    print(f"{'='*60}\n")
    
    # Load locale
    try:
        locale = load_locale(args.lang)
        translations = flatten_locale(locale)
        print(f"Loaded {len(translations)} translations from {args.lang}.json")
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return 1
    
    # Get page mappings
    mappings = get_page_mapping(args.lang)
    
    if args.page:
        mappings = [(s, t) for s, t in mappings if args.page in s or args.page in t]
    
    # Process files
    success_count = 0
    for source_rel, target_rel in mappings:
        source_path = BASE_DIR / source_rel
        target_path = BASE_DIR / target_rel
        
        if not source_path.exists():
            print(f"  ⚠ Source not found: {source_rel}")
            continue
        
        if args.dry_run:
            print(f"  Would translate: {source_rel} → {target_rel}")
        else:
            if translate_file(source_path, target_path, translations, args.lang):
                success_count += 1
    
    print(f"\n{'='*60}")
    print(f"Translation Complete")
    print(f"Processed: {success_count} files")
    print(f"{'='*60}\n")
    
    return 0


if __name__ == "__main__":
    exit(main())
