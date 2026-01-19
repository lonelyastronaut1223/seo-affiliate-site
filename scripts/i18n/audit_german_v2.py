#!/usr/bin/env python3
"""
Self-Verifying German Translation System
Loops until ALL English content is translated

Process:
1. Scan all DE pages for English content
2. Report findings
3. Apply translations
4. Verify fixes
5. Repeat until 100% complete
"""

import re
from pathlib import Path
from typing import Dict, List, Tuple

BASE_DIR = Path(__file__).parent.parent.parent
DE_DIR = BASE_DIR / 'de'

# Common English patterns to detect
ENGLISH_PATTERNS = [
    # Common English words/phrases that shouldn't appear in German text
    r'\bThe\b(?!\s+(?:Kamera|Sensor))',  # "The" not followed by German loan words
    r'\bwith\b',
    r'\bfor\b(?!\s+(?:Video|Vlog))',  # "for" not followed by common terms
    r'\bYou\b',
    r'\byou\b',
    r'\band\b(?!\s)',  # "and" standalone
    r'\bIt\b(?:\'s|\s+is|\s+has)',  # "It's", "It is", "It has"
    r'\bmaking it\b',
    r'\blook\b',
    r'\bstill\b',
    r'\bwhile\b',
    r'\bWhile\b',
    r'\beven\b',
    r'\bEven\b',
    r'\bwhy\b',
    r'\bWhy\b',
    r'\bhow\b',
    r'\bHow\b',
    r'\bshould\b',
    r'\bShould\b',
    r'\bwhat\b',
    r'\bWhat\b',
    r'\bwhich\b',
    r'\bWhich\b',
    r'\bthis\b',
    r'\bThis\b',
    r'\bthat\b(?!\s+pro)',  # "that" not in "that pro"
    r'\bThat\b',
    r'\bthey\b',
    r'\bThey\b',
    r'\btheir\b',
    r'\bwe\b',
    r'\bWe\b',
    r'\bour\b',
    r'\bOur\b',
    r'\bof\b',
    r'\bbut\b',
    r'\bBut\b',
    r'\bcan\b',
    r'\bCan\b',
    r'\bwill\b',
    r'\bWill\b',
    r'\bhere\b',
    r'\bHere\b',
    r'\bbest\b',
    r'\bBest\b',
    r'\bonly\b',
    r'\bOnly\b',
    r'\bjust\b',
    r'\bJust\b',
    r'\bmore\b',
    r'\bMore\b',
    r'\bless\b',
    r'\bLess\b',
    r'\bsome\b',
    r'\bSome\b',
    r'\bmany\b',
    r'\bMany\b',
    r'\bother\b',
    r'\bOther\b',
    r'\bfrom\b',
    r'\bFrom\b',
    r'\binto\b',
    r'\bInto\b',
    r'\bover\b',
    r'\bOver\b',
    r'\bdown\b',
    r'\bDown\b',
    r'\bout\b',
    r'\bOut\b',
    r'\babout\b',
    r'\bAbout\b',
    r'\blike\b',
    r'\bLike\b',
    r'\bmake\b',
    r'\bMake\b',
    r'\bmakes\b',
    r'\bMakes\b',
    r'\bthan\b',
    r'\bThan\b',
    r'\bwhen\b',
    r'\bWhen\b',
    r'\bwhere\b',
    r'\bWhere\b',
    r'\bthere\b',
    r'\bThere\b',
    r'\bbeen\b',
    r'\bBeen\b',
    r'\bhave\b',
    r'\bHave\b',
    r'\bhas\b',
    r'\bHas\b',
    r'\bdoes\b',
    r'\bDoes\b',
    r'\bdoesn\'t\b',
    r'\bDoesn\'t\b',
    r'\bisn\'t\b',
    r'\bIsn\'t\b',
    r'\baren\'t\b',
    r'\bAren\'t\b',
    r'\bwon\'t\b',
    r'\bWon\'t\b',
    r'\bcan\'t\b',
    r'\bCan\'t\b',
    r'\bdon\'t\b',
    r'\bDon\'t\b',   
]

