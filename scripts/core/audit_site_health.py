#!/usr/bin/env python3
"""
Site Health Audit Script
Comprehensive check for critical issues before deployment.
Run this BEFORE any git push.
"""

import os
import sys
import re
import json
from pathlib import Path
from datetime import datetime

class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'
    BOLD = '\033[1m'

def print_header(text):
    print(f"\n{Colors.BOLD}{Colors.BLUE}{'='*60}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.BLUE}{text}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.BLUE}{'='*60}{Colors.END}")

def print_error(text):
    print(f"{Colors.RED}✗ CRITICAL: {text}{Colors.END}")

def print_warning(text):
    print(f"{Colors.YELLOW}⚠ WARNING: {text}{Colors.END}")

def print_success(text):
    print(f"{Colors.GREEN}✓ {text}{Colors.END}")

def get_all_html_files(root_dir):
    """Get all HTML files in project"""
    html_files = []
    exclude_dirs = {'node_modules', '.git', 'includes'}
    
    for path in Path(root_dir).rglob('*.html'):
        if not any(excl in str(path) for excl in exclude_dirs):
            html_files.append(path)
    
    return html_files

def check_affiliate_links(root_dir):
    """Check if affiliate links system is working"""
    issues = []
    
    # Check if links.min.js exists
    links_file = Path(root_dir) / 'assets' / 'js' / 'links.min.js'
    if not links_file.exists():
        issues.append(('CRITICAL', 'links.min.js', 'Affiliate links file is MISSING!'))
        return issues
    
    # Read and parse links file
    content = links_file.read_text()
    
    # Count defined links
    link_matches = re.findall(r'"([^"]+)":\s*"(https?://[^"]+)"', content)
    empty_links = re.findall(r'"([^"]+)":\s*""', content)
    
    if len(link_matches) == 0:
        issues.append(('CRITICAL', 'links.min.js', 'No affiliate links defined!'))
    else:
        print_success(f"Found {len(link_matches)} active affiliate links")
    
    if len(empty_links) > 0:
        for link_id in empty_links:
            issues.append(('WARNING', 'links.min.js', f'Empty link for: {link_id}'))
    
    # Check if links.min.js is included in HTML files
    html_files = get_all_html_files(root_dir)
    pages_without_links = []
    
    for html_file in html_files:
        content = html_file.read_text()
        if 'links.min.js' not in content:
            # Only flag pages that have btn-buy buttons
            if 'btn-buy' in content or 'Check Price' in content or 'Preis prüfen' in content:
                pages_without_links.append(str(html_file.relative_to(root_dir)))
    
    if pages_without_links:
        for page in pages_without_links:
            issues.append(('CRITICAL', page, 'Has affiliate buttons but missing links.min.js'))
    
    return issues

def check_404_links(root_dir):
    """Check for links to non-existent pages"""
    issues = []
    html_files = get_all_html_files(root_dir)
    
    # Build list of existing files
    existing_files = set()
    for f in html_files:
        rel_path = str(f.relative_to(root_dir))
        existing_files.add(rel_path)
        existing_files.add('/' + rel_path)
    
    # Also add common files
    for ext in ['xml', 'json', 'txt']:
        for f in Path(root_dir).glob(f'*.{ext}'):
            existing_files.add(f.name)
    
    # Check links in HTML files
    href_pattern = re.compile(r'href=["\']([^"\'#]+)["\']')
    
    for html_file in html_files:
        content = html_file.read_text()
        matches = href_pattern.findall(content)
        
        for href in matches:
            # Skip external links and special protocols
            if href.startswith(('http', 'mailto:', 'tel:', 'javascript:', '//')):
                continue
            
            # Resolve relative path
            if href.startswith('/'):
                target = href[1:]
            else:
                target = str((html_file.parent / href).relative_to(root_dir))
            
            # Normalize path
            target = target.replace('../', '').replace('./', '')
            
            # Check if target exists
            target_path = Path(root_dir) / target
            if not target_path.exists() and target not in ['#', '']:
                # Only report each missing file once per source file
                issues.append(('WARNING', str(html_file.relative_to(root_dir)), f'Link to missing page: {href}'))
    
    return issues

def check_essential_pages(root_dir):
    """Check if essential pages exist"""
    issues = []
    
    essential_pages = {
        'EN': ['index.html', 'about.html', 'contact.html', 'privacy.html', 'terms.html', '404.html'],
        'DE': ['de/index.html', 'de/ueber-uns.html', 'de/kontakt.html', 'de/datenschutz.html', 'de/impressum.html']
    }
    
    for lang, pages in essential_pages.items():
        for page in pages:
            if not (Path(root_dir) / page).exists():
                issues.append(('CRITICAL', page, f'Essential {lang} page is MISSING!'))
    
    return issues

def check_js_errors(root_dir):
    """Basic syntax check on critical JS files"""
    issues = []
    
    critical_js = ['assets/js/links.min.js', 'assets/js/script.min.js', 'assets/js/script-de.min.js']
    
    for js_file in critical_js:
        js_path = Path(root_dir) / js_file
        if js_path.exists():
            content = js_path.read_text()
            # Basic syntax checks
            if content.count('{') != content.count('}'):
                issues.append(('CRITICAL', js_file, 'Mismatched braces {}'))
            if content.count('(') != content.count(')'):
                issues.append(('CRITICAL', js_file, 'Mismatched parentheses ()'))
    
    return issues

def main():
    root_dir = Path(__file__).parent.parent.parent
    
    print_header("SITE HEALTH AUDIT")
    print(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"📁 {root_dir}")
    
    all_issues = []
    
    # Run checks
    print_header("1. Checking Affiliate Links")
    issues = check_affiliate_links(root_dir)
    all_issues.extend(issues)
    
    print_header("2. Checking Essential Pages")
    issues = check_essential_pages(root_dir)
    all_issues.extend(issues)
    for i in issues:
        if i[0] == 'CRITICAL':
            print_error(f"{i[1]}: {i[2]}")
    if not issues:
        print_success("All essential pages exist")
    
    print_header("3. Checking JavaScript Files")
    issues = check_js_errors(root_dir)
    all_issues.extend(issues)
    for i in issues:
        print_error(f"{i[1]}: {i[2]}")
    if not issues:
        print_success("JavaScript files appear valid")
    
    print_header("4. Checking Internal Links (404s)")
    issues = check_404_links(root_dir)
    # Deduplicate and limit output
    unique_issues = list(set(issues))[:20]
    all_issues.extend(unique_issues)
    for i in unique_issues[:10]:
        print_warning(f"{i[1]}: {i[2]}")
    if len(unique_issues) > 10:
        print(f"  ... and {len(unique_issues) - 10} more")
    if not issues:
        print_success("No broken internal links found")
    
    # Summary
    print_header("SUMMARY")
    
    critical = len([i for i in all_issues if i[0] == 'CRITICAL'])
    warnings = len([i for i in all_issues if i[0] == 'WARNING'])
    
    if critical > 0:
        print(f"{Colors.RED}{Colors.BOLD}🚨 {critical} CRITICAL issues - DO NOT DEPLOY!{Colors.END}")
    
    if warnings > 0:
        print(f"{Colors.YELLOW}⚠️  {warnings} warnings{Colors.END}")
    
    if critical == 0 and warnings == 0:
        print(f"{Colors.GREEN}{Colors.BOLD}✅ All checks passed - Safe to deploy{Colors.END}")
    
    # Return exit code based on critical issues
    return 1 if critical > 0 else 0

if __name__ == '__main__':
    sys.exit(main())
