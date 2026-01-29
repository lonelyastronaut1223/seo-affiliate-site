
import os
import re

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to find header
    # We look for <header ... class="... header-sticky ..."> ... </header>
    # Note: .*? is non-greedy. dotall=True to match newlines.
    header_pattern = re.compile(r'(<header[^>]*class=["\'][^"\']*(?:header-sticky)[^"\']*["\'][^>]*>)(.*?)(</header>)', re.DOTALL | re.IGNORECASE)
    
    match = header_pattern.search(content)
    if not match:
        print(f"Skipping {filepath}: No sticky header found.")
        return False

    header_open_tag = match.group(1)
    header_inner_content = match.group(2)
    header_close_tag = match.group(3)
    
    modified_inner = header_inner_content
    hero_block = ""
    
    # 1. Check for Hero inside
    # We assume <section class="hero"> ... </section>
    # We need to be careful about nested sections, but usually Hero is top level in header
    # We'll use a simple find for the specific hero class string
    
    hero_start_idx = modified_inner.find('<section class="hero">')
    if hero_start_idx == -1:
        hero_start_idx = modified_inner.find('<section class="hero ') # variation
        
    if hero_start_idx != -1:
        # found hero. Find the matching closing tag.
        # Since regex is hard for balancing, and we assume hero doesn't contain sections for now (it's hero-grid etc)
        # We search for </section> after start
        hero_end_idx = modified_inner.find('</section>', hero_start_idx)
        if hero_end_idx != -1:
            hero_end_idx += len('</section>') # include tag
            
            hero_block = modified_inner[hero_start_idx:hero_end_idx]
            # Remove hero from inner
            modified_inner = modified_inner[:hero_start_idx] + modified_inner[hero_end_idx:]
            print(f"  - Extracted Hero section from header in {filepath}")
    
    # 2. Fix Container Class
    # Check if header_open_tag has 'container'
    if 'container' in header_open_tag:
        # Remove 'container' from class list
        # We need to handle class="..."
        def remove_container(m):
            cls = m.group(1)
            # Remove 'container' word and extra spaces
            cls = cls.replace('container', '').strip()
            # Clean up double spaces
            cls = re.sub(r'\s+', ' ', cls)
            return f'class="{cls}"'
            
        new_header_open_tag = re.sub(r'class=["\']([^"\']*)["\']', remove_container, header_open_tag)
        
        # Wrap inner content in div.container, BUT exclude the hero we removed (already done)
        # We wrap the REMAINING modified_inner
        # Only wrap if invalid empty content? No.
        
        # Check if we didn't accidentally remove everything (e.g. if hero was everything)
        if modified_inner.strip():
             modified_inner = f'\n    <div class="container">{modified_inner}    </div>\n'
             print(f"  - Refactored Header Container in {filepath}")
        
        header_open_tag = new_header_open_tag
    else:
        print(f"  - Header already has no container class (or not found) in {filepath}")

    # Reconstruct
    new_header = f"{header_open_tag}{modified_inner}{header_close_tag}"
    
    # Append Hero AFTER header
    if hero_block:
        new_header = new_header + "\n" + hero_block
        
    # Replace in original content
    # We use the original match span to replace safely
    new_full_content = content[:match.start()] + new_header + content[match.end():]
    
    if new_full_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_full_content)
        return True
    return False


def main():
    # Find all html files
    count = 0
    for root, dirs, files in os.walk('.'):
        if '.agent' in root: continue # skip agent
        if '.git' in root: continue
        
        for file in files:
            if file.endswith('.html'):
                path = os.path.join(root, file)
                if fix_file(path):
                    count += 1
    print(f"Fixed {count} files.")

if __name__ == '__main__':
    main()
