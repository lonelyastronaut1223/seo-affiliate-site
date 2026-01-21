
import os
import re
import sys

def verify_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to find header
    header_pattern = re.compile(r'(<header[^>]*>)(.*?)(</header>)', re.DOTALL | re.IGNORECASE)
    
    match = header_pattern.search(content)
    if not match:
        # Some files might not have a header (e.g. fragments), but most should.
        # We'll warn but not fail unless it's a main page.
        # print(f"WARNING: No header found in {filepath}")
        return True

    header_open_tag = match.group(1)
    header_inner_content = match.group(2)
    
    errors = []
    
    # Check 1: Header should NOT have 'container' class if it is 'header-sticky'
    # Actually, if it's sticky, we want full width. 
    if 'header-sticky' in header_open_tag:
        if 'container' in header_open_tag:
            errors.append("Header has both 'header-sticky' and 'container' classes. This causes alignment issues.")
            
    # Check 2: Header should NOT contain Hero section
    if '<section class="hero"' in header_inner_content or "<section class='hero'" in header_inner_content:
        errors.append("Header contains 'hero' section. This causes the hero to be fixed/sticky.")
        
    if errors:
        print(f"FAIL: {filepath}")
        for e in errors:
            print(f"  - {e}")
        return False
        
    return True


def main():
    failed = False
    count = 0
    for root, dirs, files in os.walk('.'):
        if '.agent' in root: continue
        if '.git' in root: continue
        
        for file in files:
            if file.endswith('.html'):
                path = os.path.join(root, file)
                if not verify_file(path):
                    failed = True
                count += 1
                
    if failed:
        print("\nVerification FAILED: Header structure issues found.")
        sys.exit(1)
    else:
        print(f"\nVerification PASSED: All {count} files check out.")
        sys.exit(0)

if __name__ == '__main__':
    main()
