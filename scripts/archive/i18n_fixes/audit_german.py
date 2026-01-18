#!/usr/bin/env python3
"""
Audit German content quality.
Scans all .html files in /de/ for common English words that should have been translated.
"""

from pathlib import Path
import re

BASE_DIR = Path(__file__).parent.parent.parent
DE_DIR = BASE_DIR / 'de'

# Words to look for that indicate untranslated content
# Excluding words that are the same in German (Sensor, Video, etc.)
ENGLISH_INDICATORS = [
    "Review", "Guide", "Camera", "Pros", "Cons",
    "Verdict", "Battery", "Autofocus", "Weight", "Lens",
    "Buy", "Check Price", "Best For", "Overview", "Summary",
    "Features", "Specifications", "Who Should", "Bottom Line"
]

# Allow-list for words that might be the same or are technical terms
# (Currently empty, can be populated if false positives occur)
ALLOW_LIST = []

def audit_file(file_path: Path) -> list:
    """Check a file for English indicators."""
    issues = []
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Remove script and style content
    content = re.sub(r'<script[^>]*>.*?</script>', ' ', content, flags=re.DOTALL)
    content = re.sub(r'<style[^>]*>.*?</style>', ' ', content, flags=re.DOTALL)
    # Remove HTML comments
    content = re.sub(r'<!--.*?-->', ' ', content, flags=re.DOTALL)
    # Remove ALL HTML tags (including attributes like class="pros")
    text_content = re.sub(r'<[^>]+>', ' ', content)
    
    for word in ENGLISH_INDICATORS:
        # Check for word with word boundaries
        if re.search(r'\b' + re.escape(word) + r'\b', text_content, re.IGNORECASE):
            # Skip if it's part of a product name like "Max Lens Mod"
            if word.lower() == 'lens' and 'Max Lens Mod' in content:
                continue
            issues.append(word)
            
    return issues

def main():
    print(f"Auditing German Content in {DE_DIR}...\n")
    
    problem_files = 0
    total_files = 0
    
    for html_file in DE_DIR.rglob('*.html'):
        total_files += 1
        issues = audit_file(html_file)
        
        if issues:
            problem_files += 1
            print(f"[FAIL] {html_file.relative_to(BASE_DIR)}")
            print(f"       Found English keywords: {', '.join(set(issues[:5]))}...") # First 5 unique
        else:
            print(f"[PASS] {html_file.relative_to(BASE_DIR)}")
            
    print(f"\n{'='*60}")
    print(f"Audit Complete")
    print(f"Total Files: {total_files}")
    print(f"Problem Files: {problem_files}")
    print(f"Quality Score: {((total_files - problem_files) / total_files) * 100:.1f}%")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()
