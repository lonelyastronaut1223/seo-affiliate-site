import os
import glob

# Paths to search
directories = [
    'guides/*.html',
    'reviews/*.html'
]

# Script tag to insert
script_tag = '<script src="../links.js"></script>'
target_script = '<script src="../script.js"></script>'

count = 0

for pattern in directories:
    files = glob.glob(pattern)
    for filepath in files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Skip if already exists
        if 'links.js' in content:
            print(f"Skipping {filepath} (already present)")
            continue
            
        # Insert before script.js
        if target_script in content:
            new_content = content.replace(target_script, f"{script_tag}\n  {target_script}")
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"Updated {filepath}")
            count += 1
        else:
            print(f"Warning: Could not find script.js in {filepath}")

print(f"Total files updated: {count}")
