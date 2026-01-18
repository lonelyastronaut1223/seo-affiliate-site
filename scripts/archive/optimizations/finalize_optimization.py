#!/usr/bin/env python3
"""
Finalize optimizations:
1. Minify JS files
2. Fix security (noopener)
"""

import re
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

def minify_js(content: str) -> str:
    """Simple JS minification"""
    # Remove single line comments
    content = re.sub(r'//.*', '', content)
    # Remove multi-line comments
    content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
    # Remove whitespace
    lines = [line.strip() for line in content.splitlines() if line.strip()]
    return '\n'.join(lines)

def optimize_js():
    """Create minified versions of JS files"""
    js_files = [
        'assets/js/links.js',
        'assets/js/script-de.js',
        'assets/js/animations.js'
    ]
    
    print("⚡ Minifying JS files...")
    for js_file in js_files:
        path = BASE_DIR / js_file
        if not path.exists():
            continue
            
        min_path = path.with_suffix('.min.js')
        
        content = path.read_text(encoding='utf-8')
        minified = minify_js(content)
        min_path.write_text(minified, encoding='utf-8')
        
        original_size = len(content)
        new_size = len(minified)
        reduction = ((original_size - new_size) / original_size) * 100
        
        print(f"✅ Minified {js_file}: {original_size} → {new_size} bytes (-{reduction:.1f}%)")
        
        # Update references in HTML files (simplified, assuming standard script tags)
        # This is risky doing globally without verification, but we can try to target specific files
        # Actually, let's just create the .min.js files first. Updating references needs to be careful.

def fix_security():
    """Add rel="noopener" to external links"""
    print("\n🔒 Fixing security issues...")
    
    files = [
        'deals.html',
        'de/angebote.html'
    ]
    
    for rel_path in files:
        path = BASE_DIR / rel_path
        if not path.exists():
            continue
            
        content = path.read_text(encoding='utf-8')
        
        # Regex to find external links with target="_blank" but missing noopener
        # This is a bit complex with regex, better to use specific replacements if known
        
        # Look for Amazon/affiliate links mostly
        # Pattern: <a href="..." target="_blank"> -> <a href="..." target="_blank" rel="noopener">
        
        # Safest way: replace 'target="_blank"' with 'target="_blank" rel="noopener"' 
        # but avoid double rel="noopener"
        
        # Let's verify specifically what was flagged in audit
        # The audit found them, so they definitely exist.
        
        # Simple approach: Identify the lines from the audit or just iterate
        
        new_content = content
        
        # Find all <a> tags with target="_blank"
        matches = re.finditer(r'<a[^>]+target="_blank"[^>]*>', content)
        
        count = 0 
        offset = 0
        
        for m in matches:
            tag = m.group(0)
            if 'rel="noopener"' not in tag and "rel='noopener'" not in tag:
                # Add it
                new_tag = tag.replace('target="_blank"', 'target="_blank" rel="noopener"')
                new_content = new_content.replace(tag, new_tag)
                count += 1
        
        if count > 0:
            path.write_text(new_content, encoding='utf-8')
            print(f"✅ {rel_path}: Fixed {count} links")
        else:
            print(f"ok {rel_path}: No insecure links found")

def update_html_references():
    """Update HTML to use minified JS"""
    print("\n📝 Updating HTML references to minified JS...")
    
    # We need to scan all HTML files and replace .js with .min.js for the files we just minified
    # Be careful not to replace already minified ones
    
    replacements = {
        'assets/js/links.js': 'assets/js/links.min.js',
        'assets/js/script-de.js': 'assets/js/script-de.min.js',
        'assets/js/animations.js': 'assets/js/animations.min.js'
    }
    
    count = 0
    for html_file in BASE_DIR.rglob('*.html'):
        if '.git' in str(html_file): continue
        
        content = html_file.read_text(encoding='utf-8')
        new_content = content
        
        changed = False
        for original, minified in replacements.items():
            # Check for script src="..."
            # e.g. src="../assets/js/links.js" -> src="../assets/js/links.min.js"
            
            # Simple string replacement for specific paths
            # Need to handle variations like src="assets/..." and src="../assets/..."
            
            # Search for the filename only to be safe?
            basename_orig = original.split('/')[-1]
            basename_min = minified.split('/')[-1]
            
            if basename_orig in content and basename_min not in content:
                # Replace only if it ends with "
                new_content = new_content.replace(f'{basename_orig}"', f'{basename_min}"')
                if new_content != content:
                    changed = True
                    content = new_content # Update content for next iteration
        
        if changed:
            html_file.write_text(new_content, encoding='utf-8')
            print(f"✅ Updated references in {html_file.relative_to(BASE_DIR)}")
            count += 1
            
    print(f"Total files updated: {count}")

def main():
    optimize_js()
    update_html_references()
    fix_security()

if __name__ == '__main__':
    main()
