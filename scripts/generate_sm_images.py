#!/usr/bin/env python3
"""
Generate -sm (small) variants for images using PIL/Pillow
Target: 600px width for mobile optimization
"""

import os
import sys
from pathlib import Path
from PIL import Image

# Configuration
SMALL_WIDTH = 600
QUALITY = 85

def generate_small_variant(image_path):
    """Generate -sm variant for an image"""
    try:
        # Open image
        img = Image.open(image_path)
        
        # Get original dimensions
        width, height = img.size
        
        # Skip if already small enough
        if width <= SMALL_WIDTH:
            print(f"⏭️  Skipping {image_path.name} (already {width}px)")
            return False
        
        # Calculate new height maintaining aspect ratio
        ratio = SMALL_WIDTH / width
        new_height = int(height * ratio)
        
        # Resize
        img_resized = img.resize((SMALL_WIDTH, new_height), Image.Resampling.LANCZOS)
        
        # Generate output filename
        stem = image_path.stem
        ext = image_path.suffix
        output_path = image_path.parent / f"{stem}-sm{ext}"
        
        # Save
        if ext.lower() in ['.webp']:
            img_resized.save(output_path, 'WEBP', quality=QUALITY, method=6)
        elif ext.lower() in ['.jpg', '.jpeg']:
            img_resized.save(output_path, 'JPEG', quality=QUALITY, optimize=True)
        elif ext.lower() == '.png':
            img_resized.save(output_path, 'PNG', optimize=True)
        else:
            print(f"⚠️  Unsupported format: {ext}")
            return False
        
        # Get file sizes
        original_size = os.path.getsize(image_path) / 1024
        new_size = os.path.getsize(output_path) / 1024
        savings = ((original_size - new_size) / original_size) * 100
        
        print(f"✅ {image_path.name} → {output_path.name}")
        print(f"   {width}x{height}px ({original_size:.1f}KB) → {SMALL_WIDTH}x{new_height}px ({new_size:.1f}KB) [-{savings:.0f}%]")
        return True
        
    except Exception as e:
        print(f"❌ Error processing {image_path}: {e}")
        return False

def main():
    if len(sys.argv) < 2:
        print("Usage: python generate_sm_images.py <directory>")
        sys.exit(1)
    
    directory = Path(sys.argv[1])
    
    if not directory.exists():
        print(f"❌ Directory not found: {directory}")
        sys.exit(1)
    
    print(f"🖼️  Generating -sm variants in: {directory}")
    print(f"📏 Target width: {SMALL_WIDTH}px")
    print(f"💎 Quality: {QUALITY}%")
    print()
    
    # Find all images without -sm variants
    processed = 0
    skipped = 0
    
    for ext in ['*.webp', '*.jpg', '*.jpeg', '*.png']:
        for img_path in directory.glob(f"**/{ext}"):
            # Skip if already a variant
            if '-sm' in img_path.stem or '-640' in img_path.stem or '-960' in img_path.stem or '-1280' in img_path.stem:
                continue
            
            # Skip if -sm variant already exists
            sm_path = img_path.parent / f"{img_path.stem}-sm{img_path.suffix}"
            if sm_path.exists():
                skipped += 1
                continue
            
            # Generate variant
            if generate_small_variant(img_path):
                processed += 1
    
    print()
    print(f"📊 Summary:")
    print(f"   Processed: {processed} images")
    print(f"   Skipped: {skipped} images (already exist)")

if __name__ == "__main__":
    main()
