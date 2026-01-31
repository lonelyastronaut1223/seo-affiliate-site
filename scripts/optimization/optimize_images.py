#!/usr/bin/env python3
"""
Image Optimization Script - Using PIL/Pillow
Optimizes guide images with responsive variants
"""

from PIL import Image
from pathlib import Path
import sys

# Configuration
GUIDES_DIR = Path("public/assets/images/guides")
MAIN_DIR = Path("public/assets/images")

# Responsive sizes: (width, quality)
SIZES = {
    'sm': (600, 80),   # Mobile
    'md': (900, 80),   # Tablet
    'lg': (1200, 85),  # Desktop
}

# Priority images to optimize
GUIDE_IMAGES = [
    'panasonic-g100d.webp',
    'fujifilm-x-t5.webp',
    'fullframe-video.webp',
    'nikon-z6-iii.webp',
    'canon-r100.webp',
    'sony-fx3.webp',
    'canon-r6ii.webp',
    'canon-r5-ii.webp',
    'youtube-creator.webp',
]

# Super large images to compress
LARGE_IMAGES = [
    'pexels-robert-nagy-512974-4083514.webp',
    'pexels-huysuzkadraj-19239809.webp',
]

def optimize_image(src_path, dest_path, max_width=None, quality=85):
    """Optimize a single image"""
    try:
        img = Image.open(src_path)
        
        # Convert RGBA to RGB if needed
        if img.mode in ('RGBA', 'LA'):
            background = Image.new('RGB', img.size, (255, 255, 255))
            if img.mode == 'RGBA':
                background.paste(img, mask=img.split()[3])
            else:
                background.paste(img, mask=img.split()[1])
            img = background
        
        # Resize if max_width specified
        if max_width and img.width > max_width:
            ratio = max_width / img.width
            new_height = int(img.height * ratio)
            img = img.resize((max_width, new_height), Image.LANCZOS)
        
        # Save as WebP with specified quality
        img.save(dest_path, 'WEBP', quality=quality, method=6)
        
        # Get file sizes
        src_size = src_path.stat().st_size if src_path.exists() else 0
        dest_size = dest_path.stat().st_size
        
        return src_size, dest_size
        
    except Exception as e:
        print(f"❌ Error processing {src_path.name}: {e}")
        return 0, 0

def format_size(bytes):
    """Format bytes to human readable"""
    for unit in ['B', 'KB', 'MB']:
        if bytes < 1024:
            return f"{bytes:.1f}{unit}"
        bytes /= 1024
    return f"{bytes:.1f}GB"

def main():
    total_saved = 0
    files_processed = 0
    
    print("=" * 60)
    print("🖼️  IMAGE OPTIMIZATION SCRIPT")
    print("=" * 60)
    
    # Phase 1: Optimize super large pexels images
    print("\n📦 Phase 1: Compressing Large Images")
    print("-" * 60)
    
    for img_name in LARGE_IMAGES:
        src = MAIN_DIR / img_name
        if not src.exists():
            print(f"⏭️  {img_name} not found, skipping")
            continue
        
        # Compress to max 1200px width, quality 75
        dest = src.with_stem(f"{src.stem}-opt")
        
        if dest.exists():
            print(f"⏭️  {dest.name} already exists")
            continue
        
        src_size, dest_size = optimize_image(src, dest, max_width=1200, quality=75)
        
        if dest_size > 0:
            saved = src_size - dest_size
            total_saved += saved
            files_processed += 1
            print(f"✅ {img_name}")
            print(f"   {format_size(src_size)} → {format_size(dest_size)} "
                  f"(saved {format_size(saved)})")
    
    # Phase 2: Create responsive variants for guide images
    print("\n📱 Phase 2: Creating Responsive Variants")
    print("-" * 60)
    
    for img_name in GUIDE_IMAGES:
        src = GUIDES_DIR / img_name
        if not src.exists():
            print(f"⏭️  {img_name} not found, skipping")
            continue
        
        base_name = img_name.replace('.webp', '')
        print(f"\n🔧 Processing {img_name}...")
        
        for suffix, (width, quality) in SIZES.items():
            dest = GUIDES_DIR / f"{base_name}-{suffix}.webp"
            
            if dest.exists():
                print(f"   ⏭️  {dest.name} exists")
                continue
            
            src_size, dest_size = optimize_image(src, dest, max_width=width, quality=quality)
            
            if dest_size > 0:
                saved = src_size - dest_size
                total_saved += saved
                files_processed += 1
                print(f"   ✅ {suffix}: {format_size(dest_size)}")
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 OPTIMIZATION SUMMARY")
    print("=" * 60)
    print(f"Files processed: {files_processed}")
    print(f"Total saved: {format_size(total_saved)}")
    print(f"Average per file: {format_size(total_saved / files_processed if files_processed > 0 else 0)}")
    print("=" * 60)
    print("✅ Done! Remember to:")
    print("   1. Update Astro pages with responsive srcset")
    print("   2. Build and test")
    print("   3. Deploy and verify Lighthouse scores")
    print("=" * 60)

if __name__ == "__main__":
    main()
