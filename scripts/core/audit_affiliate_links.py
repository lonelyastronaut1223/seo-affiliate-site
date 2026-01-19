#!/usr/bin/env python3
"""
Affiliate Links Audit Script
Specifically checks affiliate links functionality and reports issues.
"""

import os
import re
from pathlib import Path
from datetime import datetime

class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'
    BOLD = '\033[1m'

def main():
    root_dir = Path(__file__).parent.parent.parent
    
    print(f"\n{Colors.BOLD}{Colors.BLUE}{'='*60}")
    print("AFFILIATE LINKS AUDIT")
    print(f"{'='*60}{Colors.END}")
    print(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # 1. Check links.min.js
    links_file = root_dir / 'assets' / 'js' / 'links.min.js'
    
    if not links_file.exists():
        print(f"{Colors.RED}✗ CRITICAL: links.min.js is MISSING!{Colors.END}")
        return 1
    
    content = links_file.read_text()
    
    # Parse affiliate links
    active_links = re.findall(r'"([^"]+)":\s*"(https?://[^"]+)"', content)
    empty_links = re.findall(r'"([^"]+)":\s*""', content)
    
    print(f"\n{Colors.BOLD}Links Status:{Colors.END}")
    print(f"  ✓ Active links: {len(active_links)}")
    print(f"  ⚠ Empty links: {len(empty_links)}")
    
    if empty_links:
        print(f"\n{Colors.YELLOW}Empty link IDs (need real URLs):{Colors.END}")
        for link_id in empty_links:
            print(f"  - {link_id}")
    
    # 2. Check HTML pages for btn-buy buttons
    print(f"\n{Colors.BOLD}Scanning HTML pages...{Colors.END}")
    
    html_files = list(root_dir.rglob('*.html'))
    html_files = [f for f in html_files if '.git' not in str(f) and 'node_modules' not in str(f)]
    
    pages_with_buttons = []
    pages_missing_script = []
    buttons_without_data = []
    
    for html_file in html_files:
        html_content = html_file.read_text()
        
        has_buttons = 'btn-buy' in html_content
        has_script = 'links.min.js' in html_content
        
        if has_buttons:
            pages_with_buttons.append(html_file)
            
            if not has_script:
                pages_missing_script.append(html_file)
            
            # Check if buttons have data-product or are inside sections with IDs
            btn_matches = re.findall(r'<a[^>]*class="btn-buy"[^>]*>', html_content)
            for btn in btn_matches:
                if 'data-product=' not in btn:
                    # Check if button is likely orphaned (no product ID reference)
                    buttons_without_data.append((html_file, btn[:80]))
    
    print(f"  Pages with affiliate buttons: {len(pages_with_buttons)}")
    
    if pages_missing_script:
        print(f"\n{Colors.RED}CRITICAL: Pages with buttons but missing links.min.js:{Colors.END}")
        for p in pages_missing_script:
            print(f"  - {p.relative_to(root_dir)}")
    
    # 3. Check for buttons that might not get links applied
    if buttons_without_data:
        print(f"\n{Colors.YELLOW}Buttons without data-product attribute: {len(buttons_without_data)}{Colors.END}")
        print(f"  (These rely on section IDs or anchor hrefs to match)")
    
    # 4. Active link details
    print(f"\n{Colors.BOLD}Active Affiliate Links:{Colors.END}")
    for link_id, url in active_links[:10]:
        short_url = url[:50] + '...' if len(url) > 50 else url
        print(f"  {Colors.GREEN}✓{Colors.END} {link_id}: {short_url}")
    
    if len(active_links) > 10:
        print(f"  ... and {len(active_links) - 10} more")
    
    # Summary
    print(f"\n{Colors.BOLD}{'='*60}")
    print("SUMMARY")
    print(f"{'='*60}{Colors.END}")
    
    if pages_missing_script:
        print(f"{Colors.RED}🚨 {len(pages_missing_script)} pages need links.min.js added!{Colors.END}")
        return 1
    elif empty_links:
        print(f"{Colors.YELLOW}⚠️  {len(empty_links)} products need real affiliate URLs{Colors.END}")
        return 0
    else:
        print(f"{Colors.GREEN}✅ Affiliate links system appears healthy{Colors.END}")
        return 0

if __name__ == '__main__':
    exit(main())
