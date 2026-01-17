import os
import datetime

BASE_URL = "https://cameraupick.com"
SITEMAP_FILE = "sitemap-index.xml"

# Priority rules
PRIORITIES = {
    "index.html": "1.0",
    "guides": "0.9",
    "compare": "0.7",
    "reviews": "0.8",
    "de": "0.6",
    "default": "0.5"
}

def get_files(directory):
    html_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".html"):
                # Skip partials or special files if any (e.g., templates)
                if "fragment" in file:
                    continue
                path = os.path.join(root, file)
                html_files.append(path)
    return html_files

def generate_sitemap(files):
    sitemap_content = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
    ]

    # Get current date for lastmod (optional but good)
    today = datetime.date.today().isoformat()

    for file_path in files:
        # Relativize path
        rel_path = os.path.relpath(file_path, os.getcwd())
        
        # Convert file path to URL path
        url_path = rel_path.replace("\\", "/") # Windows fix just in case
        
        # Determine priority
        priority = PRIORITIES["default"]
        if url_path == "index.html":
            url_full = BASE_URL + "/"
            priority = PRIORITIES["index.html"]
        elif url_path.startswith("guides/"):
            url_full = BASE_URL + "/" + url_path
            priority = PRIORITIES["guides"]
        elif url_path.startswith("compare/"):
            url_full = BASE_URL + "/" + url_path
            priority = PRIORITIES["compare"]
        elif url_path.startswith("reviews/"):
            url_full = BASE_URL + "/" + url_path
            priority = PRIORITIES["reviews"]
        elif url_path.startswith("de/"):
             # Handle German index separately if needed
            if url_path == "de/index.html":
                 url_full = BASE_URL + "/de/"
            else:
                 url_full = BASE_URL + "/" + url_path
            priority = PRIORITIES["de"]
        else:
            url_full = BASE_URL + "/" + url_path
            
        # exclude 404 page if it exists
        if "404" in url_path:
            continue

        sitemap_content.append('  <url>')
        sitemap_content.append(f'    <loc>{url_full}</loc>')
        # sitemap_content.append(f'    <lastmod>{today}</lastmod>') # Optional: enable if desired
        sitemap_content.append(f'    <priority>{priority}</priority>')
        sitemap_content.append('  </url>')

    sitemap_content.append('</urlset>')
    
    return "\n".join(sitemap_content)

if __name__ == "__main__":
    current_dir = os.getcwd()
    files = get_files(current_dir)
    
    # Sort files for stable output
    files.sort()
    
    xml_content = generate_sitemap(files)
    
    with open(SITEMAP_FILE, "w", encoding="utf-8") as f:
        f.write(xml_content)
    
    print(f"✅ Generated {SITEMAP_FILE} with {len(files)} URLs.")
