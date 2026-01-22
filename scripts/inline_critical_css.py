#!/usr/bin/env python3
"""
Add critical CSS inline to BaseLayout.astro and defer non-critical CSS
"""

import re

# Read BaseLayout
with open('src/layouts/BaseLayout.astro', 'r') as f:
    content = f.read()

# Read critical CSS
with open('src/critical.css', 'r') as f:
    critical_css = f.read().strip()

# Find the position after title tag
title_pos = content.find('</title>')
if title_pos == -1:
    print("❌ Could not find </title> tag")
    exit(1)

# Insert critical CSS inline
inline_css = f'''

        <!-- Critical CSS - Inline for FCP optimization -->
        <style is:inline>
            {critical_css}
        </style>'''

# Insert after title
insert_pos = title_pos + len('</title>')
content = content[:insert_pos] + inline_css + content[insert_pos:]

# Now defer non-critical CSS
# Replace regular stylesheet links with preload + async pattern
css_links = [
    'style.min.css',
    'footer-enhancements.min.css',
    'loaders.min.css',
    'mega-menu.min.css'
]

for css_file in css_links:
    # Find the link tag
    pattern = f'<link rel="stylesheet" href="/assets/css/{css_file}" />'
    
    # Replace with preload pattern
    replacement = f'''<link rel="preload" as="style" href="/assets/css/{css_file}" onload="this.onload=null;this.rel='stylesheet'" />
        <noscript><link rel="stylesheet" href="/assets/css/{css_file}" /></noscript>'''
    
    content = content.replace(pattern, replacement)

# Write back
with open('src/layouts/BaseLayout.astro', 'w') as f:
    f.write(content)

print("✅ Critical CSS inlined")
print("✅ Non-critical CSS deferred")
print("📄 Updated: src/layouts/BaseLayout.astro")
