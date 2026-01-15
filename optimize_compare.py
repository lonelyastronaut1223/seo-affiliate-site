import glob
import os

# Define the HTML template fragments to inject
script_includes = """
  <script src="../links.js"></script>
  <script src="../script.js"></script>
</body>
"""

btn_buy_template = """
            <p style="margin-top:auto"><a href="#" class="btn-buy" rel="sponsored noopener noreferrer" target="_blank">Check Price on Amazon &rarr;</a></p>
"""

# Map of file -> expected IDs for the two products (Product A, Product B)
# We will look for <h3>Product Name</h3> and try to inject ID into the parent <article>
# Or we can just add the buttons directly if we can identify the cards.

# Let's try a rigorous regex replacement approach or BeautifulSoup if available? 
# No, standard string manipulation is safer without external libs.

files = glob.glob('compare/*.html')

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    updated = False
    
    # 1. Update Scripts (Remove old footer script, add new includes)
    if '<script src="../links.js"></script>' not in content:
        # Find the old inline script and remove/replace it
        if '<script>' in content and 'document.getElementById("year")' in content:
            # Replaces the entire footer script block with the new script tags
            # We assume the footer script is at the end.
            # Let's just find </body> and insert before it, and try to remove the old script.
            
             # Remove custom footer script
            start_script = content.find('<script>')
            end_script = content.find('</script>') + 9
            if start_script != -1 and 'document.getElementById("year")' in content[start_script:end_script]:
                content = content[:start_script] + content[end_script:]
            
            content = content.replace('</body>', script_includes)
            updated = True

    # 2. Add "Check Price" Buttons to TL;DR Cards
    # Look for </p> closing tag inside <article class="card">
    # This is tricky with simple replace. 
    # Let's wrap the <article class="card"> content.
    
    # Alternative: Use simple replacement for the specific structure found in the view_file output.
    # Structure: <h3>Name</h3> <p>Desc</p> </article>
    # We want: <h3>Name</h3> <p>Desc</p> <a...>Btn</a> </article>
    
    if 'class="btn-buy"' not in content:
        # We replace </article> with button + </article>, but only for cards inside "TL;DR picks"?
        # The file has <article class="card"> inside <div class="grid">.
        # Let's be aggressive and add it to all cards in the grid that look like product picks.
        
        # Heuristic: If it has <h3> and <p>, it's likely a product card.
        # We will replace `</p>\n      </article>` with `</p>\n      <a href="#" class="btn-buy" rel="sponsored noopener noreferrer" target="_blank">Check Price on Amazon &rarr;</a>\n      </article>`
        # Check for variations in whitespace
        content = content.replace('</p>\n      </article>', '</p>\n        <a href="#" class="btn-buy" rel="sponsored noopener noreferrer" target="_blank" style="margin-top:10px; display:inline-block; font-size:14px;">Check Price on Amazon &rarr;</a>\n      </article>')
        updated = True

    # 3. Add link placeholder to Comparison Table
    # Pattern: <td>Name</td>
    # We need to turn specific cells into "Check Price" links if they are the header? 
    # Actually, links.js targets `a[href="#id"]`. 
    # The current table has `<th>Category</th><th>Sony A7 V</th><th>Canon R6 III</th>`
    # We should add a row for Price? Or just rely on the TL;DR cards.
    # The user manual request optimization. Let's start with proper headers/footers/buttons.
    
    # 4. Inject IDs for links.js
    # We need to know WHICH product is which.
    # sony-a7-v-vs-canon-r6-iii.html -> IDs: sony-a7-v, canon-r6-iii (Hypothetically)
    
    # Logic: Define IDs based on filename?
    filename = os.path.basename(filepath)
    id_map = {
        'sony-a7-v-vs-canon-r6-iii.html': ['sony-a7-v', 'canon-r6-iii'],
        'sony-a7-iv-vs-canon-r6-ii.html': ['sony-a7-iv', 'canon-r6-ii'],
        'sony-zv-e10-vs-sony-a6700.html': ['sony-zv-e10', 'sony-a6700'],
        'fujifilm-x-s20-vs-fujifilm-x-t5.html': ['fuji-x-s20', 'fuji-x-t5']
    }
    
    tags = id_map.get(filename)
    if tags:
        # Try to inject ID into the first and second card of TL;DR
        # The first card is usually the "Pick" or first product.
        # This is risky without parsing. 
        # But we can try to find `<h3>Product Name</h3>` and add ID to nearest parent?
        pass

    if updated:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")
    else:
        print(f"No changes needed for {filepath}")

