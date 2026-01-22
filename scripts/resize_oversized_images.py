#!/usr/bin/env python3
"""
Resize oversized source images to max 1200px width.
This fixes LCP by reducing download size dramatically.
"""

from PIL import Image
import os

GUIDES_DIR = 'public/assets/images/guides'
MAX_WIDTH = 1200
QUALITY = 85

# Only process these oversized images (preserve sm variants)
oversized_files = [
    'vlog.webp',      # 8192x5461
    'beginner.webp',  # 4160x6240
    'budget.webp',    # 6000x4000
    'hybrid.webp',    # 5267x3511
    'action-360.webp',# 5812x3875
    'fullframe-video.webp', # 4672x7008
    'travel.webp'     # 5472x3648
]

def resize_image(filename):
    path = os.path.join(GUIDES_DIR, filename)
    backup_path = path + '.backup'
    
    with Image.open(path) as img:
        orig_w, orig_h = img.size
        orig_size = os.path.getsize(path) / 1024
        
        if orig_w <= MAX_WIDTH:
            print(f"  {filename}: Already {orig_w}px, skipping")
            return
        
        # Calculate new height maintaining aspect ratio
        ratio = MAX_WIDTH / orig_w
        new_h = int(orig_h * ratio)
        
        # Resize
        resized = img.resize((MAX_WIDTH, new_h), Image.LANCZOS)
        
        # Save backup first
        os.rename(path, backup_path)
        
        # Save resized version
        resized.save(path, 'WEBP', quality=QUALITY)
        
        new_size = os.path.getsize(path) / 1024
        savings = (1 - new_size / orig_size) * 100
        
        print(f"✅ {filename}: {orig_w}x{orig_h} → {MAX_WIDTH}x{new_h}")
        print(f"   Size: {orig_size:.1f}KB → {new_size:.1f}KB (-{savings:.0f}%)")

print("🔧 Resizing oversized source images...\n")

for f in oversized_files:
    try:
        resize_image(f)
    except Exception as e:
        print(f"❌ {f}: {e}")

print("\n✅ Done! Oversized images resized to max 1200px width.")
print("   Backup files created with .backup extension.")
