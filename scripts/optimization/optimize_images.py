#!/usr/bin/env python3
"""
Simplified image optimization focusing on JPEG and WebP only
PNG requires specialized tools - skip for now
"""

import sys
import io
from pathlib import Path
from PIL import Image

BASE_DIR = Path(__file__).parent.parent.parent
IMAGE_DIR = BASE_DIR / 'assets' / 'images'

# Quality settings
JPEG_QUALITY = 82  # Slightly lower for better compression
WEBP_QUALITY = 82

def optimize_jpeg(image_path: Path) -> dict:
    """Optimize JPEG images"""
    try:
        original_size = image_path.stat().st_size / 1024
        
        img = Image.open(image_path)
        
        # Convert RGBA to RGB if needed
        if img.mode == 'RGBA':
            img = img.convert('RGB')
        
        # Save optimized version to buffer first
        buffer = io.BytesIO()
        img.save(buffer, 'JPEG', quality=JPEG_QUALITY, optimize=True, progressive=True)
        new_size = buffer.tell() / 1024
        
        if new_size < original_size:
            with open(image_path, 'wb') as f:
                f.write(buffer.getvalue())
            
            reduction = ((original_size - new_size) / original_size) * 100
            
            return {
                'success': True,
                'original_kb': original_size,
                'new_kb': new_size,
                'reduction_percent': reduction
            }
        else:
            return {
                'success': False,
                'skipped': True,
                'reason': f'optimized size larger ({new_size:.1f}KB > {original_size:.1f}KB)'
            }
    except Exception as e:
        return {'error': str(e)}

def optimize_webp(image_path: Path) -> dict:
    """Optimize WebP images"""
    try:
        original_size = image_path.stat().st_size / 1024
        
        img = Image.open(image_path)
        # Save to buffer
        buffer = io.BytesIO()
        img.save(buffer, 'WEBP', quality=WEBP_QUALITY, method=4)
        new_size = buffer.tell() / 1024
        
        if new_size < original_size:
            with open(image_path, 'wb') as f:
                f.write(buffer.getvalue())
            
            reduction = ((original_size - new_size) / original_size) * 100
            
            return {
                'success': True,
                'original_kb': original_size,
                'new_kb': new_size,
                'reduction_percent': reduction
            }
        else:
            return {
                'success': False,
                'skipped': True,
                'reason': f'optimized size larger ({new_size:.1f}KB > {original_size:.1f}KB)'
            }
    except Exception as e:
        return {'error': str(e)}

def convert_png_to_webp(png_path: Path) -> bool:
    """Convert team-avatar.png to WebP"""
    try:
        webp_path = png_path.with_suffix('.webp')
        
        if webp_path.exists():
            print(f"⏭️  WebP already exists: {webp_path.name}")
            return False
        
        img = Image.open(png_path)
        img.save(webp_path, 'WEBP', quality=90, method=6)
        
        webp_size = webp_path.stat().st_size / 1024
        png_size = png_path.stat().st_size / 1024
        print(f"✅ Created {webp_path.name}: {png_size:.0f}KB → {webp_size:.0f}KB")
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    print("🖼️  Image Optimization (JPEG/WebP only)\n")
    
    # Large JPEG images to optimize
    jpeg_images = [
        'guides/beginner.jpg',
        'Vlog.jpg',
        'guides/action-360.jpg',
        'guides/travel.jpg',
        'pexels-huysuzkadraj-19239809.jpg',
        'pexels-robert-nagy-512974-4083514.jpg',
    ]
    
    # Large WebP images to optimize
    webp_images = [
        'guides/beginner.webp',
        'Vlog.webp',
        'guides/action-360.webp',
        'guides/travel.webp',
        'pexels-huysuzkadraj-19239809.webp',
        'pexels-robert-nagy-512974-4083514.webp',
    ]
    
    total_original = 0
    total_new = 0
    optimized = 0
    
    print("📸 Optimizing JPEG images...")
    for img_name in jpeg_images:
        img_path = IMAGE_DIR / img_name
        if not img_path.exists():
            continue
            
        result = optimize_jpeg(img_path)
        if result.get('success'):
            total_original += result['original_kb']
            total_new += result['new_kb']
            optimized += 1
            print(f"  ✅ {img_name}: {result['original_kb']:.0f}KB → {result['new_kb']:.0f}KB ({result['reduction_percent']:.1f}%)")
    
    print("\n🌐 Optimizing WebP images...")
    for img_name in webp_images:
        img_path = IMAGE_DIR / img_name
        if not img_path.exists():
            continue
            
        result = optimize_webp(img_path)
        if result.get('success'):
            total_original += result['original_kb']
            total_new += result['new_kb']
            optimized += 1
            print(f"  ✅ {img_name}: {result['original_kb']:.0f}KB → {result['new_kb']:.0f}KB ({result['reduction_percent']:.1f}%)")
    
    print("\n🔄 Converting PNG to WebP...")
    team_avatar = IMAGE_DIR / 'team-avatar.png'
    if team_avatar.exists():
        convert_png_to_webp(team_avatar)
    
    # Summary
    if optimized > 0:
        total_saved = (total_original - total_new) / 1024
        total_reduction = ((total_original - total_new) / total_original) * 100
        print("\n" + "="*60)
        print(f"✅ Optimized {optimized} images")
        print(f"💾 Saved {total_saved:.2f}MB ({total_reduction:.1f}% reduction)")
        print("="*60)
    
    print("\n💡 Note: PNG camera images not optimized (require specialized tools)")
    print("   They're already reasonably sized and won't significantly impact performance")

if __name__ == '__main__':
    main()