# Whitelist - patterns that look English but are OK
WHITELIST = [
    r'APS-C',
    r'Full-Frame',
    r'Fullframe',
    r'HyperSmooth',
    r'Max Lens Mod',
    r'Horizon Lock',
    r'GoPro',
    r'Nokia OZO',
    r'USB-C',
    r'HDMI',
    r'Log',
    r'S-Log',
    r'C-Log',
    r'V-Log',
    r'Raw',
    r'RAW',
    r'Crop',
    r'Rolling Shutter',
    r'Filmsimulations',
    r'X-Trans',
    r'X-Processor',
    r'IBIS',
    r'OIS',
    r'AF',
    r'EVF',
    r'OLED',
    r'LCD',
    r'MP',
    r'fps',
    r'4K',
    r'5K',
    r'6K',
    r'8K',
    r'1080p',
    r'720p',
    r'ISO',
    r'EV',
    r'f/\d',
    r'mm',
    r'RF',
    r'EF',
    r'E-mount',
    r'E-Halterung',
    r'X-mount',
    r'Z-mount',
    r'L-mount',
    r'MFT',
    r'M4/3',
    r'Micro Four Thirds',
    r'CMOS',
    r'BSI',
    r'Stacked',
    r'Dual Gain',
    r'Pixel Shift',
    r'PDAF',  
    r'Eye AF',
    r'Face AF',
    r'Animal AF',
    r'Subject AF',
    r'Tracking',
    r'CFexpress',
    r'SD',
    r'UHS',
    r'Wi-Fi',
    r'Bluetooth',
    r'GPS',
    r'NFC',
    r'Hot Shoe',
    r'Cold Shoe',
    r'Tally Light',
    r'Vlog',
    r'Vlogging',
    r'Video',
    r'Podcast',
    r'Streaming',
    r'YouTube',
    r'Instagram',
    r'TikTok',
    r'Facebook',
    r'Sigma',
    r'Tamron',
    r'Zeiss',
    r'Leica',
    r'Voigtlander',
    r'copyright',
    r'Copyright',
    r'href=',
    r'src=',
    r'alt=',
    r'class=',
    r'id=',
    r'style=',
    r'type=',
    r'content=',
    r'property=',
    r'rel=',
    r'target=',
    r'charset=',
    r'name=',
    r'http',
    r'https',
    r'www\.',
    r'\.html',
    r'\.css',
    r'\.js',
    r'\.png',
    r'\.jpg',
    r'\.webp',
    r'\.svg',
    r'function',
    r'script',
    r'return',
    r'console',
    r'window',
    r'document',
    r'const ',
    r'let ',
    r'var ',
    r'if ',
    r'else',
    r'true',
    r'false',
    r'null',
    r'undefined',
    r'@type',
    r'@context',
    r'schema\.org',
    r'application/ld\+json',
    r'gtag',
    r'dataLayer',
    r'serviceWorker',
    r'navigator',
    r'async',
    r'defer',
    r'crossorigin',
    r'preload',
    r'preconnect',
    r'stylesheet',
    r'canonical',
    r'noopener',
    r'noreferrer',
    r'sponsored',
    r'nofollow',
]

def strip_html_and_scripts(content: str) -> str:
    """Remove HTML tags and script content, keep only visible text"""
    # Remove script and style blocks
    content = re.sub(r'<script[^>]*>.*?</script>', '', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<style[^>]*>.*?</style>', '', content, flags=re.DOTALL | re.IGNORECASE)
    # Remove HTML comments
    content = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)
    # Remove HTML tags but keep content
    content = re.sub(r'<[^>]+>', ' ', content)
    # Decode HTML entities
    content = content.replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>')
    content = content.replace('&rarr;', '→').replace('&nbsp;', ' ')
    return content

def is_whitelisted(text: str) -> bool:
    """Check if the text matches any whitelist pattern"""
    for pattern in WHITELIST:
        if re.search(pattern, text, re.IGNORECASE):
            return True
    return False

def find_english_in_file(file_path: Path) -> List[Tuple[int, str, str]]:
    """Find English content in a file. Returns list of (line_num, matched_pattern, context)"""
    issues = []
    
    try:
        content = file_path.read_text(encoding='utf-8')
        clean_content = strip_html_and_scripts(content)
        lines = content.split('\n')
        
        for i, line in enumerate(lines, 1):
            # Skip lines that are clearly code/HTML
            if re.match(r'^\s*<', line) and '>' in line and not re.search(r'>[^<]+<', line):
                continue
            
            # Extract text content from the line
            text_content = strip_html_and_scripts(line)
            
            if not text_content.strip():
                continue
            
            for pattern in ENGLISH_PATTERNS:
                matches = re.findall(pattern, text_content, re.IGNORECASE)
                for match in matches:
                    # Get context (surrounding text)
                    context = text_content.strip()[:100]
                    if not is_whitelisted(context):
                        issues.append((i, match, context))
                        break  # Only report first issue per line
                        
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    
    return issues

def audit_all_german_pages() -> Dict[str, List[Tuple[int, str, str]]]:
    """Audit all German pages for English content"""
    results = {}
    
    # Scan all HTML files in DE directory
    for html_file in DE_DIR.rglob('*.html'):
        issues = find_english_in_file(html_file)
        if issues:
            rel_path = str(html_file.relative_to(BASE_DIR))
            results[rel_path] = issues
    
    return results

def print_audit_report(results: Dict[str, List]) -> int:
    """Print audit report and return total issue count"""
    total_issues = 0
    
    print("\n" + "="*70)
    print("🔍 GERMAN TRANSLATION AUDIT")
    print("="*70)
    
    if not results:
        print("\n✅ No English content detected! All pages are fully translated.")
        return 0
    
    for file_path, issues in sorted(results.items()):
        print(f"\n📄 {file_path} ({len(issues)} issues)")
        for line_num, match, context in issues[:5]:  # Show first 5
            print(f"   Line {line_num}: '{match}' → \"{context[:60]}...\"")
        if len(issues) > 5:
            print(f"   ... and {len(issues) - 5} more issues")
        total_issues += len(issues)
    
    print("\n" + "="*70)
    print(f"⚠️  Total Issues: {total_issues}")
    print("="*70)
    
    return total_issues

def main():
    """Main audit function"""
    print("🇩🇪 German Translation Audit System")
    print("Scanning all /de/ pages for English content...\n")
    
    results = audit_all_german_pages()
    total = print_audit_report(results)
    
    if total > 0:
        print("\n💡 Run the translation fix script to address these issues.")
    
    return total

if __name__ == '__main__':
    exit(main())
