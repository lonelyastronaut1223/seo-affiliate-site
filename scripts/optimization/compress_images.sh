#!/bin/bash
# Image Optimization Script - Compress large images
# Uses sips for JPEG quality reduction and cwebp for WebP conversion

cd /Users/taylor/Downloads/Project/SEO-Affiliate/seo-affiliate-site

echo "🖼️  Image Optimization Starting..."
echo "========================================"

# Compress large JPEGs (>500KB) to 80% quality
echo ""
echo "📸 Compressing large JPEG files..."

for img in $(find assets/images -name "*.jpg" -size +500k 2>/dev/null); do
    original_size=$(ls -l "$img" | awk '{print $5}')
    echo "  Processing: $img ($(numfmt --to=iec $original_size))"
    sips -s formatOptions 75 "$img" --out "$img" 2>/dev/null
    new_size=$(ls -l "$img" | awk '{print $5}')
    saved=$((original_size - new_size))
    if [ $saved -gt 0 ]; then
        echo "    ✓ Saved $(numfmt --to=iec $saved)"
    fi
done

# Compress large PNGs by converting to WebP if not already exists
echo ""
echo "🎨 Converting large PNG files to WebP..."

for img in $(find assets/images -name "*.png" -size +500k 2>/dev/null); do
    webp_file="${img%.png}.webp"
    if [ ! -f "$webp_file" ]; then
        echo "  Converting: $img"
        cwebp -q 85 "$img" -o "$webp_file" 2>/dev/null
        if [ -f "$webp_file" ]; then
            echo "    ✓ Created: $webp_file"
        fi
    fi
done

# Recompress existing WebP files that are too large
echo ""
echo "🔄 Recompressing large WebP files..."

for img in $(find assets/images -name "*.webp" -size +1M 2>/dev/null); do
    original_size=$(ls -l "$img" | awk '{print $5}')
    temp_file="${img}.tmp.webp"
    
    # Get source JPEG if exists
    jpg_source="${img%.webp}.jpg"
    if [ -f "$jpg_source" ]; then
        echo "  Regenerating: $img from $jpg_source"
        cwebp -q 80 "$jpg_source" -o "$temp_file" 2>/dev/null
        if [ -f "$temp_file" ]; then
            new_size=$(ls -l "$temp_file" | awk '{print $5}')
            if [ $new_size -lt $original_size ]; then
                mv "$temp_file" "$img"
                saved=$((original_size - new_size))
                echo "    ✓ Saved $(numfmt --to=iec $saved)"
            else
                rm "$temp_file"
                echo "    - No improvement, keeping original"
            fi
        fi
    fi
done

echo ""
echo "========================================"
echo "✅ Optimization Complete!"

# Show final stats
echo ""
echo "📊 Final Size Summary:"
total_size=$(du -sh assets/images | awk '{print $1}')
echo "  Total images folder: $total_size"
