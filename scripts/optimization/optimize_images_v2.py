#!/usr/bin/env python3
"""
Enhanced Image Optimization Script
Compresses large images and converts PNG to WebP
"""

import os
import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent
IMAGES_DIR = BASE_DIR / 'assets' / 'images'

def get_file_size_mb(path):
    return os.path.getsize(path) / (1024 * 1024)

def compress_jpeg(file_path, quality=85):
    """Compress JPEG using sips (macOS built-in)"""
    try:
        # Create backup
        backup = str(file_path) + '.bak'
        subprocess.run(['cp', str(file_path), backup], check=True)
        
        # Use sips to compress (macOS)
        subprocess.run([
            'sips', '-s', 'formatOptions', str(quality),
            str(file_path)
        ], capture_output=True)
        
        new_size = get_file_size_mb(file_path)
        old_size = get_file_size_mb(backup)
        
        if new_size < old_size:
            os.remove(backup)
            return old_size, new_size
        else:
            # Restore if no improvement
            subprocess.run(['mv', backup, str(file_path)], check=True)
            return old_size, old_size
    except Exception as e:
        print(f"  ⚠️ Error: {e}")
        return 0, 0

def png_to_webp(file_path, quality=85):
    """Convert PNG to WebP using cwebp if available"""
    webp_path = file_path.with_suffix('.webp')
    if webp_path.exists():
        return None  # Already has WebP
    
    try:
        # Try using cwebp
        result = subprocess.run([
            'cwebp', '-q', str(quality), str(file_path), '-o', str(webp_path)
        ], capture_output=True)
        
        if webp_path.exists():
            old_size = get_file_size_mb(file_path)
            new_size = get_file_size_mb(webp_path)
            return old_size, new_size
    except FileNotFoundError:
        # cwebp not available, try sips
        try:
            subprocess.run([
                'sips', '-s', 'format', 'webp', str(file_path),
                '--out', str(webp_path)
            ], capture_output=True)
            if webp_path.exists():
                old_size = get_file_size_mb(file_path)
                new_size = get_file_size_mb(webp_path)
                return old_size, new_size
        except:
            pass
    return None

def main():
    print("🖼️ Enhanced Image Optimization\n")
    
    total_saved = 0
    files_optimized = 0
    
    # Find large JPEG files
    print("📸 Compressing large JPEG files (>500KB)...")
    for jpg_file in IMAGES_DIR.rglob('*.jpg'):
        size_mb = get_file_size_mb(jpg_file)
        if size_mb > 0.5:  # > 500KB
            old, new = compress_jpeg(jpg_file, quality=82)
            if old > new:
                saved = old - new
                total_saved += saved
                files_optimized += 1
                print(f"  ✅ {jpg_file.name}: {old:.2f}MB → {new:.2f}MB ({saved:.2f}MB saved)")
    
    # Convert large PNG to WebP
    print("\n🌐 Converting PNG to WebP...")
    for png_file in IMAGES_DIR.rglob('*.png'):
        size_mb = get_file_size_mb(png_file)
        if size_mb > 0.3:  # > 300KB
            result = png_to_webp(png_file, quality=85)
            if result:
                old, new = result
                saved = old - new
                if saved > 0:
                    total_saved += saved
                    files_optimized += 1
                    print(f"  ✅ {png_file.name} → WebP: {old:.2f}MB → {new:.2f}MB ({saved:.2f}MB saved)")
    
    print(f"\n{'='*50}")
    print(f"✨ Optimized {files_optimized} files")
    print(f"💾 Total saved: {total_saved:.2f}MB")

if __name__ == '__main__':
    main()
