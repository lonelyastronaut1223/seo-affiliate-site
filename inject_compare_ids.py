import os

# Map filenames to a LIST of (Title Substring, ID to Inject)
# We will search for <article class="card"> containing the Title Substring
# And inject 'id="ID"' into the <article> tag.

file_map = {
    'compare/sony-a7-v-vs-canon-r6-iii.html': [
        ('<h3>Canon R6 III</h3>', 'canon-r6-iii'),
        ('<h3>Sony A7 V</h3>', 'sony-a7-v')
    ],
    'compare/sony-a7-iv-vs-canon-r6-ii.html': [
        ('<h3>Canon R6 II</h3>', 'canon-r6-ii'),
        ('<h3>Sony A7 IV</h3>', 'sony-a7iv')
    ],
    'compare/sony-zv-e10-vs-sony-a6700.html': [
        ('<h3>Sony A6700</h3>', 'sony-a6700'),
        ('<h3>Sony ZV-E10</h3>', 'sony-zv-e10')
    ],
    'compare/fujifilm-x-s20-vs-fujifilm-x-t5.html': [
        ('<h3>X-S20</h3>', 'fuji-x-s20'),
        ('<h3>Fujifilm X-T5</h3>', 'fuji-x-t5') 
        # Note: Need to verify if "Fujifilm X-T5" or just "X-T5" is in the <h3>.
        # Based on previous grep, I only saw X-S20. I should be careful.
        # Optimistic matching: "X-T5"
    ]
}

for filepath, injections in file_map.items():
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    
    for title_snippet, product_id in injections:
        # We look for the snippet.
        # Then we look backwards for the strict <article class="card"> or <article class="card"> (with potential other attrs?)
        # Simplest regex-free way: Split by the snippet, and modify the last occurrence of <article class="card"> in the pre-part.
        
        parts = content.split(title_snippet)
        if len(parts) > 1:
            # The snippet exists. The <article> tag must be in parts[0] (or previous parts if multiple)
            # We want the LAST <article class="card"> before this snippet.
            
            pre_part = parts[0]
            target_tag = '<article class="card">'
            last_occurrence = pre_part.rfind(target_tag)
            
            if last_occurrence != -1:
                # Check if it already has an ID
                # We can check the string immediately following target_tag
                # But easiest is just to replace that specific instance string
                
                # Careful: rfind returns index.
                # Construct new pre_part
                
                # Verify we aren't injecting twice
                if f'id="{product_id}"' in pre_part[last_occurrence:]: 
                     print(f"Skipping {product_id} in {filepath}, already looks present.")
                     continue

                new_tag = f'<article class="card" id="{product_id}">'
                
                # Replace ONLY that last occurrence
                new_pre_part = pre_part[:last_occurrence] + new_tag + pre_part[last_occurrence + len(target_tag):]
                
                # Reassemble
                content = new_pre_part + title_snippet + parts[1]
                # If there were more parts (multiple occurrences of title?), just join the rest
                if len(parts) > 2:
                    content += "".join(parts[2:])
                
                modified = True
                print(f" injected id='{product_id}' for '{title_snippet}' in {filepath}")
            else:
                 print(f"Could not find <article class='card'> before '{title_snippet}' in {filepath}")
        else:
             print(f"Could not find title '{title_snippet}' in {filepath}")
             # Fallback for X-T5 maybe?
             if 'X-T5' in title_snippet:
                 # Check for just '<h3>X-T5</h3>' ?
                 pass

    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
